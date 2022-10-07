import json
import math
import struct
import sys

import io
import numpy
import plyfile

from .gbi import F3DEX
from .parsers.glover_objbank import GloverObjbank
from .parsers.construct import glover_objbank as objbank_writer

class LinkableData(object):
    def __init__(self, segment, parent):
        self.parent = parent
        self.segment = segment
        self.segment_offset = None
        self.absolute_offset = None

    def len(self):
        return 0

    def link(self):
        return b""

class CollatedDataFile(object):
    def __init__(self, segments):
        self.segments_by_name = {}
        for segment_name in segments:
            self.segments_by_name[segment_name] = []
        self.segments = segments

    def pushData(self, segment_name, linkable_data):
        self.segments_by_name[segment_name].append(linkable_data)

    def link(self):
        raw = []
        for segment_name in self.segments:
            raw += self.segments_by_name[segment_name].link()
        # TODO: need to find and link references somehow
        return b"".join(raw)

def parent_str(parents):
    return ".".join(map(lambda m: m.name.strip("\x00"), parents))

def for_each_mesh(mesh, callback, parents=None):
    if parents is None:
        parents = []
    cur_matrix = [1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1] # TODO
    callback(mesh, parents, cur_matrix)
    if mesh.sibling is not None:
        for_each_mesh(mesh.sibling, callback, parents)
    if mesh.child is not None:
        child_parents = parents[:]
        child_parents.append(mesh)
        for_each_mesh(mesh.child, callback, child_parents)

def dump_f3dex_dl(mesh, bank):
    # Libgarib display list format is a packed array
    # of {uint32_t n_bytes, uint8_t body[n_bytes]} records.
    #
    # The first record is a utf8-encoded JSON dictionary
    # which contains file metadata
    #
    # The second record is a reference table used to
    # provide a layer of addressing indirection between
    # the following segments of binary data. All pointers
    # within the following binary data are replaced with
    # indices into this table, which itself is a series of
    # {uint32_t pointer_type, uint32_t pointer} records.
    # The following pointer types are supported:
    #   - 0: Static value (implementation-defined meaning)
    #   - 1: Index into this file's binary records
    #   - 2: {uint16_t index, uint16_t offset} into this file's binary records
    #   - 3: Cross-file identifier
    #
    # The third record is a display list, implied to be the "root" display list
    # to be executed
    #
    # All fields are big-endian.
    #
    # TODO: implement all of the above

    if mesh.display_list is not None:
        metadata = json.dumps({
            "lgdl-version": 0.1,
            "microcode-version": "F3DEX",
        })
        metadata = struct.pack(">I", len(metadata)) + bytearray(metadata)
        
        data_regions = []
        output = metadata

        raw_dl = bytearray(b"".join(struct.pack(">II", cmd.w1, cmd.w0) for cmd in mesh.display_list))

        output += struct.pack(">I", len(raw_dl))
        output += raw_dl

        offset = len(output)
        for cmd, args in F3DEX.parseList(raw_dl):
            if cmd is F3DEX.byName["G_VTX"]:
                # Replace addresses into vertex buffers with
                # an index into the TLV array
                region_offset = args["address"]
                region_size = args["length"]
                data_regions.append((region_offset, region_size))
                args["address"] = len(data_regions)
                output[offset:offset+8] = cmd.toBytes(args)
            elif (cmd is F3DEX.byName["G_MTX"]
             or cmd is F3DEX.byName["G_MOVEMEM"]
             or cmd is F3DEX.byName["G_DL"]
             or cmd is F3DEX.byName["G_BRANCH_Z"]):
                raise Exception("TODO: Not yet implemented: Export F3DEX command {:}".format(cmd))

            offset += 8
        for offset, size in data_regions:
            raw_dl += struct.pack(">I",size)
            raw_dl += bank[offset:offset+size]
        return raw_dl
    else:
        return b""

def mesh_to_ply(mesh):
    # TODO: explore use of sausage64?
    # https://github.com/buu342/N64-Sausage64/wiki/2)-The-S64-format

    def vert_data(idx):
        v = mesh.geometry.vertices[idx]
        out = [v.x, v.y, v.z]
        if mesh.geometry.colors_norms is not None:
            c = mesh.geometry.colors_norms[idx]
            out += ((c & 0xFF000000) >> 24,
                    (c & 0x00FF0000) >> 16,
                    (c & 0x0000FF00) >> 8)
        return tuple(out)
    vert_data_struct = [('x', 'f4'), ('y', 'f4'), ('z', 'f4')]
    if mesh.geometry.colors_norms is not None:
        vert_data_struct += [('red', 'u4'), ('green', 'u4'), ('blue', 'u4')]

    vertices = numpy.array([vert_data(idx) for idx in range(mesh.geometry.num_vertices)],
                         dtype=vert_data_struct)
    ply_vertices = plyfile.PlyElement.describe(vertices, 'vertex')


    def face_data(idx):
        f = mesh.geometry.faces[idx]
        out = [(f.v0, f.v1, f.v2)]
        if mesh.geometry.texture_ids is not None:
            out.append(mesh.geometry.texture_ids[idx])
        if mesh.geometry.uvs is not None:
            uv = mesh.geometry.uvs[idx]
            out += (uv.u1.value, uv.v1.value,
                    uv.u2.value, uv.v2.value,
                    uv.u3.value, uv.v3.value)
        if mesh.geometry.u1 is not None:
            norm = mesh.geometry.u1[idx]
            out += ((norm & 0xff000000) >> 24,
                    (norm & 0x00ff0000) >> 16,
                    (norm & 0x0000ff00) >> 8)
        return tuple(out)
    face_data_struct = [('vertex_indices', 'i4', (3,))]
    if mesh.geometry.texture_ids is not None:
        face_data_struct.append(('texture', 'u4'))
    if mesh.geometry.uvs is not None:
        face_data_struct += [('u1', 'f4'), ('v1', 'f4'),
                             ('u2', 'f4'), ('v2', 'f4'),
                             ('u3', 'f4'), ('v3', 'f4'),]
    if mesh.geometry.u1 is not None:
        face_data_struct += [('nx', 'f4'), ('ny', 'f4'), ('nz', 'f4')]

    faces = numpy.array([face_data(idx) for idx in range(mesh.geometry.num_faces)],
                         dtype=face_data_struct)
    ply_faces = plyfile.PlyElement.describe(faces, 'face')

    ply_file = io.BytesIO()
    plyfile.PlyData([ply_vertices, ply_faces], text=True).write(ply_file)
    return ply_file.getvalue()

import math
import struct
import sys

import io
import numpy
import plyfile

from .gbi import F3DEX
from .parsers.glover_objbank import GloverObjbank
from .parsers.construct import glover_objbank as objbank_writer

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
        child_parents += mesh
        for_each_mesh(mesh.child, callback, child_parents)

def dump_f3dex_dl(mesh, bank):
    if mesh.display_list is not None:
        data_regions = []
        output = bytearray(b"")

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
            # TODO: catch G_DL, G_MOVEMEM, etc
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

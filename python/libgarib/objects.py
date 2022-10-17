import dataclasses
import json
import math
import struct
import sys
import typing

import io
import numpy
import plyfile

from .gbi import F3DEX
from .parsers.glover_objbank import GloverObjbank
from .parsers.construct import glover_objbank as objbank_writer
from . import linkable

###############################################
# Bank packing utlities

class LinkableDirectory(linkable.LinkableBytes):
    actors: typing.List[typing.Tuple[Linkable, GloverObjbank.ObjectRoot]] = dataclasses.field(default_factory=list)

    def __init__(self):
        self.data = b""
        self.pointers = []

    def finalize(self):
        for actor, obj_root in self.actors:
            self.data += struct.pack(">I", obj_root.obj_id)
            self.pointers.append(linkable.LinkablePointer(
                offset=len(self.data),
                dtype=">I",
                target=actor
            ))
            self.data +=  b"\0" * 4
        self.data += b"\0" * 8


class LinkableDisplayList(linkable.LinkableStruct):
    dl: linkable.LinkableBytes
    vertex_data: typing.List[linkable.LinkableBytes]
    def finalize(self):
        self.data = [self.dl] + self.vertex_data
        super().finalize()

class LinkableGeometry(linkable.LinkableStruct):
    verts: linkable.LinkableBytes
    faces: linkable.LinkableBytes
    # TODO: what else?
    root: linkable.LinkableBytes
    def finalize(self):
        self.data = []
        if len(self.verts) > 0:
            self.data.append(self.verts)
        if len(self.faces) > 0:
            self.data.append(self.verts)
        self.data.append(self.root)
        super().finalize()

class LinkableObjectBank(linkable.LinkableStruct):
    directory: linkable.LinkableBytes
    display_lists: typing.List[LinkableDisplayList] = dataclasses.field(default_factory=list)
    geometries: typing.List[LinkableGeometry] = dataclasses.field(default_factory=list)
    keyframes: typing.List[linkable.LinkableBytes] = dataclasses.field(default_factory=list)
    sprites: typing.List[linkable.LinkableBytes] = dataclasses.field(default_factory=list)
    meshes: typing.List[linkable.LinkableBytes] = dataclasses.field(default_factory=list)
    anim_defs: typing.List[linkable.LinkableBytes] = dataclasses.field(default_factory=list)
    anim_props: typing.List[linkable.LinkableBytes] = dataclasses.field(default_factory=list)
    actors: typing.List[linkable.LinkableBytes] = dataclasses.field(default_factory=list)

    def finalize(self):
        # TODO: make sure structs get padded
        self.data = (
            [self.directory] +
            self.display_lists +
            self.geometries +
            self.keyframes + 
            self.sprites + 
            self.meshes + 
            self.anim_defs + 
            self.anim_props
            # TODO: mysterious 72B*n_mesh end padding?
        )
        super().finalize()

def parent_str(parents):
    return ".".join(map(lambda m: m.name.strip("\x00"), parents))

def for_each_mesh(mesh, callback, parents=None):
    if parents is None:
        parents = []
    cur_matrix = None # TODO
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
                region_size = args["length"] + 1
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

###############################################
# Bank mapping utlities

def kaitaiObjectRange(parent, field):
    if field is None:
        start_field = parent.SEQ_FIELDS[0]
        end_field = parent.SEQ_FIELDS[-1]
        return parent._debug[start_field]["start"], parent._debug[end_field]["end"]
    elif field in parent._debug:
        return parent._debug[field]["start"], parent._debug[field]["end"]
    else:
        getattr(parent, field) # Force lazy load of Kaitai object instance (grrl, ew)
        instance_name = "_m_{:}".format(field)
        return parent._debug[instance_name]["start"], parent._debug[instance_name]["end"]
    raise Exception(field)

@dataclasses.dataclass
class BankSegment:
    memory_range: typing.Tuple[int, int]
    dtype: str
    name: str

def scrapeBankSegments(bank_data):
    bank = GloverObjbank.from_bytes(bank_data)

    bank_map = []
    def bank_push(parent, field, dtype, name):
        if parent is None:
            return
        if field is not None:
            if not hasattr(parent, field):
                return
            if getattr(parent, field) is None:
                return
        bank_map.append(BankSegment(
            memory_range=kaitaiObjectRange(parent, field),
            dtype=dtype,
            name=name
        ))

    bank_push(bank, "directory", "Directory", "")
    for dir_entry in bank.directory:
        actor = dir_entry.obj_root
        if actor is None:
            continue
        bank_push(dir_entry, "obj_root", "Actor root", "{:08X}".format(dir_entry.obj_id))
        if actor.mesh is not None:

            def scrape_mesh(mesh, parents, cur_matrix):
                name = "{:08X}.".format(dir_entry.obj_id) + parent_str(parents + [mesh])
                bank_push(mesh, None, "Mesh", name)

                if mesh.geometry is not None:
                    geo = mesh.geometry
                    bank_push(mesh, "geometry", "Geometry root", name)
                    bank_push(geo, "u1", "Geometry (face normals)", name)
                    bank_push(geo, "vertices", "Geometry (vertices)", name)
                    bank_push(geo, "faces", "Geometry (faces)", name)
                    bank_push(geo, "uvs", "Geometry (UVs)", name)
                    bank_push(geo, "uvs_unmodified", "Geometry (UV original copies)", name)
                    bank_push(geo, "colors_norms", "Geometry (vertex colors)", name)
                    bank_push(geo, "u5", "Geometry (face properties)", name)
                    bank_push(geo, "texture_ids", "Geometry (texture ids)", name)
                bank_push(mesh, "sprites", "Sprites", name)
                bank_push(mesh, "scale", "Keyframes (scale)", name)
                bank_push(mesh, "translation", "Keyframes (translation)", name)
                bank_push(mesh, "rotation", "Keyframes (rotation)", name)
                bank_push(mesh, "display_list", "Display list", name)

                if mesh.display_list is not None:
                    def scrape_dl(file, offset):
                        base_offset = offset
                        while True:
                            cmd, cmd_args = F3DEX.parse(file[offset: offset+8])
                            offset += 8
                            if cmd is F3DEX.byName["G_ENDDL"]:
                                break
                            elif cmd is F3DEX.byName["G_VTX"]:
                                start = cmd_args["address"]
                                end = start + cmd_args["length"] + 1
                                bank_map.append(BankSegment(
                                    memory_range=(start, end),
                                    dtype="DL Vertex Data",
                                    name="{:}.dl.cmd[{:08X}]".format(name, offset)
                                ))
                            elif (cmd is F3DEX.byName["G_MTX"]
                             or cmd is F3DEX.byName["G_MOVEMEM"]
                             or cmd is F3DEX.byName["G_DL"]
                             or cmd is F3DEX.byName["G_BRANCH_Z"]):
                                raise Exception("TODO: Not yet implemented: Scrape F3DEX command {:}".format(cmd))
                    scrape_dl(bank_data, mesh._debug["_m_display_list"]["start"])


            for_each_mesh(actor.mesh, scrape_mesh)
        if actor.animation is not None:
            bank_push(actor, "animation", "Animation props", "{:08X}".format(dir_entry.obj_id))
            bank_push(actor.animation, "animation_definitions", "Animation defs", "{:08X}".format(dir_entry.obj_id))
    bank_map.sort(key=lambda s: s.memory_range[0])
    return bank_map

def fillGaps(segments, bank_data):
    gaps = []
    activeSegments = []

    def gapDtype(start, end):
        padding = True
        for addr in range(start, end):
            if bank_data[addr] != 0:
                padding = False
                break
        return "Padding" if padding else "???"


    for segment in segments:
        nextActiveSegments = [s for s in activeSegments if s.memory_range[1]  >= segment.memory_range[0]]
        if len(activeSegments) > 0 and len(nextActiveSegments) == 0:
            lastEnd = max(s.memory_range[1] for s in activeSegments)
            gap_range = (lastEnd, segment.memory_range[0])
            gaps.append(BankSegment(
                memory_range=gap_range,
                dtype=gapDtype(*gap_range),
                name=""
            ))
        activeSegments = nextActiveSegments
        activeSegments.append(segment)

    lastEnd = max(s.memory_range[1] for s in segments)
    if lastEnd != len(bank_data):
        gap_range = (lastEnd, len(bank_data))
        gaps.append(BankSegment(
            memory_range=gap_range,
            dtype=gapDtype(*gap_range),
            name=""
        ))

    segments = segments + gaps
    segments.sort(key=lambda s: s.memory_range[0])
    return segments

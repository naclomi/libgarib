import dataclasses
import json
import math
import struct
import sys
import typing

import io
import numpy as np
import plyfile
import pygltflib as gltf

from .gbi import F3DEX
from .parsers.glover_objbank import GloverObjbank
from .parsers.construct import glover_objbank as objbank_writer
from . import linkable

###############################################
# Bank packing utlities

class LinkableDirectory(linkable.LinkableBytes):
    def __init__(self):
        super().__init__(
            data = b"",
            pointers = []
        )
        self.actors: typing.Dict[int, linkable.Linkable] = {}

    def finalize(self):
        for obj_id, actor in self.actors.items():
            self.data += struct.pack(">I", obj_id)
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
    def __init__(self):
        super().__init__()
        self.directory: LinkableDirectory = LinkableDirectory()
        self.display_lists: typing.List[LinkableDisplayList] = []
        self.geometries: typing.List[LinkableGeometry] = []
        self.keyframes: typing.List[linkable.LinkableBytes] = []
        self.sprites: typing.List[linkable.LinkableBytes] = []
        self.meshes: typing.List[linkable.LinkableBytes] = []
        self.anim_defs: typing.List[linkable.LinkableBytes] = []
        self.anim_props: typing.List[linkable.LinkableBytes] = []
        self.actors: typing.List[linkable.LinkableBytes] = []

    def finalize(self):
        self.data = (
            [self.directory] +
            self.display_lists +
            self.geometries +
            self.keyframes + 
            self.sprites + 
            self.meshes + 
            self.anim_defs + 
            self.anim_props +
            self.actors
            # TODO: mysterious 72B*n_mesh end padding?
        )
        for segment in self.data:
            segment.parent = self
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

def getConstructFieldOffset(construct_struct, field_name):
    offset = 0
    for field in construct_struct.subcons:
        if field.name == field_name:
            return offset
        offset += field.sizeof()
    else:
        raise Exception("Field not found")

def packMesh(mesh, bank):
    pointers = []

    children = []
    for child in mesh["children"]:
        children.append(packMesh(child, bank))
        if len(children) > 1:
            children[-2].pointers.append(linkable.LinkablePointer(
                offset = getConstructFieldOffset(objbank_writer.glover_objbank__mesh, "sibling_ptr"),
                dtype = ">I",
                target = children[-1]
            ))
 
    if len(mesh.get("sprites", [])) > 0:
        raw_sprites = []
        for sprite in mesh["sprites"]:
            # {
            #         "texture_id": sprite.texture_id,
            #         "position": [sprite.x, sprite.y, sprite.z],
            #         "size": [sprite.width, sprite.height],
            #         "unknown1": sprite.u5, # TODO: ???
            #         "unknown2": sprite.u6, # TODO: ???
            #         "flags": sprite.flags
            #     })
            # TODO
            pass
        raw_sprites = b"".join(raw_sprites)
        sprites = linkable.LinkableBytes(data=raw_sprites)
        bank.sprites.append(sprites)
        pointers.append(linkable.LinkablePointer(
                offset = getConstructFieldOffset(objbank_writer.glover_objbank__mesh, "sprites_ptr"),
                dtype = ">I",
                target = sprites
        ))

    # TODO
    raw_mesh = b""
    # raw_mesh = objbank_writer.glover_objbank__mesh.build({
    #     # "id": , # / Int32ub,
    #     # "name": , # / FixedSized(8, GreedyString(encoding='ASCII')),
    #     # "unused": , # / Int8ub,
    #     # "alpha": , # / Int8ub,
    #     # "num_scale": , # / Int16ub,
    #     # "num_translation": , # / Int16ub,
    #     # "num_rotation": , # / Int16ub,
    #     # "geometry_ptr": , # / Int32ub,
    #     # "display_list_ptr": , # / Int32ub,
    #     # "scale_ptr": , # / Int32ub,
    #     # "translation_ptr": , # / Int32ub,
    #     # "rotation_ptr": , # / Int32ub,
    #     "num_sprites": len(mesh.get("sprites", [])), # / Int32ub,
    #     "sprites_ptr": 0,
    #     "num_children": len(children),
    #     # "render_mode": , # / Int16ub,
    #     "child_ptr": 0,
    #     "sibling_ptr": 0,
    #     # "runtime_collision_data_ptr": , # / Int32ub,
    #     "rotation": None,
    #     "geometry": None,
    #     "scale": None,
    #     "translation": None,
    #     "child": None,
    #     "sibling": None,
    #     "display_list": None,
    #     "sprites": None
    # })

    if len(children) > 0:
        pointers.append(linkable.LinkablePointer(
            offset = getConstructFieldOffset(objbank_writer.glover_objbank__mesh, "child_ptr"),
            dtype = ">I",
            target = children[0]
        ))
    return linkable.LinkableBytes(data=raw_mesh, pointers=pointers) 

def packActor(actor, bank):
    anim_props, anim_defs = actorAnimationFromJson(actor)
    bank.anim_defs.append(anim_defs)
    bank.anim_props.append(anim_props)

    root_mesh = packMesh(actor["mesh"], bank)
    bank.meshes.append(root_mesh)

    root_actor_raw = objbank_writer.glover_objbank__object_root.build({
        "obj_id": actor["id"],
        "bank_base_addr": 0,
        "u2": 0, # TODO: what does this do??
        "mesh_ptr": 0,
        "u3": 0, # TODO: what does this do??
        "u4": 0, # TODO: what does this do??
        "animation_ptr": 0,
        "mesh": None,
        "animation": None,
    })
    root_actor = linkable.LinkableBytes(
        data=root_actor_raw,
        pointers=[
            linkable.LinkablePointer(
                offset = getConstructFieldOffset(objbank_writer.glover_objbank__object_root, "animation_ptr"),
                dtype = ">I",
                target = anim_props
            ),
            linkable.LinkablePointer(
                offset = getConstructFieldOffset(objbank_writer.glover_objbank__object_root, "mesh_ptr"),
                dtype = ">I",
                target = root_mesh
            ),
        ]
    )
    bank.actors.append(root_actor)
    bank.directory.actors[actor["id"]] = root_actor

def actorAnimationFromJson(actor):
    raw_defs = b""
    for anim_def in actor["animations"]:
        raw_defs += objbank_writer.glover_objbank__animation_definition.build({
            "start_time": anim_def["start"],
            "end_time": anim_def["end"],
            "playback_speed": anim_def["speed"],
            "u1": anim_def["flags"],
        })
    defs = linkable.LinkableBytes(data=raw_defs, pointers=[])

    p = actor["animation_properties"]
    raw_props = objbank_writer.glover_objbank__animation.build({
        "num_animation_definitions": len(actor["animations"]),
        "current_animation_idx": p["starting_props"]["idx"],
        "is_playing": p["starting_props"]["is_playing"],
        "time_delta": p["starting_props"]["time_delta"],
        "next_anim_idx": [prop_set["idx"] for prop_set in p["prop_queue"]],
        "next_is_playing": [prop_set["is_playing"] for prop_set in p["prop_queue"]],
        "next_time_delta": [prop_set["time_delta"] for prop_set in p["prop_queue"]],
        "next_anim_slot_idx": p["prop_queue_ptr"],
        "cur_time": p["starting_time"],
        "pad": 0,
        "u3": p["unknown1"],
        "u15": p["unknown2"],
        "animation_definitions_ptr": 0,
        "animation_definitions": None
    })
    anim_ptr = linkable.LinkablePointer(
        offset = getConstructFieldOffset(objbank_writer.glover_objbank__animation, "animation_definitions_ptr"),
        dtype = ">I",
        target = defs
    )
    props = linkable.LinkableBytes(data=raw_defs, pointers=[anim_ptr])
    return props, defs


def actorAnimationToJson(obj):
    a = obj.animation
    animations = []

    def queue_idx_to_props(idx):
        return {
            "idx": a.next_anim_idx[idx],
            "is_playing": a.next_is_playing[idx] == 1,
            "time_delta": a.next_time_delta[idx],
        }
    properties = {
        "starting_props": {
            "idx": a.current_animation_idx,
            "is_playing": a.is_playing == 1, 
            "time_delta": a.time_delta,
        },
        "prop_queue": [
            queue_idx_to_props(x) for x in range(5)
        ],
        "unknown1": a.u3, # TODO: what does this do??
        "unknown2": a.u15, # TODO: what does this do??
        "prop_queue_ptr": a.next_anim_slot_idx,
        "starting_time": a.cur_time
    }
    for defn in obj.animation.animation_definitions or []:
        animations.append({
            "start": defn.start_time,
            "end": defn.end_time,
            "speed": defn.playback_speed,
            "flags": defn.u1, # TODO: what does this do??
        })
    return properties, animations

def dump_f3dex_dl(mesh, bank):
    # TODO: can we just import/export fast64 insertable binary
    #       format? it's undocumented but implemented here:
    #       https://github.com/projectcomet64/cometfast64/blob/797b07fa8f26e4101eec22ed5ba5ab037047679b/fast64_internal/utility.py#L414
    # TODO: or, maybe use this:
    #       https://github.com/engerb/Blender64
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
        }).encode()
        metadata = struct.pack(">I", len(metadata)) + metadata
        
        data_regions = []
        output = bytearray(metadata)

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

def transposeMap(fn, array):
    results = []
    for col_idx in range(len(array[0])):
        results.append(fn(*(row[col_idx] for row in array)))
    return results

def mesh_to_gltf(mesh):
    # Coalesce Glover-style per-vertex/per-face attributes into
    # glTF-style per-vertex/per-material attributes

    # Map texture/material to vertex attributes:
    primitives = {}
    def getMaterial(material):
        if material in primitives:
            return primitives[material]
        else:
            new_prim = {
                "indices": [],
                "positions": [],
                "colors": [],
                "uvs": [],
                "norms": [],
                "unknown": []
            }
            primitives[material] = new_prim
            return new_prim

    geo = mesh.geometry
    for face_idx in range(geo.num_faces):
        if mesh.geometry.texture_ids is not None:
            prims = getMaterial(mesh.geometry.texture_ids[face_idx])
        else:
            prims = getMaterial(0)
        prims["indices"] += (len(prims["positions"])+x for x in range(3))
        face = geo.faces[face_idx]
        for v_idx in (face.v0, face.v1, face.v2):
            v = geo.vertices[v_idx]
            prims["positions"].append((v.x, v.y, v.z))
            if mesh.geometry.colors_norms is not None:
                c = mesh.geometry.colors_norms[v_idx]
                prims["colors"].append((
                    ((c & 0xFF000000) >> 24) / 255,
                    ((c & 0x00FF0000) >> 16) / 255,
                    ((c & 0x0000FF00) >> 8) / 255
                ))
        if mesh.geometry.uvs is not None:
            uv = mesh.geometry.uvs[face_idx]
            prims["uvs"] += ((uv.u1.value, uv.v1.value),
                             (uv.u2.value, uv.v2.value),
                             (uv.u3.value, uv.v3.value))
        if mesh.geometry.u1 is not None:
            norm_raw = mesh.geometry.u1[face_idx]
            norm_byte = struct.unpack(">bbbb", struct.pack(">I",norm_raw))[:-1]
            norm_mag = math.sqrt(sum(coord ** 2 for coord in norm_byte))
            norm_norm = tuple(coord / norm_mag for coord in norm_byte)
            prims["norms"] += (norm_norm,) * 3
        if mesh.geometry.u5 is not None:
            # TODO: what is this data? how can we include it effectively?
            u5 = mesh.geometry.u5[face_idx]
            prims["unknown"] += ((u5,) * 3)


    ###############################################

    data_blobs = []
    def data_blob_offset():
        return sum(len(b) for b in data_blobs)
    accessors = []
    gltf_primitives = []
    bufferViews = []
    for material, prims in primitives.items():
        indices_data = b"".join(struct.pack("H", i) for i in prims["indices"])
        indices_bufferview_handle = len(bufferViews)
        bufferViews.append(gltf.BufferView(
            buffer=0,
            byteOffset=data_blob_offset(),
            byteLength=len(indices_data),
            target=gltf.ELEMENT_ARRAY_BUFFER,
        ))
        data_blobs.append(indices_data)

        indices_handle = len(accessors)
        accessors.append(gltf.Accessor(
            bufferView=indices_bufferview_handle,
            componentType=gltf.UNSIGNED_SHORT,
            count=len(prims["indices"]),
            type=gltf.SCALAR,
            max=[max(prims["indices"])],
            min=[min(prims["indices"])],
        ))

        # Build interleaved vertex data format
        attributes_bufferview_handle = len(bufferViews)
        vertex_struct_format = ""
        vertex_struct_sources = []
        gltf_attributes = {}

        def addAttributeToFormat(attrName, values, sources, componentType, elementSize, calcExtrema=True):
            nonlocal vertex_struct_format
            nonlocal vertex_struct_sources
            gltf_attributes[attrName] = len(accessors)
            if calcExtrema:
                extrema = {
                    "max": transposeMap(max, values),
                    "min": transposeMap(min, values)
                }
            else:
                extrema = {}
            accessors.append(gltf.Accessor(
                bufferView=attributes_bufferview_handle,
                componentType=componentType,
                count=len(values),
                type=elementSize,
                byteOffset=struct.calcsize(vertex_struct_format),
                **extrema
            ))
            vertex_struct_format += "{:}{:}".format(
                {gltf.SCALAR : 1,
                 gltf.VEC2 : 2,
                 gltf.VEC3 : 3,
                 gltf.VEC4 : 4}[elementSize],
                {gltf.FLOAT: "f",
                 gltf.SHORT: "h",
                 gltf.UNSIGNED_SHORT: "H",
                 gltf.BYTE: "b",
                 gltf.UNSIGNED_BYTE: "B",
                 gltf.UNSIGNED_INT: "I",
                }[componentType]
            )
            vertex_struct_sources += sources

        addAttributeToFormat(
            attrName="POSITION",
            values=prims["positions"],
            sources=(
                ("positions", ..., 0),
                ("positions", ..., 1),
                ("positions", ..., 2)
            ),
            componentType=gltf.FLOAT,
            elementSize=gltf.VEC3
        )

        if len(prims["colors"]) > 0:
            addAttributeToFormat(
                attrName="COLOR_0",
                values=prims["colors"],
                sources=(
                    ("colors", ..., 0),
                    ("colors", ..., 1),
                    ("colors", ..., 2),
                ),
                componentType=gltf.FLOAT,
                elementSize=gltf.VEC3
            )

        if len(prims["uvs"]) > 0:
            addAttributeToFormat(
                attrName="TEXCOORD_0",
                values=prims["uvs"],
                sources=(
                    ("uvs", ..., 0),
                    ("uvs", ..., 1),
                ),
                componentType=gltf.FLOAT,
                elementSize=gltf.VEC2
            )

        if len(prims["norms"]) > 0:
            addAttributeToFormat(
                attrName="NORMAL",
                values=prims["norms"],
                sources=(
                    ("norms", ..., 0),
                    ("norms", ..., 1),
                    ("norms", ..., 2),
                ),
                componentType=gltf.FLOAT,
                elementSize=gltf.VEC3
            )

        if len(prims["unknown"]) > 0:
            addAttributeToFormat(
                attrName="_GLOVER_FLAGS",
                values=prims["unknown"],
                sources=(
                    ("unknown", ...),
                ),
                componentType=gltf.UNSIGNED_INT,
                elementSize=gltf.SCALAR,
                calcExtrema=False
            )

        # Pack binary data
        vertex_data = []
        for idx in range(len(prims["positions"])):
            values = []
            for path in vertex_struct_sources:
                v = prims
                for key in path:
                    if key is ...:
                        key = idx
                    v = v.__getitem__(key)
                values.append(v)
            vertex_data.append(struct.pack(vertex_struct_format, *values))

        vertex_data = b"".join(vertex_data)
        bufferViews.append(gltf.BufferView(
            buffer=0,
            byteOffset=data_blob_offset(),
            byteLength=len(vertex_data),
            byteStride=struct.calcsize(vertex_struct_format),
            target=gltf.ARRAY_BUFFER,
        ))
        data_blobs.append(vertex_data)

        # Build GLTF primitive

        gltf_primitives.append(gltf.Primitive(
            attributes=gltf.Attributes(
                **gltf_attributes
            ),
            # material=material, # TODO
            indices=indices_handle
        ))

    data_blob = b"".join(data_blobs)

    # TODO: this superstruct eventually needs to be
    #       per-actor, not per-mesh
    # TODO: need to dump materials
    file = gltf.GLTF2(
        scene=0,
        scenes=[gltf.Scene(nodes=[0])],
        nodes=[gltf.Node(mesh=0)],
        meshes=[
            gltf.Mesh(primitives=gltf_primitives)
        ],
        accessors=accessors,
        bufferViews=bufferViews,
        buffers=[
            gltf.Buffer(byteLength=len(data_blob))
        ],
    )
    file.set_binary_blob(data_blob)

    return b"".join(file.save_to_bytes())

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

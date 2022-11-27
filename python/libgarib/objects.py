import dataclasses
import io
import json
import math
import struct
import sys
import typing

import numpy as np
import plyfile
import pygltflib as gltf
import pyrr

from .gbi import F3DEX
from .parsers.glover_objbank import GloverObjbank
from .parsers.construct import glover_objbank as objbank_writer
from . import linkable
from . import gltf_helper
from . import display_lists


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

def for_each_mesh(mesh, callback, cur_matrix=None, **kwargs):
    if cur_matrix is None:
        cur_matrix = pyrr.matrix44.Matrix44.identity()
    # TODO: matrix xforms
    updated_kwargs = callback(mesh, cur_matrix, **kwargs)
    if mesh.sibling is not None:
        for_each_mesh(mesh.sibling, callback, cur_matrix, **kwargs)
    if mesh.child is not None:
        child_kwargs = kwargs.copy()
        child_kwargs.update(updated_kwargs)
        for_each_mesh(mesh.child, callback, cur_matrix, **child_kwargs)

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


def actor_to_gltf(obj_root, texture_sizes):
    data = bytearray()
    root_node = gltf.Node()

    # TODO: add to top level extensionsUsed/extensionsRequired

    file = gltf.GLTF2(
        scene=0,
        scenes=[gltf.Scene(nodes=[0])],
        nodes=[root_node],
        samplers=[
            gltf.Sampler(
                magFilter=gltf.LINEAR,
                minFilter=gltf.LINEAR,
                wrapS=gltf.REPEAT,
                wrapT=gltf.REPEAT
            )
        ],
    )

    for_each_mesh(obj_root.mesh, mesh_to_gltf, file=file, gltf_parent=root_node, data=data, texture_sizes=texture_sizes)

    file.skins.append(
        gltf.Skin(
            skeleton=0,
            joints=list(range(len(file.nodes)))
        )
    )

    file.buffers.append(gltf.Buffer(byteLength=len(data)))
    file.set_binary_blob(bytes(data))
    return b"".join(file.save_to_bytes())

def mesh_geo_to_prims(geo, texture_sizes):
    # Coalesce Glover-style per-vertex/per-face attributes into
    # glTF-style per-vertex/per-material attributes

    # Map texture/material to vertex attributes:
    primitives = {}
 
    for face_idx in range(geo.num_faces):
        material = gltf_helper.Material()
        if geo.texture_ids is not None:
            material = material.mutate(
                texture_id=geo.texture_ids[face_idx]
            )
        prims = primitives.get(material, gltf_helper.MeshData())
        primitives[material] = prims
        prims.indices += (len(prims.positions)+x for x in range(3))
        face = geo.faces[face_idx]
        for v_idx in (face.v0, face.v1, face.v2):
            v = geo.vertices[v_idx]
            prims.positions.append((v.x, v.y, v.z))
            if geo.colors_norms is not None:
                c = geo.colors_norms[v_idx]
                prims.colors.append((
                    ((c & 0xFF000000) >> 24) / 255,
                    ((c & 0x00FF0000) >> 16) / 255,
                    ((c & 0x0000FF00) >> 8) / 255
                ))
        if geo.uvs is not None:
            uv = geo.uvs[face_idx]
            # TODO: these texture coordinates need
            #       to be normalized based on texture size,
            #       which is......unfortunate.
            #
            #       does that mean we need texture
            #       bank data to accurately dump object
            #       banks? shit.....
            prims.uvs += ((uv.u1.value, uv.v1.value),
                          (uv.u2.value, uv.v2.value),
                          (uv.u3.value, uv.v3.value))
        if geo.u1 is not None:
            norm_raw = geo.u1[face_idx]
            norm_byte = struct.unpack(">bbbb", struct.pack(">I",norm_raw))[:-1]
            norm_mag = math.sqrt(sum(coord ** 2 for coord in norm_byte))
            norm_norm = tuple(coord / norm_mag for coord in norm_byte)
            prims.norms += (norm_norm,) * 3
        if geo.u5 is not None:
            # TODO: what is this data? how can we include it effectively?
            # (11/13/22) This is more than likely the clamp and mirror flags
            #   for the texture face. They go unused in-game, because loadF3DEXTexture
            #   takes those settings directly from the texture file, rather
            #   than the mesh data. Format from GBI is {clamp bit, mirror bit},
            #   and because they go unused we can't tell which is S and which is T.
            #   Disappointing. /shrug
            u5 = geo.u5[face_idx]
            prims.unknown += ((u5,) * 3)

    return primitives

def mesh_to_gltf(mesh, cur_matrix, file, gltf_parent, data, texture_sizes):

    # TODO: choose based on selectable export strategy:
    if mesh.display_list is not None:
        lighting = (mesh.render_mode & 0x8) == 0 
        primitives = display_lists.f3dex_to_prims(mesh.display_list, mesh._io._io.getbuffer(), lighting, texture_sizes)
    elif mesh.geometry.num_faces > 0:
        primitives = mesh_geo_to_prims(mesh.geometry, texture_sizes)
    else:
        primitives = {}
        # TODO: dump animation and billboards anyway
        print("WARNING: No geometry for mesh {:}".format(mesh.name.strip("\0")))

    # TODO: link in display list binary URI, if applicable:
    gltf_mesh = gltf.Mesh(
        name=mesh.name.strip("\0"),
        extras={
            "id": "0x{:08X}".format(mesh.id),
            "render_mode": "0x{:X}".format(mesh.render_mode)
        }
    )

    gltf_helper.addMeshDataToGLTFMesh(primitives, gltf_mesh, file, data)

    # TODO: GLTF xform order is S->R->T, engine is R->T->S
    #       Make sure this node hierarchy reflects that:
    t = mesh.translation[0]
    r = mesh.rotation[0]
    s = mesh.scale[0]

    node_inheritance = {
        "EXT_transformation_inheritance": {"scale": False}
    }

    s_node = gltf.Node(
        name="{:}_SCALE".format(gltf_mesh.name),
        scale=(s.v1, s.v2, s.v3),
        extensions=node_inheritance
    )
    gltf_parent.children.append(len(file.nodes))
    file.nodes.append(s_node)

    mesh_node = gltf.Node(
        name=gltf_mesh.name,
        mesh=len(file.meshes),
        translation=(t.v1, t.v2, t.v3),
        rotation=(r.v1, r.v2, r.v3, r.v4),
    )
    s_node.children.append(len(file.nodes))
    file.nodes.append(mesh_node)

    file.meshes.append(gltf_mesh)

    channel_nodes = {
        "translation": mesh_node,
        "rotation": mesh_node,
        "scale": s_node,
    }
    gltf_helper.addAnimationDataToGLTF(mesh, channel_nodes, file, data)

    return {"gltf_parent": mesh_node}


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

            def scrape_mesh(mesh, cur_matrix, parents):
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
                return {"parents": parents + [mesh]}


            for_each_mesh(actor.mesh, scrape_mesh, parents=[])
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

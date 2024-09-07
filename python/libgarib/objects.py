import base64
import dataclasses
import enum
import json
import math
import struct
import typing

import numpy as np
import pygltflib as gltf

from .gbi import F3DEX
from .parsers.glover_objbank import GloverObjbank
from .parsers.construct import glover_objbank as objbank_writer
from . import hash as hash_str
from . import animation
from . import linkable
from . import gltf_helper
from . import display_lists
from . import objproxy


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
        self.data.clear()
        self.pointers = []
        for obj_id, actor in self.actors.items():
            self.data += struct.pack(">I", obj_id)
            self.pointers.append(linkable.LinkablePointer(
                offset=len(self.data),
                target=actor
            ))
            self.data += b"\0" * 4
        self.data += b"\0" * 8
        super().finalize()

class LinkableGeometryRoot(linkable.LinkableBytes):
    pass

class LinkableGeometry(linkable.LinkableStruct):
    def __init__(self):
        super().__init__()
        self.verts = None
        self.faces = None
        self.vertex_cn = None
        self.face_cn = None
        self.texture_ids = None
        self.uvs = None
        self.flags = None
        self.root = None

    def finalize(self):
        self.data = []
        for attr in (self.verts, self.faces,
            self.vertex_cn, self.face_cn,
            self.uvs, self.flags, self.texture_ids
        ):
            if attr is not None:
                self.data.append(attr)
                attr.parent = self
        self.data.append(self.root)
        self.root.parent = self
        super().finalize()

class LinkableKeyframes(linkable.LinkableBytes):
    pass

class LinkableSprites(linkable.LinkableBytes):
    pass

class LinkableMesh(linkable.LinkableBytes):
    pass

class LinkableAnimDefs(linkable.LinkableBytes):
    pass

class LinkableAnimProps(linkable.LinkableBytes):
    pass

class LinkableActor(linkable.LinkableBytes):
    pass

class LinkableObjectBank(linkable.LinkableStruct):
    def __init__(self):
        super().__init__()
        self.directory = LinkableDirectory()
        self.segments = {
            LinkableGeometry: [],
            LinkableKeyframes: [],
            LinkableSprites: [],
            LinkableMesh: [],
            LinkableAnimDefs: [],
            LinkableAnimProps: [],
            LinkableActor: [],
            display_lists.LinkableDisplayList: [],
        }

    def include(self, segment):
        self.segments[type(segment)].append(segment)

    def extract(self, obj_id): 
        self.finalize()
        segments = set()
        actor = self.directory.actors[obj_id]
        to_scan = [actor]
        while len(to_scan) > 0:
            node = to_scan.pop()
            if node in segments:
                continue
            segments.add(node)
            if isinstance(node, linkable.LinkableStruct):
                for member in node.data:
                    to_scan.append(member)
            if hasattr(node, "pointers"):
                for pointer in node.pointers:
                    if pointer.target is None or pointer.target is node:
                        continue
                    to_scan.append(pointer.target)

        new_bank = LinkableObjectBank()
        new_bank.directory.actors[obj_id] = actor

        for segment in segments:
            if type(segment) in new_bank.segments:
                new_bank.include(segment)

        return new_bank

    def delete(self, obj_id):
        self.finalize()
        segments = set()
        actor = self.directory.actors[obj_id]
        to_scan = [actor]
        while len(to_scan) > 0:
            node = to_scan.pop()
            if node in segments:
                continue
            segments.add(node)
            if isinstance(node, linkable.LinkableStruct):
                for member in node.data:
                    to_scan.append(member)
            if hasattr(node, "pointers"):
                for pointer in node.pointers:
                    if pointer.target is None or pointer.target is node:
                        continue
                    to_scan.append(pointer.target)

        for segment in segments:
            if type(segment) in self.segments:
                old_list = self.segments[type(segment)]
                new_list = [x for x in old_list if x is not segment]
                self.segments[type(segment)] = new_list

        del self.directory.actors[obj_id]

    def merge(self, other):
        for obj_id in other.directory.actors:
            if obj_id in self.directory.actors:
                self.delete(obj_id)
        self.directory.actors.update(other.directory.actors)
        for seg_type in self.segments.keys():
            self.segments[seg_type] += other.segments[seg_type]

    def finalize(self):
        # Maintain original bank ordering rather than just
        # a simple iteration over the segments dictionary:
        self.data = (
            [self.directory] +
            self.segments[display_lists.LinkableDisplayList] +
            self.segments[LinkableGeometry] +
            self.segments[LinkableKeyframes] +
            self.segments[LinkableSprites] +
            self.segments[LinkableMesh] +
            self.segments[LinkableAnimDefs] + 
            self.segments[LinkableAnimProps] +
            self.segments[LinkableActor]
            # TODO: mysterious 72B*n_mesh end padding?
        )
        for segment in self.data:
            segment.parent = self
        super().finalize()

def parent_str(parents):
    return ".".join(map(lambda m: m.name.strip("\x00"), parents))

def for_each_mesh(mesh, callback, **kwargs):
    if mesh is None:
        return
    try:
        updated_kwargs = callback(mesh, **kwargs)
        if mesh.sibling is not None:
            for_each_mesh(mesh.sibling, callback, **kwargs)
        if mesh.child is not None:
            child_kwargs = kwargs.copy()
            if updated_kwargs is not None:
                child_kwargs.update(updated_kwargs)
            for_each_mesh(mesh.child, callback, **child_kwargs)
    except Exception as e:
        if "_exception_handlers" in kwargs:
            for exc_type, handler in kwargs["_exception_handlers"].items():
                if isinstance(e, exc_type):
                    handler(e, mesh, **kwargs)
        else:
            raise e

def getConstructFieldOffset(construct_struct, field_name):
    offset = 0
    for field in construct_struct.subcons:
        if field.name == field_name:
            return offset
        offset += field.sizeof()
    else:
        raise Exception("Field not found")

def packSprite(sprite_idx, file, texture_db, scale_factor):
    sprite_node = file.nodes[sprite_idx]
    mesh = file.meshes[sprite_node.mesh]

    prims = gltf_helper.MeshData().loadFromGltf(mesh.primitives[0], file, texture_db)
    # TODO: do more than this half-assed validation:
    if len(mesh.primitives) != 1 or len(prims.indices) != 6:
        raise gltf_helper.GLTFStructureException("Sprite mesh must be a 2-polygon square")

    # TODO: also take xyz/scale from geo + scale factor

    return objbank_writer.glover_objbank__sprite.build({
        "texture_id": prims.material.texture_id, # / Int32ub,
        "runtime_data_ptr": 0,
        "x": sprite_node.translation[0] * scale_factor,
        "y": sprite_node.translation[1] * scale_factor,
        "z": sprite_node.translation[2] * scale_factor,
        "width": (sprite_node.scale[2 if sprite_node.scale[0] == 1 else 0]) * 3 * scale_factor, 
        "height": sprite_node.scale[1]*3*scale_factor, 
        "u5": 0, # TODO
        "u6": 0, # TODO
        "flags": 0, # TODO
    })

DEFAULT_PACK_LIST = ["display_list", "faces", "verts", "norms"]

def updatePackList(obj, pack_list):
    try:
        new_list = json.loads(obj.extras["pack_list"])
        pack_list.clear()
        pack_list += new_list
    except:
        pass

def packGeo(node_idx, bank, file, vertex_cache, pack_list):    
    node = file.nodes[node_idx]

    geo_root = LinkableGeometry()
    bank.include(geo_root)

    if should_pack_geo(pack_list):
        raw_geo_root = objbank_writer.glover_objbank__geometry.build({
            "num_faces": vertex_cache.face_count,
            "num_vertices": vertex_cache.vertex_count,
            "vertices_ptr": 0,
            "faces_ptr": 0,
            "face_cn_ptr": 0,
            "uvs_ptr": 0,
            "uvs_unmodified_ptr": 0,
            "vertex_cn_ptr": 0,
            "flags_ptr": 0,
            "texture_ids_ptr": 0,
            "texture_ids": None,
            "faces": None,
            "vertex_cn": None,
            "uvs_unmodified": None,
            "flags": None,
            "vertices": None,
            "uvs": None,
            "face_cn": None,
        })
        geo_root.root = LinkableGeometryRoot(
            data=raw_geo_root,
            pointers=[]
        )
        def setPtr(name, dst):
            geo_root.root.pointers.append(linkable.LinkablePointer(
                offset = getConstructFieldOffset(objbank_writer.glover_objbank__geometry, name),
                target = dst
            ))

        if vertex_cache.variants is not None:
            indices = vertex_cache.indices.copy() >> 2
        else:
            indices = vertex_cache.indices

        if "faces" in pack_list:
            geo_root.faces = linkable.LinkableBytes(data=indices.astype(">H").tobytes())
            setPtr("faces_ptr", geo_root.faces)
        if "verts" in pack_list:
            geo_root.verts = linkable.LinkableBytes(data=vertex_cache.position.astype(">f").tobytes())
            setPtr("vertices_ptr", geo_root.verts)
        if "colors" in pack_list:
            ubyte_values = (vertex_cache.color*255).astype("B")
            raw_colors = b"".join(struct.pack("4B", *color[:3], 0) for color in ubyte_values)
            geo_root.vertex_cn = linkable.LinkableBytes(data=raw_colors)
            setPtr("vertex_cn_ptr", geo_root.vertex_cn)
        if "norms" in pack_list:
            # Have to recalculate face norms
            raw_norms = []
            positions = vertex_cache.position
            for base_idx in range(0, vertex_cache.idx_count, 3):
                # Calculate ortho vector
                v0 = positions[indices[base_idx]]
                v1 = positions[indices[base_idx+1]]
                v2 = positions[indices[base_idx+2]]
                n = np.cross(v1-v0, v2-v0)

                # Normalize
                n_mag = math.sqrt(sum(n**2))
                n /= n_mag

                # Correct orientation
                v0n = vertex_cache.norm[indices[base_idx]]
                if np.dot(n, v0n) < 0:
                    n *= -1

                # Cast to s8 format
                n *= 127
                raw_norms.append(struct.pack("bbbB", *n.astype("b"), 0))

            geo_root.face_cn = linkable.LinkableBytes(data=b"".join(raw_norms))
            setPtr("face_cn_ptr", geo_root.face_cn)   
        if "flags" in pack_list:
            raw_attr = []
            flags = vertex_cache.flags
            for base_idx in range(0, vertex_cache.idx_count, 3):
                v0 = flags[indices[base_idx]]
                v1 = flags[indices[base_idx+1]]
                v2 = flags[indices[base_idx+2]]
                raw_attr.append(struct.pack("B", v0))
                if v1 != v2 or v1 != v0:
                    print("WARNING: Inconsistent vertex flags in {:}".format(node.name))
            geo_root.flags = linkable.LinkableBytes(data=b"".join(raw_attr))
            setPtr("flags_ptr", geo_root.flags)
        if "uvs" in pack_list or "texture_ids" in pack_list:
            if "textures" in pack_list:
                raw_attr = []
                for face_idx in range(vertex_cache.face_count):
                    t = vertex_cache.material[face_idx].texture_id
                    raw_attr.append(struct.pack(">I", t))
                geo_root.texture_ids = linkable.LinkableBytes(data=b"".join(raw_attr))
                setPtr("texture_ids_ptr", geo_root.texture_ids)

            if "uvs" in pack_list:
                uvs = vertex_cache.uv_scaled.copy()

                # Convert to 11.5 format
                uvs *= 32
                uvs = uvs.astype(">h")

                # Per-vertex -> per-face
                raw_attr = []
                for base_idx in range(0, vertex_cache.idx_count, 3):
                    v0 = uvs[indices[base_idx]]
                    v1 = uvs[indices[base_idx+1]]
                    v2 = uvs[indices[base_idx+2]]
                    raw_attr.append(struct.pack(">6h", *v0, *v1, *v2))
                geo_root.uvs = linkable.LinkableBytes(data=b"".join(raw_attr))
                setPtr("uvs_ptr", geo_root.uvs)
    else:
        geo_root.root = LinkableGeometryRoot(
            data=b"\0" * objbank_writer.glover_objbank__geometry.sizeof(),
            pointers=[]
        )

    return geo_root

def packAnimChannel(channel_data, bank):
    raw_keyframes = []
    values = channel_data[0]
    times = channel_data[1].astype("i")
    if values.shape[1] == 3:
        for idx in range(len(values)):
            raw_keyframes.append(struct.pack(">4fI", *values[idx], 0, times[idx]))
    elif values.shape[1] == 4:
        for idx in range(len(values)):
            raw_keyframes.append(struct.pack(">4fI", *values[idx], times[idx]))
    else:
        raise gltf_helper.GLTFStructureException("Unexpected animation format")
    raw_keyframes = b"".join(raw_keyframes)
    keyframes = LinkableKeyframes(data=raw_keyframes)
    bank.include(keyframes)
    return keyframes

def packNode(node_idx, bank, file, texture_db, dopesheet, scale_factor):
    node = file.nodes[node_idx]

    pack_list = DEFAULT_PACK_LIST[:]
    updatePackList(node, pack_list)

    pointers = []

    # Pack children

    children = []
    sprite_nodes = []
    for child_idx in node.children:
        if gltf_helper.gltfNodeIsBillboard(child_idx, file):
            sprite_nodes.append(child_idx)
        else:
            children.append(packNode(child_idx, bank, file, texture_db, dopesheet, scale_factor))
            if len(children) > 1:
                children[-2].pointers.append(linkable.LinkablePointer(
                    offset = getConstructFieldOffset(objbank_writer.glover_objbank__mesh, "sibling_ptr"),
                    target = children[-1]
                ))

    # Pack sprites
    if len(sprite_nodes) > 0:     
        raw_sprites = []
        sprite_alpha = None
        for sprite_idx in sprite_nodes:
            sprite_node = file.nodes[sprite_idx]
            if "alpha" in sprite_node.extras:
                if sprite_alpha is None:
                    sprite_alpha = sprite_node.extras["alpha"]
                elif sprite_alpha != sprite_node.extras["alpha"]:
                    print("WARNING: Inconsistent sprite alphas on {:}, only first will be used".format(node.name))
            raw_sprites.append(packSprite(sprite_idx, file, texture_db, scale_factor))
        if sprite_alpha is None:
            sprite_alpha = 0xFF

        raw_sprites = b"".join(raw_sprites)
        sprites = LinkableSprites(data=raw_sprites)
        bank.include(sprites)
        pointers.append(linkable.LinkablePointer(
            offset = getConstructFieldOffset(objbank_writer.glover_objbank__mesh, "sprites_ptr"),
            target = sprites
        ))
    else:
        sprite_alpha = 0

    # Set up mesh metadata
    mesh_id = hash_str.hash_str(node.name)
    
    
    if node.mesh is not None:
        gltf_mesh = file.meshes[node.mesh]

        mesh_pack_list = pack_list[:]
        updatePackList(gltf_mesh, mesh_pack_list)


        render_mode = RenderMode()
        render_mode.ripple = bool(gltf_mesh.extras.get("ripple", 0))
        render_mode.sync_to_global_clock = bool(gltf_mesh.extras.get("sync_to_global_clock", 0))
        render_mode.cloud = bool(gltf_mesh.extras.get("cloud", 0))

        first_material = True
        for prims in gltf_mesh.primitives:
            if prims.material is None:
                xlu = False
                masked = False
                unlit = False
            else:
                material = file.materials[prims.material]
                xlu = material.alphaMode == gltf.BLEND
                masked = material.alphaMode == gltf.MASK
                unlit = ("KHR_materials_unlit" in material.extensions or
                         int(material.extras.get("unlit", "0")) == 1)
            if first_material:
                render_mode.xlu = xlu
                render_mode.masked = masked
                render_mode.unlit = unlit
                first_material = False
            else:
                if (render_mode.xlu != xlu or
                    render_mode.masked != masked or
                    render_mode.unlit != unlit):
                    print("WARNING: Inconsistent render mode across materials in node {:}".format(node.name))

        if "display_list" not in mesh_pack_list:
            render_mode.per_vertex_cn = render_mode.unlit
            if render_mode.per_vertex_cn and "colors" not in mesh_pack_list:
                print("WARNING: Unlit dynamic meshes need vertex colors in pack list, game may crash")
            elif not render_mode.per_vertex_cn and "norms" not in mesh_pack_list:
                print("WARNING: Lit dynamic meshes need normals in pack list, game may crash")

        render_mode = render_mode.toInt()
        if "render_mode" in gltf_mesh.extras:
            render_misc = gltf_mesh.extras["render_mode"]
            render_misc_mask = gltf_mesh.extras.get("render_mode_mask", 0xFFFF)
            render_misc &= render_misc_mask
            render_mode = (render_mode & ~render_misc_mask) | render_misc
    else:
        render_mode = 0

    # Pack mesh

    scale_keys = dopesheet["scale"].get(node_idx,
        animation.vec3ToNeutralFrame(node.scale or (1,1,1)))
    translation_keys = dopesheet["translation"].get(node_idx,
        animation.vec3ToNeutralFrame(node.translation or (0,0,0)))
    animation.scale_channel(translation_keys, scale_factor)
    rotation_keys = dopesheet["rotation"].get(node_idx,
        animation.vec4ToNeutralFrame(node.rotation or (0,0,0,0)))

    raw_mesh = b""
    raw_mesh = objbank_writer.glover_objbank__mesh.build({
        "id": mesh_id,
        "name": node.name[:8].ljust(8, "\0"),
        # TODO: figure out alpha
        "mesh_alpha": 0, #node.extras.get("alpha", 0xFF),
        "sprite_alpha": node.extras.get("alpha", 0xFF), #sprite_alpha,
        "num_scale": len(scale_keys[0]),
        "num_translation": len(translation_keys[0]),
        "num_rotation": len(rotation_keys[0]),
        "geometry_ptr": 0,
        "display_list_ptr": 0,
        "scale_ptr": 0,
        "translation_ptr": 0,
        "rotation_ptr": 0,
        "num_sprites": len(sprite_nodes),
        "sprites_ptr": 0,
        "num_children": len(children),
        "render_mode": render_mode,
        "child_ptr": 0,
        "sibling_ptr": 0,
        "runtime_collision_data_ptr": 0,
        "rotation": None,
        "geometry": None,
        "scale": None,
        "translation": None,
        "child": None,
        "sibling": None,
        "display_list": None,
        "sprites": None
    })

    # Pack TRS/animation
    pointers.append(linkable.LinkablePointer(
        offset = getConstructFieldOffset(objbank_writer.glover_objbank__mesh, "translation_ptr"),
        target = packAnimChannel(translation_keys, bank),
    ))
    pointers.append(linkable.LinkablePointer(
        offset = getConstructFieldOffset(objbank_writer.glover_objbank__mesh, "rotation_ptr"),
        target = packAnimChannel(rotation_keys, bank),
    ))
    pointers.append(linkable.LinkablePointer(
        offset = getConstructFieldOffset(objbank_writer.glover_objbank__mesh, "scale_ptr"),
        target = packAnimChannel(scale_keys, bank),
    ))

    if node.mesh is not None:
        # Pack geo
        mesh = file.meshes[node.mesh]
        updatePackList(mesh, pack_list)

        prims = [gltf_helper.MeshData().loadFromGltf(p, file, texture_db) for p in mesh.primitives]

        for prim in prims:
            prim.optimize()

        for prim in prims:
            prim.position *= scale_factor

        vertex_cache = gltf_helper.MeshData.flatten(prims)

        geo_root = packGeo(node_idx, bank, file, vertex_cache, pack_list)
        pointers.append(linkable.LinkablePointer(
            offset = getConstructFieldOffset(objbank_writer.glover_objbank__mesh, "geometry_ptr"),
            target = geo_root,
            target_offset = geo_root.root
        ))

        # Pack DL
        if "display_list" in pack_list:
            if RenderMode().fromInt(render_mode).ripple:
                print("WARNING: Static display list will take precedence over water ripple effect in node {:}".format(node.name))
            display_list, dl_start_offset = display_lists.gltfNodeToDisplayList(node_idx, RenderMode().fromInt(render_mode), bank, file, texture_db, vertex_cache)
            pointers.append(linkable.LinkablePointer(
                offset = getConstructFieldOffset(objbank_writer.glover_objbank__mesh, "display_list_ptr"),
                target = display_list,
                target_offset = dl_start_offset
            ))

    # Fix up child ptr
    if len(children) > 0:
        pointers.append(linkable.LinkablePointer(
            offset = getConstructFieldOffset(objbank_writer.glover_objbank__mesh, "child_ptr"),
            target = children[0]
        ))

    # Finalize structure
    linkable_mesh = LinkableMesh(data=raw_mesh, pointers=pointers) 
    bank.include(linkable_mesh)
    return linkable_mesh


def actorAnimationMetadataFromJson(props_json, num_defs):
    if props_json is not None:
        p = json.loads(props_json)
        raw_props = objbank_writer.glover_objbank__animation.build({
            "num_animation_definitions": num_defs,
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
    else:
        raw_props = b"\0" * objbank_writer.glover_objbank__animation.sizeof()
    props = LinkableAnimProps(data=raw_props, pointers=[])
    return props


def actorAnimationMetadataToJson(obj):
    a = obj.animation
    
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
    
    return properties

def setupActorAnimations(file, root_node_idx, bank):
    root_node = file.nodes[root_node_idx]

    # Find relevant animations
    all_nodes = gltf_helper.getAllNodesInTree(file, root_node_idx)

    relevant_animations = []
    for gltf_animation in file.animations:
        for channel in gltf_animation:
            if channel.target.node in all_nodes:
                relevant_animations.append(gltf_animation)
                break

    # Build global timeline

    raw_defs = []
    global_time = 0
    dopesheet = {
        "translation": {},
        "rotation": {},
        "scale": {}
    }

    for gltf_animation in relevant_animations:
        if "slot" not in gltf_animation.extras:
            print("WARNING: Not packing animation '{:}' as it has no slot assignment".format(animation.name))
            continue
        slots = json.loads(gltf_animation.extras["slot"])
        if not isinstance(slots, list):
            slots = [slots]

        anim_end = 0
        for channel in gltf_animation:
            sampler = gltf_animation.samplers[channel.sampler]
            key_data = gltf_helper.getDataFromAccessor(file, sampler.input)
            key_times = gltf_helper.getDataFromAccessor(file, sampler.output)

            ##########
            # TODO: automate
            scale_value = 1.0
            playback_speed = gltf_animation.extras.get("playback_speed", 1.0)
            ##########

            key_times *= scale_value
            key_times += global_time

            dopesheet_channel = dopesheet[channel.target.path].get(channel.target.node, [np.array(),np.array()])
            dopesheet_channel[0] = np.concat(dopesheet_channel[0], key_data)
            dopesheet_channel[1] = np.concat(dopesheet_channel[1], key_data)
            dopesheet[channel.target.path][channel.target.node] = dopesheet_channel

            anim_end = max(anim_end, max(key_times))

        for slot in slots:
            if len(raw_defs) <= slot:
                raw_defs += [None] * (len(raw_defs) - slot + 1)
            raw_defs[slot] = objbank_writer.glover_objbank__animation_definition.build({
                "start_time": global_time,
                "end_time": anim_end,
                "playback_speed": playback_speed,
                "unused": 0,
            })

        global_time = anim_end + 1


    # Default animation:
    default_anim_def = objbank_writer.glover_objbank__animation_definition.build({
        "start_time": 0,
        "end_time": global_time,
        "playback_speed": 1.0,
        "unused": 0,
    })

    for idx in range(len(raw_defs)):
        if raw_defs[idx] is None:
            raw_defs[idx] = default_anim_def

    anim_props = actorAnimationMetadataFromJson(root_node.extras.get("animation_props"), len(raw_defs))
    bank.include(anim_props)

    if len(raw_defs) > 0:
        anim_defs = LinkableAnimDefs(data=b"".join(raw_defs), pointers=[])
        bank.include(anim_defs)
        anim_props.pointers.append(linkable.LinkablePointer(
            offset = getConstructFieldOffset(objbank_writer.glover_objbank__animation, "animation_definitions_ptr"),
            target = anim_defs
        ))


    return dopesheet, anim_props


def packActor(file, bank, texture_db, override_scale_factor):
    for node_idx in file.scenes[file.scene].nodes:

        root_node = file.nodes[node_idx]

        if override_scale_factor is not None:
            scale_factor = override_scale_factor
        else:
            scale_factor = root_node.extras.get("scale_factor", 1.0)

        obj_id = root_node.extras.get("id", None)
        if obj_id is None:
            obj_id = hash_str.hash_str(root_node.name)

        # Pack animations
        anim_dopesheet, anim_data = setupActorAnimations(file, node_idx, bank)

        # Pack mesh data
        root_mesh = packNode(node_idx, bank, file, texture_db, anim_dopesheet, scale_factor)

        root_actor_raw = objbank_writer.glover_objbank__object_root.build({
            "obj_id": obj_id,
            "bank_base_addr": 0,
            "u2": 0,
            "mesh_ptr": 0,
            "u3": 0,
            "u4": 0,
            "animation_ptr": 0,
            "mesh": None,
            "animation": None,
        })
        root_actor = LinkableActor(
            data=root_actor_raw,
            pointers=[
                linkable.LinkablePointer(
                    offset = getConstructFieldOffset(objbank_writer.glover_objbank__object_root, "animation_ptr"),
                    target = anim_data
                ),
                linkable.LinkablePointer(
                    offset = getConstructFieldOffset(objbank_writer.glover_objbank__object_root, "mesh_ptr"),
                    target = root_mesh
                ),
            ]
        )
        bank.include(root_actor)
        bank.directory.actors[obj_id] = root_actor

###########################################
## Bank manipulation

def kaitaiObjectToBytes(parent, field=None):
    if field is None:
        start_pos = parent._debug[parent.SEQ_FIELDS[0]]["start"]
        end_pos = parent._debug[parent.SEQ_FIELDS[-1]]["end"]
    elif field in parent._debug:
        start_pos = parent._debug[field]["start"]
        end_pos = parent._debug[field]["end"]
    else:
        getattr(parent, field) # Force lazy load of Kaitai object instance (grrl, ew)
        instance_name = "_m_{:}".format(field)
        start_pos = parent._debug[instance_name]["start"]
        end_pos = parent._debug[instance_name]["end"]

    old_pos = parent._io.pos()
    parent._io.seek(start_pos)
    data = parent._io.read_bytes(end_pos - start_pos)
    parent._io.seek(old_pos)
    return data

def getKaitaiFieldOffset(kaitai_obj, field_name):
    struct_start_pos = kaitai_obj._debug[kaitai_obj.SEQ_FIELDS[0]]["start"]
    field_start_pos = kaitai_obj._debug[field_name]["start"]
    return field_start_pos - struct_start_pos

def kaitaiAnimDataToLinkable(kaitai_anim, bank):
    anim_props = LinkableAnimProps(data=kaitaiObjectToBytes(kaitai_anim), pointers=[])
    bank.include(anim_props)

    if kaitai_anim.animation_definitions is not None:
        anim_defs = LinkableAnimDefs(data=kaitaiObjectToBytes(kaitai_anim, "animation_definitions"), pointers=[])
        bank.include(anim_defs)

        anim_props.pointers.append(linkable.LinkablePointer(
            offset = getKaitaiFieldOffset(kaitai_anim, "animation_definitions_ptr"),
            target = anim_defs
        ))

    return anim_props

def kaitaiMeshToLinkable(kaitai_mesh, bank):
    linkable_mesh = LinkableMesh(data=kaitaiObjectToBytes(kaitai_mesh), pointers=[])
    bank.include(linkable_mesh)

    if kaitai_mesh.geometry is not None:
        geo = kaitai_mesh.geometry

        linkable_geo = LinkableGeometry()
        linkable_geo.root = LinkableGeometryRoot(
            data=kaitaiObjectToBytes(geo), pointers=[])

        if geo.vertices is not None:
            linkable_geo.verts = linkable.LinkableBytes(data=kaitaiObjectToBytes(geo, "vertices"), pointers=[])
            linkable_geo.root.pointers.append(linkable.LinkablePointer(
                offset = getKaitaiFieldOffset(geo, "vertices_ptr"),
                target = linkable_geo.verts
            ))

        if geo.faces is not None:
            linkable_geo.faces = linkable.LinkableBytes(data=kaitaiObjectToBytes(geo, "faces"), pointers=[])
            linkable_geo.root.pointers.append(linkable.LinkablePointer(
                offset = getKaitaiFieldOffset(geo, "faces_ptr"),
                target = linkable_geo.faces
            ))

        if geo.face_cn is not None:
            linkable_geo.face_cn = linkable.LinkableBytes(data=kaitaiObjectToBytes(geo, "face_cn"), pointers=[])
            linkable_geo.root.pointers.append(linkable.LinkablePointer(
                offset = getKaitaiFieldOffset(geo, "face_cn_ptr"),
                target = linkable_geo.face_cn
            ))

        if geo.vertex_cn is not None:
            linkable_geo.vertex_cn = linkable.LinkableBytes(data=kaitaiObjectToBytes(geo, "vertex_cn"), pointers=[])
            linkable_geo.root.pointers.append(linkable.LinkablePointer(
                offset = getKaitaiFieldOffset(geo, "vertex_cn_ptr"),
                target = linkable_geo.vertex_cn
            ))

        if geo.uvs is not None:
            linkable_geo.uvs = linkable.LinkableBytes(data=kaitaiObjectToBytes(geo, "uvs"), pointers=[])
            linkable_geo.root.pointers.append(linkable.LinkablePointer(
                offset = getKaitaiFieldOffset(geo, "uvs_ptr"),
                target = linkable_geo.uvs
            ))

        if geo.flags is not None:
            linkable_geo.flags = linkable.LinkableBytes(data=kaitaiObjectToBytes(geo, "flags"), pointers=[])
            linkable_geo.root.pointers.append(linkable.LinkablePointer(
                offset = getKaitaiFieldOffset(geo, "flags_ptr"),
                target = linkable_geo.flags
            ))


        if geo.texture_ids is not None:
            linkable_geo.texture_ids = linkable.LinkableBytes(data=kaitaiObjectToBytes(geo, "texture_ids"), pointers=[])
            linkable_geo.root.pointers.append(linkable.LinkablePointer(
                offset = getKaitaiFieldOffset(geo, "texture_ids_ptr"),
                target = linkable_geo.texture_ids
            ))

        bank.include(linkable_geo)
        linkable_mesh.pointers.append(linkable.LinkablePointer(
            offset = getKaitaiFieldOffset(kaitai_mesh, "geometry_ptr"),
            target = linkable_geo,
            target_offset = linkable_geo.root
        ))


    if kaitai_mesh.display_list is not None:
        raw_dl = display_lists.dump_f3dex_dl(kaitai_mesh.display_list)
        linkable_dl, dl_offset = display_lists.relocatableDisplayListToLinkable(raw_dl)
        bank.include(linkable_dl)
        linkable_mesh.pointers.append(linkable.LinkablePointer(
            offset = getKaitaiFieldOffset(kaitai_mesh, "display_list_ptr"),
            target = linkable_dl,
            target_offset = dl_offset
        ))

    if kaitai_mesh.sprites is not None:
        sprites = LinkableSprites(data=kaitaiObjectToBytes(kaitai_mesh, "sprites"))
        bank.include(sprites)
        linkable_mesh.pointers.append(linkable.LinkablePointer(
            offset = getKaitaiFieldOffset(kaitai_mesh, "sprites_ptr"),
            target = sprites
        ))

    if kaitai_mesh.translation is not None:
        keyframes = LinkableKeyframes(data=kaitaiObjectToBytes(kaitai_mesh, "translation"))
        bank.include(keyframes)
        linkable_mesh.pointers.append(linkable.LinkablePointer(
            offset = getKaitaiFieldOffset(kaitai_mesh, "translation_ptr"),
            target = keyframes
        ))

    if kaitai_mesh.rotation is not None:
        keyframes = LinkableKeyframes(data=kaitaiObjectToBytes(kaitai_mesh, "rotation"))
        bank.include(keyframes)
        linkable_mesh.pointers.append(linkable.LinkablePointer(
            offset = getKaitaiFieldOffset(kaitai_mesh, "rotation_ptr"),
            target = keyframes
        ))

    if kaitai_mesh.scale is not None:
        keyframes = LinkableKeyframes(data=kaitaiObjectToBytes(kaitai_mesh, "scale"))
        bank.include(keyframes)
        linkable_mesh.pointers.append(linkable.LinkablePointer(
            offset = getKaitaiFieldOffset(kaitai_mesh, "scale_ptr"),
            target = keyframes
        ))

    if kaitai_mesh.child is not None:
        linkable_mesh.pointers.append(linkable.LinkablePointer(
            offset = getKaitaiFieldOffset(kaitai_mesh, "child_ptr"),
            target = kaitaiMeshToLinkable(kaitai_mesh.child, bank)
        ))

    if kaitai_mesh.sibling is not None:
        linkable_mesh.pointers.append(linkable.LinkablePointer(
            offset = getKaitaiFieldOffset(kaitai_mesh, "sibling_ptr"),
            target = kaitaiMeshToLinkable(kaitai_mesh.sibling, bank)
        ))

    return linkable_mesh

def kaitaiActorToLinkable(kaitai_obj, bank):
    actor = LinkableActor(data=kaitaiObjectToBytes(kaitai_obj), pointers=[])
    if kaitai_obj.animation is not None:
        actor.pointers.append(linkable.LinkablePointer(
            offset = getKaitaiFieldOffset(kaitai_obj, "animation_ptr"),
            target = kaitaiAnimDataToLinkable(kaitai_obj.animation, bank)
        ))
    if kaitai_obj.mesh is not None:
        actor.pointers.append(linkable.LinkablePointer(
            offset = getKaitaiFieldOffset(kaitai_obj, "mesh_ptr"),
            target = kaitaiMeshToLinkable(kaitai_obj.mesh, bank)
        ))
    bank.include(actor)
    return actor

def kaitaiBankToLinkable(kaitai_bank):
    bank = LinkableObjectBank()
    for entry in kaitai_bank.directory:
        obj = entry.obj_root
        if obj is None:
            continue
        linkable_obj = kaitaiActorToLinkable(obj, bank)
        bank.directory.actors[entry.obj_id] = linkable_obj
    return bank

###########################################
## Dumping utilities

def actor_to_gltf(obj_root, texture_db, scale_factor):
    data = bytearray()
    root_node = gltf.Node(
        name="0x{:08X}".format(obj_root.obj_id),
        extras={
            "_root_node": True,
            "scale_factor": scale_factor
        }
    )

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

    # Export model data

    for_each_mesh(obj_root.mesh, mesh_to_gltf, file=file, gltf_parent=root_node, data=data, texture_db=texture_db, scale_factor=scale_factor)

    # Finalize rig

    skeletal_nodes = []
    billboard_nodes = []
    for idx, node in enumerate(file.nodes):
        is_billboard = file.meshes[node.mesh].extras.get("billboard", False) if node.mesh is not None else False
        if node.mesh is None or not is_billboard:
            # Only include non-billboard nodes in skin
            skeletal_nodes.append(idx)
        if is_billboard:
            billboard_nodes.append(idx)

    is_skeletal = obj_root.mesh.child is not None or obj_root.mesh.sibling is not None

    if is_skeletal:
        file.skins.append(
            gltf.Skin(
                skeleton=0,
                joints=skeletal_nodes
            )
        )

    if any(gltf_helper.TSR_INHERITANCE_EXTENSION in n.extensions for n in file.nodes):
        file.extensionsUsed.append(gltf_helper.TSR_INHERITANCE_EXTENSION)
        file.extensionsRequired.append(gltf_helper.TSR_INHERITANCE_EXTENSION)

    if any("KHR_materials_unlit" in m.extensions for m in file.materials):
        file.extensionsUsed.append("KHR_materials_unlit")

    # Export animations
    exported_anims = {}
    for idx, anim in enumerate(obj_root.animation.animation_definitions or []):
        key = (anim.start_time, anim.end_time, anim.playback_speed, anim.unused)
        if key not in exported_anims:
            exported_anims[key] = len(file.animations)
            animation_to_gltf(anim, obj_root.mesh, file, data, scale_factor)
            file.animations[exported_anims[key]].extras["slot"] = []
        file.animations[exported_anims[key]].extras["slot"].append(idx)
        file.animations[exported_anims[key]].name += "_{:}".format(idx)

    for anim_idx in exported_anims.values():
        slots = file.animations[anim_idx].extras["slot"]
        if len(slots) == 1:
            file.animations[anim_idx].extras["slot"] = str(slots[0])
        else:
            file.animations[anim_idx].extras["slot"] = json.dumps(slots)

    if len(exported_anims) > 0:
        global_timeline_to_gltf(obj_root.mesh, file, data)

    animation_props = actorAnimationMetadataToJson(obj_root)
    file.nodes[0].extras["animation_props"] = json.dumps(animation_props)

    # Finalize binary data
    file.buffers.append(gltf.Buffer(byteLength=len(data)))
    file.set_binary_blob(bytes(data))

    # Clean up internal properties
    for node in file.nodes:
        for key in list(node.extras.keys()):
            if key.startswith("_"):
                del node.extras[key]

    # Go through and compute all necessary mesh hashes, now that buffers are constructed
    for mesh in file.meshes:
        if "data_hash" in mesh.extras:
            mesh.extras["data_hash"] = gltf_helper.hashGLTFMesh(mesh, file).hexdigest()

    return b"".join(file.save_to_bytes())

def mesh_geo_to_prims(geo, render_mode, texture_db, scale_factor):
    # Coalesce Glover-style per-vertex/per-face attributes into
    # glTF-style per-vertex/per-material attributes

    primitives = []
 
    faces_by_material = {}
    for face_idx in range(geo.num_faces):
        material = gltf_helper.Material()
        if geo.texture_ids is not None:
            material = material.mutate(
                texture_id=geo.texture_ids[face_idx]
            )
        faces_by_material[material] = faces_by_material.get(material, [])
        faces_by_material[material].append(face_idx)

    for material, face_list in faces_by_material.items():
        prims = gltf_helper.MeshData()
        primitives.append(prims)

        prims.face_count = len(face_list)
        prims.vertex_count = prims.face_count * 3
        prims.idx_count = prims.face_count * 3

        prims.material = material
        if prims.material.texture_id is not None:
            prims.texture = texture_db.byId.get(prims.material.texture_id)
            if prims.texture is None:
                raise Exception("Need dimensions of texture 0x{:08X}".format(material.texture_id))

        prims.indices = np.arange(len(face_list)*3, dtype="H")

        attr_cursor = 0
        for face_idx in face_list:
            face = geo.faces[face_idx]
            for loop_it, v_idx in ((0, face.v0), (1, face.v1), (2, face.v2)):
                v = geo.vertices[v_idx]
                prims.position[attr_cursor + loop_it] = (
                    v.x / scale_factor,
                    v.y / scale_factor,
                    v.z / scale_factor
                )
                if geo.vertex_cn is not None:
                    raw_color = geo.vertex_cn[v_idx]
                    prims.color[attr_cursor + loop_it] = (
                        ((raw_color & 0xFF000000) >> 24) / 255,
                        ((raw_color & 0x00FF0000) >> 16) / 255,
                        ((raw_color & 0x0000FF00) >> 8) / 255,
                        1
                )

            if geo.uvs is not None:
                uv = geo.uvs[face_idx]
                prims.uv_scaled[attr_cursor:attr_cursor+3] = (
                    (uv.u1.value, uv.v1.value),
                    (uv.u2.value, uv.v2.value),
                    (uv.u3.value, uv.v3.value)
                )
                prims.uv[attr_cursor:attr_cursor+3] = prims.uv[attr_cursor:attr_cursor+3]
                prims.uv[attr_cursor:attr_cursor+3] /= (prims.texture.width, prims.texture.height)

            if geo.face_cn is not None:
                face_cn = geo.face_cn[face_idx]
                norm_byte = struct.unpack(">bbbb", struct.pack(">I",face_cn))[:-1]
                norm_mag = math.sqrt(sum(coord ** 2 for coord in norm_byte))
                norm_norm = tuple(coord / norm_mag for coord in norm_byte)
                prims.norm[attr_cursor:attr_cursor+3] = (
                    norm_norm,
                    norm_norm,
                    norm_norm,
                )

            if geo.flags is not None:
                # TODO: what is this data? how can we include it effectively?
                # (11/13/22) This is more than likely the clamp and mirror flags
                #   for the texture face. They go unused in-game, because loadF3DEXTexture
                #   takes those settings directly from the texture file, rather
                #   than the mesh data. Format from GBI is {clamp bit, mirror bit},
                #   and because they go unused we can't tell which is S and which is T.
                #   Disappointing. /shrug
                flags = geo.flags[face_idx]
                prims.flags[attr_cursor:attr_cursor+3] = (
                    (flags,0),
                    (flags,0),
                    (flags,0)
                )

            attr_cursor += 3

    return primitives

def should_pack_geo(pack_list):
    return len(set(("faces", "verts", "colors", "uvs", "norms", "flags", "textures")).intersection(set(pack_list))) > 0

def mesh_to_pack_list(mesh):
    pack_list = []
    if mesh.geometry is not None:
        geo = mesh.geometry
        if geo.num_faces > 0:
            pack_list.append("faces")
        if geo.num_vertices > 0:
            pack_list.append("verts")
        if geo.vertex_cn is not None:
            pack_list.append("colors")
        if geo.uvs is not None:
            pack_list.append("uvs")
        if geo.face_cn is not None:
            pack_list.append("norms")
        if geo.flags is not None:
            pack_list.append("flags")
        if geo.texture_ids is not None:
            pack_list.append("textures")
    if mesh.display_list is not None:
        pack_list.append("display_list")
    return pack_list

class RenderMode(object):
    # TODO: look more into "cloud surfaces" -- can we represent these in gltf materials?:
    #       http://ultra64.ca/files/documentation/online-manuals/man/pro-man/pro15/index15.5.html
    FLAGS = [
        ("per_vertex_cn", 0x1),
        ("xlu", 0x2),
        ("masked", 0x4),
        ("unlit", 0x8),
        # 0x10 seems to be unused
        ("ripple", 0x20),
        ("sync_to_global_clock", 0x40),
        ("cloud", 0x80),
    ]
    MASK = sum(pos for _, pos in FLAGS)
    MISC_MASK = (~MASK) & 0xFFFF

    def __init__(self, mode=0):
        self.fromInt(mode)

    def fromInt(self, mode):
        for name, pos in self.FLAGS:
            setattr(self, name, (mode & pos) != 0)
        self.misc = mode & self.MISC_MASK
        return self

    def toInt(self):
        return sum(pos if getattr(self, name) else 0 for name, pos in self.FLAGS) | self.misc

    def toDict(self):
        d = {name: getattr(self, name) for name, _ in self.FLAGS}
        d["misc"] = self.misc
        return d

    def __str__(self):
        return str(self.toDict())

    def __repr__(self):
        return str(self.toDict())


def mesh_to_gltf(mesh, file, gltf_parent, data, texture_db, scale_factor):
    render_mode = RenderMode(mesh.render_mode)
    # Pack list represents what data channels in the gltf
    # file should be present when packing the actor
    pack_list = mesh_to_pack_list(mesh)

    # TODO: choose based on selectable export strategy:
    if mesh.display_list is not None:
        lighting = not render_mode.unlit
        primitives = display_lists.f3dex_to_prims(mesh.display_list, mesh._io._io.getbuffer(), lighting, texture_db, scale_factor)
    elif mesh.geometry.num_faces > 0:
        primitives = mesh_geo_to_prims(mesh.geometry, render_mode, texture_db, scale_factor)
    else:
        primitives = []

    name = mesh.name.strip("\0")

    if len(primitives) == 0 and len(mesh.sprites or []) == 0:
        print("WARNING: No display data for mesh {:}".format(mesh.name.strip("\0")))
   
    if mesh.display_list is None:
        dl_encoded = None
    else:
        dl_raw = display_lists.dump_f3dex_dl(mesh.display_list)
        dl_encoded = base64.b64encode(dl_raw).decode()

    if len(primitives) > 0:
        gltf_mesh = gltf.Mesh(name=name, extras={
            "pack_list": json.dumps(pack_list),
        })
        if render_mode.ripple:
            gltf_mesh.extras["ripple"] = 1
        if render_mode.sync_to_global_clock:
            gltf_mesh.extras["sync_to_global_clock"] = 1
        if render_mode.cloud:
            gltf_mesh.extras["cloud"] = 1
        if render_mode.misc != 0:
            gltf_mesh.extras["render_mode"] = "0x{:4X}".format(render_mode.misc)
            gltf_mesh.extras["render_mode_mask"] = "0x{:4X}".format(render_mode.MISC_MASK)

        gltf_helper.addMeshDataToGLTFMesh(primitives, render_mode, gltf_mesh, file, data)
        if dl_encoded is not None:
            gltf_mesh.extras["display_list"] = dl_encoded
            # Mark mesh as needing to be hashed, once all buffers are constructed:
            gltf_mesh.extras["data_hash"] = None
        mesh_id = len(file.meshes)
        file.meshes.append(gltf_mesh)
    else:
        mesh_id = None

    t = mesh.translation[0]
    r = mesh.rotation[0]
    s = mesh.scale[0]

    mesh_node = gltf.Node(
        name=name,
        mesh=mesh_id,
        translation=(t.v1 / scale_factor, t.v2 / scale_factor, t.v3 / scale_factor),
        scale=(s.v1, s.v2, s.v3),
        rotation=(r.v1, r.v2, r.v3, r.v4),
        extensions={},
        extras={
            "_id": mesh.id,
            "alpha": mesh.mesh_alpha
        }
    )
    gltf_parent.children.append(len(file.nodes))
    file.nodes.append(mesh_node)

    if gltf_parent.extras.get("_root_node", False):
        mesh_node.extensions[gltf_helper.TSR_INHERITANCE_EXTENSION] = {
            "scale": False
        }

    for idx, sprite in enumerate(mesh.sprites or []):
        gltf_helper.addBillboardSpriteToGLTF(sprite, idx, mesh.sprite_alpha, mesh_node, file, data, scale_factor)

    return {"gltf_parent": mesh_node}


def global_timeline_to_gltf(root_mesh, file, data):
    max_time = 0
    def scrape_max(mesh):
        nonlocal max_time
        max_time = max(max_time, mesh.scale[-1].t)
        max_time = max(max_time, mesh.translation[-1].t)
        max_time = max(max_time, mesh.rotation[-1].t)
    for_each_mesh(root_mesh, scrape_max)

    anim_root = gltf.Animation(
        name="Global timeline"
    )
    file.animations.append(anim_root)
    for_each_mesh(root_mesh, gltf_helper.addAnimationDataToGLTF,
        gltf_animation=anim_root, clip=(0, max_time),
        file=file, data=data)


def animation_to_gltf(anim, root_mesh, file, data, scale_factor):
    anim_root = gltf.Animation(
        name="slot",
        extras={}
    )
    if anim.playback_speed != 1:
        anim_root.extras["playback_speed"] = anim.playback_speed
    if anim.unused != 0:
        anim_root.extras["unused"] = anim.unused
    file.animations.append(anim_root)
    for_each_mesh(root_mesh, gltf_helper.addAnimationDataToGLTF,
        gltf_animation=anim_root, clip=(anim.start_time, anim.end_time),
        file=file, data=data, scale_factor=scale_factor)

###############################################
# Bank mapping utlities

class BankmapDtype(enum.Enum):
    DL_VERTEX_DATA = "DL Vertex Data"
    PADDING = "Padding"
    UNKNOWN = "???"
    DIRECTORY = "Directory"
    ACTOR = "Actor root"
    MESH = "Mesh"
    GEO = "Geometry root"
    GEO_FACE_CN = "Geometry (face colors/normals)"
    GEO_VERTICES = "Geometry (vertices)"
    GEO_FACES = "Geometry (faces)"
    GEO_UV = "Geometry (UVs)"
    GEO_UV_ORIGINAL = "Geometry (UV original copies)"
    GEO_VERT_CN = "Geometry (vertex colors/normals)"
    GEO_FACE_PROPS = "Geometry (face properties)"
    GEO_TEXTURES = "Geometry (texture ids)"
    SPRITES = "Sprites"
    KEYFRAMES_SCALE = "Keyframes (scale)"
    KEYFRAMES_TRANSLATION = "Keyframes (translation)"
    KEYFRAMES_ROTATION = "Keyframes (rotation)"
    DISPLAY_LIST = "Display list"
    ANIM_PROPS = "Animation props"
    ANIM_DEFS = "Animation defs"

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
        try:
            if parent is None:
                return
            if field is not None:
                if not hasattr(parent, field):
                    return
                if getattr(parent, field) is None:
                    return
            memory_range = kaitaiObjectRange(parent, field)
        except EOFError as e:
            if hasattr(parent, field + "_ptr"):
                ptr_val = ": 0x{:08X}".format(getattr(parent, field + "_ptr"))
            else:
                ptr_val = ""
            print("ERROR: Bad pointer for {:} '{:}'{:}, {:}".format(dtype, name, ptr_val, e))
            return
        bank_map.append(BankSegment(
            memory_range=memory_range,
            dtype=dtype,
            name=name
        ))

    bank_push(bank, "directory", BankmapDtype.DIRECTORY, "")
    for dir_entry in bank.directory:
        actor = dir_entry.obj_root
        if actor is None:
            continue
        bank_push(dir_entry, "obj_root", BankmapDtype.ACTOR, "{:08X}".format(dir_entry.obj_id))

        def scrape_mesh(mesh, parents):
            name = "{:08X}.".format(dir_entry.obj_id) + parent_str(parents + [mesh])
            bank_push(mesh, None, BankmapDtype.MESH, name)

            if mesh.geometry is not None:
                geo = mesh.geometry
                bank_push(mesh, "geometry", BankmapDtype.GEO, name)
                bank_push(geo, "face_cn", BankmapDtype.GEO_FACE_CN, name)
                bank_push(geo, "vertices", BankmapDtype.GEO_VERTICES, name)
                bank_push(geo, "faces", BankmapDtype.GEO_FACES, name)
                bank_push(geo, "uvs", BankmapDtype.GEO_UV, name)
                bank_push(geo, "uvs_unmodified", BankmapDtype.GEO_UV_ORIGINAL, name)
                bank_push(geo, "vertex_cn", BankmapDtype.GEO_VERT_CN, name)
                bank_push(geo, "flags", BankmapDtype.GEO_FACE_PROPS, name)
                bank_push(geo, "texture_ids", BankmapDtype.GEO_TEXTURES, name)
            bank_push(mesh, "sprites", BankmapDtype.SPRITES, name)
            bank_push(mesh, "scale", BankmapDtype.KEYFRAMES_SCALE, name)
            bank_push(mesh, "translation", BankmapDtype.KEYFRAMES_TRANSLATION, name)
            bank_push(mesh, "rotation", BankmapDtype.KEYFRAMES_ROTATION, name)
            bank_push(mesh, "display_list", BankmapDtype.DISPLAY_LIST, name)

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
                                dtype=BankmapDtype.DL_VERTEX_DATA,
                                name="{:}.dl.cmd[0x{:04X}]".format(name, offset-base_offset)
                            ))
                        elif (cmd is F3DEX.byName["G_MTX"]
                         or cmd is F3DEX.byName["G_MOVEMEM"]
                         or cmd is F3DEX.byName["G_DL"]
                         or cmd is F3DEX.byName["G_BRANCH_Z"]):
                            raise Exception("TODO: Not yet implemented: Scrape F3DEX command {:}".format(cmd))
                scrape_dl(bank_data, mesh._debug["_m_display_list"]["start"])
            return {"parents": parents + [mesh]}

        for_each_mesh(actor.mesh, scrape_mesh, parents=[])

        try:
            if actor.animation is not None:
                bank_push(actor, "animation", BankmapDtype.ANIM_PROPS, "{:08X}".format(dir_entry.obj_id))
                bank_push(actor.animation, "animation_definitions", BankmapDtype.ANIM_DEFS, "{:08X}".format(dir_entry.obj_id))
        except EOFError as e:
            print("ERROR: Bad pointer for actor 0x{:08X} animation data".format(dir_entry.obj_id))
    bank_map.sort(key=lambda s: s.memory_range[0])
    return bank_map

def fillGaps(segments, bank_data):
    gaps = []
    activeSegments = []

    def gapDtype(start, end):
        padding = True
        start = max(start,0)
        end = min(end, len(bank_data))
        for addr in range(start, end):
            if bank_data[addr] != 0:
                padding = False
                break
        return BankmapDtype.PADDING if padding else BankmapDtype.UNKNOWN


    for segment in segments:
        nextActiveSegments = [s for s in activeSegments if s.memory_range[1] >= segment.memory_range[0]]
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

def objBankToJson(bank):
    json = objproxy.GenericProxy.of(bank)
    def scrapeChildren(node, flat):
        flat.append(node)
        if (sibling := node.get("sibling", None)) is not None:
            scrapeChildren(sibling, flat)
        if (child := node.get("child", None)) is not None:
            scrapeChildren(child, flat)
    for entry in json["directory"]:
        all_meshes = []
        obj = entry["obj_root"]
        if obj is None:
            continue
        scrapeChildren(obj["mesh"], all_meshes)
        obj["all_meshes"] = all_meshes
    return json

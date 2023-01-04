import base64
import dataclasses
import io
import os
import json
import math
import re
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
from . import hash as hash_str
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
        for obj_id, actor in self.actors.items():
            self.data += struct.pack(">I", obj_id)
            self.pointers.append(linkable.LinkablePointer(
                offset=len(self.data),
                dtype=">I",
                target=actor
            ))
            self.data +=  b"\0" * 4
        self.data += b"\0" * 8

class LinkableGeometry(linkable.LinkableStruct):
    verts: linkable.LinkableBytes
    faces: linkable.LinkableBytes
    vertex_cn: linkable.LinkableBytes
    face_cn: linkable.LinkableBytes
    texture_ids: linkable.LinkableBytes
    uvs: linkable.LinkableBytes
    flags: linkable.LinkableBytes

    root: linkable.LinkableBytes
    def finalize(self):
        self.data = []
        for attr in (self.verts, self.faces,
            self.vertex_cn, self.face_cn,
            self.uvs, self.flags, self.texture_ids
        ):
            if len(attr) > 0:
                self.data.append(attr)
        self.data.append(self.root)
        super().finalize()

class LinkableObjectBank(linkable.LinkableStruct):
    def __init__(self):
        super().__init__()
        self.directory: LinkableDirectory = LinkableDirectory()
        self.display_lists: typing.List[linkable.LinkableBytes] = []
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

def for_each_mesh(mesh, callback, **kwargs):
    updated_kwargs = callback(mesh, **kwargs)
    if mesh.sibling is not None:
        for_each_mesh(mesh.sibling, callback, **kwargs)
    if mesh.child is not None:
        child_kwargs = kwargs.copy()
        if updated_kwargs is not None:
            child_kwargs.update(updated_kwargs)
        for_each_mesh(mesh.child, callback, **child_kwargs)

def getConstructFieldOffset(construct_struct, field_name):
    offset = 0
    for field in construct_struct.subcons:
        if field.name == field_name:
            return offset
        offset += field.sizeof()
    else:
        raise Exception("Field not found")

def textureIdFromMaterial(material_idx, file):
    material = file.materials[material_idx]
    texture_idx = material.pbrMetallicRoughness.baseColorTexture.index
    texture = file.textures[texture_idx]
    image = file.images[texture.source]
    basename = os.path.basename(image.uri)
    # TODO: fallback chain -- first look in URI, then look in gltf image's name, then in material's name
    return next(re.finditer("(0x[0-9A-Fa-f]+)|([0-9]+)", basename)).group(0)

def packSprite(sprite_idx, file, texture_db):
    sprite_node = file.nodes[sprite_idx]

    attrs = gltf_helper.gltfMeshToFlattenedVertexCache(sprite_node.mesh, file)
    # TODO: do more than this half-assed validation:
    if len(sprite_node.mesh.primitives) != 1 or len(attrs["indices"]) != 6:
        raise gltf_helper.GLTFStructureException("Sprite mesh must be a 2-polygon square")

    # TODO: also take xyz/scale from geo

    return objbank_writer.glover_objbank__sprite.build({
        "texture_id": textureIdFromMaterial(attrs["material"][0], file), # / Int32ub,
        "runtime_data_ptr": 0,
        "x": sprite_node.translation[0],
        "y": sprite_node.translation[1],
        "z": sprite_node.translation[2],
        "width": sprite_node.scale[2]*3 if sprite_node.scale[0] == 1 else sprite_node.scale[0]*3, 
        "height": sprite_node.scale[1]*3, 
        "u5": 0, # TODO
        "u6": 0, # TODO
        "flags": 0, # TODO
    })


def packGeo(node_idx, bank, file, pack_list, texture_db):
    node = file.nodes[node_idx]
    mesh = file.meshes[node.mesh]

    geo_root = LinkableGeometry()
    bank.geometries.append(geo_root)

    pack_list = node.extras["pack_list"]

    attrs = gltf_helper.gltfMeshToFlattenedVertexCache(mesh, file)

    raw_geo_root = objbank_writer.glover_objbank__geometry.build({
        "num_faces": len(attrs["indices"]),
        "num_vertices": len(attrs["POSITION"]),
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
    geo_root.root = linkable.LinkableBytes(
        data=raw_geo_root,
        pointers=[]
    )
    def setPtr(name, dst):
        geo_root.root.pointers.append(linkable.LinkablePointer(
            offset = getConstructFieldOffset(objbank_writer.glover_objbank__geometry, name),
            dtype = ">I",
            target = dst
        ))

    if "faces" in pack_list:
        geo_root.faces = linkable.LinkableBytes(data=attrs["indices"].astype(">H").tobytes())
        setPtr("faces_ptr", geo_root.faces)
    if "verts" in pack_list:
        geo_root.verts = linkable.LinkableBytes(data=attrs["POSITION"].astype(">f").tobytes())
        setPtr("vertices_ptr", geo_root.verts)
    if "colors" in pack_list:
        ubyte_values = (attrs["COLOR_0"]*255).astype("B")
        raw_colors = b"".join(struct.pack("4B", *color[:2], 0) for color in ubyte_values)
        geo_root.vertex_cn = linkable.LinkableBytes(data=raw_colors)
        setPtr("vertex_cn_ptr", geo_root.vertex_cn)
    if "norms" in pack_list:
        # Have to recalculate face norms
        raw_norms = []
        for base_idx in range(len(0, len(attrs["indices"]), 3)):
            # Calculate ortho vector
            v0 = attrs["POSITION"][attrs["indices"][base_idx]]
            v1 = attrs["POSITION"][attrs["indices"][base_idx+1]]
            v2 = attrs["POSITION"][attrs["indices"][base_idx+2]]
            n = np.cross(v1-v0, v2-v0)

            # Normalize
            n_mag = math.sqrt(sum(n**2))
            n /= n_mag

            # Correct orientation
            v0n = attrs["NORMAL"][attrs["indices"][base_idx]]
            if np.dot(n, v0n) < 0:
                n *= -1

            # Cast to s8 format
            n *= 127
            raw_norms.append(struct.pack("bbbB", *n, 0))

        geo_root.face_cn = linkable.LinkableBytes(data=b"".join(raw_norms))
        setPtr("face_cn_ptr", geo_root.face_cn)   
    if "flags" in pack_list:
        geo_root.flags = linkable.LinkableBytes(data=attrs["_GLOVER_FLAGS"].astype("B").tobytes())
        setPtr("flags_ptr", geo_root.flags)
    if "uvs" in pack_list or "texture_ids" in pack_list:
        toTextureIds = np.vectorize(textureIdFromMaterial)
        texture_ids = toTextureIds(attrs["material"], file).astype(">I")

        if "texture_ids" in pack_list:
            geo_root.texture_ids = linkable.LinkableBytes(data=texture_ids.tobytes())
            setPtr("texture_ids_ptr", geo_root.texture_ids)

        if "uvs" in pack_list:
            # Go from normalized coordinates to pixel coordinates
            uvs = attrs["TEXCOORD_0"]
            for idx in len(geo_root.uvs):
                tex = texture_db.byId.get(texture_ids[idx])
                if tex is None:
                    raise Exception("Need dimensions of texture 0x{:08X} to pack mesh node {:}".format(texture_ids[idx], node.name))
                uvs[idx] *= (tex.width, tex.height)

            # Convert to 11.5 format
            geo_root.uvs = linkable.LinkableBytes(data=(uvs * 32).astype(">H").tobytes())                
            setPtr("uvs_ptr", geo_root.flags)

    return geo_root

def packAnimChannel(channel_data, bank):
    raw_keyframes = []
    values = channel_data[0]
    times = channel_data[1]
    if values.shape[1] == 3:
        for idx in range(len(values)):
            raw_keyframes.append(struct.pack("4fI", *values[idx], 0, times[idx]))
    elif values.shape[1] == 4:
        for idx in range(len(values)):
            raw_keyframes.append(struct.pack("4fI", *values[idx], times[idx]))
    else:
        raise gltf_helper.GLTFStructureException("Unexpected animation format")
    raw_keyframes = b"".join(raw_keyframes)
    keyframes = linkable.LinkableBytes(data=raw_keyframes)
    bank.keyframes.append(keyframes)
    return keyframes

def packNode(node_idx, bank, file, texture_db, dopesheet):
    node = file.nodes[node_idx]

    pack_list = node.extras.get("pack_list", ["display_list"])

    pointers = []

    # Pack children

    children = []
    sprite_nodes = []
    for child_idx in node.children:
        if gltf_helper.gltfNodeIsBillboard(child_idx, file):
            sprite_nodes.append(child_idx)
        else:
            children.append(packNode(child_idx, bank, file, texture_db, dopesheet))
            if len(children) > 1:
                children[-2].pointers.append(linkable.LinkablePointer(
                    offset = getConstructFieldOffset(objbank_writer.glover_objbank__mesh, "sibling_ptr"),
                    dtype = ">I",
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
            raw_sprites.append(packSprite(sprite_idx, file, texture_db))
        if sprite_alpha is None:
            sprite_alpha = 0xFF

        raw_sprites = b"".join(raw_sprites)
        sprites = linkable.LinkableBytes(data=raw_sprites)
        bank.sprites.append(sprites)
        pointers.append(linkable.LinkablePointer(
            offset = getConstructFieldOffset(objbank_writer.glover_objbank__mesh, "sprites_ptr"),
            dtype = ">I",
            target = sprites
        ))
    else:
        sprite_alpha = 0

    # Pack mesh metadata
    mesh_id = hash_str.hash_str(node.name)

    scale_keys = len(dopesheet["scale"].get(node_idx, animation.neutralScaleAnimation))
    translation_keys = len(dopesheet["translation"].get(node_idx, animation.neutralTranslationAnimation))
    rotation_keys = len(dopesheet["rotation"].get(node_idx, animation.neutralRotationAnimation))

    raw_mesh = b""
    raw_mesh = objbank_writer.glover_objbank__mesh.build({
        "id": mesh_id,
        "name": node.name[:8].encode().ljust(8, b"\0"),
        "mesh_alpha": node.extras.get("alpha", 0xFF),
        "sprite_alpha": sprite_alpha,
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

        # TODO
        # "render_mode": , # / Int16ub,

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
        dtype = ">I",
        target = packAnimChannel(translation_keys, bank),
    ))
    pointers.append(linkable.LinkablePointer(
        offset = getConstructFieldOffset(objbank_writer.glover_objbank__mesh, "rotation_ptr"),
        dtype = ">I",
        target = packAnimChannel(rotation_keys, bank),
    ))
    pointers.append(linkable.LinkablePointer(
        offset = getConstructFieldOffset(objbank_writer.glover_objbank__mesh, "scale_ptr"),
        dtype = ">I",
        target = packAnimChannel(scale_keys, bank),
    ))

    # Pack geo
    if should_pack_geo(pack_list):
        geo_root = packGeo(node_idx, bank, file, pack_list, texture_db)
        pointers.append(linkable.LinkablePointer(
            offset = getConstructFieldOffset(objbank_writer.glover_objbank__mesh, "geometry_ptr"),
            dtype = ">I",
            target = geo_root,
        ))

    # Pack DL
    if "display_list" in pack_list:
        display_list, dl_start_offset = display_lists.gltfNodeToDisplayList(node_idx, bank, file)
        pointers.append(linkable.LinkablePointer(
            offset = getConstructFieldOffset(objbank_writer.glover_objbank__mesh, "display_list_ptr"),
            dtype = ">I",
            target = display_list,
            target_offset = dl_start_offset
        ))


    # Fix up child ptr
    if len(children) > 0:
        pointers.append(linkable.LinkablePointer(
            offset = getConstructFieldOffset(objbank_writer.glover_objbank__mesh, "child_ptr"),
            dtype = ">I",
            target = children[0]
        ))

    # Finalize structure
    linkable_mesh = linkable.LinkableBytes(data=raw_mesh, pointers=pointers) 
    bank.meshses.append(linkable_mesh)
    return linkable_mesh


def actorAnimationMetadataFromJson(props_json, defs, file):
    p = json.loads(props_json)
    raw_props = objbank_writer.glover_objbank__animation.build({
        "num_animation_definitions": len(file.animations),
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
    props = linkable.LinkableBytes(data=raw_props, pointers=[anim_ptr])
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
    # TODO:
    # - identify all nodes in root tree, as set N
    # - identify animations that reference nodes in N, as set S
    # - arrange animations based on slot idx into global order
    # - create dope sheet structure
    #   - for each animation, determine playback speed based on time precision
    # - pack definitions based on dope sheet
    root_node = file.nodes[root_node_idx]

    # Find relevant animations
    all_nodes = gltf_helper.getAllNodesInTree(file, root_node_idx)

    relevant_animations = []
    for animation in file.animations:
        for channel in animation:
            if channel.target.node in all_nodes:
                relevant_animations.append(animation)
                break

    # Build global timeline

    raw_defs = b""
    global_time = 0
    dopesheet = {
        "translation": {},
        "rotation": {},
        "scale": {}
    }

    for animation in relevant_animations:
        for channel in animation:
            sampler = animation.samplers[channel.sampler]
            key_data = gltf_helper.getDataFromAccessor(file, sampler.input)
            key_times = gltf_helper.getDataFromAccessor(file, sampler.output)

            ##########
            # TODO
            scale_value = 1.0
            playback_speed = 1.0
            ##########

            key_times *= scale_value
            key_times += global_time

            dopesheet_channel = dopesheet[channel.target.path].get(channel.target.node, [numpy.array(),numpy.array()])
            dopesheet_channel[0] = np.concat(dopesheet_channel[0], key_data)
            dopesheet_channel[1] = np.concat(dopesheet_channel[1], key_data)
            dopesheet[channel.target.path][channel.target.node] = dopesheet_channel

            raw_defs += objbank_writer.glover_objbank__animation_definition.build({
                "start_time": global_time,
                "end_time": max(key_times) + 1,
                "playback_speed": playback_speed,
                "unused": 0,
            })

            global_time = max(key_times) + 1

    anim_defs = linkable.LinkableBytes(data=raw_defs, pointers=[])
    bank.anim_defs.append(anim_defs)

    anim_props = actorAnimationMetadataFromJson(root_node.extras["animation_props"], anim_defs, file)
    bank.anim_props.append(anim_props)

    return dopesheet, anim_props

def packActor(file, bank, texture_db):

    if len(file.scenes) != 1:
        raise gltf_helper.GLTFStructureException("There must be only one scene")

    for node_idx in file.scenes[0].nodes:

        root_node = file.nodes[node_idx]

        obj_id = root_node.extras.get("id", None)
        if obj_id is None:
            obj_id = hash_str.hash_str(root_node.name)

        # Pack animations
        anim_dopesheet, anim_data = setupActorAnimations(file, node_idx, bank)

        # Pack mesh data
        root_mesh = packNode(node_idx, bank, file, texture_db, anim_dopesheet)

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
        root_actor = linkable.LinkableBytes(
            data=root_actor_raw,
            pointers=[
                linkable.LinkablePointer(
                    offset = getConstructFieldOffset(objbank_writer.glover_objbank__object_root, "animation_ptr"),
                    dtype = ">I",
                    target = anim_data
                ),
                linkable.LinkablePointer(
                    offset = getConstructFieldOffset(objbank_writer.glover_objbank__object_root, "mesh_ptr"),
                    dtype = ">I",
                    target = root_mesh
                ),
            ]
        )
        bank.actors.append(root_actor)
        bank.directory.actors[obj_id] = root_actor


def actor_to_gltf(obj_root, texture_db):
    data = bytearray()
    root_node = gltf.Node(name="0x{:08X}".format(obj_root.obj_id))

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

    for_each_mesh(obj_root.mesh, mesh_to_gltf, file=file, gltf_parent=root_node, data=data, texture_db=texture_db)

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

    if is_skeletal or len(billboard_nodes) > 0:
        file.extensionsUsed.append(gltf_helper.TSR_INHERITANCE_EXTENSION)
        file.extensionsRequired.append(gltf_helper.TSR_INHERITANCE_EXTENSION)

    # Export animations
    exported_anims = {}
    for idx, anim in enumerate(obj_root.animation.animation_definitions or []):
        key = (anim.start_time, anim.end_time, anim.playback_speed, anim.unused)
        if key not in exported_anims:
            exported_anims[key] = len(file.animations)
            animation_to_gltf(anim, obj_root.mesh, file, data)
        file.animations[exported_anims[key]].name += "_{:}".format(idx)

    global_timeline_to_gltf(obj_root.mesh, file, data)

    animation_props = actorAnimationMetadataToJson(obj_root)
    file.nodes[0].extras["animation_props"] = json.dumps(animation_props)

    # Finalize binary data
    file.buffers.append(gltf.Buffer(byteLength=len(data)))
    file.set_binary_blob(bytes(data))

    # Clean up internal properties
    for node in file.nodes:
        if "_id" in node.extras:
            del node.extras["_id"]

    # Go through and compute all necessary mesh hashes, now that buffers are constructed
    for mesh in file.meshes:
        if "data_hash" in mesh.extras:
            mesh.extras["data_hash"] = gltf_helper.hashGLTFMesh(mesh, file).hexdigest()

    return b"".join(file.save_to_bytes())

def mesh_geo_to_prims(geo, render_mode, texture_db):
    # Coalesce Glover-style per-vertex/per-face attributes into
    # glTF-style per-vertex/per-material attributes

    # Map texture/material to vertex attributes:
    primitives = {}
 
    tex_warnings = set()

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
            if geo.vertex_cn is not None:
                prims.pushU32Color(geo.vertex_cn[v_idx])

        if geo.uvs is not None:
            tex = texture_db.byId.get(material.texture_id, None)
            uv = geo.uvs[face_idx]
            if tex is not None:
                prims.uvs += ((uv.u1.value / tex.width, uv.v1.value / tex.height),
                              (uv.u2.value / tex.width, uv.v2.value / tex.height),
                              (uv.u3.value / tex.width, uv.v3.value / tex.height))
            else:
                if material.texture_id not in tex_warnings:
                    print("WARNING: Couldn't find image dimensions for texture id 0x{:08X}, UVs for mesh '{:}'' will be inaccurate".format(
                        material.texture_id, geo._parent.name.strip("\0")
                    ))
                    tex_warnings.add(material.texture_id)
                prims.uvs += ((uv.u1.value, uv.v1.value),
                              (uv.u2.value, uv.v2.value),
                              (uv.u3.value, uv.v3.value))

        if geo.face_cn is not None:
            prims.pushU32Normal(geo.face_cn[face_idx], 3)

        if geo.flags is not None:
            # TODO: what is this data? how can we include it effectively?
            # (11/13/22) This is more than likely the clamp and mirror flags
            #   for the texture face. They go unused in-game, because loadF3DEXTexture
            #   takes those settings directly from the texture file, rather
            #   than the mesh data. Format from GBI is {clamp bit, mirror bit},
            #   and because they go unused we can't tell which is S and which is T.
            #   Disappointing. /shrug
            flags = geo.flags[face_idx]
            prims.flags += ((flags,) * 3)

    return primitives

def should_pack_geo(pack_list):
    return set(("faces", "colors", "uvs", "norms", "flags", "textures")).union(set(pack_list))

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


def mesh_to_gltf(mesh, file, gltf_parent, data, texture_db):
    render_mode = RenderMode(mesh.render_mode)
    # Pack list represents what data channels in the gltf
    # file should be present when packing the actor
    pack_list = mesh_to_pack_list(mesh)

    # TODO: choose based on selectable export strategy:
    if mesh.display_list is not None:
        lighting = not render_mode.unlit
        primitives = display_lists.f3dex_to_prims(mesh.display_list, mesh._io._io.getbuffer(), lighting, texture_db)
    elif mesh.geometry.num_faces > 0:
        primitives = mesh_geo_to_prims(mesh.geometry, render_mode, texture_db)
    else:
        primitives = {}

    name = mesh.name.strip("\0")

    if len(primitives) == 0 and len(mesh.sprites or []) == 0:
        print("WARNING: No display data for mesh {:}".format(mesh.name.strip("\0")))
   
    if mesh.display_list is None:
        dl_encoded = None
    else:
        dl_raw = display_lists.dump_f3dex_dl(mesh.display_list, mesh._io._io.getbuffer())
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
            gltf_mesh.extras["render_mode mask"] = "0x{:4X}".format(render_mode.MISC_MASK)

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
        translation=(t.v1, t.v2, t.v3),
        scale=(s.v1, s.v2, s.v3),
        rotation=(r.v1, r.v2, r.v3, r.v4),
        extensions={
            gltf_helper.TSR_INHERITANCE_EXTENSION: {"scale": False}
        },
        extras={
            "_id": mesh.id,
            "alpha": mesh.mesh_alpha
        }
    )
    gltf_parent.children.append(len(file.nodes))
    file.nodes.append(mesh_node)

    for idx, sprite in enumerate(mesh.sprites or []):
        gltf_helper.addBillboardSpriteToGLTF(sprite, idx, mesh.sprite_alpha, mesh_node, file, data)

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


def animation_to_gltf(anim, root_mesh, file, data):
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
        file=file, data=data)

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

            def scrape_mesh(mesh, parents):
                name = "{:08X}.".format(dir_entry.obj_id) + parent_str(parents + [mesh])
                bank_push(mesh, None, "Mesh", name)

                if mesh.geometry is not None:
                    geo = mesh.geometry
                    bank_push(mesh, "geometry", "Geometry root", name)
                    bank_push(geo, "norms", "Geometry (face normals)", name)
                    bank_push(geo, "vertices", "Geometry (vertices)", name)
                    bank_push(geo, "faces", "Geometry (faces)", name)
                    bank_push(geo, "uvs", "Geometry (UVs)", name)
                    bank_push(geo, "uvs_unmodified", "Geometry (UV original copies)", name)
                    bank_push(geo, "colors", "Geometry (vertex colors)", name)
                    bank_push(geo, "flags", "Geometry (face properties)", name)
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

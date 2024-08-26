import collections
from dataclasses import dataclass, replace
import enum
import hashlib
import json
import os
import re
import math
import struct
from . import animation
from .hash import canonicalize_reference
from . import vertex_cache_optimizer

import numpy as np
import pygltflib as gltf

TSR_INHERITANCE_EXTENSION = "EXT_node_tsr_inheritance"

class GLTFStructureException(Exception):
    pass

def idToTexturePath(tex_id):
    return "textures/0x{:08X}.png".format(tex_id)

def transposeMap(fn, array):
    results = []
    for col_idx in range(len(array[0])):
        results.append(fn(list(row[col_idx] for row in array)))
    return results

@dataclass(frozen=True, order=True)
class Material(object):
    texture_id: int = None
    clamp_s: bool = False
    clamp_t: bool = False
    mirror_s: bool = False
    mirror_t: bool = False

    def mutate(self, **kwargs):
        return replace(self, **kwargs)

class PackedVertexDataWriter(object):
    def __init__(self, gltf_file):
        self.gltf_file = gltf_file
        self.vertex_struct_format = ""
        self.vertex_struct_values = []
        self.gltf_attributes = {}

    def addAttributeToFormat(self, attrName, values, componentType, elementSize, calcExtrema=True):
        self.gltf_attributes[attrName] = len(self.gltf_file.accessors)
        if calcExtrema:
            extrema = {
                "max": transposeMap(max, values),
                "min": transposeMap(min, values)
            }
        else:
            extrema = {}
        self.gltf_file.accessors.append(gltf.Accessor(
            bufferView=len(self.gltf_file.bufferViews),
            componentType=componentType,
            count=len(values),
            type=elementSize,
            byteOffset=struct.calcsize(self.vertex_struct_format),
            **extrema
        ))
        self.vertex_struct_format += "{:}{:}".format(
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
        self.vertex_struct_values.append(values)

    def pack(self):
        vertex_data = []
        for idx in range(self.vertex_struct_values[0].shape[0]):
            values = []
            for data_series in self.vertex_struct_values:
                values.extend(data_series[idx])
            vertex_data.append(struct.pack(self.vertex_struct_format, *values))
        return b"".join(vertex_data)

    def stride(self):
        return struct.calcsize(self.vertex_struct_format)

    def gltf_attribute_map(self):
        return gltf.Attributes(
            **self.gltf_attributes
        )


def findSampler(file, material):
    if material.clamp_s:
        key_s = gltf.CLAMP_TO_EDGE
    elif material.mirror_s:
        key_s = gltf.MIRRORED_REPEAT
    else:
        key_s = gltf.REPEAT

    if material.clamp_t:
        key_t = gltf.CLAMP_TO_EDGE
    elif material.mirror_t:
        key_t = gltf.MIRRORED_REPEAT
    else:
        key_t = gltf.REPEAT

    for idx, sampler in enumerate(file.samplers):
        if sampler.wrapS == key_s and sampler.wrapT == key_t:
            return idx
    file.samplers.append(gltf.Sampler(
        magFilter=gltf.LINEAR,
        minFilter=gltf.LINEAR,
        wrapS=key_s,
        wrapT=key_t
    ))
    return len(file.samplers) - 1

def textureIdFromMaterial(material_or_idx, file):
    if isinstance(material_or_idx, gltf.Material):
        material = material_or_idx
    else:
        material = file.materials[int(material_or_idx)]
    # TODO: fallback chain -- first look in URI, then look in gltf image's name, then in material's name
    try:
        texture_idx = material.pbrMetallicRoughness.baseColorTexture.index
        texture = file.textures[texture_idx]
        image = file.images[texture.source]
        basename = os.path.basename(image.uri)
    except AttributeError:
        basename = os.path.basename(material.name)
    try:
        return int(next(re.finditer("(0x[0-9A-Fa-f]{8})\.", basename)).group(1),16)
    except StopIteration:
        return canonicalize_reference(basename)

def gltfMaterialToGloverMaterial(gltf_material, file):
    try:
        texture = file.textures[gltf_material.pbrMetallicRoughness.baseColorTexture.index]
        sampler = file.samplers[texture.sampler]

        clamp_s = sampler.wrapS == gltf.CLAMP_TO_EDGE,
        clamp_t = sampler.wrapT == gltf.CLAMP_TO_EDGE,
        mirror_s = sampler.wrapS == gltf.MIRRORED_REPEAT,
        mirror_t = sampler.wrapT == gltf.MIRRORED_REPEAT,
    except AttributeError:
        clamp_s, clamp_t = False, False
        mirror_s, mirror_t = False, False
    return Material(
        clamp_s=clamp_s,
        clamp_t=clamp_t,
        mirror_s=mirror_s,
        mirror_t=mirror_t,
        texture_id=textureIdFromMaterial(gltf_material, file)
    )

def extractGloverMaterialsFromGLTF(file):
    return [gltfMaterialToGloverMaterial(material, file) for material in file.materials]

def hashGLTFMesh(gltf_mesh, file):
    materials = collections.OrderedDict()
    bufferviews = collections.OrderedDict()
    for primitive in gltf_mesh.primitives:
        materials[primitive.material] = None
        bufferviews[file.accessors[primitive.indices].bufferView] = None
        attrs = json.loads(primitive.attributes.to_json())
        for attr_name in sorted(attrs.keys()):
            if attrs[attr_name] is None:
                continue
            bufferviews[file.accessors[attrs[attr_name]].bufferView] = None
    bufferviews = [file.bufferViews[idx] for idx in bufferviews.keys()]
    materials = [file.materials[idx] for idx in materials.keys()]

    data_hash = hashlib.sha1()

    for material in materials:
        data_hash.update(str(gltfMaterialToGloverMaterial(material, file)).encode())

    buffer_cache = {}
    for bufferview in bufferviews:
        buffer = file.buffers[bufferview.buffer]
        if buffer.uri in buffer_cache:
            buffer_data = buffer_cache[buffer.uri]
        else:
            buffer_data = file.get_data_from_buffer_uri(buffer.uri)
            buffer_cache[buffer.uri] = buffer_data
        bufferview_data = buffer_data[bufferview.byteOffset: bufferview.byteOffset+bufferview.byteLength]
        data_hash.update(bufferview_data)

    return data_hash


class MeshData(object):
    class AttrType(enum.Enum):
        position="POSITION"
        color="COLOR_0"
        uv="TEXCOORD_0"
        uv_scaled="_TEXCOORD_0_scaled"
        norm="NORMAL"
        flags="TEXCOORD_1"

    ATTR_SIZES = {
        AttrType.position: 3,
        AttrType.color: 4,
        AttrType.uv: 2,
        AttrType.uv_scaled: 2,
        AttrType.norm: 3,
        AttrType.flags: 2
    }

    def __init__(self):
        self.vertex_count = 0
        self.idx_count = 0
        self.face_count = 0

        self.attrs = {}
        self.indices = np.array([])
        self.variants = None


        self.material = None
        self.texture = None


    def _get_attr(self, attr_type):
        if attr_type not in self.attrs:
            self.attrs[attr_type] = np.zeros((self.vertex_count, self.ATTR_SIZES[attr_type]))
        return self.attrs[attr_type]
    def _set_attr(self, attr_type, value):
        self.attrs[attr_type] = value

    @property
    def position(self):
        return self._get_attr(self.AttrType.position)
    @position.setter
    def position(self, value):
        return self._set_attr(self.AttrType.position, value)
    @property
    def color(self):
        return self._get_attr(self.AttrType.color)
    @color.setter
    def color(self, value):
        return self._set_attr(self.AttrType.color, value)
    @property
    def uv(self):
        return self._get_attr(self.AttrType.uv)
    @uv.setter
    def uv(self, value):
        return self._set_attr(self.AttrType.uv, value)
    @property
    def uv_scaled(self):
        return self._get_attr(self.AttrType.uv_scaled)
    @uv_scaled.setter
    def uv_scaled(self, value):
        return self._set_attr(self.AttrType.uv_scaled, value)
    @property
    def norm(self):
        return self._get_attr(self.AttrType.norm)
    @norm.setter
    def norm(self, value):
        return self._set_attr(self.AttrType.norm, value)
    @property
    def flags(self):
        return self._get_attr(self.AttrType.flags)
    @flags.setter
    def flags(self, value):
        return self._set_attr(self.AttrType.flags, value)


    def duplicates(self, indices=None):
        """
        Group vertices in attribute data based on shared positions
        and UVs. Takes as input a list of indices of vertices to
        search for duplicates. If input is None, searches all of them.
        Returns the nested structure:
        {shared_position: {shared_uv: [vert_idx, ...], ...}, ...}
        """
        if indices is None:
            indices = range(self.vertex_count)
        shared = {}
        for idx in indices:
            pos = tuple(self.position[idx])
            aux = tuple(self.uv[idx])
            if pos not in shared:
                shared[pos] = {}
            if aux not in shared[pos]:
                shared[pos][aux] = []
            shared[pos][aux].append(idx)
        return shared

    def deduplicate(self, merge_variants):
        """
        Remove duplicate vertices from vertex data.

        If merge_variants is False, vertices must share positions
        AND UVs to be considered duplicates.

        If merge_variants is True, all vertices sharing the same position
        will be merged and the variant attributes will be placed in the
        variants dictionary. Mesh indices will be modified such that
        the two LSBs of each index point to a variant in that dictionary
        """ 
        if merge_variants is True:
            self.variants = {}
        shared = self.duplicates()
        self.vertex_count = sum(len(lists) for lists in shared.values())
        old_attrs = self.attrs
        self.attrs = {}
        for attr_type in old_attrs:
            self.attrs[attr_type] = np.zeros((self.vertex_count, self.ATTR_SIZES[attr_type]))
        old_indices = self.indices
        self.indices = self.indices.copy()
        dedup_mapping = {}
        attr_wr_cursor = 0
        for idx_idx, idx in enumerate(old_indices):
            pos = tuple(old_attrs[self.AttrType.position][idx])
            uv = tuple(old_attrs[self.AttrType.uv][idx])
            if merge_variants is True:
                v_key = pos
                if v_key not in dedup_mapping:
                    for attr_type in old_attrs:
                        self.attrs[attr_type][attr_wr_cursor] = old_attrs[attr_type][idx]
                    dedup_mapping[v_key] = attr_wr_cursor << 2
                    attr_wr_cursor += 1
                
                new_idx = dedup_mapping[v_key]
                if len(shared[pos]) > 1:
                    if new_idx not in self.variants:
                        self.variants[new_idx] = []
                    for variant_idx, variant in enumerate(self.variants[new_idx]):
                        if tuple(variant[self.AttrType.uv]) == uv:
                            break
                    else:
                        if len(self.variants[new_idx]) > 4:
                            raise Exception("Too many vertex variants")
                        variant_idx = len(self.variants[new_idx])
                        self.variants[new_idx].append({
                            attr_type: old_attrs[attr_type][idx]
                                for attr_type in old_attrs
                                    if attr_type != self.AttrType.position
                        })
                    new_idx |= (variant_idx & 0x3)
            else:
                v_key = (pos, uv)
                if v_key not in dedup_mapping:
                    for attr_type in old_attrs:
                        self.attrs[attr_type][attr_wr_cursor] = old_attrs[attr_type][idx]
                    dedup_mapping[v_key] = attr_wr_cursor
                    attr_wr_cursor += 1
                new_idx = dedup_mapping[v_key]
            self.indices[idx_idx] = new_idx
                    

        print("De-duplicated mesh from {:} to {:} vertices".format(
            len(old_attrs[self.AttrType.position]),
            len(self.attrs[self.AttrType.position])))

    def optimize(self, cache_size=32):
        self.deduplicate(merge_variants=True)
        vertex_cache_optimizer.optimize(self, cache_size)

    def loadFromGltf(self, primitives, file, texture_db):
        self.material = gltfMaterialToGloverMaterial(primitives.material, file)
        if self.material.texture_id is not None:
            self.texture = texture_db.byId.get(self.material.texture_id)
            if self.texture is None:
                raise Exception("Need dimensions of texture 0x{:08X}".format(self.material.texture_id))

        self.attrs = {}
        
        for attr_name, accessor_idx in vars(primitives.attributes).items():
            try:
                attr_type = self.AttrType(attr_name)
            except ValueError:
                print("Discarding vertex attribute {:}".format(attr_name))
                continue
            if not isinstance(accessor_idx, int):
                continue
            self.attrs[attr_type] = getDataFromAccessor(file, accessor_idx)
            if self.vertex_count == 0:
                self.vertex_count = self.attrs[attr_type].shape[0]

        if primitives.indices is not None:
            self.indices = getDataFromAccessor(file, primitives.indices)
        else:
            self.indices = np.arange(start=0, stop=self.vertex_count, dtype="I")
        self.idx_count = len(self.indices)
        self.face_count = self.idx_count // 3

        self.deriveScaledUVs()

        return self

    def deriveScaledUVs(self, src_attr=AttrType.uv):
        if isinstance(self.texture, list):
            raise NotImplementedError("Can't derive scaled UVs across multi-texture mesh data")
        dst_attr = self.AttrType("_{:}_scaled".format(src_attr.value))
        tex_size = (self.texture.width, self.texture.height)
        self.attrs[dst_attr] = np.multiply(self.attrs[src_attr], tex_size)

    @classmethod
    def flatten(cls, data):
        flattened = cls()
        total_verts = sum(d.vertex_count for d in data)
        total_indices = sum(d.idx_count for d in data)
        total_faces = sum(d.face_count for d in data)

        flattened.indices = np.zeros(total_indices, data[0].indices.dtype)
        flattened.texture = [None] * total_faces
        flattened.material = [None] * total_faces

        for d in data:
            for attr_type, attr in d.attrs.items():
                if attr_type not in flattened.attrs:
                    flattened.attrs[attr_type] = np.zeros(
                        (total_verts, attr.shape[1]),
                        dtype=attr.dtype)

        base_vert_idx = 0
        base_idx_idx = 0
        base_face_idx = 0
        for d in data:

            for attr_type, attr in d.attrs.items():
                dst_slice = slice(base_vert_idx, base_vert_idx + d.vertex_count)
                flattened.attrs[attr_type][dst_slice] = attr

            dst_slice = slice(base_idx_idx, base_idx_idx + d.idx_count)
            flattened.indices[dst_slice] = d.indices + base_vert_idx

            dst_slice = slice(base_face_idx, base_face_idx + d.face_count)
            flattened.texture[dst_slice] = [d.texture] * d.face_count
            flattened.material[dst_slice] = [d.material] * d.face_count

            base_vert_idx += d.vertex_count
            base_idx_idx += d.idx_count
            base_face_idx += d.face_count

        flattened.vertex_count = base_vert_idx
        flattened.idx_count = base_idx_idx
        flattened.face_count = base_face_idx
        return flattened


def addMeshDataToGLTFMesh(primitives, render_mode, gltf_mesh, file, data):
    ###############################################
    # Build actual GLTF structures:

    for prims in sorted(primitives, key=lambda p: p.material.texture_id):
        indices_data = prims.indices.astype("=H").tobytes()
        indices_bufferview_handle = len(file.bufferViews)
        file.bufferViews.append(gltf.BufferView(
            buffer=0,
            byteOffset=len(data),
            byteLength=len(indices_data),
            target=gltf.ELEMENT_ARRAY_BUFFER,
        ))
        data.extend(indices_data)

        indices_handle = len(file.accessors)
        file.accessors.append(gltf.Accessor(
            bufferView=indices_bufferview_handle,
            componentType=gltf.UNSIGNED_SHORT,
            count=len(prims.indices),
            type=gltf.SCALAR,
            max=[max(prims.indices).tolist()],
            min=[min(prims.indices).tolist()],
        ))

        # Build interleaved vertex data format
        vertex_struct = PackedVertexDataWriter(file)
       
        for attr_type, attr_data in prims.attrs.items():
            if attr_type.value.startswith("_"):
                # Don't pack internal/derived attributes
                continue
            elem_size = {
                1: gltf.SCALAR,
                2: gltf.VEC2,
                3: gltf.VEC3,
                4: gltf.VEC4,
            }[attr_data.shape[1]]
            comp_type =  {
                "f": gltf.FLOAT,
                "u": gltf.UNSIGNED_INT
            }[attr_data.dtype.kind]
            vertex_struct.addAttributeToFormat(
                attrName=attr_type.value,
                values=attr_data,
                componentType=comp_type,
                elementSize=elem_size
            )

        # Pack binary data
        vertex_data = vertex_struct.pack()
        file.bufferViews.append(gltf.BufferView(
            buffer=0,
            byteOffset=len(data),
            byteLength=len(vertex_data),
            byteStride=vertex_struct.stride(),
            target=gltf.ARRAY_BUFFER,
        ))
        data.extend(vertex_data)

        # Build GLTF primitive

        gltf_mesh.primitives.append(gltf.Primitive(
            attributes=vertex_struct.gltf_attribute_map(),
            material=len(file.materials),
            indices=indices_handle
        ))

        if render_mode.xlu:
            blend_mode = {
                "alphaMode": gltf.BLEND,
                "alphaCutoff": None
            }
        elif render_mode.masked:
            blend_mode = {
                "alphaMode": gltf.MASK,
                "alphaCutoff": .5
            }
        else:
            blend_mode = {
                "alphaMode": gltf.OPAQUE,
                "alphaCutoff": None
            }

        if prims.material.texture_id is not None:
            file.materials.append(gltf.Material(
                name="0x{:08X}".format(prims.material.texture_id),
                pbrMetallicRoughness = gltf.PbrMetallicRoughness(
                    baseColorTexture=gltf.TextureInfo(
                        index=len(file.textures)
                    )
                ),
                **blend_mode
            ))
            file.textures.append(gltf.Texture(
                sampler=findSampler(file, prims.material),
                source=len(file.images)
            ))

            file.images.append(gltf.Image(
                uri=idToTexturePath(prims.material.texture_id),
            ))
        else:
            file.materials.append(gltf.Material(
                name="Untextured",
                pbrMetallicRoughness = gltf.PbrMetallicRoughness(
                    baseColorFactor=[1, 1, 1, 1]
                ),
                **blend_mode
            ))

        if render_mode.unlit:
            file.materials[-1].extensions["KHR_materials_unlit"] = {}


def addAnimationDataToGLTF(mesh, gltf_animation, clip, file, data):

    for mesh_node_idx, node in enumerate(file.nodes):
        if node.extras.get("_id",None) == mesh.id:
            break
    else:
        raise Exception("Couldn't find mesh node '0x{:08X}'".format(mesh.id))

    def addChannel(frames, output_type, channel_name):
        # Prep frames
        clip_frames = [frame for frame in frames if frame.t >= clip[0] and frame.t < clip[1]]

        # TODO: handle case when clip falls entirely before frame series
        if len(clip_frames) == 0:
            for idx in range(len(frames)):
                if frames[idx].t > clip[0]:
                    frame_start = frames[idx-1]
                    frame_end = frames[idx]
                    break
            else:
                frame_start = frames[-1]
                frame_end = frames[-1]

            if output_type == gltf.VEC3:
                clip_frames = [
                    animation.lerpFrame(frame_start, frame_end, clip[0]),
                    animation.lerpFrame(frame_start, frame_end, clip[1])
                ]
            else:
                clip_frames = [
                    animation.slerpFrame(frame_start, frame_end, clip[0]),
                    animation.slerpFrame(frame_start, frame_end, clip[1])
                ]
        else:            
            if clip_frames[0].t != clip[0]:
                prev_idx = frames.index(clip_frames[0]) - 1
                if prev_idx >= 0:
                    if output_type == gltf.VEC3:
                        clip_frames.insert(0, animation.lerpFrame(frames[prev_idx], clip_frames[0], clip[0]))
                    else:
                        clip_frames.insert(0, animation.slerpFrame(frames[prev_idx], clip_frames[0], clip[0]))

            if clip_frames[-1].t != clip[1]:
                next_idx = frames.index(clip_frames[-1]) + 1
                if next_idx < len(frames):
                    if output_type == gltf.VEC3:
                        clip_frames.append(animation.lerpFrame(clip_frames[-1], frames[next_idx], clip[1]))
                    else:
                        clip_frames.append(animation.slerpFrame(clip_frames[-1], frames[next_idx], clip[1]))

        # Build high-level animation structures
        gltf_animation.channels.append(gltf.AnimationChannel(
            sampler=len(gltf_animation.samplers),
            target=gltf.AnimationChannelTarget(
                node=mesh_node_idx,
                path=channel_name
            )
        ))
        gltf_animation.samplers.append(gltf.AnimationSampler(
            input=len(file.accessors),
            output=len(file.accessors)+1
        ))

        # Encode raw data

        if output_type == gltf.VEC3:
            output_struct = struct.Struct("<3f")
            output_tuples = [(frame.v1, frame.v2, frame.v3) for frame in clip_frames]
        elif output_type == gltf.VEC4:
            output_struct = struct.Struct("<4f")
            output_tuples = [(frame.v1, frame.v2, frame.v3, frame.v4) for frame in clip_frames]
        else:
            raise ValueError("Bad type")

        input_series = tuple((frame.t-clip[0])*animation.FRAME_TO_SEC for frame in clip_frames)
        encoded_output = b"".join(output_struct.pack(*frame) for frame in output_tuples)
        encoded_input = b"".join(struct.pack("<f",t) for t in input_series)


        # Build data pointer structures
        file.accessors.append(gltf.Accessor(
            bufferView=len(file.bufferViews),
            componentType=gltf.FLOAT,
            count=len(clip_frames),
            type=gltf.SCALAR,
            max=[max(input_series)],
            min=[min(input_series)]

        ))
        file.accessors.append(gltf.Accessor(
            bufferView=len(file.bufferViews)+1,
            componentType=gltf.FLOAT,
            count=len(clip_frames),
            type=output_type,
            max=transposeMap(max, output_tuples),
            min=transposeMap(min, output_tuples)
        ))
        file.bufferViews.append(gltf.BufferView(
            buffer=0,
            byteOffset=len(data),
            byteLength=len(encoded_input)
        ))
        data.extend(encoded_input)
        file.bufferViews.append(gltf.BufferView(
            buffer=0,
            byteOffset=len(data),
            byteLength=len(encoded_output)
        ))
        data.extend(encoded_output)

    if len(mesh.translation) > 1:
        addChannel(mesh.translation, gltf.VEC3, "translation")
    if len(mesh.rotation) > 1:
        addChannel(mesh.rotation, gltf.VEC4, "rotation")
    if len(mesh.scale) > 1:
        addChannel(mesh.scale, gltf.VEC3, "scale")

def gltfNodeIsBillboard(node_idx, file):
    mesh = file.meshes[file.nodes[node_idx].mesh]
    return mesh.extras.get("billboard", False)

def addBillboardSpriteToGLTF(sprite, idx, alpha, parent_node, file, data):
    name = "{:}_sprite_{:}".format(parent_node.name, idx)

    # Create node structure
    billboard_node = gltf.Node(
        name=name,
        mesh=len(file.meshes),
        translation=(sprite.x, sprite.y, sprite.z),
        scale=(1, sprite.height/3, sprite.width/3),
        extensions={
            TSR_INHERITANCE_EXTENSION: {"scale": False, "rotation": False}
        },
        extras={
            "sprite_idx": idx,
            "alpha": alpha
        }
    )
    parent_node.children.append(len(file.nodes))
    file.nodes.append(billboard_node)

    billboard_mesh = gltf.Mesh(
        name=name,
        extras={
            "billboard": True,
        }
    )
    file.meshes.append(billboard_mesh)

    # Create billboard mesh data

    positions = np.array([
        (0,-.5,.5),
        (0,-.5,-.5),
        (0,.5,.5),
        (0,-.5,-.5),
        (0,.5,-.5),
        (0,.5,.5),
    ])
    uvs = np.array([
        (1,0),
        (0,0),
        (1,1),
        (0,0),
        (0,1),
        (1,1),
    ])


    vertex_struct = PackedVertexDataWriter(file)
    vertex_struct.addAttributeToFormat(
        attrName="POSITION",
        values=positions,
        componentType=gltf.FLOAT,
        elementSize=gltf.VEC3
    )
    vertex_struct.addAttributeToFormat(
        attrName="TEXCOORD_0",
        values=uvs,
        componentType=gltf.FLOAT,
        elementSize=gltf.VEC2
    )

    vertex_data = vertex_struct.pack()
    file.bufferViews.append(gltf.BufferView(
        buffer=0,
        byteOffset=len(data),
        byteLength=len(vertex_data),
        byteStride=vertex_struct.stride(),
        target=gltf.ARRAY_BUFFER,
    ))
    data.extend(vertex_data)

    # Build GLTF primitive

    billboard_mesh.primitives.append(gltf.Primitive(
        attributes=vertex_struct.gltf_attribute_map(),
        material=len(file.materials),
    ))


    sprite_material = Material(
        texture_id=sprite.texture_id,
        clamp_s=True,
        clamp_t=True
    )

    file.materials.append(gltf.Material(
        pbrMetallicRoughness = gltf.PbrMetallicRoughness(
            baseColorTexture=gltf.TextureInfo(
                index=len(file.textures)
            )
        ),
        doubleSided=True,
        alphaMode=gltf.MASK,
        alphaCutoff=0.5,
        extensions={
            "KHR_materials_unlit": {}
        }
    ))

    file.textures.append(gltf.Texture(
        sampler=findSampler(file, sprite_material),
        source=len(file.images)
    ))

    file.images.append(gltf.Image(
        uri=idToTexturePath(sprite_material.texture_id),
    ))


def getDataFromAccessor(file, accessor_idx):
    accessor = file.accessors[accessor_idx]
    bufferView = file.bufferViews[accessor.bufferView]
    buffer = file.buffers[bufferView.buffer]
    src_data = file.get_data_from_buffer_uri(buffer.uri)

    component_count, component_dimension = {
        gltf.SCALAR: (1,0),
        gltf.VEC2: (2,1),
        gltf.VEC3: (3,1),
        gltf.VEC4: (4,1),
        gltf.MAT2: (4,2),
        gltf.MAT3: (9,2),
        gltf.MAT4: (16,2),
    }[accessor.type]

    component_dtype = {
        gltf.BYTE: "b",
        gltf.UNSIGNED_BYTE: "B",
        gltf.SHORT: "h",
        gltf.UNSIGNED_SHORT: "H",
        gltf.UNSIGNED_INT: "I",
        gltf.FLOAT: "f"
    }[accessor.componentType]

    if accessor.normalized is True:
        elem_divisor = np.iinfo(component_dtype).max
        final_dtype = "f"
    else:
        elem_divisor = 1
        final_dtype = component_dtype

    attr_struct = "<{:}{:}".format(component_count, component_dtype)
    attr_size = struct.calcsize(attr_struct)
    stride = bufferView.byteStride or attr_size

    if component_dimension == 0:
        data_shape = accessor.count
    elif component_dimension == 1:
        data_shape = (accessor.count, component_count)
    elif component_dimension == 2:
        mat_size = int(math.sqrt(component_count))
        mat_shape = (mat_size, mat_size)
        data_shape = (accessor.count, mat_size, mat_size)

    dst_data = np.zeros(data_shape, dtype=final_dtype)

    cursor = bufferView.byteOffset + accessor.byteOffset
    for idx in range(accessor.count):
        vals = struct.unpack(attr_struct, src_data[cursor:cursor+attr_size])
        if component_dimension == 2:
            vals = np.reshape(vals, mat_shape)
        dst_data[idx:idx+1] = vals
        if accessor.normalized is True:
            dst_data[idx] /= elem_divisor
        cursor += stride

    return dst_data

def getAllNodesInTree(file, root_node_idx):
    result = set()
    todo = [root_node_idx]
    while len(todo) > 0:
        node_idx = todo.pop()
        result.add(node_idx)
        todo += file.nodes[node_idx].children
    return result
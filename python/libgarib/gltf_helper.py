import collections
from dataclasses import dataclass, replace
import hashlib
import json
import os
import re
import math
import struct

from . import animation
from .hash import canonicalize_reference

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

class MeshData(object):
    def __init__(self):
        self.indices = []
        self.positions = []
        self.colors = []
        self.uvs = []
        self.norms = []
        self.flags = []

    def pushU32Color(self, value, quantity=1):
        color = (
            ((value & 0xFF000000) >> 24) / 255,
            ((value & 0x00FF0000) >> 16) / 255,
            ((value & 0x0000FF00) >> 8) / 255
        )
        for _ in range(quantity):
            self.colors.append(color)

    def pushU32Normal(self, value, quantity=1):
        norm_byte = struct.unpack(">bbbb", struct.pack(">I",value))[:-1]
        norm_mag = math.sqrt(sum(coord ** 2 for coord in norm_byte))
        norm_norm = tuple(coord / norm_mag for coord in norm_byte)
        for _ in range(quantity):
            self.norms.append(norm_norm)


    def __getitem__(self, key):
        return getattr(self, key)

class PackedVertexData(object):
    def __init__(self, gltf_file):
        self.gltf_file = gltf_file
        self.vertex_struct_format = ""
        self.vertex_struct_sources = []
        self.gltf_attributes = {}

    def addAttributeToFormat(self, attrName, values, sources, componentType, elementSize, calcExtrema=True):
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
        self.vertex_struct_sources += sources

    def pack(self, prims):
        vertex_data = []
        for idx in range(len(prims.positions)):
            values = []
            for path in self.vertex_struct_sources:
                v = prims
                for key in path:
                    if key is ...:
                        key = idx
                    v = v.__getitem__(key)
                values.append(v)
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


def addDerivedMaterialAttrs(vertex_cache, file, texture_db, src_attr):
    toTextureIds = np.vectorize(textureIdFromMaterial)
    vertex_cache["texture_ids"] = toTextureIds(vertex_cache["material"], file).astype(">I")

    vert_count = len(vertex_cache[src_attr])
    dst_attr = "{:}_scaled".format(src_attr)
    vertex_cache[dst_attr] = np.zeros((vert_count, *vertex_cache[src_attr].shape[1:]))
    tex_sizes = {}
    for idx in range(vert_count):
        material_id = vertex_cache["material"][idx]
        if material_id not in tex_sizes:
            tex = texture_db.byId.get(vertex_cache["texture_ids"][idx])
            if tex is None:
                raise Exception("Need dimensions of texture 0x{:08X}".format(vertex_cache["texture_ids"][idx]))
            tex_sizes[material_id] = (tex.width, tex.height)
        vertex_cache[dst_attr][idx] = vertex_cache[src_attr][idx] * tex_sizes[material_id]


def optimizeVertexCache(vertex_cache, cache_size=32):
    # Build de-duplicated collection of vertices
    shared = {}
    for idx, pos in enumerate(vertex_cache["POSITION"]):
        pos = tuple(pos)
        aux = tuple(vertex_cache["TEXCOORD_0"][idx])
        if pos not in shared:
            shared[pos] = {}
        if aux not in shared[pos]:
            shared[pos][aux] = []
        shared[pos][aux].append(idx)
    # TODO: insert into indices list sentinel objects that indicate UV changes


def gltfMeshToFlattenedVertexCache(gltf_mesh, file):
    # TODO: merge/compress vertices where possible
    vert_count = 0
    attrs = {
        "material": np.array([], dtype="I"),
        "indices": np.array([], dtype="I")
    }
    for primitives in gltf_mesh.primitives:
        p_vert_count = None
        for attr_name, accessor_idx in vars(primitives.attributes).items():
            if not isinstance(accessor_idx, int):
                continue
            data = getDataFromAccessor(file, accessor_idx)
            if attr_name not in attrs:
                attrs[attr_name] = np.zeros((vert_count, *data.shape[1:]))
            attrs[attr_name] = np.concatenate((attrs[attr_name], data))
            if p_vert_count is None:
                p_vert_count = data.shape[0]

        attrs["material"] = np.concatenate((attrs["material"], np.full(p_vert_count, primitives.material)))

        if primitives.indices is not None:
            p_indices = getDataFromAccessor(file, primitives.indices)
            p_indices += vert_count
        else:
            p_indices = np.arange(start=vert_count, stop=vert_count+p_vert_count, dtype="I")
        attrs["indices"] = np.concatenate((attrs["indices"], p_indices))

        vert_count += p_vert_count
    return attrs

def addMeshDataToGLTFMesh(primitives, render_mode, gltf_mesh, file, data):
    ###############################################
    # Build actual GLTF structures:

    for material, prims in sorted(primitives.items(), key=lambda p: p[0]):
        indices_data = b"".join(struct.pack("H", i) for i in prims.indices)
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
            max=[max(prims.indices)],
            min=[min(prims.indices)],
        ))

        # Build interleaved vertex data format
        vertex_struct = PackedVertexData(file)
        vertex_struct.addAttributeToFormat(
            attrName="POSITION",
            values=prims.positions,
            sources=(
                ("positions", ..., 0),
                ("positions", ..., 1),
                ("positions", ..., 2)
            ),
            componentType=gltf.FLOAT,
            elementSize=gltf.VEC3
        )

        if len(prims.colors) > 0:
            vertex_struct.addAttributeToFormat(
                attrName="COLOR_0",
                values=prims.colors,
                sources=(
                    ("colors", ..., 0),
                    ("colors", ..., 1),
                    ("colors", ..., 2),
                ),
                componentType=gltf.FLOAT,
                elementSize=gltf.VEC3
            )

        if len(prims.uvs) > 0:
            vertex_struct.addAttributeToFormat(
                attrName="TEXCOORD_0",
                values=prims.uvs,
                sources=(
                    ("uvs", ..., 0),
                    ("uvs", ..., 1),
                ),
                componentType=gltf.FLOAT,
                elementSize=gltf.VEC2
            )

        if len(prims.norms) > 0:
            vertex_struct.addAttributeToFormat(
                attrName="NORMAL",
                values=prims.norms,
                sources=(
                    ("norms", ..., 0),
                    ("norms", ..., 1),
                    ("norms", ..., 2),
                ),
                componentType=gltf.FLOAT,
                elementSize=gltf.VEC3
            )

        if len(prims.flags) > 0:
            # TODO: this is hard to transfer
            #       to blender as a custom attribute;
            #       instead, encode as a color channel?
            vertex_struct.addAttributeToFormat(
                attrName="_GLOVER_FLAGS",
                values=prims.flags,
                sources=(
                    ("flags", ...),
                ),
                componentType=gltf.UNSIGNED_INT,
                elementSize=gltf.SCALAR,
                calcExtrema=False
            )

        # Pack binary data
        vertex_data = vertex_struct.pack(prims)
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

        if material.texture_id is not None:
            file.materials.append(gltf.Material(
                name="0x{:08X}".format(material.texture_id),
                pbrMetallicRoughness = gltf.PbrMetallicRoughness(
                    baseColorTexture=gltf.TextureInfo(
                        index=len(file.textures)
                    )
                ),
                **blend_mode
            ))
            file.textures.append(gltf.Texture(
                sampler=findSampler(file, material),
                source=len(file.images)
            ))

            file.images.append(gltf.Image(
                uri=idToTexturePath(material.texture_id),
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

    prims = MeshData()
    prims.positions = [
        (0,-.5,.5),
        (0,-.5,-.5),
        (0,.5,.5),
        (0,-.5,-.5),
        (0,.5,-.5),
        (0,.5,.5),
    ]
    prims.uvs = [
        (1,0),
        (0,0),
        (1,1),
        (0,0),
        (0,1),
        (1,1),
    ]

    vertex_struct = PackedVertexData(file)
    vertex_struct.addAttributeToFormat(
        attrName="POSITION",
        values=prims.positions,
        sources=(
            ("positions", ..., 0),
            ("positions", ..., 1),
            ("positions", ..., 2)
        ),
        componentType=gltf.FLOAT,
        elementSize=gltf.VEC3
    )
    vertex_struct.addAttributeToFormat(
        attrName="TEXCOORD_0",
        values=prims.uvs,
        sources=(
            ("uvs", ..., 0),
            ("uvs", ..., 1),
        ),
        componentType=gltf.FLOAT,
        elementSize=gltf.VEC2
    )

    vertex_data = vertex_struct.pack(prims)
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
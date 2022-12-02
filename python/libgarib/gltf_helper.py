from dataclasses import dataclass, replace
import hashlib
import math
import struct

import pygltflib as gltf

# TODO: move this into another module that's not-gltf-specific:
FRAME_TO_SEC = 1/29.97

TSR_INHERTANCE_EXTENSION = "EXT_node_tsr_inheritance"

def idToTexturePath(tex_id):
    return "textures/0x{:08X}.png".format(tex_id)

def transposeMap(fn, array):
    results = []
    for col_idx in range(len(array[0])):
        results.append(fn(*(row[col_idx] for row in array)))
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
        self.unknown = []

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

def addMeshDataToGLTFMesh(primitives, gltf_mesh, file, data):
    data_hash = hashlib.sha1()

    ###############################################
    # Build actual GLTF structures:

    for material, prims in sorted(primitives.items(), key=lambda p: p[0]):
        data_hash.update(str(material).encode())

        indices_data = b"".join(struct.pack("H", i) for i in prims.indices)
        indices_bufferview_handle = len(file.bufferViews)
        file.bufferViews.append(gltf.BufferView(
            buffer=0,
            byteOffset=len(data),
            byteLength=len(indices_data),
            target=gltf.ELEMENT_ARRAY_BUFFER,
        ))
        data.extend(indices_data)
        data_hash.update(indices_data)

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

        if len(prims.unknown) > 0:
            # TODO: this is hard to transfer
            #       to blender as a custom attribuet;
            #       instead, encode as a color channel?
            vertex_struct.addAttributeToFormat(
                attrName="_GLOVER_FLAGS",
                values=prims.unknown,
                sources=(
                    ("unknown", ...),
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
        data_hash.update(vertex_data)

        # Build GLTF primitive

        gltf_mesh.primitives.append(gltf.Primitive(
            attributes=vertex_struct.gltf_attribute_map(),
            material=len(file.materials),
            indices=indices_handle
        ))

        if material.texture_id is not None:
            file.materials.append(gltf.Material(
                name="0x{:08X}".format(material.texture_id),
                pbrMetallicRoughness = gltf.PbrMetallicRoughness(
                    baseColorTexture=gltf.TextureInfo(
                        index=len(file.textures)
                    )
                ),
                alphaMode=gltf.BLEND, # TODO: choose blend vs opaque depending on alpha mode
                alphaCutoff=None
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
                alphaCutoff=None
            ))

    return data_hash


def addAnimationDataToGLTF(mesh, channel_nodes, file, data):

    def addChannel(frames, output_type, channel_name):
        if len(file.animations) == 0:
            anim_root = gltf.Animation(name="Global timeline")
            file.animations.append(anim_root)
        else:
            anim_root = file.animations[0]

        # Build high-level animation structures
        anim_root.channels.append(gltf.AnimationChannel(
            sampler=len(anim_root.samplers),
            target=gltf.AnimationChannelTarget(
                node=file.nodes.index(channel_nodes[channel_name]),
                path=channel_name
            )
        ))
        anim_root.samplers.append(gltf.AnimationSampler(
            input=len(file.accessors),
            output=len(file.accessors)+1
        ))

        # Encode raw data
        if output_type == gltf.VEC3:
            output_struct = struct.Struct("<3f")
            output_tuples = [(frame.v1, frame.v2, frame.v3) for frame in frames]
        elif output_type == gltf.VEC4:
            output_struct = struct.Struct("<4f")
            output_tuples = [(frame.v1, frame.v2, frame.v3, frame.v4) for frame in frames]
        else:
            raise ValueError("Bad type")
        input_series = tuple(frame.t*FRAME_TO_SEC for frame in frames)

        encoded_output = b"".join(output_struct.pack(*frame) for frame in output_tuples)
        encoded_input = b"".join(struct.pack("<f",t) for t in input_series)

        # Build data pointer structures

        file.accessors.append(gltf.Accessor(
            bufferView=len(file.bufferViews),
            componentType=gltf.FLOAT,
            count=len(frames),
            type=gltf.SCALAR,
            max=[max(input_series)],
            min=[min(input_series)]

        ))
        file.accessors.append(gltf.Accessor(
            bufferView=len(file.bufferViews)+1,
            componentType=gltf.FLOAT,
            count=len(frames),
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


def addBillboardSpriteToGLTF(sprite, idx, parent_node, file, data):
    # TODO: make sure textures are right-side-up
    # TODO: don't have these nodes show up as skeletal bones

    name = "{:}_sprite_{:}".format(parent_node.name, idx)

    # Create node structure
    billboard_node = gltf.Node(
        name=name,
        mesh=len(file.meshes),
        translation=(sprite.x, sprite.y, sprite.z),
        scale=(1, sprite.height/3, sprite.width/3),
        extensions={
            TSR_INHERTANCE_EXTENSION: {"scale": False, "rotation": False}
        }
    )
    parent_node.children.append(len(file.nodes))
    file.nodes.append(billboard_node)

    billboard_mesh = gltf.Mesh(
        name=name,
        extras={
            "billboard": True,
            "sprite_idx": idx
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
        alphaMode=gltf.BLEND,
        alphaCutoff=None
    ))

    file.textures.append(gltf.Texture(
        sampler=findSampler(file, sprite_material),
        source=len(file.images)
    ))

    file.images.append(gltf.Image(
        uri=idToTexturePath(sprite_material.texture_id),
    ))

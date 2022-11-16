import struct
import pygltflib as gltf
from dataclasses import dataclass

def transposeMap(fn, array):
    results = []
    for col_idx in range(len(array[0])):
        results.append(fn(*(row[col_idx] for row in array)))
    return results

@dataclass(frozen=True)
class Material(object):
    texture_id: int = None
    clamp_s: bool = False
    clamp_t: bool = False
    mirror_s: bool = False
    mirror_t: bool = False

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

def addMeshDataToGLTFMesh(primitives, gltf_mesh, file, data):

    ###############################################
    # Build actual GLTF structures:

    for material, prims in primitives.items():
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

        # Build GLTF primitive

        gltf_mesh.primitives.append(gltf.Primitive(
            attributes=vertex_struct.gltf_attribute_map(),
            material=len(file.materials),
            indices=indices_handle
        ))

        if material is not None:
            file.materials.append(gltf.Material(
                pbrMetallicRoughness = gltf.PbrMetallicRoughness(
                    baseColorTexture=gltf.TextureInfo(
                        index=len(file.textures)
                    )
                ),
            ))

            file.textures.append(gltf.Texture(
                sampler=0,
                source=len(file.images)
            ))

            file.images.append(gltf.Image(
                uri="0x{:08X}.png".format(material),
            ))
        else:
            file.materials.append(gltf.Material(
                pbrMetallicRoughness = gltf.PbrMetallicRoughness(
                    baseColorFactor=[1, 1, 1, 1]
                ),
            ))

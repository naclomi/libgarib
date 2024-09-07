import base64
import json
import math
import struct

import numpy as np

from . import gltf_helper
from . import linkable

from .gbi import F3DEX, Vertex as GbiVertex, pack_uv, pack_color
from .parsers.glover_texbank import GloverTexbank


################################
# Packing

class LinkableDisplayList(linkable.LinkableStruct):
    pass

def relocatableDisplayListToLinkable(raw_mesh_dl):
    # Import a Fast64-style insertable binary, based on the
    # spec here:
    # https://github.com/Fast-64/fast64/blob/main/fast64_internal/sm64/README.md#insertable-binary-exporting
    #
    #   0x00-0x04 : Data Type
    #       0 = Display List
    #       1 = Geolayout
    #       2 = Animation
    #       3 = Collision
    #   0x04-0x08 : Data Size (size in bytes of Data Section)
    #   0x08-0x0C : Start Address (start address of data, relative to start of Data Section)
    #   0x0C-0x10 : Number of Pointer Addresses (number of pointer addresses to be resolved)
    #   0x10-N    : List of 4-byte pointer addresses. Each address relative to start of Data Section.
    #   N-end     : Data Section (actual binary data)
    pointers = []
    data_type = struct.unpack(">I", raw_mesh_dl[0:4])[0]
    data_size = struct.unpack(">I", raw_mesh_dl[4:8])[0]
    start_offset = struct.unpack(">I", raw_mesh_dl[8:0xC])[0]
    num_ptrs = struct.unpack(">I", raw_mesh_dl[0xC:0x10])[0]
    if data_type != 0:
        raise Exception("Relocatable binary is not a display list")
    cursor = 0x10
    payload_base = cursor + num_ptrs * 4
    for _ in range(num_ptrs):
        ptr_offset = struct.unpack(">I", raw_mesh_dl[cursor:cursor+4])[0]
        pointers.append(linkable.LinkablePointer(
            offset=ptr_offset,
            target=None, # Relative
            target_offset=struct.unpack(">I", raw_mesh_dl[payload_base+ptr_offset:payload_base+ptr_offset+4])[0]
        ))
        cursor += 4
    raw_dl = raw_mesh_dl[payload_base:payload_base+data_size]
    
    relocatable = linkable.LinkableBytes(data=raw_dl, pointers=pointers)
    return LinkableDisplayList([relocatable]), start_offset

def writeCullDL(linkable_dl, cmds, prims):
    # TODO: gsSPCullDisplayList with a cube based on the min/max values
    # of the position accessor, **scaled appropriately**
    cmds.data += F3DEX["G_CLEARGEOMETRYMODE"].pack(
        G_ZBUFFER=False,
        G_SHADE=False,
        G_SHADING_SMOOTH=False,
        G_CULL_FRONT=False,
        G_CULL_BACK=False,
        G_FOG=False,
        G_LIGHTING=True,
        G_TEXTURE_GEN=False,
        G_TEXTURE_GEN_LINEAR=False,
        G_CLIPPING=False
    )
    print("WARNING: gsSPCullDisplayList() not yet implemented")

def buildDLFaceBatch(vertex_cache, cursor, unlit):
    # Step through mesh faces accumulating them in a list
    # and keep track of unique indices, stopping when we've
    # hit 32.
    batch_indices = []
    unique_indices = set()
    while cursor < vertex_cache.idx_count:
        next_index = vertex_cache.indices[cursor]
        if vertex_cache.variants is not None:
            next_index >>= 2
        if next_index not in unique_indices:
            if len(unique_indices) >= 32:
                break
            unique_indices.add(next_index)
        batch_indices.append(next_index)
        cursor += 1
    face_overhang = len(batch_indices) % 3
    if face_overhang > 0:
        batch_indices = batch_indices[:len(batch_indices) - face_overhang]
        cursor -= face_overhang
        unique_indices = set(batch_indices)

    # Now for each unique index, pack it into the gbi vertex
    # batch and store a mapping from gltf index to gbi batch index
    batch_mapping = {}
    gbi_vertices = []
    for idx in sorted(unique_indices):
        gbi_v = GbiVertex(
            pos=vertex_cache.position[idx],
            uv=vertex_cache.uv_scaled[idx],
            rgb=vertex_cache.color[idx][:3],
            a=vertex_cache.color[idx][3],
            n=vertex_cache.norm[idx]
        )
        batch_mapping[idx] = len(gbi_vertices)
        gbi_vertices.append(gbi_v)
    
    vertex_data_block = linkable.LinkableBytes(b"".join(
        v.asDLBytes(not unlit) for v in gbi_vertices
    ))
    return cursor, vertex_data_block, batch_mapping


def tileLineSize(texture):
    formats = GloverTexbank.TextureCompressionFormat
    bpp = {
        formats.ci4: 0.5,
        formats.ci8: 1,
        formats.uncompressed_16b: 2,
        formats.uncompressed_32b: 4
    }[texture.compression_format]
    line_bytes = int(texture.width * bpp)
    return line_bytes >> 3


def writeTextureLoad(dl_cmds, material, texture):
    colors = GloverTexbank.TextureColorFormat
    formats = GloverTexbank.TextureCompressionFormat

    dl_cmds.data += F3DEX["G_RDPLOADSYNC"].pack()

    if texture.compression_format not in (formats.ci4, formats.ci8):
        lut_type = F3DEX.constants["G_TT_NONE"] << F3DEX.constants["G_MDSFT_TEXTLUT"]
    elif texture.color_format == colors.rgba:
        lut_type = F3DEX.constants["G_TT_RGBA16"] << F3DEX.constants["G_MDSFT_TEXTLUT"]
    elif texture.color_format == colors.ia:
        lut_type = F3DEX.constants["G_TT_IA16"] << F3DEX.constants["G_MDSFT_TEXTLUT"]
    else:
        raise ValueError("Unsupported compression/color format combo {:}+{:}".format(
            texture.color_format, texture.compression_format))
    dl_cmds.data += F3DEX["G_SETOTHERMODE_H"].pack(_raw=True,
        sft=F3DEX.constants["G_MDSFT_TEXTLUT"],
        len=2,
        data=lut_type
    )

    if lut_type != F3DEX.constants["G_TT_NONE"]:
        # gsDPLoadTLUT_pal16() / gsDPLoadTLUT_pal256()
        if texture.compression_format == formats.ci4:
            pal = 0
            tlut_addr = (256+(((pal)&0xf)*16))
            tlut_count = 15
        elif texture.compression_format == formats.ci8:
            tlut_addr = 256
            tlut_count = 255

        dl_cmds.data += F3DEX["G_SETTIMG"].pack(_raw=True,
            fmt=texture.color_format.value,
            siz=formats.uncompressed_16b,
            width=0,
            i=material.texture_id,
        )
        dl_cmds.data += F3DEX["G_RDPTILESYNC"].pack()
        dl_cmds.data += F3DEX["G_SETTILE"].pack(_raw=True,
            fmt=0, siz=0, line=0,
            tmem=tlut_addr,
            tile=F3DEX.constants["G_TX_LOADTILE"],
            palette=0, clampt=0, mirrort=0, maskt=0, shiftt=0, clamps=0, mirrors=0, masks=0, shifts=0,
        )
        dl_cmds.data += F3DEX["G_RDPLOADSYNC"].pack()
        dl_cmds.data += F3DEX["G_LOADTLUT"].pack(_raw=True,
            tile=F3DEX.constants["G_TX_LOADTILE"],
            count=tlut_count
        )
        dl_cmds.data += F3DEX["G_RDPPIPESYNC"].pack()

    #  gsDPLoadTextureBlock / gsDPLoadTextureBlock_4b

    block_px_size = formats.uncompressed_16b if texture.compression_format != formats.uncompressed_32b else formats.uncompressed_32b
    dl_cmds.data += F3DEX["G_SETTIMG"].pack(_raw=True,
        fmt=texture.color_format.value,
        siz=block_px_size,
        width=0,
        i=material.texture_id,
    )
    dl_cmds.data += F3DEX["G_SETTILE"].pack(_raw=True,
        fmt=texture.color_format.value,
        siz=block_px_size,
        line=0,
        tmem=0,
        tile=F3DEX.constants["G_TX_LOADTILE"],
        palette=0,
        clampt=material.clamp_t,
        mirrort=material.mirror_t,
        maskt=texture.maskt,
        shiftt=F3DEX.constants["G_TX_NOLOD"],
        clamps=material.clamp_s,
        mirrors=material.mirror_s,
        masks=texture.masks,
        shifts=F3DEX.constants["G_TX_NOLOD"],
    )
    dl_cmds.data += F3DEX["G_RDPLOADSYNC"].pack()

    block_incr, block_shift, bytes_per_texel, line_bytes = {
        formats.ci4: (3, 2, 0, 0),
        formats.ci8: (1, 1, 1, 1),
        formats.uncompressed_16b: (0, 0, 2, 2),
        formats.uncompressed_32b: (0, 0, 4, 2)
    }[texture.compression_format]

    if texture.compression_format == formats.ci4:
        row_words = max(1, texture.width // 16)
    else:
        row_words = max(1, texture.width * bytes_per_texel // 8)
    dxt = ((1 << F3DEX.constants["G_TX_DXT_FRAC"]) + row_words - 1) // row_words
    dl_cmds.data += F3DEX["G_LOADBLOCK"].pack(_raw=True,
        tile=F3DEX.constants["G_TX_LOADTILE"],
        uls=0,
        ult=0,
        lrs=(((texture.width * texture.height) + block_incr) >> block_shift)-1,
        dxt=dxt
    )
    dl_cmds.data += F3DEX["G_RDPPIPESYNC"].pack()

    if texture.compression_format == formats.ci4:
        line = ((texture.width >> 1) + 7) >> 3
    else:
        line = ((texture.width * line_bytes) + 7) >> 3
    dl_cmds.data += F3DEX["G_SETTILE"].pack(_raw=True,
        fmt=texture.color_format.value,
        siz=texture.compression_format.value,
        line=line,
        tmem=0,
        tile=F3DEX.constants["G_TX_RENDERTILE"],
        palette=0,
        clampt=material.clamp_t,
        mirrort=material.mirror_t,
        maskt=texture.maskt,
        shiftt=F3DEX.constants["G_TX_NOLOD"],
        clamps=material.clamp_s,
        mirrors=material.mirror_s,
        masks=texture.masks,
        shifts=F3DEX.constants["G_TX_NOLOD"],
    )

    dl_cmds.data += F3DEX["G_SETTILESIZE"].pack(_raw=True,
        tile=F3DEX.constants["G_TX_RENDERTILE"],
        uls=0,
        ult=0,
        lrs=(texture.width - 1) << F3DEX.constants["G_TEXTURE_IMAGE_FRAC"],
        lrt=(texture.height - 1) << F3DEX.constants["G_TEXTURE_IMAGE_FRAC"]
    )


def writeTileSettings(dl_cmds, material, texture):
    dl_cmds.data += F3DEX["G_RDPTILESYNC"].pack()
    dl_cmds.data += F3DEX["G_SETTILE"].pack(_raw=True,
        fmt=texture.color_format.value,
        siz=texture.compression_format.value,
        line=tileLineSize(texture),
        tmem=0,
        tile=F3DEX.constants["G_TX_RENDERTILE"],
        palette=0,
        clampt=material.clamp_t,
        mirrort=material.mirror_t,
        maskt=texture.maskt,
        shiftt=F3DEX.constants["G_TX_NOLOD"],
        clamps=material.clamp_s,
        mirrors=material.mirror_s,
        masks=texture.masks,
        shifts=F3DEX.constants["G_TX_NOLOD"],
    )


def writeVtxLoad(dl_cmds, vertex_data_block):
    dl_cmds.data += F3DEX["G_VTX"].pack(_raw=True,
        v0=0,
        n=len(vertex_data_block.data) // GbiVertex.LENGTH,
        length=len(vertex_data_block.data)-1,
        address=0
    )
    dl_cmds.pointers.append(linkable.LinkablePointer(
        offset=len(dl_cmds.data) - 4,
        target=vertex_data_block
    ))

def prepare_variants(dl_cmds, tri_indices, vertex_cache, batch_mapping, current_variants):
    # Check if vertices are already in the cache but need to be modified.
    # If so, write the appropriate dlist commands
    for full_idx in tri_indices:
        all_variants = full_idx & 0xfffffffc
        cache_idx = batch_mapping[full_idx >> 2]
        variant_idx = full_idx & 0x3
        if current_variants[cache_idx] != variant_idx:
            old = vertex_cache.variants[all_variants][current_variants[cache_idx]]
            new = vertex_cache.variants[all_variants][variant_idx]

            # TODO: do we need to worry about this?
            #
            # The s, t coordinates specified by this macro are not scaled by the
            # texture scale value set by gSPTexture. These coordinates must be
            # pre-scaled before they are transferred. For example, to use 1/2
            # (0x8000) as the texture scale, use a value that is one half of
            # the value used by gSPVertex.

            if (tuple(old[gltf_helper.MeshData.AttrType.uv]) != 
                tuple(new[gltf_helper.MeshData.AttrType.uv])):
                dl_cmds.data += F3DEX["G_MODIFYVTX"].pack(
                    where="G_MWO_POINT_ST",
                    vtx=cache_idx,
                    val=pack_uv(new[gltf_helper.MeshData.AttrType.uv])
                )

            if (tuple(old[gltf_helper.MeshData.AttrType.color]) !=
                tuple(new[gltf_helper.MeshData.AttrType.color])):
                dl_cmds.data += F3DEX["G_MODIFYVTX"].pack(
                    where="G_MWO_POINT_RGBA",
                    vtx=cache_idx,
                    val=pack_color(new[gltf_helper.MeshData.AttrType.color])
                )

            current_variants[cache_idx] = variant_idx
    return tri_indices.copy() >> 2

def iterate_batch_faces(batch_faces, variant_indexing, materials):
    cursor = 0
    while cursor < len(batch_faces):
        face = batch_faces[cursor]
        material = materials[face[3]]
        try:
            next_face = batch_faces[cursor + 1]
            next_material = materials[next_face[3]]
        except IndexError:
            next_face = None
            next_material = None

        can_do_two = (next_face is not None and
                      material == next_material)
        if can_do_two and variant_indexing:
            # Check that all indices use the same variants
            tri_indices = np.concatenate((face[:3], next_face[:3]))
            tri_variants = tri_indices & 0x3
            tri_indices >>= 2
            variant_compat = {}
            for sub_idx in range(6):
                if tri_indices[sub_idx] in variant_compat:
                    if variant_compat[tri_indices[sub_idx]] != tri_variants[sub_idx]:
                        can_do_two = False
                        break
                else:
                    variant_compat[tri_indices[sub_idx]] = tri_variants[sub_idx]

        if can_do_two:
            cursor += 2
            yield face, next_face
        else:
            cursor += 1
            yield face, None

def sort_faces_by_variant(faces, batch_mapping, materials, loaded_material):
    # Reorder batch faces to minimize variant switching by
    # sorting based on this key:
    # (!material_is_loaded, material_idx, v1_variant, v2_variant, v3_variant, original_batch_idx)
    # There is almost certainly no correlation between the v1 vertex used by one
    # face and the v1 vertex used by another, so what we're really trying to do
    # here is just generally group _any_ vertex that uses a given variant index
    # near others that use the same index, in the hopes that this reduces the
    # number of places that we'll cause a need for an extra gsSPModifyVertex
    # () call. This algorithm is VERY ad-hoc and probably not correct, but it
    # produces good enough results and I want to move on to other things. Also
    # note that variant 0 always comes first in this ordering, so
    # gsSPModifyVertex doesn't need to run right after a vertex is loaded

    # TODO: figure out how to ACTUALLY do this. look into instruction sorting.
    # To get a quick count:
    # make at1obj
    # objbank-tool.py dlist-rip build/suzanne.obj.bin --gfxdis ~/projects/glover-rev/glankk-n64/src/gfxdis/gfxdis.f3dex --output-dir /tmp/garib && cat /tmp/garib/9A276348.Suzanne.dlist.c | grep gsSPModifyVertex | wc -l

    to_sort = []
    for original_idx, face in enumerate(faces):
        material = materials[face[3]]
        variants = face[:3] & 0x3
        to_sort.append((
            material != loaded_material,
            material,
            *variants,
            original_idx
        ))

    sorted_faces = sorted(to_sort)
    order = list(face[-1] for face in sorted_faces)
    return faces[order]


def gltfNodeToDisplayList(node_idx, render_mode, bank, file, texture_db, vertex_cache):
    node = file.nodes[node_idx]
    mesh = file.meshes[node.mesh]
    rebuild_dl = True
    if "display_list" in mesh.extras:
        if "data_hash" in mesh.extras:
            mesh_hash = gltf_helper.hashGLTFMesh(mesh, file).hexdigest()
            if mesh_hash == mesh.extras["data_hash"]:
                rebuild_dl = False
        else:
            rebuild_dl = False

    if rebuild_dl:
        # Assume triangles are arranged to optimize cache use

        # TODO: write optimizer that:
        #   a) reorders triangles to fit well into the cache
        #   b) orders materials such that seam vertices can be reused
        #      with gsSPModifyVertex()
        materials = gltf_helper.extractGloverMaterialsFromGLTF(file)

        linkable_dl = LinkableDisplayList()
        cmds = linkable.LinkableBytes(b"")
        linkable_dl.append(cmds)

        writeCullDL(linkable_dl, cmds, vertex_cache)

        mode_cmd = "G_CLEARGEOMETRYMODE" if render_mode.unlit else "G_SETGEOMETRYMODE"
        cmds.data += F3DEX[mode_cmd].pack(
            G_LIGHTING=True
        )

        batch_cursor = 0
        loaded_material = gltf_helper.Material()

        while batch_cursor < vertex_cache.idx_count:
            next_batch_cursor, vertex_data_block, batch_mapping = buildDLFaceBatch(
                vertex_cache, batch_cursor, render_mode.unlit)
            linkable_dl.append(vertex_data_block)

            batch_faces = np.ndarray(((next_batch_cursor - batch_cursor)//3, 4), dtype="H")
            batch_faces_cursor = 0
            for batch_cursor in range(batch_cursor, next_batch_cursor, 3):
                batch_faces[batch_faces_cursor][:3] = vertex_cache.indices[batch_cursor:batch_cursor+3]
                batch_faces[batch_faces_cursor][3] = batch_cursor//3
                batch_faces_cursor += 1
            batch_cursor = next_batch_cursor


            if vertex_cache.variants is not None:
                current_variants = {cache_idx: 0 for cache_idx in range(len(batch_mapping))}
                batch_faces = sort_faces_by_variant(batch_faces, batch_mapping, vertex_cache.material, loaded_material)

            # Write the display list commands, starting with loading
            # the vertex batch into the RDP and then the triangle
            # commands themselves, interleaved with texture loads
            # as appropriate
            vertices_loaded = False
            for face1, face2 in iterate_batch_faces(batch_faces, vertex_cache.variants is not None, vertex_cache.material):
                material = vertex_cache.material[face1[3]]
                if material != loaded_material:
                    if material.texture_id is not None:
                        texture = texture_db.byId[material.texture_id]
                        if material.texture_id != loaded_material.texture_id:
                            writeTextureLoad(cmds, material, texture)
                            writeVtxLoad(cmds, vertex_data_block)
                            vertices_loaded = True
                        writeTileSettings(cmds, material, texture)
                    else:
                        raise NotImplementedError("Non-textured faces")
                    loaded_material = material
                if not vertices_loaded:
                    writeVtxLoad(cmds, vertex_data_block)
                    vertices_loaded = True
                if face2 is not None:
                    tri_indices_1 = face1[:3]
                    tri_indices_2 = face2[:3]
                    if vertex_cache.variants is not None:
                        tri_indices_1 = prepare_variants(cmds, tri_indices_1, vertex_cache, batch_mapping, current_variants)
                        tri_indices_2 = prepare_variants(cmds, tri_indices_2, vertex_cache, batch_mapping, current_variants)
                    cmds.data += F3DEX["G_TRI2"].pack(
                        v00=batch_mapping[tri_indices_1[0]],
                        v01=batch_mapping[tri_indices_1[1]],
                        v02=batch_mapping[tri_indices_1[2]],
                        v10=batch_mapping[tri_indices_2[0]],
                        v11=batch_mapping[tri_indices_2[1]],
                        v12=batch_mapping[tri_indices_2[2]]
                    )
                else:
                    tri_indices = face1[:3]
                    if vertex_cache.variants is not None:
                        tri_indices = prepare_variants(cmds, tri_indices, vertex_cache, batch_mapping, current_variants)
                    cmds.data += F3DEX["G_TRI1"].pack(
                        v0=batch_mapping[tri_indices[0]],
                        v1=batch_mapping[tri_indices[1]],
                        v2=batch_mapping[tri_indices[2]],
                    )

        cmds.data += F3DEX["G_ENDDL"].pack()
        start_offset = 0
    else:
        raw_mesh_dl = base64.b64decode(mesh.extras["display_list"])
        linkable_dl, start_offset = relocatableDisplayListToLinkable(raw_mesh_dl)
    bank.include(linkable_dl)
    return linkable_dl, start_offset

################################
# Dumping

def f3dex_to_prims(display_list, bank, lighting, texture_db, scale_factor):
    raw_dl = b"".join(struct.pack(">II", cmd.w1, cmd.w0) for cmd in display_list)

    def execute_dl(tri_callback):
        vertex_buffer = [GbiVertex() for _ in range(32)]

        material = gltf_helper.Material()
        texture_size = (1,1)


        for cmd, args in F3DEX.parseList(raw_dl):
            if cmd is F3DEX["G_VTX"]:
                write_idx = args["v0"]
                for read_idx in range(args["n"]):
                    vertex_bytes = bank[args["address"] + read_idx*GbiVertex.LENGTH:
                                             args["address"] + (read_idx+1)*GbiVertex.LENGTH]
                    vertex_buffer[write_idx].unpack(vertex_bytes)
                    write_idx += 1
            elif cmd is F3DEX["G_MODIFYVTX"]:
                v = vertex_buffer[args["vtx"]]
                if args["where"] == "G_MWO_POINT_RGBA":
                    v.setNormRGBA(args["val"])
                elif args["where"] == "G_MWO_POINT_ST":
                    v.setUV(args["val"])
                elif args["where"] == "G_MWO_POINT_XYSCREEN":
                    v.setXY(args["val"])
                elif args["where"] == "G_MWO_POINT_ZSCREEN":
                    v.setZ(args["val"])
                else:
                    raise Exception("Bad G_MODIFYVTX 'where'")
            elif cmd in (F3DEX["G_TRI1"], F3DEX["G_TRI2"]):
                tri_callback(locals())
            elif cmd is F3DEX["G_SETGEOMETRYMODE"]:
                    # TODO: G_SHADING_SMOOTH
                if args["G_LIGHTING"] is True:
                    lighting = True
            elif cmd is F3DEX["G_CLEARGEOMETRYMODE"]:
                if args["G_LIGHTING"] is True:
                    lighting = False
            elif cmd is F3DEX["G_ENDDL"]:
                break
            elif cmd is F3DEX["G_SETTIMG"]:
                material = material.mutate(
                    texture_id = args["i"]
                )
            elif cmd is F3DEX["G_SETTILE"]:
                material = material.mutate(
                    clamp_s=args["clamps"] == 1,
                    mirror_s=args["mirrors"] == 1,
                    clamp_t=args["clampt"] == 1,
                    mirror_t=args["mirrort"] == 1
                )
            elif cmd is F3DEX["G_SETTILESIZE"]:
                # TODO: use uls and ult?
                texture_size = (args["lrs"], args["lrt"])
            elif cmd in (F3DEX["G_CULLDL"],
                         F3DEX["G_RDPLOADSYNC"],
                         F3DEX["G_RDPTILESYNC"],
                         F3DEX["G_RDPPIPESYNC"],
                         F3DEX["G_LOADBLOCK"],
                         F3DEX["G_LOADTLUT"],
                         F3DEX["G_SETOTHERMODE_H"]):
                pass
            else:
                raise Exception("TODO: Not yet implemented: Export F3DEX command {:}".format(cmd))


    face_counts = {}
    def count_prims(env):
        if env["cmd"] is F3DEX["G_TRI1"]:
            n = 1    
        elif env["cmd"] is F3DEX["G_TRI2"]:
            n = 2
        face_counts[env["material"]] = face_counts.get(env["material"], 0) + n
    execute_dl(count_prims)

    primitives = {}
    for material, face_count in face_counts.items():
        prims = gltf_helper.MeshData()
        primitives[material] = prims
        prims.face_count = face_count
        prims.material = material
        prims.texture = texture_db.byId[material.texture_id]
        # TODO: don't dupe vertices if you don't have to
        prims.vertex_count = face_count * 3
        prims.index_count = face_count * 3
        prims.indices = np.zeros(prims.vertex_count)

    prim_cursor = {k:0 for k in primitives.keys()}
    def build_prims(env):
        if env["cmd"] is F3DEX["G_TRI1"]:
            idx_list = (env["args"]["v0"], env["args"]["v1"], env["args"]["v2"])
        elif env["cmd"] is F3DEX["G_TRI2"]:
            idx_list = (env["args"]["v00"], env["args"]["v01"], env["args"]["v02"],
                        env["args"]["v10"], env["args"]["v11"], env["args"]["v12"])
        prims = primitives[env["material"]]
        cursor = prim_cursor[env["material"]]
        for v_idx in idx_list:
            v = env["vertex_buffer"][v_idx]
            prims.indices[cursor] = cursor
            prims.position[cursor] = (v.x / scale_factor, v.y / scale_factor, v.z / scale_factor)
            prims.uv[cursor] = (v.u/env["texture_size"][0], v.v/env["texture_size"][1])
            if lighting is True:
                norm_mag = math.sqrt(v.nx**2 + v.ny**2 + v.nz**2)
                prims.norm[cursor] = (v.nx/norm_mag, v.ny/norm_mag, v.nz/norm_mag)
            else:
                prims.color[cursor] = (v.r, v.g, v.b, 1)
            cursor += 1
        prim_cursor[env["material"]] = cursor

    execute_dl(build_prims)

    return list(primitives.values())


def dump_f3dex_dl(display_list):
    # Dump a Fast64-style insertable binary, based on the
    # spec here:
    # https://github.com/Fast-64/fast64/blob/main/fast64_internal/sm64/README.md#insertable-binary-exporting
    #
    #   0x00-0x04 : Data Type
    #       0 = Display List
    #       1 = Geolayout
    #       2 = Animation
    #       3 = Collision
    #   0x04-0x08 : Data Size (size in bytes of Data Section)
    #   0x08-0x0C : Start Address (start address of data, relative to start of Data Section)
    #   0x0C-0x10 : Number of Pointer Addresses (number of pointer addresses to be resolved)
    #   0x10-N    : List of 4-byte pointer addresses. Each address relative to start of Data Section.
    #   N-end     : Data Section (actual binary data)
    raw_dl = bytearray(b"".join(struct.pack(">II", cmd.w1, cmd.w0) for cmd in display_list))
    linked_data = []
    dl_offset = 0
    for cmd, args in F3DEX.parseList(raw_dl):
        if cmd is F3DEX["G_VTX"]:
            region_offset = args["address"]
            region_size = args["length"] + 1
            linked_data.append((dl_offset+4, region_offset, region_size))
        elif (cmd is F3DEX["G_MTX"]
         or cmd is F3DEX["G_MOVEMEM"]
         or cmd is F3DEX["G_DL"]
         or cmd is F3DEX["G_BRANCH_Z"]):
            raise Exception("TODO: Not yet implemented: Export F3DEX command {:}".format(cmd))
        dl_offset += 8

    output = bytearray()
    output += struct.pack(">I", 0) # Data type (0/display list)
    output += struct.pack(">I", len(raw_dl) + sum(region[2] for region in linked_data)) # Size of DL and associated data
    output += struct.pack(">I", 0) # Start address/entry point of DL (for us, always 0)
    output += struct.pack(">I", len(linked_data)) # Number of pointers

    # Pointer offsets in DL data
    for dl_offset, _, _ in linked_data:
        output += struct.pack(">I", dl_offset)
    
    # Write out DL itself
    payload_start = len(output)
    output += raw_dl

    # Write subsequent linked data regions
    io = display_list[0]._io
    old_pos = io.pos()
    for dl_offset, region_offset, region_size in linked_data:
        # Rewrite dl pointer to relocated data
        ptr_start = payload_start + dl_offset
        ptr_end = ptr_start + 4
        output[ptr_start: ptr_end] = struct.pack(">I", len(output) - payload_start)
        io.seek(region_offset)
        output += io.read_bytes(region_size)
    io.seek(old_pos)

    return output

import base64
import json
import math
import struct

from . import gltf_helper
from . import linkable

from .gbi import F3DEX, Vertex as GbiVertex
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
            dtype=">I",
            target=None, # Relative
            target_offset=struct.unpack(">I", raw_mesh_dl[payload_base+ptr_offset:payload_base+ptr_offset+4])[0]
        ))
        cursor += 4
    raw_dl = raw_mesh_dl[payload_base:payload_base+data_size]
    
    relocatable = linkable.LinkableBytes(data=raw_dl, pointers=pointers)
    return LinkableDisplayList([relocatable]), start_offset

def writeCullDL(linkable_dl, cmds, vertex_cache):
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
    while cursor < len(vertex_cache["indices"]):
        next_index = vertex_cache["indices"][cursor]
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
            pos=vertex_cache["POSITION"][idx],
            uv=vertex_cache["TEXCOORD_0"][idx],
            rgb=vertex_cache["COLOR_0"][idx][:3],
            a=vertex_cache["COLOR_0"][idx][3],
            n=vertex_cache["NORMAL"][idx]
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
        dtype=">I",
        target=vertex_data_block
    ))


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
        previous_material = gltf_helper.Material()
        while batch_cursor < len(vertex_cache["indices"]):
            next_batch_cursor, vertex_data_block, batch_mapping = buildDLFaceBatch(
                vertex_cache, batch_cursor, render_mode.unlit)
            linkable_dl.append(vertex_data_block)

            # Write the display list commands, starting with loading
            # the vertex batch into the RDP and then the triangle
            # commands themselves, interleaved with texture loads
            # as appropriate
            face_cursor = batch_cursor
            vertices_loaded = False
            while face_cursor < next_batch_cursor:
                material = materials[vertex_cache["material"][face_cursor]]
                can_do_two = face_cursor + 6 <= len(vertex_cache["indices"])
                if can_do_two:
                    material_2 = materials[vertex_cache["material"][face_cursor + 3]]
                    can_do_two &= (material == material_2)
                if material != previous_material:
                    if material.texture_id is not None:
                        texture = texture_db.byId[material.texture_id]
                        if material.texture_id != previous_material.texture_id:
                            writeTextureLoad(cmds, material, texture)
                            writeVtxLoad(cmds, vertex_data_block)
                            vertices_loaded = True
                        writeTileSettings(cmds, material, texture)
                    else:
                        raise NotImplementedError("Non-textured faces")
                    previous_material = material
                if not vertices_loaded:
                    writeVtxLoad(cmds, vertex_data_block)
                    vertices_loaded = True
                if can_do_two:
                    cmds.data += F3DEX["G_TRI2"].pack(
                        v00=batch_mapping[vertex_cache["indices"][face_cursor]],
                        v01=batch_mapping[vertex_cache["indices"][face_cursor+1]],
                        v02=batch_mapping[vertex_cache["indices"][face_cursor+2]],
                        v10=batch_mapping[vertex_cache["indices"][face_cursor+3]],
                        v11=batch_mapping[vertex_cache["indices"][face_cursor+4]],
                        v12=batch_mapping[vertex_cache["indices"][face_cursor+5]]
                    )
                    face_cursor += 6
                else:
                    cmds.data += F3DEX["G_TRI1"].pack(
                        v0=batch_mapping[vertex_cache["indices"][face_cursor]],
                        v1=batch_mapping[vertex_cache["indices"][face_cursor+1]],
                        v2=batch_mapping[vertex_cache["indices"][face_cursor+2]],
                    )
                    face_cursor += 3

            batch_cursor = next_batch_cursor

        cmds.data += F3DEX["G_ENDDL"].pack()
        start_offset = 0
    else:
        raw_mesh_dl = base64.b64decode(mesh.extras["display_list"])
        linkable_dl, start_offset = relocatableDisplayListToLinkable(raw_mesh_dl)
    bank.include(linkable_dl)
    return linkable_dl, start_offset

################################
# Dumping

def f3dex_to_prims(display_list, bank, lighting, texture_sizes):
    primitives = {}

    raw_dl = b"".join(struct.pack(">II", cmd.w1, cmd.w0) for cmd in display_list)

    vertex_buffer = [GbiVertex() for _ in range(32)]

    material = gltf_helper.Material()
    texture_size = (1,1)

    for cmd, args in F3DEX.parseList(raw_dl):
        if cmd is F3DEX.byName["G_VTX"]:
            write_idx = args["v0"]
            for read_idx in range(args["n"]):
                vertex_bytes = bank[args["address"] + read_idx*GbiVertex.LENGTH:
                                         args["address"] + (read_idx+1)*GbiVertex.LENGTH]
                vertex_buffer[write_idx].unpack(vertex_bytes)
                write_idx += 1
        elif cmd is F3DEX.byName["G_MODIFYVTX"]:
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
        elif cmd in (F3DEX.byName["G_TRI1"], F3DEX.byName["G_TRI2"]):
            if cmd is F3DEX.byName["G_TRI1"]:
                idx_list = (args["v0"], args["v1"], args["v2"])
            elif cmd is F3DEX.byName["G_TRI2"]:
                idx_list = (args["v00"], args["v01"], args["v02"],
                            args["v10"], args["v11"], args["v12"])
            prims = primitives.get(material, gltf_helper.MeshData())
            primitives[material] = prims
            for v_idx in idx_list:
                v = vertex_buffer[v_idx]
                prims.indices.append(len(prims.positions))
                prims.positions.append((v.x, v.y, v.z))
                prims.uvs.append((v.u/texture_size[0], v.v/texture_size[1]))
                if lighting is True:
                    norm_mag = math.sqrt(v.nx**2 + v.ny**2 + v.nz**2)
                    prims.norms.append((v.nx/norm_mag, v.ny/norm_mag, v.nz/norm_mag)) 
                else:
                    prims.colors.append((v.r, v.g, v.b))
        elif cmd is F3DEX.byName["G_SETGEOMETRYMODE"]:
                # TODO: G_SHADING_SMOOTH
            if args["G_LIGHTING"] is True:
                lighting = True
        elif cmd is F3DEX.byName["G_CLEARGEOMETRYMODE"]:
            if args["G_LIGHTING"] is True:
                lighting = False
        elif cmd is F3DEX.byName["G_ENDDL"]:
            break
        elif cmd is F3DEX.byName["G_SETTIMG"]:
            material = material.mutate(
                texture_id = args["i"]
            )
        elif cmd is F3DEX.byName["G_SETTILE"]:
            material = material.mutate(
                clamp_s=args["clamps"] == 1,
                mirror_s=args["mirrors"] == 1,
                clamp_t=args["clampt"] == 1,
                mirror_t=args["mirrort"] == 1
            )
        elif cmd is F3DEX.byName["G_SETTILESIZE"]:
            # TODO: use uls and ult?
            texture_size = (args["lrs"], args["lrt"])
        elif cmd in (F3DEX.byName["G_CULLDL"],
                     F3DEX.byName["G_RDPLOADSYNC"],
                     F3DEX.byName["G_RDPTILESYNC"],
                     F3DEX.byName["G_RDPPIPESYNC"],
                     F3DEX.byName["G_LOADBLOCK"],
                     F3DEX.byName["G_LOADTLUT"],
                     F3DEX.byName["G_SETOTHERMODE_H"]):
            pass
        else:
            raise Exception("TODO: Not yet implemented: Export F3DEX command {:}".format(cmd))

    return primitives


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
        if cmd is F3DEX.byName["G_VTX"]:
            region_offset = args["address"]
            region_size = args["length"] + 1
            linked_data.append((dl_offset+4, region_offset, region_size))
        elif (cmd is F3DEX.byName["G_MTX"]
         or cmd is F3DEX.byName["G_MOVEMEM"]
         or cmd is F3DEX.byName["G_DL"]
         or cmd is F3DEX.byName["G_BRANCH_Z"]):
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

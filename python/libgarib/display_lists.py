import json
import struct

from . import gltf_helper

from .gbi import F3DEX, Vertex as GbiVertex

def f3dex_to_prims(display_list, bank, lighting):
    primitives = {}

    raw_dl = b"".join(struct.pack(">II", cmd.w1, cmd.w0) for cmd in display_list)

    vertex_buffer = [GbiVertex() for _ in range(32)]

    next_material = gltf_helper.Material()

    # print("\n\n\n------------------")
    # print(display_list[0]._parent.name.strip("\0"))
    for cmd, args in F3DEX.parseList(raw_dl):
        # print(cmd.name, args)
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
            prims = primitives.get(next_material, gltf_helper.MeshData())
            primitives[next_material] = prims
            for v_idx in idx_list:
                v = vertex_buffer[v_idx]
                prims.indices.append(len(prims.positions))
                prims.positions.append((v.x, v.y, v.z))
                prims.uvs.append((v.u, v.v))
                if lighting is True:
                    prims.norms.append((v.nx, v.ny, v.nz)) 
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
            next_material = next_material.mutate(
                texture_id = args["i"]
            )
        elif cmd is F3DEX.byName["G_SETTILE"]:
            next_material = next_material.mutate(
                clamp_s=args["clamps"] == 1,
                mirror_s=args["mirrors"] == 1,
                clamp_t=args["clampt"] == 1,
                mirror_t=args["mirrort"] == 1
            )
        elif cmd is F3DEX.byName["G_SETTILESIZE"]:
            # TODO: use these coords to normalize texture coordinates
            pass
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
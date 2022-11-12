import json
import struct
from .gbi import F3DEX, Vertex as GbiVertex

def f3dexToGltf(display_list, bank, file):
    raw_dl = b"".join(struct.pack(">II", cmd.w1, cmd.w0) for cmd in mesh.display_list)

    vertex_buffer = [GbiVertex() for _ in range(32)]

    # TODO: materials

    for cmd, args in F3DEX.parseList(raw_dl):
        if cmd is F3DEX.byName["G_VTX"]:
            n_dma_bytes = GbiVertex.LENGTH * args["n"]
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
        elif cmd is F3DEX.byName["G_TRI1"]:
            # v0, v1, v2
            # buffer = (
            #     self.vertices[v0].asGLBytes(self.lightingEnabled) +
            #     self.vertices[v1].asGLBytes(self.lightingEnabled) +
            #     self.vertices[v2].asGLBytes(self.lightingEnabled))
            # if self.renderBackfaces:
            #     self.ctx.disable(moderngl.CULL_FACE)
            # self.vbo.write(buffer)
            # self.configureTextures()
            # self.vao.render(vertices=3)
            # return True

            # TODO
            ...
        elif cmd is F3DEX.byName["G_TRI2"]:
            # v00, v01, v02, v10, v11, v12
            # buffer = (
            #     self.vertices[v00].asGLBytes(self.lightingEnabled) +
            #     self.vertices[v01].asGLBytes(self.lightingEnabled) +
            #     self.vertices[v02].asGLBytes(self.lightingEnabled) +
            #     self.vertices[v10].asGLBytes(self.lightingEnabled) +
            #     self.vertices[v11].asGLBytes(self.lightingEnabled) +
            #     self.vertices[v12].asGLBytes(self.lightingEnabled))
            # if self.renderBackfaces:
            #     self.ctx.disable(moderngl.CULL_FACE)
            # self.vbo.write(buffer)
            # self.configureTextures()
            # self.vao.render(vertices=6)

            # TODO
            ...
        elif cmd is F3DEX.byName["G_ENDDL"]:
            break
        else:
            raise Exception("TODO: Not yet implemented: Export F3DEX command {:}".format(cmd))
        offset += 8



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
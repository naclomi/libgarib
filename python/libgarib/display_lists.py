import json
import struct
from .gbi import F3DEX


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
import base64
import json
import math
import struct

from . import gltf_helper
from . import linkable

from .gbi import F3DEX, Vertex as GbiVertex

################################
# Packing

class LinkableDisplayList(linkable.LinkableBytes):
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
    return LinkableDisplayList(data=raw_dl, pointers=pointers), start_offset


def gltfNodeToDisplayList(node_idx, bank, file):
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
        # TODO: rebuild dl
        start_offset = 0
        raise Exception()
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
    for dl_offset, region_offset, region_size in linked_data:
        # Rewrite dl pointer to relocated data
        ptr_start = payload_start + dl_offset
        ptr_end = ptr_start + 4
        output[ptr_start: ptr_end] = struct.pack(">I", len(output) - payload_start)
        display_list[0]._io.seek(region_offset)
        output += display_list[0]._io.read_bytes(region_size)

    return output

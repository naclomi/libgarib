#!/usr/bin/env python3
import argparse
import dataclasses
import json
import os
import sys
import typing

import _prefer_local_implementation
import libgarib.objects
from libgarib.parsers.glover_objbank import GloverObjbank

from libgarib.hash import hash_str
from libgarib.fla2 import compress, data_from_stream
from libgarib.gbi import F3DEX

def kaitaiObjectRange(parent, field):
    if field is None:
        start_field = parent.SEQ_FIELDS[0]
        end_field = parent.SEQ_FIELDS[-1]
        return parent._debug[start_field]["start"], parent._debug[end_field]["end"]
    elif field in parent._debug:
        return parent._debug[field]["start"], parent._debug[field]["end"]
    else:
        getattr(parent, field) # Force lazy load of Kaitai object instance (grrl, ew)
        instance_name = "_m_{:}".format(field)
        return parent._debug[instance_name]["start"], parent._debug[instance_name]["end"]
    raise Exception(field)

@dataclasses.dataclass
class BankSegment:
    memory_range: typing.Tuple[int, int]
    dtype: str
    name: str

def scrapeBankSegments(bank_data):
    bank = GloverObjbank.from_bytes(bank_data)

    bank_map = []
    def bank_push(parent, field, dtype, name):
        if parent is None:
            return
        if field is not None:
            if not hasattr(parent, field):
                return
            if getattr(parent, field) is None:
                return
        bank_map.append(BankSegment(
            memory_range=kaitaiObjectRange(parent, field),
            dtype=dtype,
            name=name
        ))

    bank_push(bank, "directory", "Directory", "")
    for dir_entry in bank.directory:
        actor = dir_entry.obj_root
        if actor is None:
            continue
        bank_push(dir_entry, "obj_root", "Actor root", "{:08X}".format(dir_entry.obj_id))
        if actor.mesh is not None:

            def scrape_mesh(mesh, parents, cur_matrix):
                name = "{:08X}.".format(dir_entry.obj_id) + libgarib.objects.parent_str(parents + [mesh])
                bank_push(mesh, None, "Mesh", name)

                if mesh.geometry is not None:
                    geo = mesh.geometry
                    bank_push(mesh, "geometry", "Geometry root", name)
                    bank_push(geo, "u1", "Geometry (face normals)", name)
                    bank_push(geo, "vertices", "Geometry (vertices)", name)
                    bank_push(geo, "faces", "Geometry (faces)", name)
                    bank_push(geo, "uvs", "Geometry (UVs)", name)
                    bank_push(geo, "uvs_unmodified", "Geometry (UV original copies)", name)
                    bank_push(geo, "colors_norms", "Geometry (vertex colors)", name)
                    bank_push(geo, "u5", "Geometry (face properties)", name)
                    bank_push(geo, "texture_ids", "Geometry (texture ids)", name)
                bank_push(mesh, "sprites", "Sprites", name)
                bank_push(mesh, "scale", "Keyframes (scale)", name)
                bank_push(mesh, "translation", "Keyframes (translation)", name)
                bank_push(mesh, "rotation", "Keyframes (rotation)", name)
                bank_push(mesh, "display_list", "Display list", name)

                if mesh.display_list is not None:
                    def scrape_dl(file, offset):
                        base_offset = offset
                        while True:
                            cmd, cmd_args = F3DEX.parse(file[offset: offset+8])
                            offset += 8
                            if cmd is F3DEX.byName["G_ENDDL"]:
                                break
                            elif cmd is F3DEX.byName["G_VTX"]:
                                start = cmd_args["address"]
                                end = start + cmd_args["length"] + 1
                                bank_map.append(BankSegment(
                                    memory_range=(start, end),
                                    dtype="DL Vertex Data",
                                    name="{:}.dl.cmd[{:08X}]".format(name, offset)
                                ))
                            elif (cmd is F3DEX.byName["G_MTX"]
                             or cmd is F3DEX.byName["G_MOVEMEM"]
                             or cmd is F3DEX.byName["G_DL"]
                             or cmd is F3DEX.byName["G_BRANCH_Z"]):
                                raise Exception("TODO: Not yet implemented: Scrape F3DEX command {:}".format(cmd))
                    scrape_dl(bank_data, mesh._debug["_m_display_list"]["start"])


            libgarib.objects.for_each_mesh(actor.mesh, scrape_mesh)
        if actor.animation is not None:
            bank_push(actor, "animation", "Animation props", "{:08X}".format(dir_entry.obj_id))
            bank_push(actor.animation, "animation_definitions", "Animation defs", "{:08X}".format(dir_entry.obj_id))
    bank_map.sort(key=lambda s: s.memory_range[0])
    return bank_map

def fillGaps(segments):
    gaps = []
    activeSegments = []
    for segment in segments:
        nextActiveSegments = [s for s in activeSegments if s.memory_range[1]  >= segment.memory_range[0]]
        if len(activeSegments) > 0 and len(nextActiveSegments) == 0:
            lastEnd = max(s.memory_range[1] for s in activeSegments)
            gaps.append(BankSegment(
                memory_range=(lastEnd, segment.memory_range[0]),
                dtype="???",
                name=""
            ))
        activeSegments = nextActiveSegments
        activeSegments.append(segment)

    segments = segments + gaps
    segments.sort(key=lambda s: s.memory_range[0])
    return segments

def bankmap(args):
    for bank_filename in args.bank_file:
        with open(bank_filename, "rb") as f:
            bank_data = data_from_stream(f)
        segments = scrapeBankSegments(bank_data)
        segments = fillGaps(segments)

        print("{:}:".format(bank_filename))
        for segment in segments:
            seg_size = segment.memory_range[1] - segment.memory_range[0]
            if seg_size == 1:
                mem_str = "0x{:08X}\t".format(segment.memory_range[0])
            elif seg_size == 0:
                mem_str = "0x{:08X} (!!ZERO LENGTH ARRAY!!)".format(segment.memory_range[0])

            else:
                mem_str = "0x{:08X}-0x{:08X}".format(
                    segment.memory_range[0],
                    segment.memory_range[1],
                )

            if segment.dtype == "???":
                padding = True
                for addr in range(*segment.memory_range):
                    if bank_data[addr] != 0:
                        padding = False
                        break
                if padding:
                    segment.dtype = "Padding"

            print("\t{:}\t{:}\t{:}".format(
                mem_str,
                segment.dtype,
                segment.name))
 

def unpack(args):
    for bank_filename in args.bank_file:
        bank_output_dir = os.path.join(args.output_dir, os.path.splitext(os.path.basename(bank_filename))[0] + ".unpacked")
        os.makedirs(bank_output_dir, exist_ok=True)
        with open(bank_filename, "rb") as f:
            bank_data = data_from_stream(f)
        bank = GloverObjbank.from_bytes(bank_data)

        for entry in bank.directory:
            obj = entry.obj_root
            if obj is None:
                continue

            # TODO: include animation data
            actor = {}

            obj_output_dir = os.path.join(bank_output_dir, "0x{:08x} ({:})".format(obj.obj_id, obj.mesh.name.strip("\x00")))
            os.makedirs(obj_output_dir, exist_ok=True)
            def mesh_dump_callback(mesh, parents, cur_matrix):
                name_str = mesh.name.strip("\x00")
                actor_node = {
                    "id": mesh.id,
                    "children": []
                }
                if len(parents) > 0:
                    name_str = libgarib.objects.parent_str(parents) + "." + name_str
                dl = libgarib.objects.dump_f3dex_dl(mesh, bank_data)
                if len(dl) > 0:
                    dl_filename = os.path.join(obj_output_dir, name_str + ".f3dex.lgdl")
                    actor_node["dl"] = os.path.relpath(dl_filename, bank_output_dir)
                    with open(dl_filename, "wb") as f:
                        f.write(dl)
                if mesh.geometry.num_faces > 0:
                    ply_filename = os.path.join(obj_output_dir, name_str + ".ply")
                    actor_node["model"] = os.path.relpath(ply_filename, bank_output_dir)
                    with open(ply_filename, "wb") as f:
                        f.write(libgarib.objects.mesh_to_ply(mesh))
                mesh.dump_actor_node = actor_node
                if len(parents) > 0:
                    parents[-1].dump_actor_node["children"].append(actor_node)


            libgarib.objects.for_each_mesh(obj.mesh, mesh_dump_callback)
            actor["mesh"] = obj.mesh.dump_actor_node

            with open(os.path.join(bank_output_dir, "0x{:08x}.actor.json".format(obj.obj_id)), "w") as f:
                json.dump(actor, f, indent=2, sort_keys=True)


def pack(args):
    directory = []

    # TODO: figure out the actual arrangement/enumeration
    data = libgarib.objects.CollatedDataFile([
        "directory", "model_vtx", "dl_vtx", "dl",
        "mesh", "sprite", "anim", "actor"
    ])

    for actor_filename in args.actor_file:
        with open(actor_filename, "r") as f:
            actor = json.load(f)
            directory.append(str(actor))

    bank = data.link()

    if args.compress:
        def compression_progress_callback(percent):
            sys.stdout.write("\rCompressing ({:}%)".format(percent));
        with open(args.output_file, "wb") as f:
            bank_stream = io.BytesIO(bank)
            compression_progress_callback(0)
            compress(bank_stream, f, progress_callback=compression_progress_callback)
            sys.stdout.write("\n")
    else:
        with open(args.output_file, "wb") as f:
            f.write(bank)
    sys.stdout.write("Packed {:} objects into bank '{:}'\n".format(len(directory), args.output_file))

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Tool to work with object bank archives from Glover (N64)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    pack_parser = subparsers.add_parser('pack', help='Build object banks from raw model assets')
    pack_parser.add_argument("actor_file", type=str, nargs="+",
                        help="Actor file to pack (.actor.json)")
    pack_parser.add_argument("--output-file", type=str, required=True,
                        help="File to write bank into")
    pack_parser.add_argument("--compress", action="store_true",
                        help="FLA2-compress the output")

    unpack_parser = subparsers.add_parser('unpack', help='Extract raw model assets from object banks')
    unpack_parser.add_argument("bank_file", type=str, nargs="+",
                        help="Object bank file (potentially FLA2-compressed)")
    unpack_parser.add_argument("--output-dir", type=str, default=os.getcwd(),
                        help="Directory to output bank contents")

    map_parser = subparsers.add_parser('map', help='Dump memory map of object banks')
    map_parser.add_argument("bank_file", type=str, nargs="+",
                        help="Object bank file (potentially FLA2-compressed)")


    args = parser.parse_args()
    if args.command == "pack":
        pack(args)
    elif args.command == "unpack":
        unpack(args)
    elif args.command == "map":
        bankmap(args)


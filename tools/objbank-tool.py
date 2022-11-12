#!/usr/bin/env python3
import argparse
import io
import json
import os
import sys

import _prefer_local_implementation
import libgarib.objects
import libgarib.display_lists
from libgarib.parsers.glover_objbank import GloverObjbank

from libgarib.fla2 import compress, data_from_stream

import pygltflib as gltf

def bankmap(args):
    # TODO! The "padding" at the end of each file seems
    #   to almost always be (72b * total_meshses), or very
    #   very slightly less than that. Investigate more what
    #   this is for, why it's sometimes a little smaller
    #   than that equation predicts, and if it needs to be
    #   present when packing
    for bank_filename in args.bank_file:
        with open(bank_filename, "rb") as f:
            bank_data = data_from_stream(f)
        segments = libgarib.objects.scrapeBankSegments(bank_data)
        segments = libgarib.objects.fillGaps(segments, bank_data)

        print("{:}:".format(bank_filename))
        for segment in segments:
            seg_size = segment.memory_range[1] - segment.memory_range[0]
            if seg_size == 1:
                mem_str = "0x{:08X}\t".format(segment.memory_range[0])
            elif seg_size == 0:
                if not args.zla:
                    continue
                mem_str = "0x{:08X} (!!ZERO LENGTH ARRAY!!)".format(segment.memory_range[0])

            else:
                mem_str = "0x{:08X}-0x{:08X}".format(
                    segment.memory_range[0],
                    segment.memory_range[1],
                )

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

            # animation_properties, animations = libgarib.objects.actorAnimationToJson(obj)
            # actor = {
            #     "id": obj.obj_id,
            #     "animation_properties": animation_properties,
            #     "animations": animations
            # }

            # for defn in obj.animation.animation_definitions or []:
            #     actor["animations"].append({
            #         "start": defn.start_time,
            #         "end": defn.end_time,
            #         "speed": defn.playback_speed,
            #         "flags": defn.u1, # TODO: what does this do??
            #     })

            # obj_output_dir = os.path.join(bank_output_dir, "0x{:08x} ({:})".format(obj.obj_id, obj.mesh.name.strip("\x00")))
            # os.makedirs(obj_output_dir, exist_ok=True)
            # def mesh_dump_callback(mesh, parents, cur_matrix):
            #     name_str = mesh.name.strip("\x00")
            #     actor_node = {
            #         "id": mesh.id,
            #         "children": []
            #     }
            #     if len(parents) > 0:
            #         name_str = libgarib.objects.parent_str(parents) + "." + name_str
            #     dl = libgarib.display_lists.dump_f3dex_dl(mesh, bank_data)
            #     if len(dl) > 0:
            #         dl_filename = os.path.join(obj_output_dir, name_str + ".f3dex.lgdl")
            #         actor_node["dl"] = os.path.relpath(dl_filename, bank_output_dir)
            #         with open(dl_filename, "wb") as f:
            #             f.write(dl)
            #     # if mesh.geometry.num_faces > 0:
            #     #     ply_filename = os.path.join(obj_output_dir, name_str + ".ply")
            #     #     actor_node["model"] = os.path.relpath(ply_filename, bank_output_dir)
            #     #     with open(ply_filename, "wb") as f:
            #     #         f.write(libgarib.objects.mesh_to_ply(mesh))


            #     if mesh.num_sprites > 0:
            #         actor_node["sprites"] = []
            #         for sprite in mesh.sprites:
            #             actor_node["sprites"].append({
            #                 "texture_id": sprite.texture_id,
            #                 "position": [sprite.x, sprite.y, sprite.z],
            #                 "size": [sprite.width, sprite.height],
            #                 "unknown1": sprite.u5, # TODO: ???
            #                 "unknown2": sprite.u6, # TODO: ???
            #                 "flags": sprite.flags
            #             })
            #     mesh.dump_actor_node = actor_node
            #     if len(parents) > 0:
            #         parents[-1].dump_actor_node["children"].append(actor_node)


            # libgarib.objects.for_each_mesh(obj.mesh, mesh_dump_callback)
            # actor["mesh"] = obj.mesh.dump_actor_node
            # with open(os.path.join(bank_output_dir, "0x{:08x}.actor.json".format(obj.obj_id)), "w") as f:
            #     json.dump(actor, f, indent=2, sort_keys=True)

            with open(os.path.join(bank_output_dir, "0x{:08x}-{:}.glb".format(obj.obj_id, obj.mesh.name.strip("\0"))), "wb") as f:
                f.write(libgarib.objects.actor_to_gltf(obj))


def pack(args):

    root = libgarib.objects.LinkableObjectBank()

    for actor_filename in args.actor_file:
        with open(actor_filename, "r") as f:
            actor = json.load(f)
            libgarib.objects.packActor(actor, root)
    root.finalize()
    bank = root.link()

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
    sys.stdout.write("Packed {:} objects into bank '{:}'\n".format(len(root.directory.actors), args.output_file))

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
    map_parser.add_argument("--zla", action="store_true",
                        help="Print pointers to zero-length arrays")


    args = parser.parse_args()
    if args.command == "pack":
        pack(args)
    elif args.command == "unpack":
        unpack(args)
    elif args.command == "map":
        bankmap(args)


#!/usr/bin/env python3
import argparse
import cmd
import io
import json
import os
import sys

import _prefer_local_implementation
import libgarib.objects
import libgarib.display_lists
import libgarib.textures
from libgarib.parsers.glover_objbank import GloverObjbank

from libgarib.fla2 import compress, data_from_stream

import jmespath

import PIL.Image

import pygltflib as gltf

def build_texture_db(textures):
    db = libgarib.textures.TextureDB()
    if textures is not None:
        for filename in textures:
            with open(filename, "rb") as f:
                header = f.read(4)
                f.seek(0)
                if header == b"\x89PNG":
                    im = PIL.Image.open(f)
                    db.addIm(im, filename)
                else:
                    raw_data = data_from_stream(f)
                    db.addBank(raw_data)
    return db

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
    texture_db = build_texture_db(args.textures)

    for bank_filename in args.bank_file:
        os.makedirs(args.output_dir, exist_ok=True)
        with open(bank_filename, "rb") as f:
            bank_data = data_from_stream(f)
        bank = GloverObjbank.from_bytes(bank_data)

        for entry in bank.directory:
            obj = entry.obj_root
            if obj is None:
                continue

            with open(os.path.join(args.output_dir, "0x{:08x}-{:}.glb".format(obj.obj_id, obj.mesh.name.strip("\0"))), "wb") as f:
                f.write(libgarib.objects.actor_to_gltf(obj, texture_db))


def pack(args):
    texture_db = build_texture_db(args.textures)

    root = libgarib.objects.LinkableObjectBank()

    for actor_filename in args.actor_file:
        with open(actor_filename, "r") as f:
            file = gltf.GLTF2.load(actor_filename)
            libgarib.objects.packActor(file, root, texture_db)
 
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

def query(args):
    json_banks = {}
    for bank_filename in args.bank_file:
            with open(bank_filename, "rb") as f:
                bank_data = data_from_stream(f)

            bank = GloverObjbank.from_bytes(bank_data)
            json_banks[bank_filename] = libgarib.objects.objBankToJson(bank)

    def run_query(query_txt):
        results = {}
        for bank_filename, bank_data in json_banks.items():
            results[bank_filename] = jmespath.search(query_txt, bank_data)

        if args.output_format == "json":
            print(json.dumps(results))
        elif args.output_format == "pretty":
            print(json.dumps(results, indent=4))
        print("\n\n")

    if args.query is not None and len(args.query) > 0:
        for query_txt in args.query:
            run_query(query_txt)
    else:
        class JMESPathShell(cmd.Cmd):
            prompt="> "
            def default(self, line):
                try:
                    run_query(line)
                except Exception as e:
                    print(e)
        JMESPathShell().cmdloop()

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Tool to work with object bank archives from Glover (N64)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    pack_parser = subparsers.add_parser('pack', help='Build object banks from raw model assets')
    pack_parser.add_argument("actor_file", type=str, nargs="+",
                        help="glTF2 file to pack")
    pack_parser.add_argument("--output-file", type=str, required=True,
                        help="File to write bank into")
    pack_parser.add_argument("--compress", action="store_true",
                        help="FLA2-compress the output")
    pack_parser.add_argument("-t", "--textures", action="append", type=str,
                        help="Textures used by object bank (*.png images or *.bin/*.bin.fla texture banks)")

    unpack_parser = subparsers.add_parser('unpack', help='Extract raw model assets from object banks')
    unpack_parser.add_argument("bank_file", type=str, nargs="+",
                        help="Object bank file (potentially FLA2-compressed)")
    unpack_parser.add_argument("--output-dir", type=str, default=os.getcwd(),
                        help="Directory to output bank contents")
    unpack_parser.add_argument("-t", "--textures", action="append", type=str,
                        help="Textures used by object bank (*.png images or *.bin/*.bin.fla texture banks)")

    map_parser = subparsers.add_parser('map', help='Dump memory map of object banks')
    map_parser.add_argument("bank_file", type=str, nargs="+",
                        help="Object bank file (potentially FLA2-compressed)")
    map_parser.add_argument("--zla", action="store_true",
                        help="Print pointers to zero-length arrays")

    query_parser = subparsers.add_parser('query', help='Extract individual pieces of data from object data en masse')
    query_parser.add_argument("--query", action="append",
                        help="JMESPath query")
    query_parser.add_argument("bank_file", type=str, nargs="+",
                        help="Object bank file (potentially FLA2-compressed)")
    query_parser.add_argument("--output-format", choices=["json", "pretty"], default="pretty",
                        help="Choose output data format")

    args = parser.parse_args()
    if args.command == "pack":
        pack(args)
    elif args.command == "unpack":
        unpack(args)
    elif args.command == "map":
        bankmap(args)
    elif args.command == "query":
        query(args)


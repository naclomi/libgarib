#!/usr/bin/env python3
import argparse
import cmd
import io
import json
import os
import re
import subprocess
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

DEFAULT_SCALE_FACTOR = 10

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
                    db.addBank(raw_data, bank_filename=filename)
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
                segment.dtype.value,
                segment.name))
 

def split(args):
    for bank_filename in args.bank_file:
        os.makedirs(args.output_dir, exist_ok=True)
        with open(bank_filename, "rb") as f:
            bank_data = data_from_stream(f)
        bank = GloverObjbank.from_bytes(bank_data)
        linkable_bank = libgarib.objects.kaitaiBankToLinkable(bank)
        for entry in bank.directory:
            if entry.obj_root is None:
                continue
            single_bank = linkable_bank.extract(entry.obj_id)
            single_bank.finalize()
            with open(os.path.join(args.output_dir, "0x{:08x}-{:}.obj.bin".format(entry.obj_root.obj_id, entry.obj_root.mesh.name.strip("\0"))), "wb") as f:
                f.write(single_bank.link())

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
                f.write(libgarib.objects.actor_to_gltf(obj, texture_db, args.scale))


def pack(args):
    texture_db = build_texture_db(args.textures)

    root = libgarib.objects.LinkableObjectBank()

    for filename in args.actor_or_bank_file:
        with open(filename, "rb") as f:
            header = f.read(4)
            f.seek(0)
            if header == b"glTF" or header[0] == ord("{"):
                file = gltf.GLTF2.load(filename)
                libgarib.objects.packActor(file, root, texture_db, args.scale)
            else:
                bank_data = data_from_stream(f)
                bank = GloverObjbank.from_bytes(bank_data)
                linkable_bank = libgarib.objects.kaitaiBankToLinkable(bank)
                root.merge(linkable_bank)

    root.finalize()
    bank = root.link()

    if args.compress:
        def compression_progress_callback(percent):
            sys.stdout.write("\rCompressing ({:}%)".format(percent))
        with open(args.output_file, "wb") as f:
            bank_stream = io.BytesIO(bank)
            compression_progress_callback(0)
            compress(bank_stream, f, progress_callback=compression_progress_callback)
            compression_progress_callback(100)
            sys.stdout.write("\n")
    else:
        with open(args.output_file, "wb") as f:
            f.write(bank)
    sys.stdout.write("Packed {:} objects into bank '{:}'\n".format(len(root.directory.actors), args.output_file))

def dlist_rip(args):
    texture_db = build_texture_db(args.textures)
    def texture_summary(tex_id):
        texture = texture_db.byId[tex_id]
        origin = os.path.basename(texture_db.origin[tex_id])
        return """//***************************
//* TEXTURE REFERENCE:
//* id: 0x{tex_id:08X}
//* size: {texture.width}x{texture.height}
//* mask: {texture.masks}x{texture.maskt}
//* format: {texture.color_format.name} / {texture.compression_format.name}
//* flags: 0x{texture.flags:X}
//* palette: +0x{texture.palette_offset:X}
//* origin: {origin}
//***************************""".format(**locals())

    for bank_filename in args.bank_file:
        os.makedirs(args.output_dir, exist_ok=True)
        with open(bank_filename, "rb") as f:
            bank_data = data_from_stream(f)
        segments = libgarib.objects.scrapeBankSegments(bank_data)
        for seg in segments:
            if seg.dtype is libgarib.objects.BankmapDtype.DISPLAY_LIST:
                dl_name = seg.name
                dl_raw = bank_data[seg.memory_range[0]:seg.memory_range[1]]

                bin_filename = os.path.join(args.output_dir, "{:}.dlist.bin".format(dl_name))
                with open(bin_filename, "wb") as f:
                    f.write(dl_raw)
                if args.gfxdis is not None:
                    disasm_run = subprocess.run([args.gfxdis, "-r", "-i", "-f", bin_filename], capture_output=True)
                    if disasm_run.returncode != 0:
                        print("{:} returned code {:}:".format(args.gfxdis, disasm_run.returncode))
                        print(disasm_run.stderr.decode())
                    else:
                        c_filename = os.path.join(args.output_dir, "{:}.dlist.c".format(dl_name))
                        c_output = disasm_run.stdout.decode()
                        if len(texture_db.byId) > 0:
                            addr_pattern = re.compile("0x[A-Fa-f0-9]{8}")
                            new_c_output = []
                            last_tex_ref_id = None
                            for c_line in c_output.split("\n"):
                                for addr_match in addr_pattern.finditer(c_line):
                                    addr = int(addr_match.group(0), 0)
                                    if addr in texture_db.byId and last_tex_ref_id != addr:
                                        last_tex_ref_id = addr
                                        new_c_output.append(texture_summary(addr))
                                new_c_output.append(c_line)
                            c_output = "\n".join(new_c_output)
                        with open(c_filename, "w") as f:
                            f.write(c_output)

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
    pack_parser.add_argument("actor_or_bank_file", type=str, nargs="+",
                        help="glTF2 file or object bank to pack")
    pack_parser.add_argument("--output-file", type=str, required=True,
                        help="File to write bank into")
    pack_parser.add_argument("--compress", action="store_true",
                        help="FLA2-compress the output")
    pack_parser.add_argument("-t", "--textures", action="append", type=str,
                        help="Textures used by object bank (*.png images or *.bin/*.bin.fla texture banks)")
    pack_parser.add_argument("--scale", type=float,
                        help="Scale factor for vertex coordinates (by default taken from glTF metadata, this argument will override)")

    unpack_parser = subparsers.add_parser('unpack', help='Extract raw model assets from object banks')
    unpack_parser.add_argument("bank_file", type=str, nargs="+",
                        help="Object bank file (potentially FLA2-compressed)")
    unpack_parser.add_argument("--output-dir", type=str, default=os.getcwd(),
                        help="Directory to output bank contents")
    unpack_parser.add_argument("-t", "--textures", action="append", type=str,
                        help="Textures used by object bank (*.png images or *.bin/*.bin.fla texture banks)")
    unpack_parser.add_argument("--scale", type=float, default=DEFAULT_SCALE_FACTOR,
                        help="Scale factor for vertex coordinates (default: {:})".format(DEFAULT_SCALE_FACTOR))

    split_parser = subparsers.add_parser('split', help='Split one object bank into individual objects')
    split_parser.add_argument("bank_file", type=str, nargs="+",
                        help="Object bank file (potentially FLA2-compressed)")
    split_parser.add_argument("--output-dir", type=str, default=os.getcwd(),
                        help="Directory to output bank contents")

    map_parser = subparsers.add_parser('map', help='Dump memory map of object banks')
    map_parser.add_argument("bank_file", type=str, nargs="+",
                        help="Object bank file (potentially FLA2-compressed)")
    map_parser.add_argument("--zla", action="store_true",
                        help="Print pointers to zero-length arrays")

    unpack_parser = subparsers.add_parser('dlist-rip', help='Rip display lists from an object bank')
    unpack_parser.add_argument("bank_file", type=str, nargs="+",
                        help="Object bank file (potentially FLA2-compressed)")
    unpack_parser.add_argument("--output-dir", type=str, default=os.getcwd(),
                        help="Directory to output bank contents")
    unpack_parser.add_argument("--gfxdis", type=str, required=False,
                        help="Path to display list disassembler (to convert binary dumps to C macros)")
    unpack_parser.add_argument("-t", "--textures", action="append", type=str,
                        help="Textures used by object bank (*.png images or *.bin/*.bin.fla texture banks)")

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
    elif args.command == "split":
        split(args)
    elif args.command == "map":
        bankmap(args)
    elif args.command == "dlist-rip":
        dlist_rip(args)
    elif args.command == "query":
        query(args)


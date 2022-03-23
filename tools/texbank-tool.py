#!/usr/bin/env python3
import _prefer_local_implementation
import argparse
import os
import libgarib.textures
from libgarib.parsers.glover_texbank import GloverTexbank

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Tool to work with texture bank archives from Glover (N64)")
    subparsers = parser.add_subparsers(dest="command", required=True)
    pack_parser = subparsers.add_parser('pack', help='Build texture banks from raw image assets')

    unpack_parser = subparsers.add_parser('unpack', help='Extract raw image assets from texture banks')    
    unpack_parser.add_argument("bank_file", type=str, nargs="+",
                        help="Texture bank file (input)")
    unpack_parser.add_argument("--output-dir", type=str, default=os.getcwd(),
                        help="Directory to output bank contents")

    args = parser.parse_args()
    if args.command == "pack":
        pass
    elif args.command == "unpack":
        for bank_filename in args.bank_file:
            bank_output_dir = os.path.join(args.output_dir, os.path.splitext(os.path.basename(bank_filename))[0] + ".unpacked")
            os.makedirs(bank_output_dir, exist_ok=True)
            bank = GloverTexbank.from_file(bank_filename)
            for texture in bank.asset:
                im = libgarib.textures.texToPillow(texture)
                out_file = os.path.join(bank_output_dir, "0x{:08X}.png".format(texture.id))
                im.save(out_file, "PNG")
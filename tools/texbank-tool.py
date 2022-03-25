#!/usr/bin/env python3
import _prefer_local_implementation

import argparse
import os

import sys

import PIL.Image

import libgarib.textures
from libgarib.parsers.glover_texbank import GloverTexbank
from libgarib.hash import hash_str

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Tool to work with texture bank archives from Glover (N64)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    pack_parser = subparsers.add_parser('pack', help='Build texture banks from raw image assets')
    pack_parser.add_argument("image_file", type=str, nargs="+",
                        help="Texture image to pack")
    pack_parser.add_argument("--output-file", type=str, required=False,
                        help="File to write bank into")

    unpack_parser = subparsers.add_parser('unpack', help='Extract raw image assets from texture banks')    
    unpack_parser.add_argument("bank_file", type=str, nargs="+",
                        help="Texture bank file (input)")
    unpack_parser.add_argument("--output-dir", type=str, default=os.getcwd(),
                        help="Directory to output bank contents")

    args = parser.parse_args()
    if args.command == "pack":
        textures = []
        for filename in args.image_file:
            ext = os.path.splitext(filename)[1]
            if ext == "json":
                continue
            try:
                with PIL.Image.open(filename) as im:
                    basename = os.path.basename(filename)
                    if basename.startswith("0x"):
                        tex_id = int(basename.split(".")[0], 16)
                    else:
                        tex_id = hash_str(basename)
                    textures.append(libgarib.textures.imToTex(im, tex_id))
            except PIL.UnidentifiedImageError:
                sys.stderr.write("WARNING: Couldn't open image {:}, was not included in bank\n".format(filename))
        print(len(textures), "textures")
    elif args.command == "unpack":
        for bank_filename in args.bank_file:
            bank_output_dir = os.path.join(args.output_dir, os.path.splitext(os.path.basename(bank_filename))[0] + ".unpacked")
            os.makedirs(bank_output_dir, exist_ok=True)
            bank = GloverTexbank.from_file(bank_filename)
            for texture in bank.asset:
                try:
                    im = libgarib.textures.texToIm(texture)
                    out_file = os.path.join(bank_output_dir, "0x{:08X}.png".format(texture.id))
                    im.save(out_file, "PNG")
                except libgarib.textures.TextureDecodeException as e:
                    sys.stderr.write("WARNING: " + str(e) + "\n")
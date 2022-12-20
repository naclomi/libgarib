#!/usr/bin/env python3
import argparse
import io
import json
import os
import sys

import construct
import PIL.Image
from PIL.PngImagePlugin import PngInfo

import _prefer_local_implementation
import libgarib.textures
from libgarib.parsers.glover_texbank import GloverTexbank
from libgarib.parsers.construct import glover_texbank as texbank_writer

from libgarib.hash import hash_str
from libgarib.fla2 import compress, data_from_stream

def pack(args):
    textures = []
    filenames = []
    for filename in args.image_file:
        ext = os.path.splitext(filename)[1]
        if ext == "json":
            continue
        try:
            with PIL.Image.open(filename) as im:
                texID = libgarib.textures.filenameToTexID(filename)
                textures.append(libgarib.textures.imToTex(im, texID))
            metadata_filename = os.path.basename(filename)
            if not metadata_filename.startswith("0x"):
                filenames.append("{:}".format(metadata_filename))
            else:
                filenames.append("")
        except (json.JSONDecodeError, construct.core.MappingError, libgarib.textures.TextureEncodeException) as e:
            sys.stderr.write("WARNING: Malformed image metadata for texture '{:}': {:}. Texture was not included in bank\n".format(filename, str(e)))
        except PIL.UnidentifiedImageError:
            sys.stderr.write("WARNING: Couldn't open image {:}. Texture was not included in bank\n".format(filename))

    if args.strip_filenames:
        # If we're not writing the filenames metadata,
        # remove it from the Construct texbank structure
        texbank_writer.glover_texbank.subcons.pop()

    bank = texbank_writer.glover_texbank.build({
        "n_textures": len(textures),
        "assets": list(map(lambda t: texbank_writer.glover_texbank__texture.parse(t), textures)),
        "filenames": None if args.strip_filenames else filenames
    })
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
    sys.stdout.write("Packed {:} textures into bank '{:}'\n".format(len(textures), args.output_file))

def unpack(args):
    for bank_filename in args.bank_file:
        os.makedirs(args.output_dir, exist_ok=True)
        with open(bank_filename, "rb") as f:
            bank_data = data_from_stream(f)
        bank = GloverTexbank.from_bytes(bank_data)
        for idx, texture in enumerate(bank.assets):
            try:
                if idx < len(bank.filenames) and len(bank.filenames[idx]) > 0:
                    # Use sanitized filename from metadata
                    filename = os.path.basename(bank.filenames[idx])
                else:
                    filename = "0x{:08X}.png".format(texture.id)
                im = libgarib.textures.texToIm(texture)
                out_file = os.path.join(args.output_dir, filename)
                metadata = {
                    "flags": texture.flags,
                    "color_format": texture.color_format.name,
                    "compression_format": texture.compression_format.name,
                }
                if texture.palette_anim_idx_min != texture.palette_anim_idx_max:
                    metadata["palette_anim_idx_min"] = texture.palette_anim_idx_min
                    metadata["palette_anim_idx_max"] = texture.palette_anim_idx_max
                    metadata["frame_increment"] = texture.frame_increment
                    metadata["frame_counter"] = texture.frame_counter
                if texture.width != 2 ** texture.masks:
                    metadata["masks"] = texture.masks
                if texture.height != 2 ** texture.maskt:
                    metadata["maskt"] = texture.maskt                        
                binary_metadata = PngInfo()
                binary_metadata.add_text("Comment", json.dumps(metadata, indent=2))
                im.save(out_file, "PNG", pnginfo=binary_metadata)                    
            except libgarib.textures.TextureDecodeException as e:
                sys.stderr.write("WARNING: " + str(e) + "\n")

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Tool to work with texture bank archives from Glover (N64)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    pack_parser = subparsers.add_parser('pack', help='Build texture banks from raw image assets')
    pack_parser.add_argument("image_file", type=str, nargs="+",
                        help="Texture image to pack")
    pack_parser.add_argument("--output-file", type=str, required=True,
                        help="File to write bank into")
    pack_parser.add_argument("--compress", action="store_true",
                        help="FLA2-compress the output")
    pack_parser.add_argument("--strip-filenames", action="store_true",
                        help="Don't store filenames in bank")

    unpack_parser = subparsers.add_parser('unpack', help='Extract raw image assets from texture banks')    
    unpack_parser.add_argument("bank_file", type=str, nargs="+",
                        help="Texture bank file (potentially FLA2-compressed)")
    unpack_parser.add_argument("--output-dir", type=str, default=os.getcwd(),
                        help="Directory to output bank contents")

    args = parser.parse_args()
    if args.command == "pack":
        pack(args)
    elif args.command == "unpack":
        unpack(args)

#!/usr/bin/env python3
import argparse
import sys
import os

def patch(args):
    pass

def dump(args):
    output_dir = os.path.join(args.output_dir, os.path.splitext(os.path.basename(rom_file))[0] + ".unpacked")
    os.makedirs(output_dir, exist_ok=True)
    with open(args.rom_filename, "rb") as f:
        rom_data = f.read()

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Tool to dump/replace/relocate ROM assets within Glover (N64)")
    
    parser.add_argument("rom_file", type=str,
                        help="Glover N64 ROM")
    parser.add_argument("--map", type=str, required=True,
                        help="YAML file outlining ROM memory regions and the pointers to them within the game code")

    subparsers = parser.add_subparsers(dest="command", required=True)

    patch_parser = subparsers.add_parser('patch', help='Build texture banks from raw image assets')

    dump_parser = subparsers.add_parser('dump', help='Extract raw binary assets from game ROM')    
    dump_parser.add_argument("--output-dir", type=str, default=os.getcwd(),
                        help="Directory to output bank contents")


    args = parser.parse_args()
    if args.command == "patch":
        pass
    elif args.command == "dump":
        dump(args)
#!/usr/bin/env python3
import argparse
import sys
import os

import yaml

import _prefer_local_implementation
import libgarib.rom

def patch(rom_data, map_data, args):
    pass

def dump(rom_data, map_data, args):
    rom = libgarib.rom.Rom(rom_data, map_data)
    output_dir = os.path.join(args.output_dir, os.path.splitext(os.path.basename(args.rom_file))[0] + ".unpacked")
    os.makedirs(output_dir, exist_ok=True)

    filenames = []
    for region in rom.data:
        filenames += region.dump_to_file(output_dir)

    filenames = list(map(lambda f: os.path.relpath(f, output_dir), filenames))
    with open(os.path.join(output_dir, "manifest.yaml"), "w") as f:
        # TODO
        yaml.dump(filenames, f, indent=3)


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

    with open(args.rom_file, "rb") as f:
        rom_data = f.read()

    with open(args.map, "r") as f:
        map_data = yaml.safe_load(f.read())

    if args.command == "patch":
        patch(rom_data, map_data, args)
    elif args.command == "dump":
        dump(rom_data, map_data, args)
#!/usr/bin/env python3
import ast
import argparse
import logging
import os
import re
import shutil
import sys

import yaml

import _prefer_local_implementation
import libgarib.rom

def patch(rom_data, map_data, args):    
    rom = libgarib.rom.Rom(rom_data, map_data)
    with open(args.manifest, "r") as f:
        manifest = yaml.safe_load(f.read())
    manifest_dir = os.path.dirname(args.manifest)


    for region_key, region_filename in manifest.items():
        region_key = ast.literal_eval(region_key)
        try:
            region = rom.get_region(region_key)
        except KeyError:
            logging.warning("Region key {:} not found in ROM map, skipping".format(region_key))
            continue
        if type(region_filename) is dict:
            for elem_idx, elem_filename in region_filename.items():
                region.patch(elem_filename, manifest_dir, elem_idx)
        else:
            region.patch(elem_filename, manifest_dir)

    final_rom_data = rom.finalize()
    out_filename = os.path.basename(args.rom_file).split(".")
    out_filename.insert(-1,"patched")
    out_filename = ".".join(out_filename)
    with open(os.path.join(args.output_dir, out_filename), "wb") as f:
        f.write(final_rom_data)

    map_filename = out_filename.split(".")[:-1]
    map_filename.append("memmap.yaml")
    map_filename = ".".join(map_filename)
    with open(os.path.join(args.output_dir, map_filename), "w") as f:
        yaml.dump(map_data, f)


def dump(rom_data, map_data, args):
    rom = libgarib.rom.Rom(rom_data, map_data)
    output_dir = os.path.join(args.output_dir, os.path.splitext(os.path.basename(args.rom_file))[0] + ".unpacked")
    os.makedirs(output_dir, exist_ok=True)

    shutil.copy(args.map, os.path.join(output_dir, os.path.basename(args.map)))

    manifest = {}
    for region in rom.data:
        dumped_files = region.dump_to_file(output_dir)
        dumped_files = list(map(lambda f: os.path.relpath(f, output_dir), dumped_files))
        if len(dumped_files) == 1:
            dumped_files = dumped_files[0]
        else:
            dumped_files = {idx:val for idx,val in enumerate(dumped_files)}
        manifest[str(region.key())] = dumped_files

    with open(os.path.join(output_dir, "manifest.yaml"), "w") as f:
        yaml.dump(manifest, f, indent=3)


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Tool to dump/replace/relocate ROM assets within Glover (N64)")
    
    parser.add_argument("rom_file", type=str,
                        help="Glover N64 ROM")
    parser.add_argument("--map", type=str, required=True,
                        help="YAML file outlining ROM memory regions and the pointers to them within the game code")
    parser.add_argument("--output-dir", type=str, default=os.getcwd(),
                        help="Directory to output bank contents")

    parser.add_argument('-v', '--verbose', action="store_const", dest="loglevel",
                        const=logging.DEBUG, default=logging.WARNING,
                        help="Be verbose")

    subparsers = parser.add_subparsers(dest="command", required=True)

    patch_parser = subparsers.add_parser('patch', help='Patch new assets into game ROM')
    patch_parser.add_argument("--manifest", type=str, required=True,
                        help="YAML file outlining binary assets to patch into game ROM")


    dump_parser = subparsers.add_parser('dump', help='Extract raw binary assets from game ROM')    

    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)

    with open(args.rom_file, "rb") as f:
        rom_data = f.read()

    with open(args.map, "r") as f:
        map_data = yaml.safe_load(f.read())

    if args.command == "patch":
        patch(rom_data, map_data, args)
    elif args.command == "dump":
        dump(rom_data, map_data, args)
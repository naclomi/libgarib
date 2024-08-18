#!/usr/bin/env python3
import ast
import argparse
import logging
import os
import re
import shutil
import string
import struct
import sys
import textwrap

import yaml

import _prefer_local_implementation
import libgarib.rom
import libgarib.maps


class QolPatch(object):
    def __init__(self, name, desc, src):
        self.name = name
        self.desc = desc
        self.src = textwrap.dedent(src)
        self.args = []
        for seg in string.Formatter().parse(self.src):
            arg = seg[1]
            if arg is None:
                continue
            self.args.append(arg)

    def format(self, *args, **kwargs):
        return self.src.format(*args, **kwargs)

    def signature(self):
        if len(self.args) > 0:
            return "{:}({:})".format(self.name, ", ".join(self.args))
        else:
            return self.name

    @staticmethod
    def to_dict(*patches):
        d = {}
        for qol_patch in patches:
            d[qol_patch.name] = qol_patch
        return d

qol_patches = QolPatch.to_dict(
    QolPatch("copyskip", "Skip copyright screen",
    """
        .text 0x8010e86c
        j 0x8010eb0c
        addi $v0, $zero, 1        
    """),
    QolPatch("quickboot", "Make opening logo scene playable and force to specified level",
    """
        # Force presentation segment to be playable:
        .text 0x8012bcfc
        addi $v0, $zero, 0

        # Force presentation loader to boot specific level:
        .text 0x8012bd0c
        addi $a0, $zero, {level_id} # Immediate is level ID to start on
    """),
)

def patch(rom_data, map_data, args):    
    rom = libgarib.rom.Rom(rom_data, map_data)
    with open(args.manifest, "r") as f:
        manifest = yaml.safe_load(f.read())
    manifest_dir = os.path.dirname(args.manifest)

    if args.qol is not None:
        try:
            combined_txt = []
            for qol_patch in args.qol:
                match = re.match("([A-Za-z0-9_-]+)(\(([^)]*)\))?", qol_patch)
                patch_name = match.group(1).strip()
                patch_args = match.group(3)
                arg_dict = {}
                if patch_args is not None:
                    for patch_arg in patch_args.split(","):
                        arg_name, arg_val = patch_arg.split("=")
                        arg_name = arg_name.strip()
                        arg_val = arg_val.strip()
                        arg_dict[arg_name] = arg_val
                combined_txt.append(qol_patches[patch_name].format(
                    **arg_dict
                ))

            combined_txt = "\n".join(combined_txt)
            code_region = rom.get_region(('opaque', 'code'))
            code_region.patch({"asm": combined_txt}, manifest_dir)
        except IndexError:
            raise Exception("Bad QoL patch spec '{:}'".format(qol_patch))

    for region_key, region_filename in manifest.items():
        region_key = ast.literal_eval(region_key)
        if len(region_key) == 3:
            elem_idx = region_key[2]
            region_key = region_key[0:2]
        else:
            elem_idx = None
        try:
            region = rom.get_region(region_key)
        except KeyError:
            logging.warning("Region key {:} not found in ROM map, skipping".format(region_key))
            continue
        if elem_idx is not None:
            region.patch(region_filename, manifest_dir, elem_idx)
        else:
            region.patch(region_filename, manifest_dir)

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

def findBuiltinRomMap(rom_file):
    with open(rom_file, "rb") as f:
        cksum = tuple(struct.unpack(">I", w)[0] for w in libgarib.rom.calculateChecksum(f, bigEndian=True))
        map_filename = "map.0x{:08x}.0x{:08x}.yaml".format(*cksum)
        maps_dir = os.path.dirname(libgarib.maps.__file__)
        return os.path.join(maps_dir, map_filename)


def patch_list_help(patches):
    text = []
    for qol_patch in patches.values():
        text.append("  {:}\n    {:}".format(qol_patch.signature(), qol_patch.desc))
    return "\n".join(text)

if __name__=="__main__":
    parser = argparse.ArgumentParser(
        description="Tool to dump/replace/relocate ROM assets within Glover (N64)")
    
    parser.add_argument("--map", type=str, required=False,
                        help="YAML file describing structure of input ROM")
    parser.add_argument('-v', '--verbose', action="store_const", dest="loglevel",
                        const=logging.DEBUG, default=logging.WARNING,
                        help="Be verbose")

    subparsers = parser.add_subparsers(dest="command", required=True)

    patch_parser = subparsers.add_parser('patch',
        description='Patch new assets into game ROM',
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="Available QoL patches:\n{:}".format(patch_list_help(qol_patches)))
    patch_parser.add_argument("rom_file", type=str,
                        help="Glover N64 ROM")
    patch_parser.add_argument("--manifest", type=str, required=True,
                        help="YAML file outlining binary assets to patch into game ROM")
    patch_parser.add_argument("--qol", type=str, action="append",
                        help="Include the specified quality-of-life patch")


    dump_parser = subparsers.add_parser('dump',
        description='Extract raw binary assets from game ROM')    
    dump_parser.add_argument("rom_file", type=str,
                        help="Glover N64 ROM")
    parser.add_argument("--output-dir", type=str, default=os.getcwd(),
                        help="Directory to output bank contents")

    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)

    if args.map is None:
        args.map = findBuiltinRomMap(args.rom_file)

    with open(args.rom_file, "rb") as f:
        rom_data = f.read()

    with open(args.map, "r") as f:
        map_data = yaml.safe_load(f.read())

    if args.command == "patch":
        patch(rom_data, map_data, args)
    elif args.command == "dump":
        dump(rom_data, map_data, args)
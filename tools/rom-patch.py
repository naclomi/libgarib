#!/usr/bin/env python3
import argparse
import sys
import os

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Tool to re-pack a Glover ROM with new assets")
    parser.add_argument("patch_file", type=str)
    parser.add_argument("rom_file", type=str)
    parser.add_argument("patch_offset", type=str)
    args = parser.parse_args()

    with open(args.patch_file, "rb") as patch:
        patch_data = patch.read()
    with open(args.rom_file, "r+b") as rom:
        print(rom.tell())
        rom.seek(int(args.patch_offset,0), os.SEEK_SET)
        print(rom.tell())
        print(len(patch_data))
        rom.write(patch_data)
    sys.exit(0)
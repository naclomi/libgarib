#!/usr/bin/env python3
import argparse
import struct
import sys

import _prefer_local_implementation
import libgarib.rom as rom

def formatted_crc(crcs):
    return list(map(lambda c: c.hex(), crcs))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("rom_file", type=str,
                        help="N64 ROM")
    parser.add_argument("--endianness", type=str,
                        choices=["le", "be"], default="be",
                        help="ROM file endianness (default: be)")
    parser.add_argument("--patch", action="store_true",
                        help="Write calculated CRC into the ROM file")
    parser.add_argument("--quiet", action="store_true",
                        help="Don't print ROM values")

    args = parser.parse_args()

    bigEndian = args.endianness == "be"
    # TODO: support byte-swapped. can detect via first rom word

    with open(args.rom_file, "rb") as f:

        calculated = rom.calculateChecksum(f, bigEndian)

        if not args.quiet:
            f.seek(rom.N64_HEADER_CRC_OFFSET)
            observed = (f.read(4), f.read(4))
            print("CIC:\t" + str(rom.identifyCIC(f)))
            print("Observed:\t" + str(formatted_crc(observed)))
            print("Calculated:\t" + str(formatted_crc(calculated)))

    if args.patch:
        with open(args.rom_file, "r+b") as f:
            f.seek(rom.N64_HEADER_CRC_OFFSET)
            f.write(calculated[0])
            f.write(calculated[1])

    sys.exit(0)

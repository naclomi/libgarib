#!/usr/bin/env python3
import argparse
import struct
import sys

import zlib

N64_HEADER_SIZE = 0x40
N64_HEADER_CRC_OFFSET = 0x10


def identifyCIC(f):
    f.seek(N64_HEADER_SIZE)
    data = f.read(0x1000-N64_HEADER_SIZE)
    crc = zlib.crc32(data)
    return {
        0x6170A4A1: 6101,
        0x90BB6CB5: 6102,
        0x0B050EE0: 6103,
        0x98BC2C86: 6105,
        0xACC8580A: 6106
    }[crc]


def calculateChecksum(f, bigEndian=True):
    # Adapted from http://n64dev.org/n64crc.html

    word_struct = ">I" if bigEndian else "<I"

    # TODO: test on non-6102 roms

    bootcode = identifyCIC(f)
    seed = {
        6101: 0xF8CA4DDC,
        6102: 0xF8CA4DDC,
        6103: 0xA3886759,
        6105: 0xDF26F436,
        6106: 0x1FEA617A
    }[bootcode]

    f.seek(0x1000)
    data = f.read(0x100000)

    if bootcode == 6105:
        f.seek(N64_HEADER_SIZE + 0x0710)
        lut = f.read(260)

    t1 = t2 = t3 = t4 = t5 = t6 = seed

    offset = 0
    while offset < len(data):
        data_word = struct.unpack(word_struct, data[offset:offset+4])[0]
        if t6 + data_word > 0xFFFFFFFF:
            t4 += 1
            t4 &= 0xFFFFFFFF
        t6 += data_word
        t6 &= 0xFFFFFFFF
        t3 ^= data_word

        delta = data_word & 0x1F
        r = (data_word << delta) | (data_word >> (32-delta))
        r &= 0xFFFFFFFF
        t5 += r
        t5 &= 0xFFFFFFFF
        if t2 > data_word:
            t2 ^= r
        else:
            t2 ^= t6 ^ data_word

        if bootcode == 6105:
            lut_offset = offset & 0xFF
            t1 += struct.unpack(word_struct, lut[lut_offset:lut_offset+4])[0] ^ data_word
        else:
            t1 += t5 ^ data_word
        t1 &= 0xFFFFFFFF

        offset += 4

    if bootcode == 6103:
        crc = ((t6 ^ t4) + t3, (t5 ^ t2) + t1)
    elif bootcode == 6106:
        crc = ((t6 * t4) + t3, (t5 * t2) + t1)
    else:
        crc = (t6 ^ t4 ^ t3, t5 ^ t2 ^ t1)

    return (
        struct.pack(word_struct, crc[0] & 0xFFFFFFFF),
        struct.pack(word_struct, crc[1] & 0xFFFFFFFF)
    )


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

        calculated = calculateChecksum(f, bigEndian)

        if not args.quiet:
            f.seek(N64_HEADER_CRC_OFFSET)
            observed = (f.read(4), f.read(4))
            print("CIC:\t" + str(identifyCIC(f)))
            print("Observed:\t" + str(formatted_crc(observed)))
            print("Calculated:\t" + str(formatted_crc(calculated)))

    if args.patch:
        with open(args.rom_file, "r+b") as f:
            f.seek(N64_HEADER_CRC_OFFSET)
            f.write(calculated[0])
            f.write(calculated[1])

    sys.exit(0)

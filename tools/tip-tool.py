#!/usr/bin/env python3
import argparse
import struct
import sys

import yaml

import checksum

def toROM(addr):
    return (addr & 0xFFFFF) + 0x1000

def toRAM(addr):
    return (addr - 0x1000) | 0x80100000

def getString(data, addr):
    start = addr
    while data[addr] != 0:
        addr += 1
    return data[start:addr].decode("unicode_escape")

def structReader(data, start_offset):
    cursor = args.message_table
    def read(fmt):
        nonlocal cursor
        fmt = ">" + fmt
        size = struct.calcsize(fmt)
        data = struct.unpack(">I", rom_data[cursor:cursor+size])
        if len(data) == 1:
            data = data[0]
        cursor += size
        return data
    return read


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["rip", "patch"])
    parser.add_argument("--message-table", type=lambda x: int(x,0), default=0xec538)
    parser.add_argument("--string-table", type=lambda x: int(x,0), default=0x4210)
    parser.add_argument("--rom", type=str)
    parser.add_argument("--script", type=str, required=False)
    parser.add_argument("--message-count", type=int, default=33)
    args = parser.parse_args()

    if args.action == "rip":
        with open(args.rom, "rb") as rom:
            rom_data = rom.read()

        read = structReader(rom_data, args.message_table)

        script = [[[]]]
        msg = script[-1]
        page = msg[-1]
        while True:
            str_address = read("I")
            if args.message_count > 0 and len(script) > args.message_count:
                break
            if (str_address & 0xFFFF0000) != 0x80100000:
                break
            action = read("I")
            page.append(getString(rom_data, toROM(str_address)))
            if action == 1:
                msg.append([])
                page = msg[-1]
            elif action == 2:
                script.append([[]])
                msg = script[-1]
                page = msg[-1]
        script = script[:-1]
        print(yaml.dump(script))
    elif args.action == "patch":
        if args.script == None:
            script = sys.stdin.read()
        else:
            with open(args.script, "r") as f:
                script = yaml.safe_load(f.read())

        addresses = []
        with open(args.rom, "r+b") as f:
            # TODO:
            #   - give warnings when overflowing original
            #     region sizes

            # Write string table
            f.seek(args.string_table)
            for msg in script:
                addresses.append([])
                addr_msg = addresses[-1]
                for page in msg:
                    addr_msg.append([])
                    addr_page = addr_msg[-1]
                    for line in page:
                        addr_page.append(f.tell())
                        f.write(line.encode("raw_unicode_escape"))
                        f.write(b"\x00")

            # Write message table
            f.seek(args.message_table)
            for msg in addresses:
                for pageIdx, page in enumerate(msg):
                    for strIdx, strAddr in enumerate(page):
                        if strIdx == len(page) - 1:
                            if pageIdx == len(msg) - 1:
                                action = 2
                            else:
                                action = 1
                        else:
                            action = 0
                        f.write(struct.pack(">I",toRAM(strAddr)))
                        f.write(struct.pack(">I",action))
                        pass

            # Rewrite ROM checksum
            f.seek(0)
            csum = checksum.calculateChecksum(f, True)
            f.seek(checksum.N64_HEADER_CRC_OFFSET)
            f.write(csum[0])
            f.write(csum[1])


#!/usr/bin/env python3
#
# Mr. Tip dialog editing tool
# 01/03/2022 // naclomi
#
# Usage notes:
#
# Default ROM offsets expect a big-endian Glover N64 ROM
# with a checksum of 0x9661EFD7.
#
# Rip dialog to YAML with the 'rip' command, patch new
# dialog with the 'patch' command. Patches are read either
# from a yaml script file specified or, if none is specified,
# stdin.
#
# YAML format is a list of list of lists: script is a list
# of messages, message is a list of pages, page is a list
# of lines of text.
#
# Techincal notes:
#
# Tip messages are stored in a table whose records
# correspond to individual lines of text. The record's
# format is as follows:
#
# struct MsgLine {
#   char *text; // RAM address
#   uint32_t action;   
# }
# 
# The text itself is stored as a null-terminated string
# elsewhere in ROM. The record's text pointer is relative
# to the game's RAM layout, not ROM layout, so to work
# with text in the ROM you have to translate:
#   rom_address = (ram_address & 0xFFFFF) + 0x1000;
# and
#   ram_address = (rom_address - 0x1000) | 0x80100000;
#
# The action byte indicates what to do after printing
# a line of text to the screen:
#   0 - next line
#   1 - next page
#   2 - end message
#
# A message's ID is given by how many complete messages
# came before it in this table. Thus, an in-level Mr. Tip
# object that prints the message with ID 9 will search from
# the beginning of this table and start printing lines of
# text immediately following the ninth record with an action
# byte equalling 2 ("end message")
#

import argparse
import struct
import sys

import yaml

import _prefer_local_implementation
import libgarib.rom

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
            csum = rom.calculateChecksum(f, True)
            f.seek(rom.N64_HEADER_CRC_OFFSET)
            f.write(csum[0])
            f.write(csum[1])


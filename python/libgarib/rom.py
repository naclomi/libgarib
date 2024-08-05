import logging
import io
import os
import re
import struct
import sys

import capstone
import unicorn
import unicorn.mips_const
import keystone
import zlib

N64_HEADER_SIZE = 0x40
N64_HEADER_CRC_OFFSET = 0x10

file_extensions = {
    "texbank": ".tex.bin",
    "objbank": ".obj.bin",
    "landscape": ".lev.bin",
    "midi_sequence": ".seq.bin",
    "audio_ptr_table": ".ptr.bin",
    "audio_wave_table": ".wav.bin",
    "sndbank": ".snd.bin"
}

def landscape_name(data):
    cursor = 4
    name = ""
    while data[cursor] != 0:
        name += chr(data[cursor])
        cursor += 1
    return name

name_extractors = {
    "landscape": landscape_name
}

regs = {
    "AT": 1,
    "V0": 2,
    "V1": 3,
    "A0": 4,
    "A1": 5,
    "A2": 6,
    "A3": 7,
    "T0": 8,
    "T1": 9,
    "T2": 10,
    "T3": 11,
    "T4": 12,
    "T5": 13,
    "T6": 14,
    "T7": 15,
    "S0": 16,
    "S1": 17,
    "S2": 18,
    "S3": 19,
    "S4": 20,
    "S5": 21,
    "S6": 22,
    "S7": 23,
    "T8": 24,
    "T9": 25,
    "GP": 28,
    "SP": 29,
    "FP": 30,
    "RA": 31
}

# lol, ew
mips_to_unicorn = {}
for name, mips_num in regs.items():
    mips_to_unicorn[mips_num] = getattr(unicorn.mips_const, "UC_MIPS_REG_" + name.upper())

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


def unique_filename(filename):
    next_number = 1
    file_dir = os.path.dirname(filename)
    file_base = os.path.basename(filename).split(".")
    file_base.insert(1, "{:}")
    file_base = ".".join(file_base)
    while os.path.exists(filename):
        filename = os.path.join(file_dir, file_base.format(next_number))
        next_number += 1
    return filename


class RomParseException(Exception):
    pass

class PtrCode(object):
    def __init__(self):
        self.asm = keystone.Ks(keystone.KS_ARCH_MIPS, keystone.KS_MODE_MIPS32 | keystone.KS_MODE_BIG_ENDIAN)

        self.disasm = capstone.Cs(capstone.CS_ARCH_MIPS, capstone.CS_MODE_MIPS32 | capstone.CS_MODE_BIG_ENDIAN)
        self.disasm.detail = True

        self.emu = unicorn.Uc(unicorn.UC_ARCH_MIPS, unicorn.UC_MODE_MIPS32 | unicorn.UC_MODE_BIG_ENDIAN)
        self.emu.mem_map(0, 2*1024*1024)

    def get_code(self, address, out_reg):
        if type(out_reg) is str:
            out_reg = regs[out_reg.upper()]
        asm_output = self.asm.asm("""
            lui ${out_reg}, 0x{upper:04X}
            ori ${out_reg}, ${out_reg}, 0x{lower:04X}
        """.format(
            out_reg=out_reg,
            upper = (address & 0xFFFF0000) >> 16,
            lower = (address & 0xFFFF)
        ))
        return bytes(asm_output[0])

    def get_output_reg(self, code):
        instrs = list(self.disasm.disasm(code, 0))
        reg_name = instrs[-1].reg_name(instrs[-1].operands[0].value.reg)
        return regs[reg_name.upper()]

    def emulate(self, code, out_reg = None):
        if type(out_reg) is str:
            out_reg = regs[out_reg.upper()]
        self.emu.mem_write(0, code)
        self.emu.emu_start(0, len(code))
        detected_out_reg = self.get_output_reg(code)
        if out_reg is None:
            out_reg = detected_out_reg
        elif out_reg != detected_out_reg:
            raise RomParseException("Inconsistent pointer register (expected {:}, found {:})".format(out_reg, detected_out_reg))
        return self.emu.reg_read(mips_to_unicorn[out_reg])

ptrCode = PtrCode()

def _dump_to_file(descriptor, data_bytes, data_offset, basepath, data_idx=None):
    if descriptor["data_type"] in file_extensions:
        basepath = os.path.join(basepath, descriptor["data_type"])
    os.makedirs(basepath, exist_ok=True)
    if data_idx is not None:
        filename = "{:}.".format(data_idx)
    else:
        filename = ""
    if "name" in descriptor:
        filename += descriptor["name"]
    elif descriptor["data_type"] in name_extractors:
        filename += name_extractors[descriptor["data_type"]](data_bytes)
    else:
        filename = "0x{:08X}".format(data_offset)
    filename += file_extensions.get(descriptor["data_type"], ".bin")
    filename = os.path.join(basepath, filename)
    filename = unique_filename(filename)
    with open(filename, "wb") as f:
        f.write(data_bytes)
    return filename

def _patch_data(data_name, data_buffer, manifest_directive, manifest_dir):
    fn_pattern = re.compile(r"([A-Za-z_][A-Za-z0-9_]*)\(([^)]*)\)")
    if manifest_directive is None:
        data_buffer.clear()
        logging.info("Deleted region {:}".format(data_name))
    elif (match := fn_pattern.match(manifest_directive)) is not None:
        fn, arg = match.groups()
        if fn.lower() == "ips":
            # TODO
            ...
            # patch_filename = os.path.join(manifest_dir, arg)
            # apply_ips_patch(self.data, patch_filename)
            # print("ips")
        else:
            raise Exception("Unknown function in manifest: {:}".format(fn))
    else:
        manifest_directive = os.path.join(manifest_dir, manifest_directive)
        with open(manifest_directive, "rb") as f:
            new_data = f.read()
        data_buffer.clear()
        data_buffer += new_data
        logging.info("Patched {:} into {:}".format(manifest_directive, data_name))

class Region(object):
    def __init__(self, descriptor):
        self.offset = 0
        self.data = bytearray()
        self.descriptor = descriptor

    def key(self):
        if "namespaced_id" in self.descriptor:
            return (self.descriptor.get("data_type"), self.descriptor["namespaced_id"])
        elif "name" in self.descriptor:
            return (self.descriptor.get("data_type"), self.descriptor["name"])
        else:
            raise Exception("Couldn't build key")

    def __repr__(self):
        return str(self.key())

    def pad(self, boundary=8):
        gap = -len(self.data) % boundary
        if gap != 0:
            self.data += b"\0" * gap

    def size(self):
        return len(self.data)


    def dump_to_buffer(self, buffer):
        buffer.write(self.data)

    def dump_to_file(self, basepath):
        return [_dump_to_file(self.descriptor, self.data, self.offset, basepath)]

    def update_pointers(self, buffer):
        pass

    def update_descriptor(self):
        pass

    def parse(self, rom_data):
        pass

    def patch(self, manifest_directive, manifest_dir):
        _patch_data("{:}".format(self.key()), self.data, manifest_directive, manifest_dir)

def scrape_pointers(rom_data, pointer_list):
    val = None
    for pointer in pointer_list:
        code_start = pointer["address"]
        code_end = code_start + 8
        result = ptrCode.emulate(rom_data[code_start:code_end], pointer["reg"])
        if val is not None and result != val:
            raise RomParseException("Inconsistent pointer values")
        val = result
    return val

class BoundedSingleRegion(Region):
    def parse(self, rom_data):
        start_pointer = scrape_pointers(rom_data, self.descriptor["start_pointers"]) & 0x0FFFFFFF
        end_pointer = scrape_pointers(rom_data, self.descriptor["end_pointers"]) & 0x0FFFFFFF
        self.offset = start_pointer
        self.data = bytearray(rom_data[start_pointer:end_pointer])

    def update_pointers(self, buffer):
        addr = self.offset | 0xB0000000
        for pointer in self.descriptor["start_pointers"]:
            buffer.seek(pointer["address"])
            buffer.write(ptrCode.get_code(addr, pointer["reg"]))
        addr += self.size()
        for pointer in self.descriptor["end_pointers"]:
            buffer.seek(pointer["address"])
            buffer.write(ptrCode.get_code(addr, pointer["reg"]))


class UnboundedSingleRegion(Region):
    def parse(self, rom_data):
        start_pointer = scrape_pointers(rom_data, self.descriptor["start_pointers"]) & 0x0FFFFFFF
        end_pointer = start_pointer + self.descriptor["size"]
        self.offset = start_pointer
        self.data = bytearray(rom_data[start_pointer:end_pointer])

    def update_descriptor(self):
        self.descriptor["size"] = len(self.data)

    def update_pointers(self, buffer):
        addr = self.offset | 0xB0000000
        for pointer in self.descriptor["start_pointers"]:
            buffer.seek(pointer["address"])
            buffer.write(ptrCode.get_code(addr, pointer["reg"]))
        

class BoundedArrayRegion(Region):
    def parse(self, rom_data):
        start_pointer = scrape_pointers(rom_data, self.descriptor["start_pointers"]) & 0x0FFFFFFF
        end_pointer = scrape_pointers(rom_data, self.descriptor["end_pointers"]) & 0x0FFFFFFF

        self.offset = start_pointer
        self.data = []
        self.pad_data = b""
        cursor = start_pointer
        while cursor < end_pointer:
            elem_len = struct.unpack(">I", rom_data[cursor:cursor+4])[0]
            self.data.append(bytearray(rom_data[cursor:cursor+elem_len]))
            cursor += elem_len

    def pad(self, boundary=8):
        gap = -self.size() % boundary
        if gap != 0:
            self.pad_data += b"\0" * gap

    def size(self):
        return sum(len(data) for data in self.data) + len(self.pad_data)

    def dump_to_buffer(self, buffer):
        for elem in self.data:
            buffer.write(elem)
        buffer.write(self.pad_data)

    def dump_to_file(self, basepath):
        files = []
        running_offset = self.offset
        for idx, elem_data in enumerate(self.data):
            files.append(_dump_to_file(
                self.descriptor, elem_data, running_offset, basepath, idx))
            running_offset += len(elem_data)
        return files

    def patch(self, manifest_directive, manifest_dir, idx):
        _patch_data("{:}[{:}]".format(self.key(), idx), self.data[idx], manifest_directive, manifest_dir)

    def update_pointers(self, buffer):
        # TODO: update individual elem lengths?
        addr = self.offset | 0xB0000000
        for pointer in self.descriptor["start_pointers"]:
            buffer.seek(pointer["address"])
            buffer.write(ptrCode.get_code(addr, pointer["reg"]))
        addr += self.size()
        for pointer in self.descriptor["end_pointers"]:
            buffer.seek(pointer["address"])
            buffer.write(ptrCode.get_code(addr, pointer["reg"]))


class StaticRegion(Region):
    def parse(self, rom_data):
        self.offset = self.descriptor["start"]
        self.data = bytearray(rom_data[self.descriptor["start"]:self.descriptor["end"]])

    def update_descriptor(self):
        self.descriptor["start"] = self.offset
        self.descriptor["end"] = self.offset + len(self.data)


class Rom(object):
    def __init__(self, rom_data, map_data):
        self.rom_checksum = struct.unpack(">II", rom_data[N64_HEADER_CRC_OFFSET: N64_HEADER_CRC_OFFSET+8])
        self.map_data = map_data
        self.regions = map_data["regions"]

        if self.rom_checksum != tuple(map_data["rom_checksum"]):
            logging.warning("Rom and memory map checksums do not match!")

        self.data = []
        for region in self.regions:
            region_type = {
                "bounded_single": BoundedSingleRegion,
                "bounded_array": BoundedArrayRegion,
                "unbounded_single": UnboundedSingleRegion,
                "static": StaticRegion,
            }[region["region_type"]]
            region = region_type(region)
            region.parse(rom_data)
            self.data.append(region)
        self.data.sort(key=lambda r:r.offset)

    def get_region(self, key):
        for region in self.data:
            if region.key() == key:
                return region
        raise KeyError(key)

    def finalize(self):
        cursor = 0
        rom_data = io.BytesIO()
        for region in self.data:
            region.offset = cursor
            region.pad(8)
            cursor += region.size()
            region.dump_to_buffer(rom_data)
        for region in self.data:
            region.update_pointers(rom_data)

        rom_data.seek(0)
        self.rom_checksum = calculateChecksum(rom_data, True)
        rom_data.seek(N64_HEADER_CRC_OFFSET)
        rom_data.write(self.rom_checksum[0])
        rom_data.write(self.rom_checksum[1])

        self.map_data["rom_checksum"] = list(map(lambda x: struct.unpack(">I",x)[0], self.rom_checksum))

        return rom_data.getvalue()




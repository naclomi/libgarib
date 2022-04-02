import logging
import os
import struct
import sys

import capstone
import unicorn
import unicorn.mips_const
import keystone

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

class Region(object):
    def __init__(self, descriptor):
        self.offset = 0
        self.data = b""
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

    def dump_to_file(self, basepath):
        if self.descriptor["data_type"] in file_extensions:
            basepath = os.path.join(basepath, self.descriptor["data_type"])
            os.makedirs(basepath, exist_ok=True)
        if "name" in self.descriptor:
            filename = self.descriptor["name"]
        elif self.descriptor["data_type"] in name_extractors:
            filename = name_extractors[self.descriptor["data_type"]](self.data)
        else:
            filename = "0x{:08X}".format(self.offset)
        filename += file_extensions.get(self.descriptor["data_type"], ".bin")
        filename = os.path.join(basepath, filename)
        with open(filename, "wb") as f:
            f.write(self.data)
        return [filename]

    def parse(self, rom_data):
        pass

    def patch(self, rom_data):
        pass

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
        self.data = rom_data[start_pointer:end_pointer]

class SizedSingleRegion(Region):
    def parse(self, rom_data):
        start_pointer = scrape_pointers(rom_data, self.descriptor["start_pointers"]) & 0x0FFFFFFF
        end_pointer = start_pointer + self.descriptor["size"]
        self.offset = start_pointer
        self.data = rom_data[start_pointer:end_pointer]

class BoundedArrayRegion(Region):
    def parse(self, rom_data):
        start_pointer = scrape_pointers(rom_data, self.descriptor["start_pointers"]) & 0x0FFFFFFF
        end_pointer = scrape_pointers(rom_data, self.descriptor["end_pointers"]) & 0x0FFFFFFF

        self.offset = start_pointer
        self.data = []
        cursor = start_pointer
        while cursor < end_pointer:
            elem_len = struct.unpack(">I", rom_data[cursor:cursor+4])[0]
            self.data.append(rom_data[cursor:cursor+elem_len])
            cursor += elem_len
    
    def dump_to_file(self, basepath):
        if self.descriptor["data_type"] in file_extensions:
            basepath = os.path.join(basepath, self.descriptor["data_type"])
        if "name" in self.descriptor:
            basename = self.descriptor["name"]
        else:
            basename = "0x{:08X}".format(self.offset)
        basepath = os.path.join(basepath, basename)
        os.makedirs(basepath, exist_ok=True)

        extension = file_extensions.get(self.descriptor["data_type"], ".bin")
        filenames = []
        for idx, elem_data in enumerate(self.data):
            if self.descriptor["data_type"] in name_extractors:
                filename = name_extractors[self.descriptor["data_type"]](elem_data)
                filename = "{:}.{:}{:}".format(idx, filename, extension)
            else:
                filename = "{:}{:}".format(idx, extension)
            filename = os.path.join(basepath, filename)
            filenames.append(filename)
            with open(filename, "wb") as f:
                f.write(elem_data)
        return filenames

class StaticRegion(Region):
    def parse(self, rom_data):
        self.offset = self.descriptor["start"]
        self.data = rom_data[self.descriptor["start"]:self.descriptor["end"]]


class Rom(object):
    def __init__(self, rom_data, map_data):
        self.rom_checksum = struct.unpack(">I", rom_data[N64_HEADER_CRC_OFFSET: N64_HEADER_CRC_OFFSET+4])[0]
        self.map = map_data["regions"]

        if self.rom_checksum != map_data["rom_checksum"]:
            logging.warning("Rom and memory map checksums do not match!")

        self.data = []
        for region in self.map:
            region_type = {
                "bounded_single": BoundedSingleRegion,
                "bounded_array": BoundedArrayRegion,
                "sized_single": SizedSingleRegion,
                "static": StaticRegion,
            }[region["region_type"]]
            region = region_type(region)
            region.parse(rom_data)
            self.data.append(region)
        self.data.sort(key=lambda r:r.offset)

    def finalize(self):
        for region in self.data:
            pass
            # TODO


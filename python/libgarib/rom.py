import capstone
import unicorn
import keystone

import struct

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

class PtrCode(object):
    def __init__(self):
        self.asm = keystone.Ks(keystone.KS_ARCH_MIPS, keystone.KS_MODE_MIPS32 | keystone.KS_MODE_BIG_ENDIAN)

        self.disasm = capstone.Cs(capstone.CS_ARCH_MIPS, capstone.CS_MODE_MIPS32 | capstone.CS_MODE_BIG_ENDIAN)
        self.disasm.detail = True

        self.emu = unicorn.Uc(unicorn.UC_ARCH_MIPS, unicorn.UC_MODE_MIPS32 | unicorn.UC_MODE_BIG_ENDIAN)
        self.emu.mem_map(0, 2*1024*1024)

    def get_code(self, address, out_reg):
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
        return instrs[-1].operands[0].value.reg

    def emulate(self, code, out_reg = None):
        self.emu.mem_write(0, code)
        self.emu.emu_start(0, len(code))
        if out_reg is None:
            out_reg = self.get_output_reg(code)
        return self.emu.reg_read(out_reg)

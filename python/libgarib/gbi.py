from enum import Enum
import re
import struct


def mutate(dict, *pairs):
    for k, v in pairs:
        dict[k] = v
    return dict


def mask(width, shift):
    return int("1"*width + "0"*shift, 2)


def signed(num, bits):
    signed_type, unsigned_type = {
        8: ("b", "B"),
        16: ("h", "H"),
        32: ("i", "I"),
        64: ("q", "Q"),
    }[bits]
    return struct.unpack(signed_type, struct.pack(unsigned_type, num))[0]

def pack_uv(uv):
    return struct.pack(">hh", int(uv[0] * (2**5)), int(uv[1] * (2**5)))

def pack_color(color):
    if len(color) > 3:
        a = color[3]
    else:
        a = 1
    return struct.pack(">bbbB", int(color[0] * 255), int(color[1] * 255), int(color[2] * 255), int(a * 255))


class Vertex(object):
    LENGTH = 16
    GL_STRUCTURE = "3f2f4f"
    GL_LENGTH = struct.calcsize("="+GL_STRUCTURE)
    GBI_STRUCTURE_UNLIT = ">3hH2h4B"
    GBI_STRUCTURE_LIT = ">3hH2h3bB"
    def __init__(self, pos=(0,0,0), uv=(0,0), rgb=(0,0,0), n=(0,0,0), a=0):
        self.x, self.y, self.z = pos
        self.f = 0
        self.u, self.v = uv
        self.r, self.g, self.b = rgb
        self.a = a
        self.nx, self.ny, self.nz = n

    def asDLBytes(self, lighting):
        if lighting:
            return struct.pack(
                self.GBI_STRUCTURE_LIT,
                int(self.x), int(self.y), int(self.z),
                0,
                int(self.u * (2**5)), int(self.v * (2**5)),
                int(self.nx * 128), int(self.ny * 128), int(self.nz * 128), int(self.a * 255))
        else:
            return struct.pack(
                self.GBI_STRUCTURE_UNLIT,
                int(self.x), int(self.y), int(self.z),
                0,
                int(self.u * (2**5)), int(self.v * (2**5)),
                int(self.r * 255), int(self.g * 255), int(self.b * 255), int(self.a * 255))

    def asGLBytes(self, lighting):
        # TODO: deal w/ lighting
        if lighting:
            return struct.pack(
                self.GL_STRUCTURE,
                self.x, self.y, self.z,
                self.u, self.v,
                self.nx, self.ny, self.nz, self.a)
        else:
            return struct.pack(
                self.GL_STRUCTURE,
                self.x, self.y, self.z,
                self.u, self.v,
                self.r, self.g, self.b, self.a)

    def unpack(self, raw_bytes):
        self.setXY(raw_bytes[0:4])
        self.setZ(raw_bytes[4:8])
        self.setUV(raw_bytes[8:12])
        self.setNormRGBA(raw_bytes[12:16])
        return self

    def setXY(self, raw_bytes):
        self.x, self.y = struct.unpack(">hh", raw_bytes)

    def setZ(self, raw_bytes):
        self.z, = struct.unpack(">hxx", raw_bytes)

    def setUV(self, raw_bytes):
        raw_u, raw_v = struct.unpack(">hh", raw_bytes)
        self.u = raw_u / 2**5
        self.v = raw_v / 2**5

    def setNormRGBA(self, raw_bytes):
        raw_r, raw_g, raw_b, raw_a = struct.unpack(">4B", raw_bytes)
        raw_nx, raw_ny, raw_nz = struct.unpack(">3bx", raw_bytes)
        self.nx = raw_nx / 128
        self.ny = raw_ny / 128
        self.nz = raw_nz / 128
        self.r = raw_r / 255
        self.g = raw_g / 255
        self.b = raw_b / 255
        self.a = raw_a / 255

    def __str__(self):
        return ("<xyz({x:.02f},{y:.02f},{z:.02f})/"
                "uv({u:.02f},{v:.02f})/"
                "rgba({r:.02f},{g:.02f},{b:.02f},{a:.02f})>".format(
                 **self.__dict__)
                )


class Field(object):
    def __init__(self, name, offset, size, default=None):
        self.name = name
        self.offset = offset
        self.size = size
        self.mask = mask(self.size, self.offset)
        self.default = default

    @classmethod
    def list(cls, *tuples):
        return tuple(cls(*tuple) for tuple in tuples)


class Command(object):
    def __init__(self, name, opcode, fields=[], xform=None, inverse_xform=None):
        self.name = name
        self.opcode = opcode
        self.fields = fields
        self.xform = xform
        self.inverse_xform = inverse_xform
        if (self.xform is None) ^ (self.inverse_xform is None):
            raise Exception("{:}: If xform is provided, inverse must be as well".format(name))

        self.byName = dict(
            (field.name, field) for field in self.fields
        )

    def __repr__(self):
        return self.name

    def pack(self, **kwargs):
        raw_args = kwargs.pop("_raw", False)
        for field in self.fields:
            if field.default is not None and field.name not in kwargs:
                kwargs[field.name] = field.default
        if kwargs.keys() != self.byName.keys():
            raise ValueError()
        bits = 0
        bits |= self.opcode << 56
        if raw_args is False and self.inverse_xform is not None:
            kwargs = self.inverse_xform(kwargs)
        for arg_name, arg_value in kwargs.items():
            arg_value = unwrap_enum(arg_value)
            field = self.byName[arg_name]
            bits |= (arg_value & (2**field.size - 1)) << field.offset
        return struct.pack(">II", (bits >> 32) & 0xFFFFFFFF, bits & 0xFFFFFFFF)

    @classmethod
    def list(cls, *tuples):
        return tuple(cls(*tuple) for tuple in tuples)


class GBI(object):
    def __init__(self, *, commands=[], constants={}, inherit=None):
        if inherit is None:
            self.constants = constants
            self.commands = Command.list(*commands)
        else:
            self.constants = dict(inherit.constants)
            self.constants.update(constants)
            self.commands = list(inherit.commands)
            new_commands = Command.list(*commands)
            for command in new_commands:
                old_cmd = inherit.byOpcode.get(command.opcode, None)
                if old_cmd is not None:
                    self.commands.remove(old_cmd)
                self.commands.append(command)
            self.commands = tuple(self.commands)

        for k, v in self.constants.items():
            setattr(self, k, v)

        self.byName = dict(
            (command.name, command) for command in self.commands
        )
        self.byOpcode = dict(
            (command.opcode, command) for command in self.commands
        )

    def __getitem__(self, key):
        if isinstance(key, str):
            return self.byName[key]
        elif isinstance(key, int):
            return self.byOpcode[key]

    def parseList(self, display_list_bytes):
        offset = 0
        while offset < len(display_list_bytes):
            op_bytes = display_list_bytes[offset:offset+8]
            cmd, args = self.parse(op_bytes)
            yield cmd, args
            offset += 8

    def parse(self, raw_command):
        opcode = raw_command[0]
        arg_bytes = raw_command[1:]
        arg_bits = "".join("{:08b}".format(byte) for byte in arg_bytes)
        command = self.byOpcode[opcode]
        args = {}
        for field in command.fields:
            field_start = len(arg_bits)-field.offset
            field_end = field_start - field.size
            field_bits = arg_bits[field_end:field_start]
            args[field.name] = int(field_bits, 2)
        if command.xform is not None:
            args = command.xform(args)
        return (command, args)

    def pack(self, command, **kwargs):
        return command.pack(kwargs)

othermode_h_fields = Field.list(
    ("G_MDSFT_ALPHADITHER", 4, 2),
    ("G_MDSFT_RGBDITHER", 6, 2),
    ("G_MDSFT_COMBKEY", 8, 1),
    ("G_MDSFT_TEXTCONV", 9, 3),
    ("G_MDSFT_TEXTFILT", 12, 2),
    ("G_MDSFT_TEXTLUT", 14, 2),
    ("G_MDSFT_TEXTLOD", 16, 1),
    ("G_MDSFT_TEXTDETAIL", 17, 2),
    ("G_MDSFT_TEXTPERSP", 19, 1),
    ("G_MDSFT_CYCLETYPE", 20, 2),
    ("G_MDSFT_COLORDITHER", 22, 1),
    ("G_MDSFT_PIPELINE", 23, 1)
)


def process_othermode_h_args(args):
    shift = args["sft"]
    width = args["len"]
    data = args["data"]
    data_mask = mask(width, shift)
    out_args = dict((field.name, None) for field in othermode_h_fields)
    for field in othermode_h_fields:
        overlap = data_mask & field.mask
        if overlap != 0:
            out_args[field.name] = (
                (data & data_mask) >> field.offset,
                overlap >> field.offset)
    return out_args


def process_othermode_h_args_inv(args):
    raise NotImplementedError()

class ImSize(Enum):
    ci4 = 0
    ci8 = 1
    uncompressed_16b = 2
    uncompressed_32b = 3

class ImFormat(Enum):
    rgba = 0
    yuv = 1
    ci = 2
    ia = 3
    i = 4

def unwrap_enum(val):
    if isinstance(val, Enum):
        return val.value
    else:
        return val

# TODO:
#   Find some way to parse G_TEXRECT alongside
#   G_RDPHALF_1 and G_RDPHALF_2

Fast3D = GBI(commands=[
    ("G_SPNOOP", 0),
    ("G_MTX", 1, Field.list(
        ("matrix", 48, 1),
        ("math_op", 49, 1),
        ("stack_op", 50, 1), 
        ("address", 0, 32)
    ), lambda args: mutate(
        args,
        ("matrix", "G_MTX_PROJECTION" if args["matrix"] else "G_MTX_MODELVIEW"),
        ("math_op", "G_MTX_LOAD" if args["math_op"] else "G_MTX_MUL"),
        ("stack_op", "G_MTX_PUSH" if args["stack_op"] else "G_MTX_NOPUSH")
    ), lambda args: mutate(
        args,
        ("matrix", {"G_MTX_PROJECTION": 1, "G_MTX_MODELVIEW":0}[args["matrix"]]),
        ("math_op", {"G_MTX_LOAD": 1, "G_MTX_MUL":0}[args["math_op"]]),
        ("stack_op",  {"G_MTX_PUSH": 1, "G_MTX_NOPUSH":0}[args["stack_op"]])
    )),
    ("G_RESERVED0", 2),
    ("G_MOVEMEM", 3, Field.list(
        ("size", 48, 8),
        ("offset", 40, 8),
        ("index", 32, 8),
        ("address", 0, 32),
    ), lambda args: mutate(
        args,
        ("size", int(((args["size"] >> 3)+1)*8)),
        ("offset", int(args["offset"]*8)),
        ("index", {
                2: "G_MV_MMTX",
                6: "G_MV_PMTX",
                8: "G_MV_VIEWPORT",
                10: "G_MV_LIGHT",
                12: "G_MV_POINT",
                14: "G_MV_MATRIX"
            }.get(args["index"], "UNKNOWN_0x{:02X}".format(args["index"])))
    ), lambda args: mutate(
        args,
        ("size", ((args["size"]//8)-1) << 3),
        ("offset", args["offset"]//8),
        ("index", {
                "G_MV_MMTX": 2,
                "G_MV_PMTX": 6,
                "G_MV_VIEWPORT": 8,
                "G_MV_LIGHT": 10,
                "G_MV_POINT": 12,
                "G_MV_MATRIX": 14
            }.get(args["index"], int(re.match("UNKNOWN_(0x[0-9A-Fa-f]{2})$", "UNKNOWN_0xAF").group(1),0)))
    )),
    ("G_VTX", 4),
    ("G_RESERVED1", 5),
    ("G_DL", 6, Field.list(
        ("link", 48, 8),
        ("address", 0, 32),
    ), lambda args: mutate(
        args,
        ("link", args["link"] == 0),
    ), lambda args: mutate(
        args,
        ("link", 0 if args["link"] else 1),
    )),
    ("G_RESERVED2", 7),
    ("G_RESERVED3", 8),
    ("G_SPRITE2D_BASE", 9),

    # IMMEDIATE
    ("G_TRI1", 0xBF, Field.list(
        ("v0", 16, 8),
        ("v1", 8, 8),
        ("v2", 0, 8),
    ), lambda args: mutate(
        args,
        ("v0", args["v0"]//2),
        ("v1", args["v1"]//2),
        ("v2", args["v2"]//2)
    ), lambda args: mutate(
        args,
        ("v0", int(args["v0"]*2)),
        ("v1", int(args["v1"]*2)),
        ("v2", int(args["v2"]*2))
    )),
    ("G_CULLDL", 0xBE, Field.list(
        ("vstart", 32, 16),
        ("vend", 0, 16),
    )),
    ("G_POPMTX", 0xBD, Field.list(
        ("count", 0, 32)
    )),
    ("G_MOVEWORD", 0xBC, Field.list(
        ("offset", 40, 16),
        ("index", 32, 8),
        ("value", 0, 32),
    ), lambda args: mutate(
        args,
        ("index", {
                0x00: "G_MW_MATRIX",
                0x02: "G_MW_NUMLIGHT",
                0x04: "G_MW_CLIP",
                0x06: "G_MW_SEGMENT",
                0x08: "G_MW_FOG",
                0x0A: "G_MW_LIGHTCOL",
                0x0C: "G_MW_FORCEMTX",
                0x0E: "G_MW_PERSPNORM",
            }[args["index"]]),
    ), lambda args: mutate(
        args,
        ("index", {
                "G_MW_MATRIX": 0x00,
                "G_MW_NUMLIGHT": 0x02,
                "G_MW_CLIP": 0x04,
                "G_MW_SEGMENT": 0x06,
                "G_MW_FOG": 0x08,
                "G_MW_LIGHTCOL": 0x0A,
                "G_MW_FORCEMTX": 0x0C,
                "G_MW_PERSPNORM": 0x0E,
            }[args["index"]]),
    )),
    ("G_TEXTURE", 0xBB, Field.list(
        ("mipmap_levels", 43, 3),
        ("tile", 40, 3),
        ("enable", 32, 8),
        ("scale_s", 16, 16),
        ("scale_t", 0, 16)
    ), lambda args: mutate(
        args,
        ("enable", args["enable"] == 1),
        ("scale_s", args["scale_s"]/2**16),
        ("scale_t", args["scale_t"]/2**16),
    ), lambda args: mutate(
        args,
        ("enable", 1 if args["enable"] else 0),
        ("scale_s", args["scale_s"]*2**16),
        ("scale_t", args["scale_t"]*2**16),
    )),
    ("G_SETOTHERMODE_H", 0xBA, Field.list(
        ("sft", 40, 8),
        ("len", 32, 8),
        ("data", 0, 32),
    ), process_othermode_h_args,
       process_othermode_h_args_inv),
    ("G_SETOTHERMODE_L", 0xB9, Field.list(
        ("sft", 40, 8),
        ("len", 32, 8),
        ("data", 0, 32),
    )),
    ("G_ENDDL", 0xB8),
    ("G_SETGEOMETRYMODE", 0xB7, Field.list(
        ("G_ZBUFFER", 0, 1, False),
        ("G_SHADE", 2, 1, False),
        ("G_SHADING_SMOOTH", 9, 1, False),
        ("G_CULL_FRONT", 12, 1, False),
        ("G_CULL_BACK", 13, 1, False),
        ("G_FOG", 16, 1, False),
        ("G_LIGHTING", 17, 1, False),
        ("G_TEXTURE_GEN", 18, 1, False),
        ("G_TEXTURE_GEN_LINEAR", 19, 1, False),
        ("G_CLIPPING", 23, 1, False),
    )),
    ("G_CLEARGEOMETRYMODE", 0xB6, Field.list(
        ("G_ZBUFFER", 0, 1, False),
        ("G_SHADE", 2, 1, False),
        ("G_SHADING_SMOOTH", 9, 1, False),
        ("G_CULL_FRONT", 12, 1, False),
        ("G_CULL_BACK", 13, 1, False),
        ("G_FOG", 16, 1, False),
        ("G_LIGHTING", 17, 1, False),
        ("G_TEXTURE_GEN", 18, 1, False),
        ("G_TEXTURE_GEN_LINEAR", 19, 1, False),
        ("G_CLIPPING", 23, 1, False),
    )),
    ("G_LINE3D", 0xB5),
    ("G_RDPHALF_1", 0xB4, Field.list(
        ("word", 0, 32)
    )),
    ("G_RDPHALF_2", 0xB3, Field.list(
        ("word", 0, 32)
    )),

    ("G_RDPHALF_CONT", 0xB2),

    # TODO: make a sprite derivative that
    #   includes these:
    # "G_SPRITE2D_SCALEFLIP": 0xBE,
    # "G_SPRITE2D_DRAW": 0xBD,

    # RDP
    ("G_NOOP", 0xc0),

    ("G_SETCIMG", 0xff),
    ("G_SETZIMG", 0xfe, Field.list(
        ("address", 0, 32)
    )),
    ("G_SETTIMG", 0xfd, Field.list(
        ("fmt", 53, 3),
        ("siz", 51, 2),
        ("width", 32, 12),
        ("i", 0, 32),
    ), lambda args: mutate(
        args,
        ("width", args["width"]+1),
        ("fmt", ImFormat(args["fmt"])),
        ("siz", ImSize(args["siz"]))
    ),  lambda args: mutate(
        args,
        ("width", args["width"]-1),
        ("fmt", args["fmt"]),
        ("siz", args["siz"])
    )),

    ("G_SETCOMBINE", 0xfc, Field.list(
        ("a_color_1", 52, 4),
        ("c_color_1", 47, 5),
        ("a_alpha_1", 44, 3),
        ("c_alpha_1", 41, 3),
        ("a_color_2", 37, 4),
        ("c_color_2", 32, 5),
        ("b_color_1", 28, 4),
        ("b_color_2", 24, 4),
        ("a_alpha_2", 21, 3),
        ("c_alpha_2", 18, 3),
        ("d_color_1", 15, 3),
        ("b_alpha_1", 12, 3),
        ("d_alpha_1", 9, 3),
        ("d_color_2", 6, 3),
        ("b_alpha_2", 3, 3),
        ("d_alpha_2", 0, 3)
    )),
    ("G_SETENVCOLOR", 0xfb),
    ("G_SETPRIMCOLOR", 0xfa, Field.list(
        ("lod_min", 40, 8),
        ("lod_fraction", 32, 8),
        ("r", 24, 8),
        ("g", 16, 8),
        ("b", 8, 8),
        ("a", 0, 8),
    ), lambda args: mutate(
        args,
        ("lod_min", args["lod_min"]/256),
        ("lod_fraction", args["lod_fraction"]/256),
    ), lambda args: mutate(
        args,
        ("lod_min", args["lod_min"]*256),
        ("lod_fraction", args["lod_fraction"]*256),
    )),
    ("G_SETBLENDCOLOR", 0xf9, Field.list(
        ("r", 24, 8),
        ("g", 16, 8),
        ("b", 8, 8),
        ("a", 0, 8),
    )),
    ("G_SETFOGCOLOR", 0xf8, Field.list(
        ("r", 24, 8),
        ("g", 16, 8),
        ("b", 8, 8),
        ("a", 0, 8),
    )),
    ("G_SETFILLCOLOR", 0xf7),
    ("G_FILLRECT", 0xf6),
    ("G_SETTILE", 0xf5, Field.list(
        ("fmt", 53, 3),
        ("siz", 51, 2),
        ("line", 41, 9),
        ("tmem", 32, 9),
        ("tile", 24, 3),
        ("palette", 20, 4),
        ("clampt", 19, 1),
        ("mirrort", 18, 1),
        ("maskt", 14, 4),
        ("shiftt", 10, 4),
        ("clamps", 9, 1),
        ("mirrors", 8, 1),
        ("masks", 4, 4),
        ("shifts", 0, 4),
    ), lambda args: mutate(
        args,
        ("fmt", ImFormat(args["fmt"])),
        ("siz", ImSize(args["siz"]))
    ),  lambda args: mutate(
        args,
        ("fmt", args["fmt"]),
        ("siz", args["siz"])
    )),
    ("G_LOADTILE", 0xf4, Field.list(
        ("uls", 44, 12),
        ("ult", 32, 12),
        ("tile", 24, 4),
        ("lrs", 12, 12),
        ("lrt", 0, 12),
    ), lambda args: mutate(
        args,
        ("uls", args["uls"]/4),
        ("ult", args["ult"]/4),
        ("lrs", args["lrs"]/4),
        ("lrt", args["lrt"]/4),
    ), lambda args: mutate(
        args,
        ("uls", args["uls"]*4),
        ("ult", args["ult"]*4),
        ("lrs", args["lrs"]*4),
        ("lrt", args["lrt"]*4),
    )),
    ("G_LOADBLOCK", 0xf3, Field.list(
        ("uls", 44, 12),
        ("ult", 32, 12),
        ("tile", 24, 3),
        ("lrs", 12, 12),
        ("dxt", 0, 12),
    ), lambda args: mutate(
        args,
        ("uls", args["uls"]/4),
        ("ult", args["ult"]/4),
        ("lrs", (args["lrs"]+1)/4),
        ("dxt", args["dxt"]/2048),
    ), lambda args: mutate(
        args,
        ("uls", args["uls"]*4),
        ("ult", args["ult"]*4),
        ("lrs", (args["lrs"]*4)-1),
        ("dxt", args["dxt"]*2048),
    )),
    ("G_SETTILESIZE", 0xf2, Field.list(
        ("uls", 44, 12),
        ("ult", 32, 12),
        ("tile", 24, 3),
        ("lrs", 12, 12),
        ("lrt", 0, 12),
    ), lambda args: mutate(
        args,
        ("uls", args["uls"]/4),
        ("ult", args["ult"]/4),
        ("lrs", args["lrs"]/4),
        ("lrt", args["lrt"]/4),
    ), lambda args: mutate(
        args,
        ("uls", args["uls"]*4),
        ("ult", args["ult"]*4),
        ("lrs", args["lrs"]*4),
        ("lrt", args["lrt"]*4),
    )),
    ("G_LOADTLUT", 0xf0, Field.list(
        ("tile", 24, 3),
        ("count", 14, 10)
    )),
    ("G_RDPSETOTHERMODE", 0xef),
    ("G_SETPRIMDEPTH", 0xee, Field.list(
        ("z", 16, 16),
        ("delta_z", 0, 16)
    ), lambda args: mutate(
        args,
        ("z", signed(args["z"], 16)),
        ("delta_z", signed(args["delta_z"], 16))
    ), mutate # inverse is just a no-op, args don't need to be cast as signed when packing
    ),
    ("G_SETSCISSOR", 0xed, Field.list(
        ("ulx", 44, 12),
        ("uly", 32, 12),
        ("mode", 24, 4),
        ("lrx", 12, 12),
        ("lry", 0, 12),
    ), lambda args: mutate(
        args,
        ("mode", {
                0x00: "G_SC_NON_INTERLACE",
                0x02: "G_SC_EVEN_INTERLACE",
                0x03: "G_SC_ODD_INTERLACE",
            }[args["mode"]]),
    ), lambda args: mutate(
        args,
        ("mode", {
                "G_SC_NON_INTERLACE": 0x00,
                "G_SC_EVEN_INTERLACE": 0x02,
                "G_SC_ODD_INTERLACE": 0x03,
            }[args["mode"]]),
    )),
    ("G_SETCONVERT", 0xec),
    ("G_SETKEYR", 0xeb),
    ("G_SETKEYGB", 0xea),
    ("G_RDPFULLSYNC", 0xe9),
    ("G_RDPTILESYNC", 0xe8),
    ("G_RDPPIPESYNC", 0xe7),
    ("G_RDPLOADSYNC", 0xe6),
    ("G_TEXRECTFLIP", 0xe5, Field.list(
        ("lrx", 44, 12),
        ("lry", 32, 12),
        ("tile", 24, 4),
        ("ulx", 12, 12),
        ("uly", 0, 12),
    )),


    # TODO:
    # Draws a textured rectangle from screen coordinates (ulx,uly) to (lrx, lry), using the texture specified by tile to color the rectangle. The texture is positioned using (uls, ult) as the texture coordinate of (ulx, uly), and changing the texture coordinates with the use of dsdx and dtdy.
    # ulx, uly, lrx, and lry are 12-bit numbers in a fixed point 10.2 format, giving a range of 0 ≤ n ≤ 1023.75 for each value (with 0b0.01 / 0d0.25 precision). This means that the coordinates cannot reference the framebuffer past a 1024-pixel square, if the framebuffer exceeds those limits in either dimension.
    # tile refers to any of the eight tile descriptors whose texture will be used on the rectangle. uls and ult specify the S and T coordinate, respectively, of the upper-left corner of the rectangle. uls and ult are in signed fixed point 10.5 format, giving a range -1024 ≤ n ≤ 1023.96875 for each value (with 0b0.00001 / 1/32 precision).
    # The texture coordinates for other parts of the rectangle are calculated via dsdx and dtdy, which are in signed fixed point 5.10 format, giving a range of -32 ≤ n ≤ 31.999023 (with 0b0.0000000001 / 1/1024 precision). These parameters change the S coordinate per a change of 1.0 in the X coordinate of the rectangle, and the T coordinate per change of 1.0 in the Y coordinate (XXX not entirely sure on what the 'per change's are, but 1.0 seems reasonable).
    ("G_TEXRECT", 0xe4, Field.list(
        ("lrx", 44, 12),
        ("lry", 32, 12),
        ("tile", 24, 4),
        ("ulx", 12, 12),
        ("uly", 0, 12),
    )),

    # GENERATED

    ("G_TRI_FILL", 0xc8),
    ("G_TRI_SHADE", 0xcc),
    ("G_TRI_TXTR", 0xca),
    ("G_TRI_SHADE_TXTR", 0xce),
    ("G_TRI_FILL_ZBUFF", 0xc9),
    ("G_TRI_SHADE_ZBUFF", 0xcd),
    ("G_TRI_TXTR_ZBUFF", 0xcb),
    ("G_TRI_SHADE_TXTR_ZBUFF", 0xcf)
], constants={
    # G_MDSFT_TEXTLUT values
    "G_TT_NONE": 0,
    "G_TT_RGBA16": 2,
    "G_TT_IA16": 3,

    # G_SETTILE values
    "G_TX_NOLOD": 0,
    "G_TX_RENDERTILE": 0,
    "G_TX_LOADTILE": 7,

    "G_TEXTURE_IMAGE_FRAC": 2,

    "G_TX_DXT_FRAC": 11,

    # G_SETOTHERMODE_H sft values
    "G_MDSFT_TEXTLUT": 14
})

F3DEX = GBI(inherit=Fast3D, commands=[
    # Different binary format from Fast3D
    ("G_VTX", 4, Field.list(
        ("v0", 48, 8),
        ("n", 42, 6),
        ("length", 32, 10),
        ("address", 0, 32),
    ), lambda args: mutate(
        args,
        ("v0", args["v0"]//2)
    ), lambda args: mutate(
        args,
        ("v0", int(args["v0"]*2))
    )),

    # New commands
    ("G_MODIFYVTX", 0xB2, Field.list(
        ("where", 48, 8),
        ("vtx", 32, 16),
        ("val", 0, 32),
    ), lambda args: mutate(
        args,
        ("vtx", args["vtx"]//2),
        ("val", struct.pack(">I", args["val"])),
        ("where", {
            0x10: "G_MWO_POINT_RGBA",
            0x14: "G_MWO_POINT_ST",
            0x18: "G_MWO_POINT_XYSCREEN",
            0x1C: "G_MWO_POINT_ZSCREEN",
        }[args["where"]]),
    ), lambda args: mutate(
        args,
        ("vtx", int(args["vtx"]*2)),
        ("val", struct.unpack(">I", args["val"])[0]),
        ("where", {
            "G_MWO_POINT_RGBA": 0x10,
            "G_MWO_POINT_ST": 0x14,
            "G_MWO_POINT_XYSCREEN": 0x18,
            "G_MWO_POINT_ZSCREEN": 0x1C,
        }[args["where"]]),
    )),
    ("G_TRI2", 0xB1, Field.list(
        ("v00", 48, 8),
        ("v01", 40, 8),
        ("v02", 32, 8),
        ("v10", 16, 8),
        ("v11", 8, 8),
        ("v12", 0, 8),
    ), lambda args: mutate(
        args,
        ("v00", args["v00"]//2),
        ("v01", args["v01"]//2),
        ("v02", args["v02"]//2),
        ("v10", args["v10"]//2),
        ("v11", args["v11"]//2),
        ("v12", args["v12"]//2)
    ), lambda args: mutate(
        args,
        ("v00", int(args["v00"]*2)),
        ("v01", int(args["v01"]*2)),
        ("v02", int(args["v02"]*2)),
        ("v10", int(args["v10"]*2)),
        ("v11", int(args["v11"]*2)),
        ("v12", int(args["v12"]*2))
    )),
    ("G_BRANCH_Z", 0xB0),
    ("G_LOAD_UCODE", 0xAF),
])


F3DEX2 = GBI()
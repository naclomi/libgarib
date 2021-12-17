# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class GloverLevel(KaitaiStruct):
    SEQ_FIELDS = ["length", "name", "body"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['length']['start'] = self._io.pos()
        self.length = self._io.read_u4be()
        self._debug['length']['end'] = self._io.pos()
        self._debug['name']['start'] = self._io.pos()
        self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
        self._debug['name']['end'] = self._io.pos()
        self._debug['body']['start'] = self._io.pos()
        self.body = []
        i = 0
        while not self._io.is_eof():
            if not 'arr' in self._debug['body']:
                self._debug['body']['arr'] = []
            self._debug['body']['arr'].append({'start': self._io.pos()})
            self.body.append(GloverLevel.Cmd(self._io, self, self._root))
            self._debug['body']['arr'][len(self.body) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['body']['end'] = self._io.pos()

    class PlatSpecial0x68(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x5c", "u32_0x60", "u32_0x65"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x5c']['start'] = self._io.pos()
            self.u32_0x5c = self._io.read_u4be()
            self._debug['u32_0x5c']['end'] = self._io.pos()
            self._debug['u32_0x60']['start'] = self._io.pos()
            self.u32_0x60 = self._io.read_u4be()
            self._debug['u32_0x60']['end'] = self._io.pos()
            self._debug['u32_0x65']['start'] = self._io.pos()
            self.u32_0x65 = self._io.read_u4be()
            self._debug['u32_0x65']['end'] = self._io.pos()


    class PuzzleAction0x54(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x14", "u32_0x16", "u32_0x18", "u32_0x1a", "u32_0x1c", "u32_0x1e", "u32_0x10", "u16_0x0e", "u32_0x24", "u32_0x28", "u32_0x2c", "u16_0x0a"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x14']['start'] = self._io.pos()
            self.u32_0x14 = self._io.read_u2be()
            self._debug['u32_0x14']['end'] = self._io.pos()
            self._debug['u32_0x16']['start'] = self._io.pos()
            self.u32_0x16 = self._io.read_u2be()
            self._debug['u32_0x16']['end'] = self._io.pos()
            self._debug['u32_0x18']['start'] = self._io.pos()
            self.u32_0x18 = self._io.read_u2be()
            self._debug['u32_0x18']['end'] = self._io.pos()
            self._debug['u32_0x1a']['start'] = self._io.pos()
            self.u32_0x1a = self._io.read_u2be()
            self._debug['u32_0x1a']['end'] = self._io.pos()
            self._debug['u32_0x1c']['start'] = self._io.pos()
            self.u32_0x1c = self._io.read_u2be()
            self._debug['u32_0x1c']['end'] = self._io.pos()
            self._debug['u32_0x1e']['start'] = self._io.pos()
            self.u32_0x1e = self._io.read_u2be()
            self._debug['u32_0x1e']['end'] = self._io.pos()
            self._debug['u32_0x10']['start'] = self._io.pos()
            self.u32_0x10 = self._io.read_u2be()
            self._debug['u32_0x10']['end'] = self._io.pos()
            self._debug['u16_0x0e']['start'] = self._io.pos()
            self.u16_0x0e = self._io.read_u2be()
            self._debug['u16_0x0e']['end'] = self._io.pos()
            self._debug['u32_0x24']['start'] = self._io.pos()
            self.u32_0x24 = self._io.read_u4be()
            self._debug['u32_0x24']['end'] = self._io.pos()
            self._debug['u32_0x28']['start'] = self._io.pos()
            self.u32_0x28 = self._io.read_u4be()
            self._debug['u32_0x28']['end'] = self._io.pos()
            self._debug['u32_0x2c']['start'] = self._io.pos()
            self.u32_0x2c = self._io.read_u4be()
            self._debug['u32_0x2c']['end'] = self._io.pos()
            self._debug['u16_0x0a']['start'] = self._io.pos()
            self.u16_0x0a = self._io.read_u2be()
            self._debug['u16_0x0a']['end'] = self._io.pos()


    class PuzzleAction0x460x470x48(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x24", "u16_0x0a"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x24']['start'] = self._io.pos()
            self.u32_0x24 = self._io.read_u4be()
            self._debug['u32_0x24']['end'] = self._io.pos()
            self._debug['u16_0x0a']['start'] = self._io.pos()
            self.u16_0x0a = self._io.read_u2be()
            self._debug['u16_0x0a']['end'] = self._io.pos()


    class PlatSound0xc2(KaitaiStruct):
        SEQ_FIELDS = ["sound_id", "volume", "pitch"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['sound_id']['start'] = self._io.pos()
            self.sound_id = self._io.read_u2be()
            self._debug['sound_id']['end'] = self._io.pos()
            self._debug['volume']['start'] = self._io.pos()
            self.volume = self._io.read_u2be()
            self._debug['volume']['end'] = self._io.pos()
            self._debug['pitch']['start'] = self._io.pos()
            self.pitch = self._io.read_u2be()
            self._debug['pitch']['end'] = self._io.pos()


    class PlatSpinPause0x7c(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x0c", "u16_0x0a"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x0c']['start'] = self._io.pos()
            self.u16_0x0c = self._io.read_u2be()
            self._debug['u16_0x0c']['end'] = self._io.pos()
            self._debug['u16_0x0a']['start'] = self._io.pos()
            self.u16_0x0a = self._io.read_u2be()
            self._debug['u16_0x0a']['end'] = self._io.pos()


    class PlatMagnet0x8b(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x0c", "u32_0x48", "u32_0x4c", "u32_0x50", "u32_0x10", "u32_0x14", "u32_0x18", "u32_0x1c"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x0c']['start'] = self._io.pos()
            self.u16_0x0c = self._io.read_u2be()
            self._debug['u16_0x0c']['end'] = self._io.pos()
            self._debug['u32_0x48']['start'] = self._io.pos()
            self.u32_0x48 = self._io.read_u4be()
            self._debug['u32_0x48']['end'] = self._io.pos()
            self._debug['u32_0x4c']['start'] = self._io.pos()
            self.u32_0x4c = self._io.read_u4be()
            self._debug['u32_0x4c']['end'] = self._io.pos()
            self._debug['u32_0x50']['start'] = self._io.pos()
            self.u32_0x50 = self._io.read_u4be()
            self._debug['u32_0x50']['end'] = self._io.pos()
            self._debug['u32_0x10']['start'] = self._io.pos()
            self.u32_0x10 = self._io.read_u4be()
            self._debug['u32_0x10']['end'] = self._io.pos()
            self._debug['u32_0x14']['start'] = self._io.pos()
            self.u32_0x14 = self._io.read_u4be()
            self._debug['u32_0x14']['end'] = self._io.pos()
            self._debug['u32_0x18']['start'] = self._io.pos()
            self.u32_0x18 = self._io.read_u4be()
            self._debug['u32_0x18']['end'] = self._io.pos()
            self._debug['u32_0x1c']['start'] = self._io.pos()
            self.u32_0x1c = self._io.read_u4be()
            self._debug['u32_0x1c']['end'] = self._io.pos()


    class EnemyInstructionError(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class Backdrop(KaitaiStruct):
        SEQ_FIELDS = ["texture_id", "decal_pos_x", "decal_pos_y", "sort_key", "offset_y", "scale_x", "scale_y", "flip_x", "flip_y", "scroll_speed_x", "unused", "decal_parent_idx"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['texture_id']['start'] = self._io.pos()
            self.texture_id = self._io.read_u4be()
            self._debug['texture_id']['end'] = self._io.pos()
            self._debug['decal_pos_x']['start'] = self._io.pos()
            self.decal_pos_x = self._io.read_u2be()
            self._debug['decal_pos_x']['end'] = self._io.pos()
            self._debug['decal_pos_y']['start'] = self._io.pos()
            self.decal_pos_y = self._io.read_u2be()
            self._debug['decal_pos_y']['end'] = self._io.pos()
            self._debug['sort_key']['start'] = self._io.pos()
            self.sort_key = self._io.read_u2be()
            self._debug['sort_key']['end'] = self._io.pos()
            self._debug['offset_y']['start'] = self._io.pos()
            self.offset_y = self._io.read_s2be()
            self._debug['offset_y']['end'] = self._io.pos()
            self._debug['scale_x']['start'] = self._io.pos()
            self.scale_x = self._io.read_u2be()
            self._debug['scale_x']['end'] = self._io.pos()
            self._debug['scale_y']['start'] = self._io.pos()
            self.scale_y = self._io.read_u2be()
            self._debug['scale_y']['end'] = self._io.pos()
            self._debug['flip_x']['start'] = self._io.pos()
            self.flip_x = self._io.read_u2be()
            self._debug['flip_x']['end'] = self._io.pos()
            self._debug['flip_y']['start'] = self._io.pos()
            self.flip_y = self._io.read_u2be()
            self._debug['flip_y']['end'] = self._io.pos()
            self._debug['scroll_speed_x']['start'] = self._io.pos()
            self.scroll_speed_x = self._io.read_u2be()
            self._debug['scroll_speed_x']['end'] = self._io.pos()
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_u2be()
            self._debug['unused']['end'] = self._io.pos()
            self._debug['decal_parent_idx']['start'] = self._io.pos()
            self.decal_parent_idx = self._io.read_u2be()
            self._debug['decal_parent_idx']['end'] = self._io.pos()


    class DiffuseLight(KaitaiStruct):
        SEQ_FIELDS = ["r", "g", "b", "theta_1", "theta_2"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['r']['start'] = self._io.pos()
            self.r = self._io.read_u2be()
            self._debug['r']['end'] = self._io.pos()
            self._debug['g']['start'] = self._io.pos()
            self.g = self._io.read_u2be()
            self._debug['g']['end'] = self._io.pos()
            self._debug['b']['start'] = self._io.pos()
            self.b = self._io.read_u2be()
            self._debug['b']['end'] = self._io.pos()
            self._debug['theta_1']['start'] = self._io.pos()
            self.theta_1 = self._io.read_f4be()
            self._debug['theta_1']['end'] = self._io.pos()
            self._debug['theta_2']['start'] = self._io.pos()
            self.theta_2 = self._io.read_f4be()
            self._debug['theta_2']['end'] = self._io.pos()


    class Buzzer(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x2a", "tag_0x24", "tag_0x20", "u16_0x28", "u8_0x2c", "u8_0x2d", "u8_0x2e", "u8_0x2f", "u32_0x08", "u32_0x0c", "u32_0x10", "u32_0x14", "u32_0x18", "u32_0x1c", "u32_0x50", "u32_0x54"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x2a']['start'] = self._io.pos()
            self.u16_0x2a = self._io.read_u2be()
            self._debug['u16_0x2a']['end'] = self._io.pos()
            self._debug['tag_0x24']['start'] = self._io.pos()
            self.tag_0x24 = self._io.read_u2be()
            self._debug['tag_0x24']['end'] = self._io.pos()
            self._debug['tag_0x20']['start'] = self._io.pos()
            self.tag_0x20 = self._io.read_u2be()
            self._debug['tag_0x20']['end'] = self._io.pos()
            self._debug['u16_0x28']['start'] = self._io.pos()
            self.u16_0x28 = self._io.read_u2be()
            self._debug['u16_0x28']['end'] = self._io.pos()
            self._debug['u8_0x2c']['start'] = self._io.pos()
            self.u8_0x2c = self._io.read_u2be()
            self._debug['u8_0x2c']['end'] = self._io.pos()
            self._debug['u8_0x2d']['start'] = self._io.pos()
            self.u8_0x2d = self._io.read_u2be()
            self._debug['u8_0x2d']['end'] = self._io.pos()
            self._debug['u8_0x2e']['start'] = self._io.pos()
            self.u8_0x2e = self._io.read_u2be()
            self._debug['u8_0x2e']['end'] = self._io.pos()
            self._debug['u8_0x2f']['start'] = self._io.pos()
            self.u8_0x2f = self._io.read_u2be()
            self._debug['u8_0x2f']['end'] = self._io.pos()
            self._debug['u32_0x08']['start'] = self._io.pos()
            self.u32_0x08 = self._io.read_u4be()
            self._debug['u32_0x08']['end'] = self._io.pos()
            self._debug['u32_0x0c']['start'] = self._io.pos()
            self.u32_0x0c = self._io.read_u4be()
            self._debug['u32_0x0c']['end'] = self._io.pos()
            self._debug['u32_0x10']['start'] = self._io.pos()
            self.u32_0x10 = self._io.read_u4be()
            self._debug['u32_0x10']['end'] = self._io.pos()
            self._debug['u32_0x14']['start'] = self._io.pos()
            self.u32_0x14 = self._io.read_u4be()
            self._debug['u32_0x14']['end'] = self._io.pos()
            self._debug['u32_0x18']['start'] = self._io.pos()
            self.u32_0x18 = self._io.read_u4be()
            self._debug['u32_0x18']['end'] = self._io.pos()
            self._debug['u32_0x1c']['start'] = self._io.pos()
            self.u32_0x1c = self._io.read_u4be()
            self._debug['u32_0x1c']['end'] = self._io.pos()
            self._debug['u32_0x50']['start'] = self._io.pos()
            self.u32_0x50 = self._io.read_u4be()
            self._debug['u32_0x50']['end'] = self._io.pos()
            self._debug['u32_0x54']['start'] = self._io.pos()
            self.u32_0x54 = self._io.read_u4be()
            self._debug['u32_0x54']['end'] = self._io.pos()


    class PuzzleAny(KaitaiStruct):
        SEQ_FIELDS = ["op"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['op']['start'] = self._io.pos()
            self.op = self._io.read_u2be()
            self._debug['op']['end'] = self._io.pos()


    class SetActorRotation(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f4be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()


    class CameoInst(KaitaiStruct):
        SEQ_FIELDS = ["inst_type", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['inst_type']['start'] = self._io.pos()
            self.inst_type = self._io.read_u2be()
            self._debug['inst_type']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.inst_type
            if _on == 0:
                self.body = GloverLevel.CameoInst0(self._io, self, self._root)
            elif _on == 4:
                self.body = GloverLevel.CameoInst4(self._io, self, self._root)
            elif _on == 6:
                self.body = GloverLevel.CameoInst6(self._io, self, self._root)
            elif _on == 1:
                self.body = GloverLevel.CameoInst1(self._io, self, self._root)
            elif _on == 3:
                self.body = GloverLevel.CameoInst3(self._io, self, self._root)
            elif _on == 5:
                self.body = GloverLevel.CameoInst5(self._io, self, self._root)
            elif _on == 2:
                self.body = GloverLevel.CameoInst2(self._io, self, self._root)
            else:
                self.body = GloverLevel.CameoInstDefault(self._io, self, self._root)
            self._debug['body']['end'] = self._io.pos()


    class PlatMvspn0x5a(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x1c", "u32_0x18"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x1c']['start'] = self._io.pos()
            self.u16_0x1c = self._io.read_u2be()
            self._debug['u16_0x1c']['end'] = self._io.pos()
            self._debug['u32_0x18']['start'] = self._io.pos()
            self.u32_0x18 = self._io.read_u4be()
            self._debug['u32_0x18']['end'] = self._io.pos()


    class PlatMvspn0x74(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x34", "u32_0x38", "u32_0x3c"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x34']['start'] = self._io.pos()
            self.u32_0x34 = self._io.read_u4be()
            self._debug['u32_0x34']['end'] = self._io.pos()
            self._debug['u32_0x38']['start'] = self._io.pos()
            self.u32_0x38 = self._io.read_u4be()
            self._debug['u32_0x38']['end'] = self._io.pos()
            self._debug['u32_0x3c']['start'] = self._io.pos()
            self.u32_0x3c = self._io.read_u4be()
            self._debug['u32_0x3c']['end'] = self._io.pos()


    class PlatOrbit(KaitaiStruct):
        SEQ_FIELDS = ["u16_120", "u16_136", "u16_134", "u16_132", "u32_116", "name", "f_112", "f_108", "f_104", "f_100", "f_96", "f_92", "f_88", "f_84", "f_80", "u32_176"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_120']['start'] = self._io.pos()
            self.u16_120 = self._io.read_u2be()
            self._debug['u16_120']['end'] = self._io.pos()
            self._debug['u16_136']['start'] = self._io.pos()
            self.u16_136 = self._io.read_u2be()
            self._debug['u16_136']['end'] = self._io.pos()
            self._debug['u16_134']['start'] = self._io.pos()
            self.u16_134 = self._io.read_u2be()
            self._debug['u16_134']['end'] = self._io.pos()
            self._debug['u16_132']['start'] = self._io.pos()
            self.u16_132 = self._io.read_u2be()
            self._debug['u16_132']['end'] = self._io.pos()
            self._debug['u32_116']['start'] = self._io.pos()
            self.u32_116 = self._io.read_u4be()
            self._debug['u32_116']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(8)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['f_112']['start'] = self._io.pos()
            self.f_112 = self._io.read_f4be()
            self._debug['f_112']['end'] = self._io.pos()
            self._debug['f_108']['start'] = self._io.pos()
            self.f_108 = self._io.read_f4be()
            self._debug['f_108']['end'] = self._io.pos()
            self._debug['f_104']['start'] = self._io.pos()
            self.f_104 = self._io.read_f4be()
            self._debug['f_104']['end'] = self._io.pos()
            self._debug['f_100']['start'] = self._io.pos()
            self.f_100 = self._io.read_f4be()
            self._debug['f_100']['end'] = self._io.pos()
            self._debug['f_96']['start'] = self._io.pos()
            self.f_96 = self._io.read_f4be()
            self._debug['f_96']['end'] = self._io.pos()
            self._debug['f_92']['start'] = self._io.pos()
            self.f_92 = self._io.read_f4be()
            self._debug['f_92']['end'] = self._io.pos()
            self._debug['f_88']['start'] = self._io.pos()
            self.f_88 = self._io.read_f4be()
            self._debug['f_88']['end'] = self._io.pos()
            self._debug['f_84']['start'] = self._io.pos()
            self.f_84 = self._io.read_f4be()
            self._debug['f_84']['end'] = self._io.pos()
            self._debug['f_80']['start'] = self._io.pos()
            self.f_80 = self._io.read_f4be()
            self._debug['f_80']['end'] = self._io.pos()
            self._debug['u32_176']['start'] = self._io.pos()
            self.u32_176 = self._io.read_u4be()
            self._debug['u32_176']['end'] = self._io.pos()


    class PlatSpike(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class PlatSpecial0x8e(KaitaiStruct):
        SEQ_FIELDS = ["enable"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['enable']['start'] = self._io.pos()
            self.enable = self._io.read_u2be()
            self._debug['enable']['end'] = self._io.pos()


    class Plat0x9f(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x6c", "u32_0x70", "u32_0x1c", "u32_0x28"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x6c']['start'] = self._io.pos()
            self.u32_0x6c = self._io.read_u4be()
            self._debug['u32_0x6c']['end'] = self._io.pos()
            self._debug['u32_0x70']['start'] = self._io.pos()
            self.u32_0x70 = self._io.read_u4be()
            self._debug['u32_0x70']['end'] = self._io.pos()
            self._debug['u32_0x1c']['start'] = self._io.pos()
            self.u32_0x1c = self._io.read_u4be()
            self._debug['u32_0x1c']['end'] = self._io.pos()
            self._debug['u32_0x28']['start'] = self._io.pos()
            self.u32_0x28 = self._io.read_u4be()
            self._debug['u32_0x28']['end'] = self._io.pos()


    class EnvironmentalSound(KaitaiStruct):
        SEQ_FIELDS = ["sound_id", "volume", "flags", "h_0x06", "h_0x08", "h_0x0a", "h_0x0c", "h_0x0e", "x", "y", "z", "radius"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['sound_id']['start'] = self._io.pos()
            self.sound_id = self._io.read_u2be()
            self._debug['sound_id']['end'] = self._io.pos()
            self._debug['volume']['start'] = self._io.pos()
            self.volume = self._io.read_u2be()
            self._debug['volume']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u2be()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['h_0x06']['start'] = self._io.pos()
            self.h_0x06 = self._io.read_u2be()
            self._debug['h_0x06']['end'] = self._io.pos()
            self._debug['h_0x08']['start'] = self._io.pos()
            self.h_0x08 = self._io.read_u2be()
            self._debug['h_0x08']['end'] = self._io.pos()
            self._debug['h_0x0a']['start'] = self._io.pos()
            self.h_0x0a = self._io.read_u2be()
            self._debug['h_0x0a']['end'] = self._io.pos()
            self._debug['h_0x0c']['start'] = self._io.pos()
            self.h_0x0c = self._io.read_u2be()
            self._debug['h_0x0c']['end'] = self._io.pos()
            self._debug['h_0x0e']['start'] = self._io.pos()
            self.h_0x0e = self._io.read_u2be()
            self._debug['h_0x0e']['end'] = self._io.pos()
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f4be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()
            self._debug['radius']['start'] = self._io.pos()
            self.radius = self._io.read_f4be()
            self._debug['radius']['end'] = self._io.pos()


    class EnemyInstructionB(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x02", "u32_0x06", "u32_0x0a", "u32_0x08", "u32_0x0c", "u32_0x10", "u32_0x0e", "u32_0x18", "u32_0x1e", "u32_0x14", "u32_0x16"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x02']['start'] = self._io.pos()
            self.u32_0x02 = self._io.read_u4be()
            self._debug['u32_0x02']['end'] = self._io.pos()
            self._debug['u32_0x06']['start'] = self._io.pos()
            self.u32_0x06 = self._io.read_u4be()
            self._debug['u32_0x06']['end'] = self._io.pos()
            self._debug['u32_0x0a']['start'] = self._io.pos()
            self.u32_0x0a = self._io.read_u4be()
            self._debug['u32_0x0a']['end'] = self._io.pos()
            self._debug['u32_0x08']['start'] = self._io.pos()
            self.u32_0x08 = self._io.read_u4be()
            self._debug['u32_0x08']['end'] = self._io.pos()
            self._debug['u32_0x0c']['start'] = self._io.pos()
            self.u32_0x0c = self._io.read_u4be()
            self._debug['u32_0x0c']['end'] = self._io.pos()
            self._debug['u32_0x10']['start'] = self._io.pos()
            self.u32_0x10 = self._io.read_u4be()
            self._debug['u32_0x10']['end'] = self._io.pos()
            self._debug['u32_0x0e']['start'] = self._io.pos()
            self.u32_0x0e = self._io.read_u4be()
            self._debug['u32_0x0e']['end'] = self._io.pos()
            self._debug['u32_0x18']['start'] = self._io.pos()
            self.u32_0x18 = self._io.read_u4be()
            self._debug['u32_0x18']['end'] = self._io.pos()
            self._debug['u32_0x1e']['start'] = self._io.pos()
            self.u32_0x1e = self._io.read_u4be()
            self._debug['u32_0x1e']['end'] = self._io.pos()
            self._debug['u32_0x14']['start'] = self._io.pos()
            self.u32_0x14 = self._io.read_u4be()
            self._debug['u32_0x14']['end'] = self._io.pos()
            self._debug['u32_0x16']['start'] = self._io.pos()
            self.u32_0x16 = self._io.read_u2be()
            self._debug['u32_0x16']['end'] = self._io.pos()


    class PlatPathSpeed(KaitaiStruct):
        SEQ_FIELDS = ["speed"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['speed']['start'] = self._io.pos()
            self.speed = self._io.read_f4be()
            self._debug['speed']['end'] = self._io.pos()


    class PlatMaxVelocity(KaitaiStruct):
        SEQ_FIELDS = ["velocity"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['velocity']['start'] = self._io.pos()
            self.velocity = self._io.read_f4be()
            self._debug['velocity']['end'] = self._io.pos()


    class PlatMvspn0x59(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x24", "u32_0x20", "u32_0x28", "u32_0x2c", "u32_0x30"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x24']['start'] = self._io.pos()
            self.u16_0x24 = self._io.read_u2be()
            self._debug['u16_0x24']['end'] = self._io.pos()
            self._debug['u32_0x20']['start'] = self._io.pos()
            self.u32_0x20 = self._io.read_u4be()
            self._debug['u32_0x20']['end'] = self._io.pos()
            self._debug['u32_0x28']['start'] = self._io.pos()
            self.u32_0x28 = self._io.read_u4be()
            self._debug['u32_0x28']['end'] = self._io.pos()
            self._debug['u32_0x2c']['start'] = self._io.pos()
            self.u32_0x2c = self._io.read_u4be()
            self._debug['u32_0x2c']['end'] = self._io.pos()
            self._debug['u32_0x30']['start'] = self._io.pos()
            self.u32_0x30 = self._io.read_u4be()
            self._debug['u32_0x30']['end'] = self._io.pos()


    class Cameo(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class PlatSpinFlip0x7d(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x0a", "u32_0x14"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x0a']['start'] = self._io.pos()
            self.u16_0x0a = self._io.read_u2be()
            self._debug['u16_0x0a']['end'] = self._io.pos()
            self._debug['u32_0x14']['start'] = self._io.pos()
            self.u32_0x14 = self._io.read_u4be()
            self._debug['u32_0x14']['end'] = self._io.pos()


    class PlatRest0x63(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x17", "theta"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x17']['start'] = self._io.pos()
            self.u16_0x17 = self._io.read_u2be()
            self._debug['u16_0x17']['end'] = self._io.pos()
            self._debug['theta']['start'] = self._io.pos()
            self.theta = self._io.read_f4be()
            self._debug['theta']['end'] = self._io.pos()


    class Plat0xc3(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x86", "u32_0x78_0x80", "u16_0x84"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x86']['start'] = self._io.pos()
            self.u16_0x86 = self._io.read_u2be()
            self._debug['u16_0x86']['end'] = self._io.pos()
            self._debug['u32_0x78_0x80']['start'] = self._io.pos()
            self.u32_0x78_0x80 = self._io.read_u2be()
            self._debug['u32_0x78_0x80']['end'] = self._io.pos()
            self._debug['u16_0x84']['start'] = self._io.pos()
            self.u16_0x84 = self._io.read_u2be()
            self._debug['u16_0x84']['end'] = self._io.pos()


    class EndLevelData(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class PlatFan0x8a(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x0c", "u32_0x48", "u32_0x4c", "u32_0x50", "u32_0x10", "u32_0x14", "u32_0x18", "u32_0x1c"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x0c']['start'] = self._io.pos()
            self.u16_0x0c = self._io.read_u2be()
            self._debug['u16_0x0c']['end'] = self._io.pos()
            self._debug['u32_0x48']['start'] = self._io.pos()
            self.u32_0x48 = self._io.read_u4be()
            self._debug['u32_0x48']['end'] = self._io.pos()
            self._debug['u32_0x4c']['start'] = self._io.pos()
            self.u32_0x4c = self._io.read_u4be()
            self._debug['u32_0x4c']['end'] = self._io.pos()
            self._debug['u32_0x50']['start'] = self._io.pos()
            self.u32_0x50 = self._io.read_u4be()
            self._debug['u32_0x50']['end'] = self._io.pos()
            self._debug['u32_0x10']['start'] = self._io.pos()
            self.u32_0x10 = self._io.read_u4be()
            self._debug['u32_0x10']['end'] = self._io.pos()
            self._debug['u32_0x14']['start'] = self._io.pos()
            self.u32_0x14 = self._io.read_u4be()
            self._debug['u32_0x14']['end'] = self._io.pos()
            self._debug['u32_0x18']['start'] = self._io.pos()
            self.u32_0x18 = self._io.read_u4be()
            self._debug['u32_0x18']['end'] = self._io.pos()
            self._debug['u32_0x1c']['start'] = self._io.pos()
            self.u32_0x1c = self._io.read_u4be()
            self._debug['u32_0x1c']['end'] = self._io.pos()


    class PlatSpinBlur0x70(KaitaiStruct):
        SEQ_FIELDS = ["idx", "u32_0x38", "u32_0x18", "f_blur_0x578", "count"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['idx']['start'] = self._io.pos()
            self.idx = self._io.read_u2be()
            self._debug['idx']['end'] = self._io.pos()
            self._debug['u32_0x38']['start'] = self._io.pos()
            self.u32_0x38 = self._io.read_u4be()
            self._debug['u32_0x38']['end'] = self._io.pos()
            self._debug['u32_0x18']['start'] = self._io.pos()
            self.u32_0x18 = self._io.read_u4be()
            self._debug['u32_0x18']['end'] = self._io.pos()
            self._debug['f_blur_0x578']['start'] = self._io.pos()
            self.f_blur_0x578 = self._io.read_f4be()
            self._debug['f_blur_0x578']['end'] = self._io.pos()
            self._debug['count']['start'] = self._io.pos()
            self.count = self._io.read_u2be()
            self._debug['count']['end'] = self._io.pos()


    class PlatSpinSound0xc5(KaitaiStruct):
        SEQ_FIELDS = ["sound_id", "volume", "pitch"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['sound_id']['start'] = self._io.pos()
            self.sound_id = self._io.read_u2be()
            self._debug['sound_id']['end'] = self._io.pos()
            self._debug['volume']['start'] = self._io.pos()
            self.volume = self._io.read_u2be()
            self._debug['volume']['end'] = self._io.pos()
            self._debug['pitch']['start'] = self._io.pos()
            self.pitch = self._io.read_u2be()
            self._debug['pitch']['end'] = self._io.pos()


    class PuzzleCondC(KaitaiStruct):
        SEQ_FIELDS = ["i_0x00", "i_0x04", "i_0x08", "i_0x0c", "i_0x10", "i_0x14"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['i_0x00']['start'] = self._io.pos()
            self.i_0x00 = self._io.read_u4be()
            self._debug['i_0x00']['end'] = self._io.pos()
            self._debug['i_0x04']['start'] = self._io.pos()
            self.i_0x04 = self._io.read_u4be()
            self._debug['i_0x04']['end'] = self._io.pos()
            self._debug['i_0x08']['start'] = self._io.pos()
            self.i_0x08 = self._io.read_u4be()
            self._debug['i_0x08']['end'] = self._io.pos()
            self._debug['i_0x0c']['start'] = self._io.pos()
            self.i_0x0c = self._io.read_u4be()
            self._debug['i_0x0c']['end'] = self._io.pos()
            self._debug['i_0x10']['start'] = self._io.pos()
            self.i_0x10 = self._io.read_u4be()
            self._debug['i_0x10']['end'] = self._io.pos()
            self._debug['i_0x14']['start'] = self._io.pos()
            self.i_0x14 = self._io.read_u4be()
            self._debug['i_0x14']['end'] = self._io.pos()


    class PlatSpin0x7f(KaitaiStruct):
        SEQ_FIELDS = ["axis", "initial_theta", "speed"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['axis']['start'] = self._io.pos()
            self.axis = self._io.read_u2be()
            self._debug['axis']['end'] = self._io.pos()
            self._debug['initial_theta']['start'] = self._io.pos()
            self.initial_theta = self._io.read_f4be()
            self._debug['initial_theta']['end'] = self._io.pos()
            self._debug['speed']['start'] = self._io.pos()
            self.speed = self._io.read_f4be()
            self._debug['speed']['end'] = self._io.pos()


    class PuzzleAction0x4a(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x24", "u32_0x24_0x0c", "u16_0x0a"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x24']['start'] = self._io.pos()
            self.u32_0x24 = self._io.read_u4be()
            self._debug['u32_0x24']['end'] = self._io.pos()
            self._debug['u32_0x24_0x0c']['start'] = self._io.pos()
            self.u32_0x24_0x0c = self._io.read_u4be()
            self._debug['u32_0x24_0x0c']['end'] = self._io.pos()
            self._debug['u16_0x0a']['start'] = self._io.pos()
            self.u16_0x0a = self._io.read_u2be()
            self._debug['u16_0x0a']['end'] = self._io.pos()


    class EnemyConditionalInstruction(KaitaiStruct):
        SEQ_FIELDS = ["instr"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['instr']['start'] = self._io.pos()
            self.instr = GloverLevel.EnemyInstruction(self._io, self, self._root)
            self._debug['instr']['end'] = self._io.pos()


    class Enemy0xa1(KaitaiStruct):
        SEQ_FIELDS = ["u32_1", "u32_2", "u32_3", "u32_4", "u32_5", "u32_6"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_1']['start'] = self._io.pos()
            self.u32_1 = self._io.read_u4be()
            self._debug['u32_1']['end'] = self._io.pos()
            self._debug['u32_2']['start'] = self._io.pos()
            self.u32_2 = self._io.read_u4be()
            self._debug['u32_2']['end'] = self._io.pos()
            self._debug['u32_3']['start'] = self._io.pos()
            self.u32_3 = self._io.read_u4be()
            self._debug['u32_3']['end'] = self._io.pos()
            self._debug['u32_4']['start'] = self._io.pos()
            self.u32_4 = self._io.read_u4be()
            self._debug['u32_4']['end'] = self._io.pos()
            self._debug['u32_5']['start'] = self._io.pos()
            self.u32_5 = self._io.read_u4be()
            self._debug['u32_5']['end'] = self._io.pos()
            self._debug['u32_6']['start'] = self._io.pos()
            self.u32_6 = self._io.read_u4be()
            self._debug['u32_6']['end'] = self._io.pos()


    class Vent(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x08", "u16_0x0a", "tag", "f_0x38", "f_0x3c", "f_0x40", "f_0x2c", "f_0x30", "f_0x34"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x08']['start'] = self._io.pos()
            self.u16_0x08 = self._io.read_u2be()
            self._debug['u16_0x08']['end'] = self._io.pos()
            self._debug['u16_0x0a']['start'] = self._io.pos()
            self.u16_0x0a = self._io.read_u2be()
            self._debug['u16_0x0a']['end'] = self._io.pos()
            self._debug['tag']['start'] = self._io.pos()
            self.tag = self._io.read_u2be()
            self._debug['tag']['end'] = self._io.pos()
            self._debug['f_0x38']['start'] = self._io.pos()
            self.f_0x38 = self._io.read_f4be()
            self._debug['f_0x38']['end'] = self._io.pos()
            self._debug['f_0x3c']['start'] = self._io.pos()
            self.f_0x3c = self._io.read_f4be()
            self._debug['f_0x3c']['end'] = self._io.pos()
            self._debug['f_0x40']['start'] = self._io.pos()
            self.f_0x40 = self._io.read_f4be()
            self._debug['f_0x40']['end'] = self._io.pos()
            self._debug['f_0x2c']['start'] = self._io.pos()
            self.f_0x2c = self._io.read_f4be()
            self._debug['f_0x2c']['end'] = self._io.pos()
            self._debug['f_0x30']['start'] = self._io.pos()
            self.f_0x30 = self._io.read_f4be()
            self._debug['f_0x30']['end'] = self._io.pos()
            self._debug['f_0x34']['start'] = self._io.pos()
            self.f_0x34 = self._io.read_f4be()
            self._debug['f_0x34']['end'] = self._io.pos()


    class PuzzleCond(KaitaiStruct):
        SEQ_FIELDS = ["cond_type", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['cond_type']['start'] = self._io.pos()
            self.cond_type = self._io.read_u2be()
            self._debug['cond_type']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.cond_type
            if _on == 39:
                self.body = GloverLevel.PuzzleCondC(self._io, self, self._root)
            elif _on == 35:
                self.body = GloverLevel.PuzzleCondC(self._io, self, self._root)
            elif _on == 38:
                self.body = GloverLevel.PuzzleCondD(self._io, self, self._root)
            elif _on == 40:
                self.body = GloverLevel.PuzzleCondD(self._io, self, self._root)
            elif _on == 37:
                self.body = GloverLevel.PuzzleCondC(self._io, self, self._root)
            elif _on == 41:
                self.body = GloverLevel.PuzzleCondE(self._io, self, self._root)
            elif _on == 36:
                self.body = GloverLevel.PuzzleCondD(self._io, self, self._root)
            elif _on == 34:
                self.body = GloverLevel.PuzzleCondB(self._io, self, self._root)
            else:
                self.body = GloverLevel.PuzzleCondA(self._io, self, self._root)
            self._debug['body']['end'] = self._io.pos()


    class PlatMvspn0x73(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x0c", "u32_0x34", "u32_0x38", "u32_0x3c"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x0c']['start'] = self._io.pos()
            self.u16_0x0c = self._io.read_u2be()
            self._debug['u16_0x0c']['end'] = self._io.pos()
            self._debug['u32_0x34']['start'] = self._io.pos()
            self.u32_0x34 = self._io.read_u4be()
            self._debug['u32_0x34']['end'] = self._io.pos()
            self._debug['u32_0x38']['start'] = self._io.pos()
            self.u32_0x38 = self._io.read_u4be()
            self._debug['u32_0x38']['end'] = self._io.pos()
            self._debug['u32_0x3c']['start'] = self._io.pos()
            self.u32_0x3c = self._io.read_u4be()
            self._debug['u32_0x3c']['end'] = self._io.pos()


    class LookAtBall0x61(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x6c", "u32_0x1c"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x6c']['start'] = self._io.pos()
            self.u32_0x6c = self._io.read_u4be()
            self._debug['u32_0x6c']['end'] = self._io.pos()
            self._debug['u32_0x1c']['start'] = self._io.pos()
            self.u32_0x1c = self._io.read_u4be()
            self._debug['u32_0x1c']['end'] = self._io.pos()


    class LookAtHand0x60(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x6c", "u32_0x1c"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x6c']['start'] = self._io.pos()
            self.u32_0x6c = self._io.read_u4be()
            self._debug['u32_0x6c']['end'] = self._io.pos()
            self._debug['u32_0x1c']['start'] = self._io.pos()
            self.u32_0x1c = self._io.read_u4be()
            self._debug['u32_0x1c']['end'] = self._io.pos()


    class CameoInst2(KaitaiStruct):
        SEQ_FIELDS = ["h_0x00", "i_0x02", "i_0x06", "i_0x0a", "i_0x0e", "h_0x12", "h_0x14"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['h_0x00']['start'] = self._io.pos()
            self.h_0x00 = self._io.read_u2be()
            self._debug['h_0x00']['end'] = self._io.pos()
            self._debug['i_0x02']['start'] = self._io.pos()
            self.i_0x02 = self._io.read_u4be()
            self._debug['i_0x02']['end'] = self._io.pos()
            self._debug['i_0x06']['start'] = self._io.pos()
            self.i_0x06 = self._io.read_u4be()
            self._debug['i_0x06']['end'] = self._io.pos()
            self._debug['i_0x0a']['start'] = self._io.pos()
            self.i_0x0a = self._io.read_u4be()
            self._debug['i_0x0a']['end'] = self._io.pos()
            self._debug['i_0x0e']['start'] = self._io.pos()
            self.i_0x0e = self._io.read_u4be()
            self._debug['i_0x0e']['end'] = self._io.pos()
            self._debug['h_0x12']['start'] = self._io.pos()
            self.h_0x12 = self._io.read_u2be()
            self._debug['h_0x12']['end'] = self._io.pos()
            self._debug['h_0x14']['start'] = self._io.pos()
            self.h_0x14 = self._io.read_u2be()
            self._debug['h_0x14']['end'] = self._io.pos()


    class Unknown0xa9(KaitaiStruct):
        SEQ_FIELDS = ["i_0x00"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['i_0x00']['start'] = self._io.pos()
            self.i_0x00 = self._io.read_u4be()
            self._debug['i_0x00']['end'] = self._io.pos()


    class PlatVentAdvanceFrames(KaitaiStruct):
        SEQ_FIELDS = ["num_frames"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_frames']['start'] = self._io.pos()
            self.num_frames = self._io.read_u2be()
            self._debug['num_frames']['end'] = self._io.pos()


    class SetExit(KaitaiStruct):
        SEQ_FIELDS = ["behavior_u16_0x40", "visible"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['behavior_u16_0x40']['start'] = self._io.pos()
            self.behavior_u16_0x40 = self._io.read_u2be()
            self._debug['behavior_u16_0x40']['end'] = self._io.pos()
            self._debug['visible']['start'] = self._io.pos()
            self.visible = self._io.read_u2be()
            self._debug['visible']['end'] = self._io.pos()


    class PlatOrbit0x75(KaitaiStruct):
        SEQ_FIELDS = ["idx", "u32_0x18", "u32_0x1c", "u32_0x20", "u32_0x28"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['idx']['start'] = self._io.pos()
            self.idx = self._io.read_u2be()
            self._debug['idx']['end'] = self._io.pos()
            self._debug['u32_0x18']['start'] = self._io.pos()
            self.u32_0x18 = self._io.read_u4be()
            self._debug['u32_0x18']['end'] = self._io.pos()
            self._debug['u32_0x1c']['start'] = self._io.pos()
            self.u32_0x1c = self._io.read_u4be()
            self._debug['u32_0x1c']['end'] = self._io.pos()
            self._debug['u32_0x20']['start'] = self._io.pos()
            self.u32_0x20 = self._io.read_u4be()
            self._debug['u32_0x20']['end'] = self._io.pos()
            self._debug['u32_0x28']['start'] = self._io.pos()
            self.u32_0x28 = self._io.read_u4be()
            self._debug['u32_0x28']['end'] = self._io.pos()


    class PlatSound0xc1(KaitaiStruct):
        SEQ_FIELDS = ["sound_id", "volume", "pitch"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['sound_id']['start'] = self._io.pos()
            self.sound_id = self._io.read_u2be()
            self._debug['sound_id']['end'] = self._io.pos()
            self._debug['volume']['start'] = self._io.pos()
            self.volume = self._io.read_u2be()
            self._debug['volume']['end'] = self._io.pos()
            self._debug['pitch']['start'] = self._io.pos()
            self.pitch = self._io.read_u2be()
            self._debug['pitch']['end'] = self._io.pos()


    class EnemyInstructionC(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x02", "u32_0x0e", "u32_0x18", "u32_0x1e", "u32_0x14", "u32_0x16"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x02']['start'] = self._io.pos()
            self.u32_0x02 = self._io.read_u4be()
            self._debug['u32_0x02']['end'] = self._io.pos()
            self._debug['u32_0x0e']['start'] = self._io.pos()
            self.u32_0x0e = self._io.read_u4be()
            self._debug['u32_0x0e']['end'] = self._io.pos()
            self._debug['u32_0x18']['start'] = self._io.pos()
            self.u32_0x18 = self._io.read_u4be()
            self._debug['u32_0x18']['end'] = self._io.pos()
            self._debug['u32_0x1e']['start'] = self._io.pos()
            self.u32_0x1e = self._io.read_u4be()
            self._debug['u32_0x1e']['end'] = self._io.pos()
            self._debug['u32_0x14']['start'] = self._io.pos()
            self.u32_0x14 = self._io.read_u4be()
            self._debug['u32_0x14']['end'] = self._io.pos()
            self._debug['u32_0x16']['start'] = self._io.pos()
            self.u32_0x16 = self._io.read_u2be()
            self._debug['u32_0x16']['end'] = self._io.pos()


    class PuzzleAnd(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class Plat0x66(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class PlatPos0xa6(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f4be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()


    class PlatSpecial0xc7(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x2a", "u16_0x1c_and_0x24", "u16_0x28"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x2a']['start'] = self._io.pos()
            self.u16_0x2a = self._io.read_u2be()
            self._debug['u16_0x2a']['end'] = self._io.pos()
            self._debug['u16_0x1c_and_0x24']['start'] = self._io.pos()
            self.u16_0x1c_and_0x24 = self._io.read_u2be()
            self._debug['u16_0x1c_and_0x24']['end'] = self._io.pos()
            self._debug['u16_0x28']['start'] = self._io.pos()
            self.u16_0x28 = self._io.read_u2be()
            self._debug['u16_0x28']['end'] = self._io.pos()


    class Powerup(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x00", "u16_0x02", "u16_0x04", "f_0x06", "f_0x0a", "f_0x0e"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x00']['start'] = self._io.pos()
            self.u16_0x00 = self._io.read_u2be()
            self._debug['u16_0x00']['end'] = self._io.pos()
            self._debug['u16_0x02']['start'] = self._io.pos()
            self.u16_0x02 = self._io.read_u2be()
            self._debug['u16_0x02']['end'] = self._io.pos()
            self._debug['u16_0x04']['start'] = self._io.pos()
            self.u16_0x04 = self._io.read_u2be()
            self._debug['u16_0x04']['end'] = self._io.pos()
            self._debug['f_0x06']['start'] = self._io.pos()
            self.f_0x06 = self._io.read_f4be()
            self._debug['f_0x06']['end'] = self._io.pos()
            self._debug['f_0x0a']['start'] = self._io.pos()
            self.f_0x0a = self._io.read_f4be()
            self._debug['f_0x0a']['end'] = self._io.pos()
            self._debug['f_0x0e']['start'] = self._io.pos()
            self.f_0x0e = self._io.read_f4be()
            self._debug['f_0x0e']['end'] = self._io.pos()


    class SetTeleport(KaitaiStruct):
        SEQ_FIELDS = ["target_tag", "u16_0x0c", "u16_0x10", "u16_0x12", "u32_0x00", "u32_0x04", "u32_0x08"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['target_tag']['start'] = self._io.pos()
            self.target_tag = self._io.read_u2be()
            self._debug['target_tag']['end'] = self._io.pos()
            self._debug['u16_0x0c']['start'] = self._io.pos()
            self.u16_0x0c = self._io.read_u2be()
            self._debug['u16_0x0c']['end'] = self._io.pos()
            self._debug['u16_0x10']['start'] = self._io.pos()
            self.u16_0x10 = self._io.read_u2be()
            self._debug['u16_0x10']['end'] = self._io.pos()
            self._debug['u16_0x12']['start'] = self._io.pos()
            self.u16_0x12 = self._io.read_u2be()
            self._debug['u16_0x12']['end'] = self._io.pos()
            self._debug['u32_0x00']['start'] = self._io.pos()
            self.u32_0x00 = self._io.read_u4be()
            self._debug['u32_0x00']['end'] = self._io.pos()
            self._debug['u32_0x04']['start'] = self._io.pos()
            self.u32_0x04 = self._io.read_u4be()
            self._debug['u32_0x04']['end'] = self._io.pos()
            self._debug['u32_0x08']['start'] = self._io.pos()
            self.u32_0x08 = self._io.read_u4be()
            self._debug['u32_0x08']['end'] = self._io.pos()


    class PuzzleCondD(KaitaiStruct):
        SEQ_FIELDS = ["i_0x00", "i_0x04", "i_0x08", "i_0x0c"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['i_0x00']['start'] = self._io.pos()
            self.i_0x00 = self._io.read_u4be()
            self._debug['i_0x00']['end'] = self._io.pos()
            self._debug['i_0x04']['start'] = self._io.pos()
            self.i_0x04 = self._io.read_u4be()
            self._debug['i_0x04']['end'] = self._io.pos()
            self._debug['i_0x08']['start'] = self._io.pos()
            self.i_0x08 = self._io.read_u4be()
            self._debug['i_0x08']['end'] = self._io.pos()
            self._debug['i_0x0c']['start'] = self._io.pos()
            self.i_0x0c = self._io.read_u4be()
            self._debug['i_0x0c']['end'] = self._io.pos()


    class VentAppend0xa3(KaitaiStruct):
        SEQ_FIELDS = ["u16_idx_plus_0x10", "u16_idx_plus_0x1c"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_idx_plus_0x10']['start'] = self._io.pos()
            self.u16_idx_plus_0x10 = self._io.read_u2be()
            self._debug['u16_idx_plus_0x10']['end'] = self._io.pos()
            self._debug['u16_idx_plus_0x1c']['start'] = self._io.pos()
            self.u16_idx_plus_0x1c = self._io.read_u2be()
            self._debug['u16_idx_plus_0x1c']['end'] = self._io.pos()


    class UnknownSound0xbd(KaitaiStruct):
        SEQ_FIELDS = ["h_0x00", "h_0x02", "h_0x04"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['h_0x00']['start'] = self._io.pos()
            self.h_0x00 = self._io.read_u2be()
            self._debug['h_0x00']['end'] = self._io.pos()
            self._debug['h_0x02']['start'] = self._io.pos()
            self.h_0x02 = self._io.read_u2be()
            self._debug['h_0x02']['end'] = self._io.pos()
            self._debug['h_0x04']['start'] = self._io.pos()
            self.h_0x04 = self._io.read_u2be()
            self._debug['h_0x04']['end'] = self._io.pos()


    class Plat0x5d(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class PlatCheckpoint(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class CameoInst4(KaitaiStruct):
        SEQ_FIELDS = ["h_0x00", "h_0x02", "h_0x04", "h_0x06", "h_0x08"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['h_0x00']['start'] = self._io.pos()
            self.h_0x00 = self._io.read_u2be()
            self._debug['h_0x00']['end'] = self._io.pos()
            self._debug['h_0x02']['start'] = self._io.pos()
            self.h_0x02 = self._io.read_u2be()
            self._debug['h_0x02']['end'] = self._io.pos()
            self._debug['h_0x04']['start'] = self._io.pos()
            self.h_0x04 = self._io.read_u2be()
            self._debug['h_0x04']['end'] = self._io.pos()
            self._debug['h_0x06']['start'] = self._io.pos()
            self.h_0x06 = self._io.read_u2be()
            self._debug['h_0x06']['end'] = self._io.pos()
            self._debug['h_0x08']['start'] = self._io.pos()
            self.h_0x08 = self._io.read_u2be()
            self._debug['h_0x08']['end'] = self._io.pos()


    class BallSpawnPoint(KaitaiStruct):
        SEQ_FIELDS = ["h_0x00", "x", "y", "z"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['h_0x00']['start'] = self._io.pos()
            self.h_0x00 = self._io.read_u2be()
            self._debug['h_0x00']['end'] = self._io.pos()
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f4be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()


    class Unknown0x01(KaitaiStruct):
        SEQ_FIELDS = ["f_0x00", "f_0x04", "f_0x08"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['f_0x00']['start'] = self._io.pos()
            self.f_0x00 = self._io.read_f4be()
            self._debug['f_0x00']['end'] = self._io.pos()
            self._debug['f_0x04']['start'] = self._io.pos()
            self.f_0x04 = self._io.read_f4be()
            self._debug['f_0x04']['end'] = self._io.pos()
            self._debug['f_0x08']['start'] = self._io.pos()
            self.f_0x08 = self._io.read_f4be()
            self._debug['f_0x08']['end'] = self._io.pos()


    class PlatAnim0xc0(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class PuzzleOr(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class PuzzleAction0x56(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x14", "u32_0x18", "u16_0x1c", "u16_0x0a"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x14']['start'] = self._io.pos()
            self.u32_0x14 = self._io.read_u4be()
            self._debug['u32_0x14']['end'] = self._io.pos()
            self._debug['u32_0x18']['start'] = self._io.pos()
            self.u32_0x18 = self._io.read_u4be()
            self._debug['u32_0x18']['end'] = self._io.pos()
            self._debug['u16_0x1c']['start'] = self._io.pos()
            self.u16_0x1c = self._io.read_u2be()
            self._debug['u16_0x1c']['end'] = self._io.pos()
            self._debug['u16_0x0a']['start'] = self._io.pos()
            self.u16_0x0a = self._io.read_u2be()
            self._debug['u16_0x0a']['end'] = self._io.pos()


    class Cmd(KaitaiStruct):
        SEQ_FIELDS = ["type_code", "params"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type_code']['start'] = self._io.pos()
            self.type_code = self._io.read_u2be()
            self._debug['type_code']['end'] = self._io.pos()
            self._debug['params']['start'] = self._io.pos()
            _on = self.type_code
            if _on == 120:
                self.params = GloverLevel.Plat0x78(self._io, self, self._root)
            elif _on == 141:
                self.params = GloverLevel.PlatRope(self._io, self, self._root)
            elif _on == 93:
                self.params = GloverLevel.Plat0x5d(self._io, self, self._root)
            elif _on == 118:
                self.params = GloverLevel.PlatOrbitPause0x76(self._io, self, self._root)
            elif _on == 159:
                self.params = GloverLevel.Plat0x9f(self._io, self, self._root)
            elif _on == 194:
                self.params = GloverLevel.PlatSound0xc2(self._io, self, self._root)
            elif _on == 184:
                self.params = GloverLevel.PlatSpecial0xb8(self._io, self, self._root)
            elif _on == 105:
                self.params = GloverLevel.PlatCat0x69(self._io, self, self._root)
            elif _on == 142:
                self.params = GloverLevel.PlatSpecial0x8e(self._io, self, self._root)
            elif _on == 112:
                self.params = GloverLevel.PlatSpinBlur0x70(self._io, self, self._root)
            elif _on == 163:
                self.params = GloverLevel.VentAppend0xa3(self._io, self, self._root)
            elif _on == 131:
                self.params = GloverLevel.Enemy(self._io, self, self._root)
            elif _on == 167:
                self.params = GloverLevel.PlatPos0xa7(self._io, self, self._root)
            elif _on == 146:
                self.params = GloverLevel.LandActor(self._io, self, self._root)
            elif _on == 4:
                self.params = GloverLevel.Puzzle(self._io, self, self._root)
            elif _on == 169:
                self.params = GloverLevel.Unknown0xa9(self._io, self, self._root)
            elif _on == 162:
                self.params = GloverLevel.Vent(self._io, self, self._root)
            elif _on == 116:
                self.params = GloverLevel.PlatMvspn0x74(self._io, self, self._root)
            elif _on == 119:
                self.params = GloverLevel.PlatOrbitFlip0x77(self._io, self, self._root)
            elif _on == 6:
                self.params = GloverLevel.PuzzleOr(self._io, self, self._root)
            elif _on == 7:
                self.params = GloverLevel.PuzzleNumtimes(self._io, self, self._root)
            elif _on == 113:
                self.params = GloverLevel.PlatMvspnSetparent(self._io, self, self._root)
            elif _on == 121:
                self.params = GloverLevel.PlatScale(self._io, self, self._root)
            elif _on == 96:
                self.params = GloverLevel.LookAtHand0x60(self._io, self, self._root)
            elif _on == 191:
                self.params = GloverLevel.Unknown0xbf(self._io, self, self._root)
            elif _on == 1:
                self.params = GloverLevel.Unknown0x01(self._io, self, self._root)
            elif _on == 150:
                self.params = GloverLevel.PuzzleAction(self._io, self, self._root)
            elif _on == 97:
                self.params = GloverLevel.LookAtBall0x61(self._io, self, self._root)
            elif _on == 106:
                self.params = GloverLevel.PlatOrActor0x6a(self._io, self, self._root)
            elif _on == 145:
                self.params = GloverLevel.BackgroundActor0x91(self._io, self, self._root)
            elif _on == 101:
                self.params = GloverLevel.PlatDestructible(self._io, self, self._root)
            elif _on == 144:
                self.params = GloverLevel.PlatSine(self._io, self, self._root)
            elif _on == 127:
                self.params = GloverLevel.PlatSpin0x7f(self._io, self, self._root)
            elif _on == 100:
                self.params = GloverLevel.PlatCheckpoint(self._io, self, self._root)
            elif _on == 149:
                self.params = GloverLevel.PuzzleCond(self._io, self, self._root)
            elif _on == 115:
                self.params = GloverLevel.PlatMvspn0x73(self._io, self, self._root)
            elif _on == 91:
                self.params = GloverLevel.PlatPush0x5b(self._io, self, self._root)
            elif _on == 107:
                self.params = GloverLevel.PlatPathPoint(self._io, self, self._root)
            elif _on == 143:
                self.params = GloverLevel.PlatOrbit(self._io, self, self._root)
            elif _on == 89:
                self.params = GloverLevel.PlatMvspn0x59(self._io, self, self._root)
            elif _on == 104:
                self.params = GloverLevel.PlatSpecial0x68(self._io, self, self._root)
            elif _on == 98:
                self.params = GloverLevel.Platform(self._io, self, self._root)
            elif _on == 197:
                self.params = GloverLevel.PlatSpinSound0xc5(self._io, self, self._root)
            elif _on == 95:
                self.params = GloverLevel.PlatGoForwards0x5f(self._io, self, self._root)
            elif _on == 137:
                self.params = GloverLevel.SetTeleport(self._io, self, self._root)
            elif _on == 88:
                self.params = GloverLevel.PlatMvspn0x58(self._io, self, self._root)
            elif _on == 161:
                self.params = GloverLevel.Enemy0xa1(self._io, self, self._root)
            elif _on == 138:
                self.params = GloverLevel.PlatFan0x8a(self._io, self, self._root)
            elif _on == 3:
                self.params = GloverLevel.Unknown0x03(self._io, self, self._root)
            elif _on == 192:
                self.params = GloverLevel.PlatAnim0xc0(self._io, self, self._root)
            elif _on == 126:
                self.params = GloverLevel.Plat0x7e(self._io, self, self._root)
            elif _on == 165:
                self.params = GloverLevel.FogConfiguration(self._io, self, self._root)
            elif _on == 5:
                self.params = GloverLevel.PuzzleAnd(self._io, self, self._root)
            elif _on == 103:
                self.params = GloverLevel.PlatCrumb0x67(self._io, self, self._root)
            elif _on == 99:
                self.params = GloverLevel.PlatRest0x63(self._io, self, self._root)
            elif _on == 185:
                self.params = GloverLevel.PlatSpecial0xb9(self._io, self, self._root)
            elif _on == 180:
                self.params = GloverLevel.PlatSpecial0xb4(self._io, self, self._root)
            elif _on == 156:
                self.params = GloverLevel.EnemyAttackInstruction(self._io, self, self._root)
            elif _on == 125:
                self.params = GloverLevel.PlatSpinFlip0x7d(self._io, self, self._root)
            elif _on == 186:
                self.params = GloverLevel.Enemy0xba(self._io, self, self._root)
            elif _on == 188:
                self.params = GloverLevel.BackgroundActor0xbc(self._io, self, self._root)
            elif _on == 153:
                self.params = GloverLevel.Backdrop(self._io, self, self._root)
            elif _on == 123:
                self.params = GloverLevel.PlatSpin0x7b(self._io, self, self._root)
            elif _on == 160:
                self.params = GloverLevel.Water(self._io, self, self._root)
            elif _on == 8:
                self.params = GloverLevel.PuzzleAny(self._io, self, self._root)
            elif _on == 166:
                self.params = GloverLevel.PlatPos0xa6(self._io, self, self._root)
            elif _on == 114:
                self.params = GloverLevel.PlatConf0x72(self._io, self, self._root)
            elif _on == 181:
                self.params = GloverLevel.Buzzer(self._io, self, self._root)
            elif _on == 148:
                self.params = GloverLevel.SetActorScale(self._io, self, self._root)
            elif _on == 158:
                self.params = GloverLevel.PlatSpecial0x9e(self._io, self, self._root)
            elif _on == 117:
                self.params = GloverLevel.PlatOrbit0x75(self._io, self, self._root)
            elif _on == 152:
                self.params = GloverLevel.Unknown0x98(self._io, self, self._root)
            elif _on == 109:
                self.params = GloverLevel.PlatPathSpeed(self._io, self, self._root)
            elif _on == 32000:
                self.params = GloverLevel.EndLevelData(self._io, self, self._root)
            elif _on == 140:
                self.params = GloverLevel.Wind(self._io, self, self._root)
            elif _on == 122:
                self.params = GloverLevel.PlatStr0x7a(self._io, self, self._root)
            elif _on == 179:
                self.params = GloverLevel.Render0xb3(self._io, self, self._root)
            elif _on == 195:
                self.params = GloverLevel.Plat0xc3(self._io, self, self._root)
            elif _on == 130:
                self.params = GloverLevel.PlatSpike(self._io, self, self._root)
            elif _on == 187:
                self.params = GloverLevel.MrTip(self._io, self, self._root)
            elif _on == 170:
                self.params = GloverLevel.Cameo(self._io, self, self._root)
            elif _on == 199:
                self.params = GloverLevel.PlatSpecial0xc7(self._io, self, self._root)
            elif _on == 164:
                self.params = GloverLevel.Plat0xa4(self._io, self, self._root)
            elif _on == 182:
                self.params = GloverLevel.PlatSpecial0xb6(self._io, self, self._root)
            elif _on == 108:
                self.params = GloverLevel.PlatMaxVelocity(self._io, self, self._root)
            elif _on == 189:
                self.params = GloverLevel.UnknownSound0xbd(self._io, self, self._root)
            elif _on == 168:
                self.params = GloverLevel.SetExit(self._io, self, self._root)
            elif _on == 171:
                self.params = GloverLevel.CameoInst(self._io, self, self._root)
            elif _on == 193:
                self.params = GloverLevel.PlatSound0xc1(self._io, self, self._root)
            elif _on == 133:
                self.params = GloverLevel.GaribGroup(self._io, self, self._root)
            elif _on == 129:
                self.params = GloverLevel.PlatTopple0x81(self._io, self, self._root)
            elif _on == 151:
                self.params = GloverLevel.DiffuseLight(self._io, self, self._root)
            elif _on == 157:
                self.params = GloverLevel.Plat0x9d(self._io, self, self._root)
            elif _on == 147:
                self.params = GloverLevel.SetActorRotation(self._io, self, self._root)
            elif _on == 134:
                self.params = GloverLevel.Garib(self._io, self, self._root)
            elif _on == 102:
                self.params = GloverLevel.Plat0x66(self._io, self, self._root)
            elif _on == 110:
                self.params = GloverLevel.PlatSpecial0x6e(self._io, self, self._root)
            elif _on == 139:
                self.params = GloverLevel.PlatMagnet0x8b(self._io, self, self._root)
            elif _on == 155:
                self.params = GloverLevel.EnemyConditionalInstruction(self._io, self, self._root)
            elif _on == 2:
                self.params = GloverLevel.BallSpawnPoint(self._io, self, self._root)
            elif _on == 135:
                self.params = GloverLevel.Powerup(self._io, self, self._root)
            elif _on == 124:
                self.params = GloverLevel.PlatSpinPause0x7c(self._io, self, self._root)
            elif _on == 200:
                self.params = GloverLevel.PlatDestructibleSound(self._io, self, self._root)
            elif _on == 132:
                self.params = GloverLevel.Enemy0x84(self._io, self, self._root)
            elif _on == 92:
                self.params = GloverLevel.PlatVentAdvanceFrames(self._io, self, self._root)
            elif _on == 198:
                self.params = GloverLevel.Plat0xc6(self._io, self, self._root)
            elif _on == 111:
                self.params = GloverLevel.PlatPuzzle0x6f(self._io, self, self._root)
            elif _on == 190:
                self.params = GloverLevel.EnvironmentalSound(self._io, self, self._root)
            elif _on == 196:
                self.params = GloverLevel.Plat0xc4(self._io, self, self._root)
            elif _on == 183:
                self.params = GloverLevel.SetGlobal0xb7(self._io, self, self._root)
            elif _on == 128:
                self.params = GloverLevel.PlatSpin0x80(self._io, self, self._root)
            elif _on == 90:
                self.params = GloverLevel.PlatMvspn0x5a(self._io, self, self._root)
            elif _on == 154:
                self.params = GloverLevel.EnemyNormalInstruction(self._io, self, self._root)
            else:
                self.params = GloverLevel.Unrecognized(self._io, self, self._root)
            self._debug['params']['end'] = self._io.pos()


    class Plat0xc6(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x4a", "u16_0x44", "u16_0x48"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x4a']['start'] = self._io.pos()
            self.u16_0x4a = self._io.read_u2be()
            self._debug['u16_0x4a']['end'] = self._io.pos()
            self._debug['u16_0x44']['start'] = self._io.pos()
            self.u16_0x44 = self._io.read_u2be()
            self._debug['u16_0x44']['end'] = self._io.pos()
            self._debug['u16_0x48']['start'] = self._io.pos()
            self.u16_0x48 = self._io.read_u2be()
            self._debug['u16_0x48']['end'] = self._io.pos()


    class Wind(KaitaiStruct):
        SEQ_FIELDS = ["i_0x00", "i_0x04", "i_0x08", "i_0x0c", "i_0x10", "i_0x14", "i_0x18", "i_0x1c", "i_0x20", "i_0x28", "i_0x2c", "i_0x24", "i_0x30"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['i_0x00']['start'] = self._io.pos()
            self.i_0x00 = self._io.read_u4be()
            self._debug['i_0x00']['end'] = self._io.pos()
            self._debug['i_0x04']['start'] = self._io.pos()
            self.i_0x04 = self._io.read_u4be()
            self._debug['i_0x04']['end'] = self._io.pos()
            self._debug['i_0x08']['start'] = self._io.pos()
            self.i_0x08 = self._io.read_u4be()
            self._debug['i_0x08']['end'] = self._io.pos()
            self._debug['i_0x0c']['start'] = self._io.pos()
            self.i_0x0c = self._io.read_u4be()
            self._debug['i_0x0c']['end'] = self._io.pos()
            self._debug['i_0x10']['start'] = self._io.pos()
            self.i_0x10 = self._io.read_u4be()
            self._debug['i_0x10']['end'] = self._io.pos()
            self._debug['i_0x14']['start'] = self._io.pos()
            self.i_0x14 = self._io.read_u4be()
            self._debug['i_0x14']['end'] = self._io.pos()
            self._debug['i_0x18']['start'] = self._io.pos()
            self.i_0x18 = self._io.read_u4be()
            self._debug['i_0x18']['end'] = self._io.pos()
            self._debug['i_0x1c']['start'] = self._io.pos()
            self.i_0x1c = self._io.read_u4be()
            self._debug['i_0x1c']['end'] = self._io.pos()
            self._debug['i_0x20']['start'] = self._io.pos()
            self.i_0x20 = self._io.read_u4be()
            self._debug['i_0x20']['end'] = self._io.pos()
            self._debug['i_0x28']['start'] = self._io.pos()
            self.i_0x28 = self._io.read_u4be()
            self._debug['i_0x28']['end'] = self._io.pos()
            self._debug['i_0x2c']['start'] = self._io.pos()
            self.i_0x2c = self._io.read_u4be()
            self._debug['i_0x2c']['end'] = self._io.pos()
            self._debug['i_0x24']['start'] = self._io.pos()
            self.i_0x24 = self._io.read_u4be()
            self._debug['i_0x24']['end'] = self._io.pos()
            self._debug['i_0x30']['start'] = self._io.pos()
            self.i_0x30 = self._io.read_u4be()
            self._debug['i_0x30']['end'] = self._io.pos()


    class Puzzle(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class PlatPush0x5b(KaitaiStruct):
        SEQ_FIELDS = ["flags", "u32_0x04", "actor_f_0x70", "u32_0x1c"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u2be()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['u32_0x04']['start'] = self._io.pos()
            self.u32_0x04 = self._io.read_u4be()
            self._debug['u32_0x04']['end'] = self._io.pos()
            self._debug['actor_f_0x70']['start'] = self._io.pos()
            self.actor_f_0x70 = self._io.read_f4be()
            self._debug['actor_f_0x70']['end'] = self._io.pos()
            self._debug['u32_0x1c']['start'] = self._io.pos()
            self.u32_0x1c = self._io.read_u4be()
            self._debug['u32_0x1c']['end'] = self._io.pos()


    class PlatMvspn0x58(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x14", "u32_0x10"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x14']['start'] = self._io.pos()
            self.u16_0x14 = self._io.read_u2be()
            self._debug['u16_0x14']['end'] = self._io.pos()
            self._debug['u32_0x10']['start'] = self._io.pos()
            self.u32_0x10 = self._io.read_u4be()
            self._debug['u32_0x10']['end'] = self._io.pos()


    class PlatDestructible(KaitaiStruct):
        SEQ_FIELDS = ["flags", "num_particles", "particle_object_id", "name"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u2be()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['num_particles']['start'] = self._io.pos()
            self.num_particles = self._io.read_u4be()
            self._debug['num_particles']['end'] = self._io.pos()
            self._debug['particle_object_id']['start'] = self._io.pos()
            self.particle_object_id = self._io.read_u4be()
            self._debug['particle_object_id']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(8)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()


    class PuzzleAction(KaitaiStruct):
        SEQ_FIELDS = ["action_type", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['action_type']['start'] = self._io.pos()
            self.action_type = self._io.read_u2be()
            self._debug['action_type']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.action_type
            if _on == 61:
                self.body = GloverLevel.PuzzleAction0x350x3b0x3c0x3d0x3e0x3f0x40(self._io, self, self._root)
            elif _on == 73:
                self.body = GloverLevel.PuzzleAction0x490x4d(self._io, self, self._root)
            elif _on == 60:
                self.body = GloverLevel.PuzzleAction0x350x3b0x3c0x3d0x3e0x3f0x40(self._io, self, self._root)
            elif _on == 62:
                self.body = GloverLevel.PuzzleAction0x350x3b0x3c0x3d0x3e0x3f0x40(self._io, self, self._root)
            elif _on == 77:
                self.body = GloverLevel.PuzzleAction0x490x4d(self._io, self, self._root)
            elif _on == 85:
                self.body = GloverLevel.PuzzleAction0x55(self._io, self, self._root)
            elif _on == 59:
                self.body = GloverLevel.PuzzleAction0x350x3b0x3c0x3d0x3e0x3f0x40(self._io, self, self._root)
            elif _on == 86:
                self.body = GloverLevel.PuzzleAction0x56(self._io, self, self._root)
            elif _on == 84:
                self.body = GloverLevel.PuzzleAction0x54(self._io, self, self._root)
            elif _on == 63:
                self.body = GloverLevel.PuzzleAction0x350x3b0x3c0x3d0x3e0x3f0x40(self._io, self, self._root)
            elif _on == 53:
                self.body = GloverLevel.PuzzleAction0x350x3b0x3c0x3d0x3e0x3f0x40(self._io, self, self._root)
            elif _on == 64:
                self.body = GloverLevel.PuzzleAction0x350x3b0x3c0x3d0x3e0x3f0x40(self._io, self, self._root)
            elif _on == 76:
                self.body = GloverLevel.PuzzleAction0x4b0x4c(self._io, self, self._root)
            elif _on == 79:
                self.body = GloverLevel.PuzzleAction0x4f(self._io, self, self._root)
            elif _on == 72:
                self.body = GloverLevel.PuzzleAction0x460x470x48(self._io, self, self._root)
            elif _on == 71:
                self.body = GloverLevel.PuzzleAction0x460x470x48(self._io, self, self._root)
            elif _on == 70:
                self.body = GloverLevel.PuzzleAction0x460x470x48(self._io, self, self._root)
            elif _on == 74:
                self.body = GloverLevel.PuzzleAction0x4a(self._io, self, self._root)
            elif _on == 75:
                self.body = GloverLevel.PuzzleAction0x4b0x4c(self._io, self, self._root)
            else:
                self.body = GloverLevel.PuzzleActionDefault(self._io, self, self._root)
            self._debug['body']['end'] = self._io.pos()


    class Plat0xc4(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x3a", "u16_0x2c_and_0x34", "u16_0x38"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x3a']['start'] = self._io.pos()
            self.u16_0x3a = self._io.read_u2be()
            self._debug['u16_0x3a']['end'] = self._io.pos()
            self._debug['u16_0x2c_and_0x34']['start'] = self._io.pos()
            self.u16_0x2c_and_0x34 = self._io.read_u2be()
            self._debug['u16_0x2c_and_0x34']['end'] = self._io.pos()
            self._debug['u16_0x38']['start'] = self._io.pos()
            self.u16_0x38 = self._io.read_u2be()
            self._debug['u16_0x38']['end'] = self._io.pos()


    class Water(KaitaiStruct):
        SEQ_FIELDS = ["left", "top", "front", "width", "bottom", "depth", "surface_y", "current_x", "current_z", "unknown_1", "object_id", "name", "x", "y", "z"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['left']['start'] = self._io.pos()
            self.left = self._io.read_f4be()
            self._debug['left']['end'] = self._io.pos()
            self._debug['top']['start'] = self._io.pos()
            self.top = self._io.read_f4be()
            self._debug['top']['end'] = self._io.pos()
            self._debug['front']['start'] = self._io.pos()
            self.front = self._io.read_f4be()
            self._debug['front']['end'] = self._io.pos()
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_f4be()
            self._debug['width']['end'] = self._io.pos()
            self._debug['bottom']['start'] = self._io.pos()
            self.bottom = self._io.read_f4be()
            self._debug['bottom']['end'] = self._io.pos()
            self._debug['depth']['start'] = self._io.pos()
            self.depth = self._io.read_f4be()
            self._debug['depth']['end'] = self._io.pos()
            self._debug['surface_y']['start'] = self._io.pos()
            self.surface_y = self._io.read_f4be()
            self._debug['surface_y']['end'] = self._io.pos()
            self._debug['current_x']['start'] = self._io.pos()
            self.current_x = self._io.read_f4be()
            self._debug['current_x']['end'] = self._io.pos()
            self._debug['current_z']['start'] = self._io.pos()
            self.current_z = self._io.read_f4be()
            self._debug['current_z']['end'] = self._io.pos()
            self._debug['unknown_1']['start'] = self._io.pos()
            self.unknown_1 = self._io.read_u2be()
            self._debug['unknown_1']['end'] = self._io.pos()
            self._debug['object_id']['start'] = self._io.pos()
            self.object_id = self._io.read_u4be()
            self._debug['object_id']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(8)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f4be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()


    class PuzzleAction0x4f(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x14", "u32_0x18", "u32_0x10", "u16_0x0e", "u16_0x0a", "u32_0x20"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x14']['start'] = self._io.pos()
            self.u32_0x14 = self._io.read_u4be()
            self._debug['u32_0x14']['end'] = self._io.pos()
            self._debug['u32_0x18']['start'] = self._io.pos()
            self.u32_0x18 = self._io.read_u4be()
            self._debug['u32_0x18']['end'] = self._io.pos()
            self._debug['u32_0x10']['start'] = self._io.pos()
            self.u32_0x10 = self._io.read_u4be()
            self._debug['u32_0x10']['end'] = self._io.pos()
            self._debug['u16_0x0e']['start'] = self._io.pos()
            self.u16_0x0e = self._io.read_u2be()
            self._debug['u16_0x0e']['end'] = self._io.pos()
            self._debug['u16_0x0a']['start'] = self._io.pos()
            self.u16_0x0a = self._io.read_u2be()
            self._debug['u16_0x0a']['end'] = self._io.pos()
            self._debug['u32_0x20']['start'] = self._io.pos()
            self.u32_0x20 = self._io.read_u4be()
            self._debug['u32_0x20']['end'] = self._io.pos()


    class Unrecognized(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class PlatScale(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f4be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()


    class Unknown0xbf(KaitaiStruct):
        SEQ_FIELDS = ["mode", "i_0x02"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['mode']['start'] = self._io.pos()
            self.mode = self._io.read_u2be()
            self._debug['mode']['end'] = self._io.pos()
            self._debug['i_0x02']['start'] = self._io.pos()
            self.i_0x02 = self._io.read_u4be()
            self._debug['i_0x02']['end'] = self._io.pos()


    class PuzzleAction0x4b0x4c(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x0a"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x0a']['start'] = self._io.pos()
            self.u16_0x0a = self._io.read_u2be()
            self._debug['u16_0x0a']['end'] = self._io.pos()


    class SetActorScale(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f4be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()


    class PlatSpecial0xb8(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class PlatOrbitFlip0x77(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x08", "u16_0x10"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x08']['start'] = self._io.pos()
            self.u16_0x08 = self._io.read_u2be()
            self._debug['u16_0x08']['end'] = self._io.pos()
            self._debug['u16_0x10']['start'] = self._io.pos()
            self.u16_0x10 = self._io.read_u2be()
            self._debug['u16_0x10']['end'] = self._io.pos()


    class PlatDestructibleSound(KaitaiStruct):
        SEQ_FIELDS = ["sound_id", "volume", "pitch"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['sound_id']['start'] = self._io.pos()
            self.sound_id = self._io.read_u2be()
            self._debug['sound_id']['end'] = self._io.pos()
            self._debug['volume']['start'] = self._io.pos()
            self.volume = self._io.read_u2be()
            self._debug['volume']['end'] = self._io.pos()
            self._debug['pitch']['start'] = self._io.pos()
            self.pitch = self._io.read_u2be()
            self._debug['pitch']['end'] = self._io.pos()


    class Enemy(KaitaiStruct):
        SEQ_FIELDS = ["enemy_type", "u1", "x", "y", "z", "y_rotation"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['enemy_type']['start'] = self._io.pos()
            self.enemy_type = self._io.read_u2be()
            self._debug['enemy_type']['end'] = self._io.pos()
            self._debug['u1']['start'] = self._io.pos()
            self.u1 = self._io.read_u2be()
            self._debug['u1']['end'] = self._io.pos()
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f4be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()
            self._debug['y_rotation']['start'] = self._io.pos()
            self.y_rotation = self._io.read_f4be()
            self._debug['y_rotation']['end'] = self._io.pos()


    class PlatPuzzle0x6f(KaitaiStruct):
        SEQ_FIELDS = ["tag"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['tag']['start'] = self._io.pos()
            self.tag = self._io.read_u2be()
            self._debug['tag']['end'] = self._io.pos()


    class Plat0xa4(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class PlatOrActor0x6a(KaitaiStruct):
        SEQ_FIELDS = ["value"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_u2be()
            self._debug['value']['end'] = self._io.pos()


    class PlatSpin0x7b(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class PlatSpecial0xb6(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x34", "u16_0x40"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x34']['start'] = self._io.pos()
            self.u16_0x34 = self._io.read_u2be()
            self._debug['u16_0x34']['end'] = self._io.pos()
            self._debug['u16_0x40']['start'] = self._io.pos()
            self.u16_0x40 = self._io.read_u2be()
            self._debug['u16_0x40']['end'] = self._io.pos()


    class PlatCrumb0x67(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x02", "u16_0x04", "u16_0x08"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x02']['start'] = self._io.pos()
            self.u16_0x02 = self._io.read_u2be()
            self._debug['u16_0x02']['end'] = self._io.pos()
            self._debug['u16_0x04']['start'] = self._io.pos()
            self.u16_0x04 = self._io.read_u2be()
            self._debug['u16_0x04']['end'] = self._io.pos()
            self._debug['u16_0x08']['start'] = self._io.pos()
            self.u16_0x08 = self._io.read_u4be()
            self._debug['u16_0x08']['end'] = self._io.pos()


    class PuzzleActionDefault(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x10", "u16_0x0e", "u16_0x0a", "u32_0x20"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x10']['start'] = self._io.pos()
            self.u32_0x10 = self._io.read_u4be()
            self._debug['u32_0x10']['end'] = self._io.pos()
            self._debug['u16_0x0e']['start'] = self._io.pos()
            self.u16_0x0e = self._io.read_u2be()
            self._debug['u16_0x0e']['end'] = self._io.pos()
            self._debug['u16_0x0a']['start'] = self._io.pos()
            self.u16_0x0a = self._io.read_u2be()
            self._debug['u16_0x0a']['end'] = self._io.pos()
            self._debug['u32_0x20']['start'] = self._io.pos()
            self.u32_0x20 = self._io.read_u4be()
            self._debug['u32_0x20']['end'] = self._io.pos()


    class Garib(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z", "u8_0x0e", "u8_0x0f"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f4be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()
            self._debug['u8_0x0e']['start'] = self._io.pos()
            self.u8_0x0e = self._io.read_u2be()
            self._debug['u8_0x0e']['end'] = self._io.pos()
            self._debug['u8_0x0f']['start'] = self._io.pos()
            self.u8_0x0f = self._io.read_u2be()
            self._debug['u8_0x0f']['end'] = self._io.pos()


    class GaribGroup(KaitaiStruct):
        SEQ_FIELDS = ["u16_0xd2", "u8_0xd1"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0xd2']['start'] = self._io.pos()
            self.u16_0xd2 = self._io.read_u2be()
            self._debug['u16_0xd2']['end'] = self._io.pos()
            self._debug['u8_0xd1']['start'] = self._io.pos()
            self.u8_0xd1 = self._io.read_u2be()
            self._debug['u8_0xd1']['end'] = self._io.pos()


    class CameoInst6(KaitaiStruct):
        SEQ_FIELDS = ["h_0x00", "h_0x02", "h_0x04", "h_0x06"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['h_0x00']['start'] = self._io.pos()
            self.h_0x00 = self._io.read_u2be()
            self._debug['h_0x00']['end'] = self._io.pos()
            self._debug['h_0x02']['start'] = self._io.pos()
            self.h_0x02 = self._io.read_u2be()
            self._debug['h_0x02']['end'] = self._io.pos()
            self._debug['h_0x04']['start'] = self._io.pos()
            self.h_0x04 = self._io.read_u2be()
            self._debug['h_0x04']['end'] = self._io.pos()
            self._debug['h_0x06']['start'] = self._io.pos()
            self.h_0x06 = self._io.read_u2be()
            self._debug['h_0x06']['end'] = self._io.pos()


    class PlatPathPoint(KaitaiStruct):
        SEQ_FIELDS = ["frame_id", "x", "y", "z"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['frame_id']['start'] = self._io.pos()
            self.frame_id = self._io.read_u2be()
            self._debug['frame_id']['end'] = self._io.pos()
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f4be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()


    class Plat0x78(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x08"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x08']['start'] = self._io.pos()
            self.u16_0x08 = self._io.read_u2be()
            self._debug['u16_0x08']['end'] = self._io.pos()


    class BackgroundActor0x91(KaitaiStruct):
        SEQ_FIELDS = ["object_id", "name", "x", "y", "z"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['object_id']['start'] = self._io.pos()
            self.object_id = self._io.read_u4be()
            self._debug['object_id']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(8)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f4be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()


    class Enemy0xba(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class PuzzleCondA(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x24", "u16_0x0a"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x24']['start'] = self._io.pos()
            self.u32_0x24 = self._io.read_u2be()
            self._debug['u32_0x24']['end'] = self._io.pos()
            self._debug['u16_0x0a']['start'] = self._io.pos()
            self.u16_0x0a = self._io.read_u2be()
            self._debug['u16_0x0a']['end'] = self._io.pos()


    class PlatSine(KaitaiStruct):
        SEQ_FIELDS = ["u32_count", "u32_116", "name", "f_108", "f_104", "f_100", "f_96", "f_92", "f_88", "f_84", "f_80", "u32_176", "u32_172"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_count']['start'] = self._io.pos()
            self.u32_count = self._io.read_u4be()
            self._debug['u32_count']['end'] = self._io.pos()
            self._debug['u32_116']['start'] = self._io.pos()
            self.u32_116 = self._io.read_u4be()
            self._debug['u32_116']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(8)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['f_108']['start'] = self._io.pos()
            self.f_108 = self._io.read_f4be()
            self._debug['f_108']['end'] = self._io.pos()
            self._debug['f_104']['start'] = self._io.pos()
            self.f_104 = self._io.read_f4be()
            self._debug['f_104']['end'] = self._io.pos()
            self._debug['f_100']['start'] = self._io.pos()
            self.f_100 = self._io.read_f4be()
            self._debug['f_100']['end'] = self._io.pos()
            self._debug['f_96']['start'] = self._io.pos()
            self.f_96 = self._io.read_f4be()
            self._debug['f_96']['end'] = self._io.pos()
            self._debug['f_92']['start'] = self._io.pos()
            self.f_92 = self._io.read_f4be()
            self._debug['f_92']['end'] = self._io.pos()
            self._debug['f_88']['start'] = self._io.pos()
            self.f_88 = self._io.read_f4be()
            self._debug['f_88']['end'] = self._io.pos()
            self._debug['f_84']['start'] = self._io.pos()
            self.f_84 = self._io.read_f4be()
            self._debug['f_84']['end'] = self._io.pos()
            self._debug['f_80']['start'] = self._io.pos()
            self.f_80 = self._io.read_f4be()
            self._debug['f_80']['end'] = self._io.pos()
            self._debug['u32_176']['start'] = self._io.pos()
            self.u32_176 = self._io.read_u4be()
            self._debug['u32_176']['end'] = self._io.pos()
            self._debug['u32_172']['start'] = self._io.pos()
            self.u32_172 = self._io.read_u4be()
            self._debug['u32_172']['end'] = self._io.pos()


    class PlatCat0x69(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x20", "u32_0x00", "u32_0x04", "u32_0x08", "u32_0x0c", "u32_0x10", "u32_0x1c"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x20']['start'] = self._io.pos()
            self.u16_0x20 = self._io.read_u2be()
            self._debug['u16_0x20']['end'] = self._io.pos()
            self._debug['u32_0x00']['start'] = self._io.pos()
            self.u32_0x00 = self._io.read_u4be()
            self._debug['u32_0x00']['end'] = self._io.pos()
            self._debug['u32_0x04']['start'] = self._io.pos()
            self.u32_0x04 = self._io.read_u4be()
            self._debug['u32_0x04']['end'] = self._io.pos()
            self._debug['u32_0x08']['start'] = self._io.pos()
            self.u32_0x08 = self._io.read_u4be()
            self._debug['u32_0x08']['end'] = self._io.pos()
            self._debug['u32_0x0c']['start'] = self._io.pos()
            self.u32_0x0c = self._io.read_u4be()
            self._debug['u32_0x0c']['end'] = self._io.pos()
            self._debug['u32_0x10']['start'] = self._io.pos()
            self.u32_0x10 = self._io.read_u4be()
            self._debug['u32_0x10']['end'] = self._io.pos()
            self._debug['u32_0x1c']['start'] = self._io.pos()
            self.u32_0x1c = self._io.read_u4be()
            self._debug['u32_0x1c']['end'] = self._io.pos()


    class PlatRope(KaitaiStruct):
        SEQ_FIELDS = ["u32_count", "u16_idx", "u32_u1", "name", "ustack176_0", "ustack176_1", "ustack176_2", "ustack176_3", "ustack176_4", "ustack176_5", "ustack176_6", "f_112", "f_108", "f_104", "f_100", "f_96", "f_92"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_count']['start'] = self._io.pos()
            self.u32_count = self._io.read_u4be()
            self._debug['u32_count']['end'] = self._io.pos()
            self._debug['u16_idx']['start'] = self._io.pos()
            self.u16_idx = self._io.read_u2be()
            self._debug['u16_idx']['end'] = self._io.pos()
            self._debug['u32_u1']['start'] = self._io.pos()
            self.u32_u1 = self._io.read_u4be()
            self._debug['u32_u1']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(8)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['ustack176_0']['start'] = self._io.pos()
            self.ustack176_0 = self._io.read_u4be()
            self._debug['ustack176_0']['end'] = self._io.pos()
            self._debug['ustack176_1']['start'] = self._io.pos()
            self.ustack176_1 = self._io.read_u4be()
            self._debug['ustack176_1']['end'] = self._io.pos()
            self._debug['ustack176_2']['start'] = self._io.pos()
            self.ustack176_2 = self._io.read_u4be()
            self._debug['ustack176_2']['end'] = self._io.pos()
            self._debug['ustack176_3']['start'] = self._io.pos()
            self.ustack176_3 = self._io.read_u4be()
            self._debug['ustack176_3']['end'] = self._io.pos()
            self._debug['ustack176_4']['start'] = self._io.pos()
            self.ustack176_4 = self._io.read_u4be()
            self._debug['ustack176_4']['end'] = self._io.pos()
            self._debug['ustack176_5']['start'] = self._io.pos()
            self.ustack176_5 = self._io.read_u4be()
            self._debug['ustack176_5']['end'] = self._io.pos()
            self._debug['ustack176_6']['start'] = self._io.pos()
            self.ustack176_6 = self._io.read_u4be()
            self._debug['ustack176_6']['end'] = self._io.pos()
            self._debug['f_112']['start'] = self._io.pos()
            self.f_112 = self._io.read_f4be()
            self._debug['f_112']['end'] = self._io.pos()
            self._debug['f_108']['start'] = self._io.pos()
            self.f_108 = self._io.read_f4be()
            self._debug['f_108']['end'] = self._io.pos()
            self._debug['f_104']['start'] = self._io.pos()
            self.f_104 = self._io.read_f4be()
            self._debug['f_104']['end'] = self._io.pos()
            self._debug['f_100']['start'] = self._io.pos()
            self.f_100 = self._io.read_f4be()
            self._debug['f_100']['end'] = self._io.pos()
            self._debug['f_96']['start'] = self._io.pos()
            self.f_96 = self._io.read_f4be()
            self._debug['f_96']['end'] = self._io.pos()
            self._debug['f_92']['start'] = self._io.pos()
            self.f_92 = self._io.read_f4be()
            self._debug['f_92']['end'] = self._io.pos()


    class PuzzleNumtimes(KaitaiStruct):
        SEQ_FIELDS = ["n"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['n']['start'] = self._io.pos()
            self.n = self._io.read_u2be()
            self._debug['n']['end'] = self._io.pos()


    class PlatSpin0x80(KaitaiStruct):
        SEQ_FIELDS = ["idx", "f_0x1c", "u32_0x28", "u32_ustack56", "u32_0x2c", "f_0x6c", "f_0x70"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['idx']['start'] = self._io.pos()
            self.idx = self._io.read_u2be()
            self._debug['idx']['end'] = self._io.pos()
            self._debug['f_0x1c']['start'] = self._io.pos()
            self.f_0x1c = self._io.read_f4be()
            self._debug['f_0x1c']['end'] = self._io.pos()
            self._debug['u32_0x28']['start'] = self._io.pos()
            self.u32_0x28 = self._io.read_u4be()
            self._debug['u32_0x28']['end'] = self._io.pos()
            self._debug['u32_ustack56']['start'] = self._io.pos()
            self.u32_ustack56 = self._io.read_u4be()
            self._debug['u32_ustack56']['end'] = self._io.pos()
            self._debug['u32_0x2c']['start'] = self._io.pos()
            self.u32_0x2c = self._io.read_u4be()
            self._debug['u32_0x2c']['end'] = self._io.pos()
            self._debug['f_0x6c']['start'] = self._io.pos()
            self.f_0x6c = self._io.read_f4be()
            self._debug['f_0x6c']['end'] = self._io.pos()
            self._debug['f_0x70']['start'] = self._io.pos()
            self.f_0x70 = self._io.read_u2be()
            self._debug['f_0x70']['end'] = self._io.pos()


    class Plat0x7e(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x28"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x28']['start'] = self._io.pos()
            self.u32_0x28 = self._io.read_u4be()
            self._debug['u32_0x28']['end'] = self._io.pos()


    class Unknown0x98(KaitaiStruct):
        SEQ_FIELDS = ["h_0x00", "h_0x02", "h_0x04"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['h_0x00']['start'] = self._io.pos()
            self.h_0x00 = self._io.read_u2be()
            self._debug['h_0x00']['end'] = self._io.pos()
            self._debug['h_0x02']['start'] = self._io.pos()
            self.h_0x02 = self._io.read_u2be()
            self._debug['h_0x02']['end'] = self._io.pos()
            self._debug['h_0x04']['start'] = self._io.pos()
            self.h_0x04 = self._io.read_u2be()
            self._debug['h_0x04']['end'] = self._io.pos()


    class CameoInst1(KaitaiStruct):
        SEQ_FIELDS = ["h_0x00", "i_0x02", "i_0x06", "i_0x0a", "h_0x0e", "h_0x10"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['h_0x00']['start'] = self._io.pos()
            self.h_0x00 = self._io.read_u2be()
            self._debug['h_0x00']['end'] = self._io.pos()
            self._debug['i_0x02']['start'] = self._io.pos()
            self.i_0x02 = self._io.read_u4be()
            self._debug['i_0x02']['end'] = self._io.pos()
            self._debug['i_0x06']['start'] = self._io.pos()
            self.i_0x06 = self._io.read_u4be()
            self._debug['i_0x06']['end'] = self._io.pos()
            self._debug['i_0x0a']['start'] = self._io.pos()
            self.i_0x0a = self._io.read_u4be()
            self._debug['i_0x0a']['end'] = self._io.pos()
            self._debug['h_0x0e']['start'] = self._io.pos()
            self.h_0x0e = self._io.read_u2be()
            self._debug['h_0x0e']['end'] = self._io.pos()
            self._debug['h_0x10']['start'] = self._io.pos()
            self.h_0x10 = self._io.read_u2be()
            self._debug['h_0x10']['end'] = self._io.pos()


    class Plat0x9d(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class EnemyNormalInstruction(KaitaiStruct):
        SEQ_FIELDS = ["instr"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['instr']['start'] = self._io.pos()
            self.instr = GloverLevel.EnemyInstruction(self._io, self, self._root)
            self._debug['instr']['end'] = self._io.pos()


    class FogConfiguration(KaitaiStruct):
        SEQ_FIELDS = ["fog_enabled", "r", "g", "b", "fog_distance", "near_clip"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['fog_enabled']['start'] = self._io.pos()
            self.fog_enabled = self._io.read_u1()
            self._debug['fog_enabled']['end'] = self._io.pos()
            self._debug['r']['start'] = self._io.pos()
            self.r = self._io.read_u1()
            self._debug['r']['end'] = self._io.pos()
            self._debug['g']['start'] = self._io.pos()
            self.g = self._io.read_u1()
            self._debug['g']['end'] = self._io.pos()
            self._debug['b']['start'] = self._io.pos()
            self.b = self._io.read_u1()
            self._debug['b']['end'] = self._io.pos()
            self._debug['fog_distance']['start'] = self._io.pos()
            self.fog_distance = self._io.read_u2be()
            self._debug['fog_distance']['end'] = self._io.pos()
            self._debug['near_clip']['start'] = self._io.pos()
            self.near_clip = self._io.read_u2be()
            self._debug['near_clip']['end'] = self._io.pos()


    class CameoInst5(KaitaiStruct):
        SEQ_FIELDS = ["h_0x00", "h_0x02", "h_0x04"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['h_0x00']['start'] = self._io.pos()
            self.h_0x00 = self._io.read_u2be()
            self._debug['h_0x00']['end'] = self._io.pos()
            self._debug['h_0x02']['start'] = self._io.pos()
            self.h_0x02 = self._io.read_u2be()
            self._debug['h_0x02']['end'] = self._io.pos()
            self._debug['h_0x04']['start'] = self._io.pos()
            self.h_0x04 = self._io.read_u2be()
            self._debug['h_0x04']['end'] = self._io.pos()


    class Render0xb3(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class PlatTopple0x81(KaitaiStruct):
        SEQ_FIELDS = ["idx", "f_0x1c", "f_0x28", "f_0x24", "f_0x2c", "f_0x6c", "f_0x70_pivot_height", "u16_0x10"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['idx']['start'] = self._io.pos()
            self.idx = self._io.read_u2be()
            self._debug['idx']['end'] = self._io.pos()
            self._debug['f_0x1c']['start'] = self._io.pos()
            self.f_0x1c = self._io.read_f4be()
            self._debug['f_0x1c']['end'] = self._io.pos()
            self._debug['f_0x28']['start'] = self._io.pos()
            self.f_0x28 = self._io.read_f4be()
            self._debug['f_0x28']['end'] = self._io.pos()
            self._debug['f_0x24']['start'] = self._io.pos()
            self.f_0x24 = self._io.read_f4be()
            self._debug['f_0x24']['end'] = self._io.pos()
            self._debug['f_0x2c']['start'] = self._io.pos()
            self.f_0x2c = self._io.read_f4be()
            self._debug['f_0x2c']['end'] = self._io.pos()
            self._debug['f_0x6c']['start'] = self._io.pos()
            self.f_0x6c = self._io.read_f4be()
            self._debug['f_0x6c']['end'] = self._io.pos()
            self._debug['f_0x70_pivot_height']['start'] = self._io.pos()
            self.f_0x70_pivot_height = self._io.read_f4be()
            self._debug['f_0x70_pivot_height']['end'] = self._io.pos()
            self._debug['u16_0x10']['start'] = self._io.pos()
            self.u16_0x10 = self._io.read_u2be()
            self._debug['u16_0x10']['end'] = self._io.pos()


    class PuzzleAction0x55(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x24", "u16_0x0a"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x24']['start'] = self._io.pos()
            self.u32_0x24 = self._io.read_u4be()
            self._debug['u32_0x24']['end'] = self._io.pos()
            self._debug['u16_0x0a']['start'] = self._io.pos()
            self.u16_0x0a = self._io.read_u2be()
            self._debug['u16_0x0a']['end'] = self._io.pos()


    class CameoInst3(KaitaiStruct):
        SEQ_FIELDS = ["h_0x00", "i_0x02", "h_0x06", "h_0x08"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['h_0x00']['start'] = self._io.pos()
            self.h_0x00 = self._io.read_u2be()
            self._debug['h_0x00']['end'] = self._io.pos()
            self._debug['i_0x02']['start'] = self._io.pos()
            self.i_0x02 = self._io.read_u4be()
            self._debug['i_0x02']['end'] = self._io.pos()
            self._debug['h_0x06']['start'] = self._io.pos()
            self.h_0x06 = self._io.read_u2be()
            self._debug['h_0x06']['end'] = self._io.pos()
            self._debug['h_0x08']['start'] = self._io.pos()
            self.h_0x08 = self._io.read_u2be()
            self._debug['h_0x08']['end'] = self._io.pos()


    class PlatGoForwards0x5f(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x2c_0x6c", "u32_0x2c_0x1c", "u32_0xf0", "u32_0x2c_0x34"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x2c_0x6c']['start'] = self._io.pos()
            self.u32_0x2c_0x6c = self._io.read_u4be()
            self._debug['u32_0x2c_0x6c']['end'] = self._io.pos()
            self._debug['u32_0x2c_0x1c']['start'] = self._io.pos()
            self.u32_0x2c_0x1c = self._io.read_u4be()
            self._debug['u32_0x2c_0x1c']['end'] = self._io.pos()
            self._debug['u32_0xf0']['start'] = self._io.pos()
            self.u32_0xf0 = self._io.read_u4be()
            self._debug['u32_0xf0']['end'] = self._io.pos()
            self._debug['u32_0x2c_0x34']['start'] = self._io.pos()
            self.u32_0x2c_0x34 = self._io.read_u4be()
            self._debug['u32_0x2c_0x34']['end'] = self._io.pos()


    class PlatSpecial0x9e(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x5c", "u32_0x60", "u32_0x65", "u32_0x68"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x5c']['start'] = self._io.pos()
            self.u32_0x5c = self._io.read_u4be()
            self._debug['u32_0x5c']['end'] = self._io.pos()
            self._debug['u32_0x60']['start'] = self._io.pos()
            self.u32_0x60 = self._io.read_u4be()
            self._debug['u32_0x60']['end'] = self._io.pos()
            self._debug['u32_0x65']['start'] = self._io.pos()
            self.u32_0x65 = self._io.read_u4be()
            self._debug['u32_0x65']['end'] = self._io.pos()
            self._debug['u32_0x68']['start'] = self._io.pos()
            self.u32_0x68 = self._io.read_u4be()
            self._debug['u32_0x68']['end'] = self._io.pos()


    class EnemyInstruction(KaitaiStruct):
        SEQ_FIELDS = ["type_code", "u16_0x02", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type_code']['start'] = self._io.pos()
            self.type_code = self._io.read_u2be()
            self._debug['type_code']['end'] = self._io.pos()
            self._debug['u16_0x02']['start'] = self._io.pos()
            self.u16_0x02 = self._io.read_u2be()
            self._debug['u16_0x02']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.type_code
            if _on == 14:
                self.body = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 10:
                self.body = GloverLevel.EnemyInstructionA(self._io, self, self._root)
            elif _on == 17:
                self.body = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 0:
                self.body = GloverLevel.EnemyInstructionA(self._io, self, self._root)
            elif _on == 4:
                self.body = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 24:
                self.body = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 6:
                self.body = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 20:
                self.body = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 7:
                self.body = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 1:
                self.body = GloverLevel.EnemyInstructionA(self._io, self, self._root)
            elif _on == 13:
                self.body = GloverLevel.EnemyInstructionA(self._io, self, self._root)
            elif _on == 11:
                self.body = GloverLevel.EnemyInstructionA(self._io, self, self._root)
            elif _on == 12:
                self.body = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 3:
                self.body = GloverLevel.EnemyInstructionB(self._io, self, self._root)
            elif _on == 5:
                self.body = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 19:
                self.body = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 23:
                self.body = GloverLevel.EnemyInstructionA(self._io, self, self._root)
            elif _on == 15:
                self.body = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 8:
                self.body = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 9:
                self.body = GloverLevel.EnemyInstructionA(self._io, self, self._root)
            elif _on == 21:
                self.body = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 16:
                self.body = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 18:
                self.body = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 2:
                self.body = GloverLevel.EnemyInstructionA(self._io, self, self._root)
            elif _on == 22:
                self.body = GloverLevel.EnemyInstructionA(self._io, self, self._root)
            else:
                self.body = GloverLevel.EnemyInstructionError(self._io, self, self._root)
            self._debug['body']['end'] = self._io.pos()


    class SetGlobal0xb7(KaitaiStruct):
        SEQ_FIELDS = ["value"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_u4be()
            self._debug['value']['end'] = self._io.pos()


    class PlatConf0x72(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x00", "u32_0x04", "u32_0x08", "u32_0x0c", "u32_0x10", "u32_0x14"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x00']['start'] = self._io.pos()
            self.u32_0x00 = self._io.read_u4be()
            self._debug['u32_0x00']['end'] = self._io.pos()
            self._debug['u32_0x04']['start'] = self._io.pos()
            self.u32_0x04 = self._io.read_u4be()
            self._debug['u32_0x04']['end'] = self._io.pos()
            self._debug['u32_0x08']['start'] = self._io.pos()
            self.u32_0x08 = self._io.read_u4be()
            self._debug['u32_0x08']['end'] = self._io.pos()
            self._debug['u32_0x0c']['start'] = self._io.pos()
            self.u32_0x0c = self._io.read_u4be()
            self._debug['u32_0x0c']['end'] = self._io.pos()
            self._debug['u32_0x10']['start'] = self._io.pos()
            self.u32_0x10 = self._io.read_u4be()
            self._debug['u32_0x10']['end'] = self._io.pos()
            self._debug['u32_0x14']['start'] = self._io.pos()
            self.u32_0x14 = self._io.read_u4be()
            self._debug['u32_0x14']['end'] = self._io.pos()


    class PuzzleCondE(KaitaiStruct):
        SEQ_FIELDS = ["i_0x00", "i_0x04", "i_0x08", "i_0x0c", "i_0x10"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['i_0x00']['start'] = self._io.pos()
            self.i_0x00 = self._io.read_u4be()
            self._debug['i_0x00']['end'] = self._io.pos()
            self._debug['i_0x04']['start'] = self._io.pos()
            self.i_0x04 = self._io.read_u4be()
            self._debug['i_0x04']['end'] = self._io.pos()
            self._debug['i_0x08']['start'] = self._io.pos()
            self.i_0x08 = self._io.read_u4be()
            self._debug['i_0x08']['end'] = self._io.pos()
            self._debug['i_0x0c']['start'] = self._io.pos()
            self.i_0x0c = self._io.read_u4be()
            self._debug['i_0x0c']['end'] = self._io.pos()
            self._debug['i_0x10']['start'] = self._io.pos()
            self.i_0x10 = self._io.read_u4be()
            self._debug['i_0x10']['end'] = self._io.pos()


    class Platform(KaitaiStruct):
        SEQ_FIELDS = ["object_id", "name"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['object_id']['start'] = self._io.pos()
            self.object_id = self._io.read_u4be()
            self._debug['object_id']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(8)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()


    class PlatSpecial0xb4(KaitaiStruct):
        SEQ_FIELDS = ["u8_0x23"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u8_0x23']['start'] = self._io.pos()
            self.u8_0x23 = self._io.read_u2be()
            self._debug['u8_0x23']['end'] = self._io.pos()


    class PlatPos0xa7(KaitaiStruct):
        SEQ_FIELDS = ["u8_idx"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u8_idx']['start'] = self._io.pos()
            self.u8_idx = self._io.read_u2be()
            self._debug['u8_idx']['end'] = self._io.pos()


    class BackgroundActor0xbc(KaitaiStruct):
        SEQ_FIELDS = ["object_id", "name", "x", "y", "z"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['object_id']['start'] = self._io.pos()
            self.object_id = self._io.read_u4be()
            self._debug['object_id']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(8)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f4be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()


    class PlatSpecial0x6e(KaitaiStruct):
        SEQ_FIELDS = ["flags", "u32_0x70"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u2be()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['u32_0x70']['start'] = self._io.pos()
            self.u32_0x70 = self._io.read_u4be()
            self._debug['u32_0x70']['end'] = self._io.pos()


    class CameoInstDefault(KaitaiStruct):
        SEQ_FIELDS = ["h_0x00", "h_0x02"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['h_0x00']['start'] = self._io.pos()
            self.h_0x00 = self._io.read_u2be()
            self._debug['h_0x00']['end'] = self._io.pos()
            self._debug['h_0x02']['start'] = self._io.pos()
            self.h_0x02 = self._io.read_u2be()
            self._debug['h_0x02']['end'] = self._io.pos()


    class PuzzleAction0x350x3b0x3c0x3d0x3e0x3f0x40(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x14", "u32_0x18", "u32_0x1c", "u32_0x10", "u16_0x0e", "u16_0x0a", "u32_0x20"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x14']['start'] = self._io.pos()
            self.u32_0x14 = self._io.read_u4be()
            self._debug['u32_0x14']['end'] = self._io.pos()
            self._debug['u32_0x18']['start'] = self._io.pos()
            self.u32_0x18 = self._io.read_u4be()
            self._debug['u32_0x18']['end'] = self._io.pos()
            self._debug['u32_0x1c']['start'] = self._io.pos()
            self.u32_0x1c = self._io.read_u4be()
            self._debug['u32_0x1c']['end'] = self._io.pos()
            self._debug['u32_0x10']['start'] = self._io.pos()
            self.u32_0x10 = self._io.read_u4be()
            self._debug['u32_0x10']['end'] = self._io.pos()
            self._debug['u16_0x0e']['start'] = self._io.pos()
            self.u16_0x0e = self._io.read_u2be()
            self._debug['u16_0x0e']['end'] = self._io.pos()
            self._debug['u16_0x0a']['start'] = self._io.pos()
            self.u16_0x0a = self._io.read_u2be()
            self._debug['u16_0x0a']['end'] = self._io.pos()
            self._debug['u32_0x20']['start'] = self._io.pos()
            self.u32_0x20 = self._io.read_u4be()
            self._debug['u32_0x20']['end'] = self._io.pos()


    class PuzzleCondB(KaitaiStruct):
        SEQ_FIELDS = ["i_0x00", "i_0x04", "i_0x08", "i_0x0c", "i_0x10", "i_0x14", "i_0x18"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['i_0x00']['start'] = self._io.pos()
            self.i_0x00 = self._io.read_u4be()
            self._debug['i_0x00']['end'] = self._io.pos()
            self._debug['i_0x04']['start'] = self._io.pos()
            self.i_0x04 = self._io.read_u4be()
            self._debug['i_0x04']['end'] = self._io.pos()
            self._debug['i_0x08']['start'] = self._io.pos()
            self.i_0x08 = self._io.read_u4be()
            self._debug['i_0x08']['end'] = self._io.pos()
            self._debug['i_0x0c']['start'] = self._io.pos()
            self.i_0x0c = self._io.read_u4be()
            self._debug['i_0x0c']['end'] = self._io.pos()
            self._debug['i_0x10']['start'] = self._io.pos()
            self.i_0x10 = self._io.read_u4be()
            self._debug['i_0x10']['end'] = self._io.pos()
            self._debug['i_0x14']['start'] = self._io.pos()
            self.i_0x14 = self._io.read_u4be()
            self._debug['i_0x14']['end'] = self._io.pos()
            self._debug['i_0x18']['start'] = self._io.pos()
            self.i_0x18 = self._io.read_u4be()
            self._debug['i_0x18']['end'] = self._io.pos()


    class PlatStr0x7a(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x0c", "u32_0x10", "u32_0x14", "u16_0x18", "u16_0x1c"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x0c']['start'] = self._io.pos()
            self.u32_0x0c = self._io.read_u4be()
            self._debug['u32_0x0c']['end'] = self._io.pos()
            self._debug['u32_0x10']['start'] = self._io.pos()
            self.u32_0x10 = self._io.read_u4be()
            self._debug['u32_0x10']['end'] = self._io.pos()
            self._debug['u32_0x14']['start'] = self._io.pos()
            self.u32_0x14 = self._io.read_u4be()
            self._debug['u32_0x14']['end'] = self._io.pos()
            self._debug['u16_0x18']['start'] = self._io.pos()
            self.u16_0x18 = self._io.read_u2be()
            self._debug['u16_0x18']['end'] = self._io.pos()
            self._debug['u16_0x1c']['start'] = self._io.pos()
            self.u16_0x1c = self._io.read_u2be()
            self._debug['u16_0x1c']['end'] = self._io.pos()


    class Enemy0x84(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class EnemyInstructionA(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x02", "u32_0x06", "u32_0x0a", "u32_0x0e", "u32_0x18", "u32_0x1e", "u32_0x14", "u32_0x16"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x02']['start'] = self._io.pos()
            self.u32_0x02 = self._io.read_u4be()
            self._debug['u32_0x02']['end'] = self._io.pos()
            self._debug['u32_0x06']['start'] = self._io.pos()
            self.u32_0x06 = self._io.read_u4be()
            self._debug['u32_0x06']['end'] = self._io.pos()
            self._debug['u32_0x0a']['start'] = self._io.pos()
            self.u32_0x0a = self._io.read_u4be()
            self._debug['u32_0x0a']['end'] = self._io.pos()
            self._debug['u32_0x0e']['start'] = self._io.pos()
            self.u32_0x0e = self._io.read_u4be()
            self._debug['u32_0x0e']['end'] = self._io.pos()
            self._debug['u32_0x18']['start'] = self._io.pos()
            self.u32_0x18 = self._io.read_u4be()
            self._debug['u32_0x18']['end'] = self._io.pos()
            self._debug['u32_0x1e']['start'] = self._io.pos()
            self.u32_0x1e = self._io.read_u4be()
            self._debug['u32_0x1e']['end'] = self._io.pos()
            self._debug['u32_0x14']['start'] = self._io.pos()
            self.u32_0x14 = self._io.read_u4be()
            self._debug['u32_0x14']['end'] = self._io.pos()
            self._debug['u32_0x16']['start'] = self._io.pos()
            self.u32_0x16 = self._io.read_u2be()
            self._debug['u32_0x16']['end'] = self._io.pos()


    class PlatSpecial0xb9(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class EnemyAttackInstruction(KaitaiStruct):
        SEQ_FIELDS = ["instr"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['instr']['start'] = self._io.pos()
            self.instr = GloverLevel.EnemyInstruction(self._io, self, self._root)
            self._debug['instr']['end'] = self._io.pos()


    class LandActor(KaitaiStruct):
        SEQ_FIELDS = ["object_id", "name", "x", "y", "z"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['object_id']['start'] = self._io.pos()
            self.object_id = self._io.read_u4be()
            self._debug['object_id']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(8)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f4be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()


    class PlatOrbitPause0x76(KaitaiStruct):
        SEQ_FIELDS = ["u16_0x08", "u16_0x0c"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u16_0x08']['start'] = self._io.pos()
            self.u16_0x08 = self._io.read_u2be()
            self._debug['u16_0x08']['end'] = self._io.pos()
            self._debug['u16_0x0c']['start'] = self._io.pos()
            self.u16_0x0c = self._io.read_u2be()
            self._debug['u16_0x0c']['end'] = self._io.pos()


    class MrTip(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z", "message_id"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f4be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()
            self._debug['message_id']['start'] = self._io.pos()
            self.message_id = self._io.read_u2be()
            self._debug['message_id']['end'] = self._io.pos()


    class PlatMvspnSetparent(KaitaiStruct):
        SEQ_FIELDS = ["parent_tag"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['parent_tag']['start'] = self._io.pos()
            self.parent_tag = self._io.read_u2be()
            self._debug['parent_tag']['end'] = self._io.pos()


    class PuzzleAction0x490x4d(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x24", "u32_0x28", "u32_0x2c", "u16_0x0a"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x24']['start'] = self._io.pos()
            self.u32_0x24 = self._io.read_u4be()
            self._debug['u32_0x24']['end'] = self._io.pos()
            self._debug['u32_0x28']['start'] = self._io.pos()
            self.u32_0x28 = self._io.read_u4be()
            self._debug['u32_0x28']['end'] = self._io.pos()
            self._debug['u32_0x2c']['start'] = self._io.pos()
            self.u32_0x2c = self._io.read_u4be()
            self._debug['u32_0x2c']['end'] = self._io.pos()
            self._debug['u16_0x0a']['start'] = self._io.pos()
            self.u16_0x0a = self._io.read_u2be()
            self._debug['u16_0x0a']['end'] = self._io.pos()


    class CameoInst0(KaitaiStruct):
        SEQ_FIELDS = ["h_0x00", "h_0x02", "h_0x04", "i_0x06", "h_0x0a", "h_0x0c"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['h_0x00']['start'] = self._io.pos()
            self.h_0x00 = self._io.read_u2be()
            self._debug['h_0x00']['end'] = self._io.pos()
            self._debug['h_0x02']['start'] = self._io.pos()
            self.h_0x02 = self._io.read_u2be()
            self._debug['h_0x02']['end'] = self._io.pos()
            self._debug['h_0x04']['start'] = self._io.pos()
            self.h_0x04 = self._io.read_u2be()
            self._debug['h_0x04']['end'] = self._io.pos()
            self._debug['i_0x06']['start'] = self._io.pos()
            self.i_0x06 = self._io.read_u4be()
            self._debug['i_0x06']['end'] = self._io.pos()
            self._debug['h_0x0a']['start'] = self._io.pos()
            self.h_0x0a = self._io.read_u2be()
            self._debug['h_0x0a']['end'] = self._io.pos()
            self._debug['h_0x0c']['start'] = self._io.pos()
            self.h_0x0c = self._io.read_u2be()
            self._debug['h_0x0c']['end'] = self._io.pos()


    class Unknown0x03(KaitaiStruct):
        SEQ_FIELDS = ["f_0x00", "f_0x04", "f_0x08", "f_0x0c", "f_0x10"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['f_0x00']['start'] = self._io.pos()
            self.f_0x00 = self._io.read_f4be()
            self._debug['f_0x00']['end'] = self._io.pos()
            self._debug['f_0x04']['start'] = self._io.pos()
            self.f_0x04 = self._io.read_f4be()
            self._debug['f_0x04']['end'] = self._io.pos()
            self._debug['f_0x08']['start'] = self._io.pos()
            self.f_0x08 = self._io.read_f4be()
            self._debug['f_0x08']['end'] = self._io.pos()
            self._debug['f_0x0c']['start'] = self._io.pos()
            self.f_0x0c = self._io.read_f4be()
            self._debug['f_0x0c']['end'] = self._io.pos()
            self._debug['f_0x10']['start'] = self._io.pos()
            self.f_0x10 = self._io.read_f4be()
            self._debug['f_0x10']['end'] = self._io.pos()




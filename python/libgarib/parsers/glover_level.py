# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections
from enum import Enum


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
        SEQ_FIELDS = ["r", "g", "b", "theta_x", "theta_y"]
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
            self._debug['theta_x']['start'] = self._io.pos()
            self.theta_x = self._io.read_f4be()
            self._debug['theta_x']['end'] = self._io.pos()
            self._debug['theta_y']['start'] = self._io.pos()
            self.theta_y = self._io.read_f4be()
            self._debug['theta_y']['end'] = self._io.pos()


    class PlatPathAcceleration(KaitaiStruct):
        SEQ_FIELDS = ["acceleration"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['acceleration']['start'] = self._io.pos()
            self.acceleration = self._io.read_f4be()
            self._debug['acceleration']['end'] = self._io.pos()


    class Buzzer(KaitaiStruct):
        SEQ_FIELDS = ["tag", "platform_1_tag", "platform_2_tag", "draw_flags", "r", "g", "b", "color_jitter", "end_1_x", "end_1_y", "end_1_z", "end_2_x", "end_2_y", "end_2_z", "draw_diameter", "draw_thickness"]
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
            self._debug['platform_1_tag']['start'] = self._io.pos()
            self.platform_1_tag = self._io.read_u2be()
            self._debug['platform_1_tag']['end'] = self._io.pos()
            self._debug['platform_2_tag']['start'] = self._io.pos()
            self.platform_2_tag = self._io.read_u2be()
            self._debug['platform_2_tag']['end'] = self._io.pos()
            self._debug['draw_flags']['start'] = self._io.pos()
            self.draw_flags = self._io.read_u2be()
            self._debug['draw_flags']['end'] = self._io.pos()
            self._debug['r']['start'] = self._io.pos()
            self.r = self._io.read_u2be()
            self._debug['r']['end'] = self._io.pos()
            self._debug['g']['start'] = self._io.pos()
            self.g = self._io.read_u2be()
            self._debug['g']['end'] = self._io.pos()
            self._debug['b']['start'] = self._io.pos()
            self.b = self._io.read_u2be()
            self._debug['b']['end'] = self._io.pos()
            self._debug['color_jitter']['start'] = self._io.pos()
            self.color_jitter = self._io.read_u2be()
            self._debug['color_jitter']['end'] = self._io.pos()
            self._debug['end_1_x']['start'] = self._io.pos()
            self.end_1_x = self._io.read_f4be()
            self._debug['end_1_x']['end'] = self._io.pos()
            self._debug['end_1_y']['start'] = self._io.pos()
            self.end_1_y = self._io.read_f4be()
            self._debug['end_1_y']['end'] = self._io.pos()
            self._debug['end_1_z']['start'] = self._io.pos()
            self.end_1_z = self._io.read_f4be()
            self._debug['end_1_z']['end'] = self._io.pos()
            self._debug['end_2_x']['start'] = self._io.pos()
            self.end_2_x = self._io.read_f4be()
            self._debug['end_2_x']['end'] = self._io.pos()
            self._debug['end_2_y']['start'] = self._io.pos()
            self.end_2_y = self._io.read_f4be()
            self._debug['end_2_y']['end'] = self._io.pos()
            self._debug['end_2_z']['start'] = self._io.pos()
            self.end_2_z = self._io.read_f4be()
            self._debug['end_2_z']['end'] = self._io.pos()
            self._debug['draw_diameter']['start'] = self._io.pos()
            self.draw_diameter = self._io.read_f4be()
            self._debug['draw_diameter']['end'] = self._io.pos()
            self._debug['draw_thickness']['start'] = self._io.pos()
            self.draw_thickness = self._io.read_f4be()
            self._debug['draw_thickness']['end'] = self._io.pos()


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


    class PlatTurnTowardsPathPoint(KaitaiStruct):
        SEQ_FIELDS = ["input_1", "input_2"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['input_1']['start'] = self._io.pos()
            self.input_1 = self._io.read_u4be()
            self._debug['input_1']['end'] = self._io.pos()
            self._debug['input_2']['start'] = self._io.pos()
            self.input_2 = self._io.read_u4be()
            self._debug['input_2']['end'] = self._io.pos()


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


    class PlatActorSurfaceType(KaitaiStruct):
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


    class EnemyInstructionDash(KaitaiStruct):
        SEQ_FIELDS = ["destination_x", "destination_y", "destination_z", "vel_magnitude"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['destination_x']['start'] = self._io.pos()
            self.destination_x = self._io.read_f4be()
            self._debug['destination_x']['end'] = self._io.pos()
            self._debug['destination_y']['start'] = self._io.pos()
            self.destination_y = self._io.read_f4be()
            self._debug['destination_y']['end'] = self._io.pos()
            self._debug['destination_z']['start'] = self._io.pos()
            self.destination_z = self._io.read_f4be()
            self._debug['destination_z']['end'] = self._io.pos()
            self._debug['vel_magnitude']['start'] = self._io.pos()
            self.vel_magnitude = self._io.read_f4be()
            self._debug['vel_magnitude']['end'] = self._io.pos()


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


    class PlatSetInitialPos(KaitaiStruct):
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


    class Actor0xbf(KaitaiStruct):
        SEQ_FIELDS = ["mode", "child_mesh_id"]
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
            self._debug['child_mesh_id']['start'] = self._io.pos()
            self.child_mesh_id = self._io.read_u4be()
            self._debug['child_mesh_id']['end'] = self._io.pos()


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


    class EnemyFinalize(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


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


    class PlatConstantSpin(KaitaiStruct):

        class Axis(Enum):
            x = 0
            y = 1
            z = 2
        SEQ_FIELDS = ["axis", "initial_theta", "speed"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['axis']['start'] = self._io.pos()
            self.axis = KaitaiStream.resolve_enum(GloverLevel.PlatConstantSpin.Axis, self._io.read_u2be())
            self._debug['axis']['end'] = self._io.pos()
            self._debug['initial_theta']['start'] = self._io.pos()
            self.initial_theta = self._io.read_f4be()
            self._debug['initial_theta']['end'] = self._io.pos()
            self._debug['speed']['start'] = self._io.pos()
            self.speed = self._io.read_f4be()
            self._debug['speed']['end'] = self._io.pos()


    class VentDutyCycle(KaitaiStruct):
        SEQ_FIELDS = ["frames_off", "frames_on"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['frames_off']['start'] = self._io.pos()
            self.frames_off = self._io.read_s2be()
            self._debug['frames_off']['end'] = self._io.pos()
            self._debug['frames_on']['start'] = self._io.pos()
            self.frames_on = self._io.read_s2be()
            self._debug['frames_on']['end'] = self._io.pos()


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


    class SetObjectSparkle(KaitaiStruct):
        SEQ_FIELDS = ["period"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['period']['start'] = self._io.pos()
            self.period = self._io.read_u2be()
            self._debug['period']['end'] = self._io.pos()


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


    class EnemyInstructionTurn(KaitaiStruct):
        SEQ_FIELDS = ["lookat_x", "lookat_y", "lookat_z", "choose_random_direction"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['lookat_x']['start'] = self._io.pos()
            self.lookat_x = self._io.read_f4be()
            self._debug['lookat_x']['end'] = self._io.pos()
            self._debug['lookat_y']['start'] = self._io.pos()
            self.lookat_y = self._io.read_f4be()
            self._debug['lookat_y']['end'] = self._io.pos()
            self._debug['lookat_z']['start'] = self._io.pos()
            self.lookat_z = self._io.read_f4be()
            self._debug['lookat_z']['end'] = self._io.pos()
            self._debug['choose_random_direction']['start'] = self._io.pos()
            self.choose_random_direction = self._io.read_u4be()
            self._debug['choose_random_direction']['end'] = self._io.pos()


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


    class PlatSetTag(KaitaiStruct):
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


    class PlatCopySpinFromParent(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class Vent(KaitaiStruct):
        SEQ_FIELDS = ["type", "u16_0x0a", "parent_tag", "origin_x", "origin_y", "origin_z", "particle_velocity_x", "particle_velocity_y", "particle_velocity_z"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = self._io.read_u2be()
            self._debug['type']['end'] = self._io.pos()
            self._debug['u16_0x0a']['start'] = self._io.pos()
            self.u16_0x0a = self._io.read_u2be()
            self._debug['u16_0x0a']['end'] = self._io.pos()
            self._debug['parent_tag']['start'] = self._io.pos()
            self.parent_tag = self._io.read_u2be()
            self._debug['parent_tag']['end'] = self._io.pos()
            self._debug['origin_x']['start'] = self._io.pos()
            self.origin_x = self._io.read_f4be()
            self._debug['origin_x']['end'] = self._io.pos()
            self._debug['origin_y']['start'] = self._io.pos()
            self.origin_y = self._io.read_f4be()
            self._debug['origin_y']['end'] = self._io.pos()
            self._debug['origin_z']['start'] = self._io.pos()
            self.origin_z = self._io.read_f4be()
            self._debug['origin_z']['end'] = self._io.pos()
            self._debug['particle_velocity_x']['start'] = self._io.pos()
            self.particle_velocity_x = self._io.read_f4be()
            self._debug['particle_velocity_x']['end'] = self._io.pos()
            self._debug['particle_velocity_y']['start'] = self._io.pos()
            self.particle_velocity_y = self._io.read_f4be()
            self._debug['particle_velocity_y']['end'] = self._io.pos()
            self._debug['particle_velocity_z']['start'] = self._io.pos()
            self.particle_velocity_z = self._io.read_f4be()
            self._debug['particle_velocity_z']['end'] = self._io.pos()


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


    class EnemyInstructionAttack(KaitaiStruct):
        SEQ_FIELDS = ["unused_1", "unused_2"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['unused_1']['start'] = self._io.pos()
            self.unused_1 = self._io.read_u4be()
            self._debug['unused_1']['end'] = self._io.pos()
            self._debug['unused_2']['start'] = self._io.pos()
            self.unused_2 = self._io.read_u4be()
            self._debug['unused_2']['end'] = self._io.pos()


    class EnemyInstructionRest(KaitaiStruct):
        SEQ_FIELDS = ["flags", "anim_start_playing"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4be()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['anim_start_playing']['start'] = self._io.pos()
            self.anim_start_playing = self._io.read_u4be()
            self._debug['anim_start_playing']['end'] = self._io.pos()


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


    class Unknown(KaitaiStruct):
        SEQ_FIELDS = ["body"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['body']['start'] = self._io.pos()
            self.body = self._io.read_bytes_full()
            self._debug['body']['end'] = self._io.pos()


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
        SEQ_FIELDS = ["type", "plat_flags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = self._io.read_u2be()
            self._debug['type']['end'] = self._io.pos()
            self._debug['plat_flags']['start'] = self._io.pos()
            self.plat_flags = self._io.read_u2be()
            self._debug['plat_flags']['end'] = self._io.pos()


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


    class PlatActorEnableWaterAnimation(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class EnemyInstructionC(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x02", "u32_0x0e"]
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


    class NullPlatform(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class Powerup(KaitaiStruct):
        SEQ_FIELDS = ["type", "u16_0x02", "u16_0x04", "x", "y", "z"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = self._io.read_u2be()
            self._debug['type']['end'] = self._io.pos()
            self._debug['u16_0x02']['start'] = self._io.pos()
            self.u16_0x02 = self._io.read_u2be()
            self._debug['u16_0x02']['end'] = self._io.pos()
            self._debug['u16_0x04']['start'] = self._io.pos()
            self.u16_0x04 = self._io.read_u2be()
            self._debug['u16_0x04']['end'] = self._io.pos()
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f4be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()


    class PlatformConveyor(KaitaiStruct):
        SEQ_FIELDS = ["vel_x", "vel_y", "vel_z"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['vel_x']['start'] = self._io.pos()
            self.vel_x = self._io.read_f4be()
            self._debug['vel_x']['end'] = self._io.pos()
            self._debug['vel_y']['start'] = self._io.pos()
            self.vel_y = self._io.read_f4be()
            self._debug['vel_y']['end'] = self._io.pos()
            self._debug['vel_z']['start'] = self._io.pos()
            self.vel_z = self._io.read_f4be()
            self._debug['vel_z']['end'] = self._io.pos()


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


    class PlatCheckpoint(KaitaiStruct):
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
        SEQ_FIELDS = ["type", "x", "y", "z"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = self._io.read_u2be()
            self._debug['type']['end'] = self._io.pos()
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f4be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()


    class PlatSetParent(KaitaiStruct):
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
                self.params = GloverLevel.Rope(self._io, self, self._root)
            elif _on == 93:
                self.params = GloverLevel.NullPlatform(self._io, self, self._root)
            elif _on == 118:
                self.params = GloverLevel.PlatOrbitPause(self._io, self, self._root)
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
                self.params = GloverLevel.PlatRocking(self._io, self, self._root)
            elif _on == 163:
                self.params = GloverLevel.VentDutyCycle(self._io, self, self._root)
            elif _on == 131:
                self.params = GloverLevel.Enemy(self._io, self, self._root)
            elif _on == 0:
                self.params = GloverLevel.Noop(self._io, self, self._root)
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
                self.params = GloverLevel.PlatSetParent(self._io, self, self._root)
            elif _on == 121:
                self.params = GloverLevel.PlatScale(self._io, self, self._root)
            elif _on == 96:
                self.params = GloverLevel.LookAtHand0x60(self._io, self, self._root)
            elif _on == 191:
                self.params = GloverLevel.Actor0xbf(self._io, self, self._root)
            elif _on == 1:
                self.params = GloverLevel.GloverSpawnPoint(self._io, self, self._root)
            elif _on == 150:
                self.params = GloverLevel.PuzzleAction(self._io, self, self._root)
            elif _on == 97:
                self.params = GloverLevel.LookAtBall0x61(self._io, self, self._root)
            elif _on == 106:
                self.params = GloverLevel.PlatActorSurfaceType(self._io, self, self._root)
            elif _on == 145:
                self.params = GloverLevel.BackgroundActor(self._io, self, self._root)
            elif _on == 101:
                self.params = GloverLevel.PlatDestructible(self._io, self, self._root)
            elif _on == 144:
                self.params = GloverLevel.PlatSine(self._io, self, self._root)
            elif _on == 127:
                self.params = GloverLevel.PlatConstantSpin(self._io, self, self._root)
            elif _on == 100:
                self.params = GloverLevel.PlatNoClip(self._io, self, self._root)
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
                self.params = GloverLevel.PlatformConveyor(self._io, self, self._root)
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
                self.params = GloverLevel.EnemySetAttentionBbox(self._io, self, self._root)
            elif _on == 138:
                self.params = GloverLevel.PlatFan0x8a(self._io, self, self._root)
            elif _on == 3:
                self.params = GloverLevel.CameraSpawnPoint(self._io, self, self._root)
            elif _on == 192:
                self.params = GloverLevel.PlatPlayObjectAnimation(self._io, self, self._root)
            elif _on == 126:
                self.params = GloverLevel.Plat0x7e(self._io, self, self._root)
            elif _on == 165:
                self.params = GloverLevel.FogConfiguration(self._io, self, self._root)
            elif _on == 5:
                self.params = GloverLevel.PuzzleAnd(self._io, self, self._root)
            elif _on == 103:
                self.params = GloverLevel.PlatCrumb0x67(self._io, self, self._root)
            elif _on == 99:
                self.params = GloverLevel.PlatCheckpoint(self._io, self, self._root)
            elif _on == 185:
                self.params = GloverLevel.PlatSpecial0xb9(self._io, self, self._root)
            elif _on == 180:
                self.params = GloverLevel.SetObjectSparkle(self._io, self, self._root)
            elif _on == 156:
                self.params = GloverLevel.EnemyAttackInstruction(self._io, self, self._root)
            elif _on == 125:
                self.params = GloverLevel.PlatSpinFlip(self._io, self, self._root)
            elif _on == 186:
                self.params = GloverLevel.Enemy0xba(self._io, self, self._root)
            elif _on == 188:
                self.params = GloverLevel.AnimatedBackgroundActor(self._io, self, self._root)
            elif _on == 153:
                self.params = GloverLevel.Backdrop(self._io, self, self._root)
            elif _on == 123:
                self.params = GloverLevel.PlatCopySpinFromParent(self._io, self, self._root)
            elif _on == 160:
                self.params = GloverLevel.Water(self._io, self, self._root)
            elif _on == 8:
                self.params = GloverLevel.PuzzleAny(self._io, self, self._root)
            elif _on == 166:
                self.params = GloverLevel.PlatSetInitialPos(self._io, self, self._root)
            elif _on == 114:
                self.params = GloverLevel.PlatConf0x72(self._io, self, self._root)
            elif _on == 181:
                self.params = GloverLevel.Buzzer(self._io, self, self._root)
            elif _on == 148:
                self.params = GloverLevel.SetActorScale(self._io, self, self._root)
            elif _on == 158:
                self.params = GloverLevel.PlatSpecial0x9e(self._io, self, self._root)
            elif _on == 117:
                self.params = GloverLevel.PlatOrbitAroundPoint(self._io, self, self._root)
            elif _on == 152:
                self.params = GloverLevel.AmbientLight(self._io, self, self._root)
            elif _on == 94:
                self.params = GloverLevel.PlatTurnTowardsPathPoint(self._io, self, self._root)
            elif _on == 109:
                self.params = GloverLevel.PlatPathAcceleration(self._io, self, self._root)
            elif _on == 32000:
                self.params = GloverLevel.EndLevelData(self._io, self, self._root)
            elif _on == 140:
                self.params = GloverLevel.Wind(self._io, self, self._root)
            elif _on == 122:
                self.params = GloverLevel.PlatStr0x7a(self._io, self, self._root)
            elif _on == 179:
                self.params = GloverLevel.PlatActorEnableWaterAnimation(self._io, self, self._root)
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
                self.params = GloverLevel.BuzzerDutyCycle(self._io, self, self._root)
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
                self.params = GloverLevel.EnemyFinalize(self._io, self, self._root)
            elif _on == 92:
                self.params = GloverLevel.PlatVentAdvanceFrames(self._io, self, self._root)
            elif _on == 198:
                self.params = GloverLevel.Plat0xc6(self._io, self, self._root)
            elif _on == 111:
                self.params = GloverLevel.PlatSetTag(self._io, self, self._root)
            elif _on == 190:
                self.params = GloverLevel.EnvironmentalSound(self._io, self, self._root)
            elif _on == 196:
                self.params = GloverLevel.PlatOrbitSound0xc4(self._io, self, self._root)
            elif _on == 183:
                self.params = GloverLevel.SetGlobal0xb7(self._io, self, self._root)
            elif _on == 128:
                self.params = GloverLevel.PlatSpin0x80(self._io, self, self._root)
            elif _on == 90:
                self.params = GloverLevel.PlatMvspn0x5a(self._io, self, self._root)
            elif _on == 154:
                self.params = GloverLevel.EnemyNormalInstruction(self._io, self, self._root)
            else:
                self.params = GloverLevel.Unknown(self._io, self, self._root)
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
        SEQ_FIELDS = ["left", "top", "front", "width", "height", "depth", "vel_x", "vel_y", "vel_z", "turbulence", "unknown_0x2c", "active", "tag"]
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
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_f4be()
            self._debug['height']['end'] = self._io.pos()
            self._debug['depth']['start'] = self._io.pos()
            self.depth = self._io.read_f4be()
            self._debug['depth']['end'] = self._io.pos()
            self._debug['vel_x']['start'] = self._io.pos()
            self.vel_x = self._io.read_f4be()
            self._debug['vel_x']['end'] = self._io.pos()
            self._debug['vel_y']['start'] = self._io.pos()
            self.vel_y = self._io.read_f4be()
            self._debug['vel_y']['end'] = self._io.pos()
            self._debug['vel_z']['start'] = self._io.pos()
            self.vel_z = self._io.read_f4be()
            self._debug['vel_z']['end'] = self._io.pos()
            self._debug['turbulence']['start'] = self._io.pos()
            self.turbulence = self._io.read_f4be()
            self._debug['turbulence']['end'] = self._io.pos()
            self._debug['unknown_0x2c']['start'] = self._io.pos()
            self.unknown_0x2c = self._io.read_u4be()
            self._debug['unknown_0x2c']['end'] = self._io.pos()
            self._debug['active']['start'] = self._io.pos()
            self.active = self._io.read_u4be()
            self._debug['active']['end'] = self._io.pos()
            self._debug['tag']['start'] = self._io.pos()
            self.tag = self._io.read_u4be()
            self._debug['tag']['end'] = self._io.pos()


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
        SEQ_FIELDS = ["flags", "num_fragments", "fragment_object_id", "name"]
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
            self._debug['num_fragments']['start'] = self._io.pos()
            self.num_fragments = self._io.read_u4be()
            self._debug['num_fragments']['end'] = self._io.pos()
            self._debug['fragment_object_id']['start'] = self._io.pos()
            self.fragment_object_id = self._io.read_u4be()
            self._debug['fragment_object_id']['end'] = self._io.pos()
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


    class Noop(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


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


    class PlatNoClip(KaitaiStruct):
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


    class PlatOrbitSound0xc4(KaitaiStruct):
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


    class AmbientLight(KaitaiStruct):
        SEQ_FIELDS = ["r", "g", "b"]
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


    class Enemy(KaitaiStruct):

        class EnemyType(Enum):
            bovva = 7
            cannon = 8
            samtex = 9
            mallet = 10
            generalw = 11
            lionfish = 12
            chester = 13
            keg = 14
            reggie = 15
            swish = 16
            thrice = 17
            robes = 18
            fumble = 19
            mike = 20
            raptor = 21
            crumpet = 22
            tracey = 23
            yoofow = 24
            opec = 25
            cymon = 26
            sucker = 27
            bugle = 28
            dennis = 29
            chuck = 30
            hubchicken1 = 31
            frankie2 = 32
            kloset = 33
            willy = 34
            joff = 35
            cancer = 36
            kirk = 37
            robot = 38
            evilrobot = 39
            spank = 40
            babyspk2 = 41
            evilglove = 42
            dibber = 43
            brundle = 44
            malcom = 45
            spotty = 46
            gordon = 47
            sidney = 48
            weevil = 49
            chopstik = 50
            butterfly = 51
            spider = 52
            bat = 53
            frog = 54
            dragfly = 55
            boxthing = 56
            bug = 57
            nmefrog = 58
        SEQ_FIELDS = ["type", "u1", "x", "y", "z", "y_rotation"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(GloverLevel.Enemy.EnemyType, self._io.read_u2be())
            self._debug['type']['end'] = self._io.pos()
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


    class PlatOrbitPause(KaitaiStruct):
        SEQ_FIELDS = ["num_frames", "num_pauses"]
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
            self._debug['num_pauses']['start'] = self._io.pos()
            self.num_pauses = self._io.read_u2be()
            self._debug['num_pauses']['end'] = self._io.pos()


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

        class GaribType(Enum):
            garib = 0
            bang_500pt = 1
            extra_life = 2
            mad_garib = 3
        SEQ_FIELDS = ["x", "y", "z", "type", "dynamic_shadow"]
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
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(GloverLevel.Garib.GaribType, self._io.read_u2be())
            self._debug['type']['end'] = self._io.pos()
            self._debug['dynamic_shadow']['start'] = self._io.pos()
            self.dynamic_shadow = self._io.read_u2be()
            self._debug['dynamic_shadow']['end'] = self._io.pos()


    class GaribGroup(KaitaiStruct):
        SEQ_FIELDS = ["group_id", "initial_state"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['group_id']['start'] = self._io.pos()
            self.group_id = self._io.read_u2be()
            self._debug['group_id']['end'] = self._io.pos()
            self._debug['initial_state']['start'] = self._io.pos()
            self.initial_state = self._io.read_s2be()
            self._debug['initial_state']['end'] = self._io.pos()


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


    class AnimatedBackgroundActor(KaitaiStruct):
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


    class BackgroundActor(KaitaiStruct):
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


    class EnemyInstructionMove(KaitaiStruct):
        SEQ_FIELDS = ["destination_x", "destination_y", "destination_z", "vel_magnitude"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['destination_x']['start'] = self._io.pos()
            self.destination_x = self._io.read_f4be()
            self._debug['destination_x']['end'] = self._io.pos()
            self._debug['destination_y']['start'] = self._io.pos()
            self.destination_y = self._io.read_f4be()
            self._debug['destination_y']['end'] = self._io.pos()
            self._debug['destination_z']['start'] = self._io.pos()
            self.destination_z = self._io.read_f4be()
            self._debug['destination_z']['end'] = self._io.pos()
            self._debug['vel_magnitude']['start'] = self._io.pos()
            self.vel_magnitude = self._io.read_f4be()
            self._debug['vel_magnitude']['end'] = self._io.pos()


    class PlatPathPoint(KaitaiStruct):
        SEQ_FIELDS = ["duration", "x", "y", "z"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['duration']['start'] = self._io.pos()
            self.duration = self._io.read_s2be()
            self._debug['duration']['end'] = self._io.pos()
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


    class PlatRocking(KaitaiStruct):
        SEQ_FIELDS = ["axis", "theta", "deceleration", "blur_height", "frame_advance"]
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
            self._debug['theta']['start'] = self._io.pos()
            self.theta = self._io.read_f4be()
            self._debug['theta']['end'] = self._io.pos()
            self._debug['deceleration']['start'] = self._io.pos()
            self.deceleration = self._io.read_f4be()
            self._debug['deceleration']['end'] = self._io.pos()
            self._debug['blur_height']['start'] = self._io.pos()
            self.blur_height = self._io.read_f4be()
            self._debug['blur_height']['end'] = self._io.pos()
            self._debug['frame_advance']['start'] = self._io.pos()
            self.frame_advance = self._io.read_u2be()
            self._debug['frame_advance']['end'] = self._io.pos()


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


    class GloverSpawnPoint(KaitaiStruct):
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


    class BuzzerDutyCycle(KaitaiStruct):
        SEQ_FIELDS = ["frames_off", "frames_on"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['frames_off']['start'] = self._io.pos()
            self.frames_off = self._io.read_u2be()
            self._debug['frames_off']['end'] = self._io.pos()
            self._debug['frames_on']['start'] = self._io.pos()
            self.frames_on = self._io.read_u2be()
            self._debug['frames_on']['end'] = self._io.pos()


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


    class PlatPlayObjectAnimation(KaitaiStruct):
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


    class EnemyInstructionPlayAnimation(KaitaiStruct):
        SEQ_FIELDS = ["anim_idx_1", "anim_idx_2"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['anim_idx_1']['start'] = self._io.pos()
            self.anim_idx_1 = self._io.read_s4be()
            self._debug['anim_idx_1']['end'] = self._io.pos()
            self._debug['anim_idx_2']['start'] = self._io.pos()
            self.anim_idx_2 = self._io.read_s4be()
            self._debug['anim_idx_2']['end'] = self._io.pos()


    class EnemyInstructionRandomWalk(KaitaiStruct):
        SEQ_FIELDS = ["home_x", "home_y", "home_z", "extent_x", "extent_y", "extent_z", "min_travel_distance"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['home_x']['start'] = self._io.pos()
            self.home_x = self._io.read_f4be()
            self._debug['home_x']['end'] = self._io.pos()
            self._debug['home_y']['start'] = self._io.pos()
            self.home_y = self._io.read_f4be()
            self._debug['home_y']['end'] = self._io.pos()
            self._debug['home_z']['start'] = self._io.pos()
            self.home_z = self._io.read_f4be()
            self._debug['home_z']['end'] = self._io.pos()
            self._debug['extent_x']['start'] = self._io.pos()
            self.extent_x = self._io.read_f4be()
            self._debug['extent_x']['end'] = self._io.pos()
            self._debug['extent_y']['start'] = self._io.pos()
            self.extent_y = self._io.read_f4be()
            self._debug['extent_y']['end'] = self._io.pos()
            self._debug['extent_z']['start'] = self._io.pos()
            self.extent_z = self._io.read_f4be()
            self._debug['extent_z']['end'] = self._io.pos()
            self._debug['min_travel_distance']['start'] = self._io.pos()
            self.min_travel_distance = self._io.read_f4be()
            self._debug['min_travel_distance']['end'] = self._io.pos()


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

        class ExecutionConditionType(Enum):
            ball_within_range = 0
            ball_within_ground_range = 1
            glover_within_range = 2
            glover_within_ground_range = 3
            ball_or_glover_within_range = 4
            ball_or_glover_within_ground_range = 5
            ball_within_angle_of_view = 6
            glover_within_angle_of_view = 7
            ball_or_glover_within_angle_of_view = 8
            periodic = 9
            roll_angle_within_range_and_periodic = 10
            glover_holding_ball = 11
            glover_not_holding_ball = 12
            enemy_holding_ball = 13
            enemy_not_holding_ball = 14
            glover_holding_enemy = 15
            glover_not_holding_enemy = 16
            on_ball = 17
            on_glover = 18
            enemy_within_attention_bbox = 19
            always = 20
            never = 21
            random_chance_param_a_over_1000 = 22

        class InstructionFlags(Enum):
            face_player = 1048576
            face_ball = 2097152
            face_closer_of_player_or_ball = 4194304
        SEQ_FIELDS = ["instr_type", "lifetime", "params", "execution_condition_param_a", "execution_condition_param_b", "flags", "execution_condition"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['instr_type']['start'] = self._io.pos()
            self.instr_type = self._io.read_u2be()
            self._debug['instr_type']['end'] = self._io.pos()
            self._debug['lifetime']['start'] = self._io.pos()
            self.lifetime = self._io.read_s2be()
            self._debug['lifetime']['end'] = self._io.pos()
            self._debug['params']['start'] = self._io.pos()
            _on = self.instr_type
            if _on == 14:
                self.params = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 10:
                self.params = GloverLevel.EnemyInstructionA(self._io, self, self._root)
            elif _on == 17:
                self.params = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 0:
                self.params = GloverLevel.EnemyInstructionMove(self._io, self, self._root)
            elif _on == 4:
                self.params = GloverLevel.EnemyInstructionRest(self._io, self, self._root)
            elif _on == 24:
                self.params = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 6:
                self.params = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 20:
                self.params = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 7:
                self.params = GloverLevel.EnemyInstructionPlayAnimation(self._io, self, self._root)
            elif _on == 1:
                self.params = GloverLevel.EnemyInstructionDash(self._io, self, self._root)
            elif _on == 13:
                self.params = GloverLevel.EnemyInstructionA(self._io, self, self._root)
            elif _on == 11:
                self.params = GloverLevel.EnemyInstructionA(self._io, self, self._root)
            elif _on == 12:
                self.params = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 3:
                self.params = GloverLevel.EnemyInstructionRandomWalk(self._io, self, self._root)
            elif _on == 5:
                self.params = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 19:
                self.params = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 23:
                self.params = GloverLevel.EnemyInstructionA(self._io, self, self._root)
            elif _on == 15:
                self.params = GloverLevel.EnemyInstructionAttack(self._io, self, self._root)
            elif _on == 8:
                self.params = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 9:
                self.params = GloverLevel.EnemyInstructionA(self._io, self, self._root)
            elif _on == 21:
                self.params = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 16:
                self.params = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 18:
                self.params = GloverLevel.EnemyInstructionGoto(self._io, self, self._root)
            elif _on == 2:
                self.params = GloverLevel.EnemyInstructionTurn(self._io, self, self._root)
            elif _on == 22:
                self.params = GloverLevel.EnemyInstructionA(self._io, self, self._root)
            else:
                self.params = GloverLevel.EnemyInstructionError(self._io, self, self._root)
            self._debug['params']['end'] = self._io.pos()
            self._debug['execution_condition_param_a']['start'] = self._io.pos()
            self.execution_condition_param_a = self._io.read_f4be()
            self._debug['execution_condition_param_a']['end'] = self._io.pos()
            self._debug['execution_condition_param_b']['start'] = self._io.pos()
            self.execution_condition_param_b = self._io.read_f4be()
            self._debug['execution_condition_param_b']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.EnemyInstruction.InstructionFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()
            self._debug['execution_condition']['start'] = self._io.pos()
            self.execution_condition = KaitaiStream.resolve_enum(GloverLevel.EnemyInstruction.ExecutionConditionType, self._io.read_u2be())
            self._debug['execution_condition']['end'] = self._io.pos()


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


    class PlatOrbitAroundPoint(KaitaiStruct):
        SEQ_FIELDS = ["axis", "x", "y", "z", "speed"]
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
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f4be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()
            self._debug['speed']['start'] = self._io.pos()
            self.speed = self._io.read_f4be()
            self._debug['speed']['end'] = self._io.pos()


    class Rope(KaitaiStruct):
        SEQ_FIELDS = ["num_components", "wiggle_axis", "component_obj_id", "name", "puzzle_unknown_1", "sway_unknown_1", "sway_unknown_2", "sway_unknown_3", "sway_rocking_theta", "sway_unknown_4", "sway_unknown_5", "x", "y", "z", "component_w", "component_h", "component_d"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_components']['start'] = self._io.pos()
            self.num_components = self._io.read_u4be()
            self._debug['num_components']['end'] = self._io.pos()
            self._debug['wiggle_axis']['start'] = self._io.pos()
            self.wiggle_axis = self._io.read_u2be()
            self._debug['wiggle_axis']['end'] = self._io.pos()
            self._debug['component_obj_id']['start'] = self._io.pos()
            self.component_obj_id = self._io.read_u4be()
            self._debug['component_obj_id']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(8)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['puzzle_unknown_1']['start'] = self._io.pos()
            self.puzzle_unknown_1 = self._io.read_f4be()
            self._debug['puzzle_unknown_1']['end'] = self._io.pos()
            self._debug['sway_unknown_1']['start'] = self._io.pos()
            self.sway_unknown_1 = self._io.read_f4be()
            self._debug['sway_unknown_1']['end'] = self._io.pos()
            self._debug['sway_unknown_2']['start'] = self._io.pos()
            self.sway_unknown_2 = self._io.read_f4be()
            self._debug['sway_unknown_2']['end'] = self._io.pos()
            self._debug['sway_unknown_3']['start'] = self._io.pos()
            self.sway_unknown_3 = self._io.read_f4be()
            self._debug['sway_unknown_3']['end'] = self._io.pos()
            self._debug['sway_rocking_theta']['start'] = self._io.pos()
            self.sway_rocking_theta = self._io.read_u4be()
            self._debug['sway_rocking_theta']['end'] = self._io.pos()
            self._debug['sway_unknown_4']['start'] = self._io.pos()
            self.sway_unknown_4 = self._io.read_u4be()
            self._debug['sway_unknown_4']['end'] = self._io.pos()
            self._debug['sway_unknown_5']['start'] = self._io.pos()
            self.sway_unknown_5 = self._io.read_f4be()
            self._debug['sway_unknown_5']['end'] = self._io.pos()
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f4be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()
            self._debug['component_w']['start'] = self._io.pos()
            self.component_w = self._io.read_f4be()
            self._debug['component_w']['end'] = self._io.pos()
            self._debug['component_h']['start'] = self._io.pos()
            self.component_h = self._io.read_f4be()
            self._debug['component_h']['end'] = self._io.pos()
            self._debug['component_d']['start'] = self._io.pos()
            self.component_d = self._io.read_f4be()
            self._debug['component_d']['end'] = self._io.pos()


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


    class EnemyInstructionGoto(KaitaiStruct):
        SEQ_FIELDS = ["instr_idx", "unused"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['instr_idx']['start'] = self._io.pos()
            self.instr_idx = self._io.read_u4be()
            self._debug['instr_idx']['end'] = self._io.pos()
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_u4be()
            self._debug['unused']['end'] = self._io.pos()


    class EnemyInstructionA(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x02", "u32_0x06", "u32_0x0a", "u32_0x0e"]
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


    class CameraSpawnPoint(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z", "pitch", "yaw"]
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
            self._debug['pitch']['start'] = self._io.pos()
            self.pitch = self._io.read_f4be()
            self._debug['pitch']['end'] = self._io.pos()
            self._debug['yaw']['start'] = self._io.pos()
            self.yaw = self._io.read_f4be()
            self._debug['yaw']['end'] = self._io.pos()


    class PlatSpinFlip(KaitaiStruct):
        SEQ_FIELDS = ["cooldown_timer", "theta"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['cooldown_timer']['start'] = self._io.pos()
            self.cooldown_timer = self._io.read_u2be()
            self._debug['cooldown_timer']['end'] = self._io.pos()
            self._debug['theta']['start'] = self._io.pos()
            self.theta = self._io.read_f4be()
            self._debug['theta']['end'] = self._io.pos()


    class EnemySetAttentionBbox(KaitaiStruct):
        SEQ_FIELDS = ["left", "top", "front", "width", "height", "depth"]
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
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_f4be()
            self._debug['height']['end'] = self._io.pos()
            self._debug['depth']['start'] = self._io.pos()
            self.depth = self._io.read_f4be()
            self._debug['depth']['end'] = self._io.pos()




#############
# PATCHED BY ./python/scripts/ksy-patcher.py

switch_fields = {
    'GloverLevel.Cmd': {
        'params': {
            'field': 'type_code',
            'code-to-type': {
                0xbd: GloverLevel.UnknownSound0xbd,
                0xbe: GloverLevel.EnvironmentalSound,
                0xa9: GloverLevel.Unknown0xa9,
                0xbb: GloverLevel.MrTip,
                0x97: GloverLevel.DiffuseLight,
                0x98: GloverLevel.AmbientLight,
                0x1: GloverLevel.GloverSpawnPoint,
                0x2: GloverLevel.BallSpawnPoint,
                0x3: GloverLevel.CameraSpawnPoint,
                0xa5: GloverLevel.FogConfiguration,
                0xbf: GloverLevel.Actor0xbf,
                0xbc: GloverLevel.AnimatedBackgroundActor,
                0x91: GloverLevel.BackgroundActor,
                0x92: GloverLevel.LandActor,
                0x93: GloverLevel.SetActorRotation,
                0x94: GloverLevel.SetActorScale,
                0x8c: GloverLevel.Wind,
                0xa0: GloverLevel.Water,
                0x99: GloverLevel.Backdrop,
                0xaa: GloverLevel.Cameo,
                0xab: GloverLevel.CameoInst,
                0x4: GloverLevel.Puzzle,
                0x5: GloverLevel.PuzzleAnd,
                0x6: GloverLevel.PuzzleOr,
                0x7: GloverLevel.PuzzleNumtimes,
                0x8: GloverLevel.PuzzleAny,
                0x95: GloverLevel.PuzzleCond,
                0x96: GloverLevel.PuzzleAction,
                0x85: GloverLevel.GaribGroup,
                0x86: GloverLevel.Garib,
                0x87: GloverLevel.Powerup,
                0x58: GloverLevel.PlatMvspn0x58,
                0x59: GloverLevel.PlatMvspn0x59,
                0x5a: GloverLevel.PlatMvspn0x5a,
                0x71: GloverLevel.PlatSetParent,
                0x73: GloverLevel.PlatMvspn0x73,
                0x74: GloverLevel.PlatMvspn0x74,
                0x7b: GloverLevel.PlatCopySpinFromParent,
                0xb8: GloverLevel.PlatSpecial0xb8,
                0xb3: GloverLevel.PlatActorEnableWaterAnimation,
                0xb7: GloverLevel.SetGlobal0xb7,
                0xb5: GloverLevel.Buzzer,
                0xb6: GloverLevel.BuzzerDutyCycle,
                0xb4: GloverLevel.SetObjectSparkle,
                0xb9: GloverLevel.PlatSpecial0xb9,
                0xa8: GloverLevel.SetExit,
                0x69: GloverLevel.PlatCat0x69,
                0x68: GloverLevel.PlatformConveyor,
                0x9e: GloverLevel.PlatSpecial0x9e,
                0x89: GloverLevel.SetTeleport,
                0x8a: GloverLevel.PlatFan0x8a,
                0x8b: GloverLevel.PlatMagnet0x8b,
                0x63: GloverLevel.PlatCheckpoint,
                0x67: GloverLevel.PlatCrumb0x67,
                0xc7: GloverLevel.PlatSpecial0xc7,
                0x6e: GloverLevel.PlatSpecial0x6e,
                0x8e: GloverLevel.PlatSpecial0x8e,
                0x5b: GloverLevel.PlatPush0x5b,
                0x72: GloverLevel.PlatConf0x72,
                0xc4: GloverLevel.PlatOrbitSound0xc4,
                0xc6: GloverLevel.Plat0xc6,
                0x75: GloverLevel.PlatOrbitAroundPoint,
                0x76: GloverLevel.PlatOrbitPause,
                0x77: GloverLevel.PlatOrbitFlip0x77,
                0xc3: GloverLevel.Plat0xc3,
                0xc5: GloverLevel.PlatSpinSound0xc5,
                0x9f: GloverLevel.Plat0x9f,
                0x7c: GloverLevel.PlatSpinPause0x7c,
                0x7d: GloverLevel.PlatSpinFlip,
                0x7e: GloverLevel.Plat0x7e,
                0x7f: GloverLevel.PlatConstantSpin,
                0x80: GloverLevel.PlatSpin0x80,
                0x81: GloverLevel.PlatTopple0x81,
                0x60: GloverLevel.LookAtHand0x60,
                0x61: GloverLevel.LookAtBall0x61,
                0x70: GloverLevel.PlatRocking,
                0x78: GloverLevel.Plat0x78,
                0xc1: GloverLevel.PlatSound0xc1,
                0xc2: GloverLevel.PlatSound0xc2,
                0x5e: GloverLevel.PlatTurnTowardsPathPoint,
                0x5f: GloverLevel.PlatGoForwards0x5f,
                0x6b: GloverLevel.PlatPathPoint,
                0x6c: GloverLevel.PlatMaxVelocity,
                0x6d: GloverLevel.PlatPathAcceleration,
                0xa7: GloverLevel.PlatPos0xa7,
                0xa6: GloverLevel.PlatSetInitialPos,
                0xc0: GloverLevel.PlatPlayObjectAnimation,
                0xa4: GloverLevel.Plat0xa4,
                0x5c: GloverLevel.PlatVentAdvanceFrames,
                0x64: GloverLevel.PlatNoClip,
                0x65: GloverLevel.PlatDestructible,
                0xc8: GloverLevel.PlatDestructibleSound,
                0x9d: GloverLevel.Plat0x9d,
                0x66: GloverLevel.Plat0x66,
                0x6a: GloverLevel.PlatActorSurfaceType,
                0x6f: GloverLevel.PlatSetTag,
                0x82: GloverLevel.PlatSpike,
                0x79: GloverLevel.PlatScale,
                0x7a: GloverLevel.PlatStr0x7a,
                0x8d: GloverLevel.Rope,
                0x90: GloverLevel.PlatSine,
                0x8f: GloverLevel.PlatOrbit,
                0xa2: GloverLevel.Vent,
                0xa3: GloverLevel.VentDutyCycle,
                0x62: GloverLevel.Platform,
                0x5d: GloverLevel.NullPlatform,
                0x83: GloverLevel.Enemy,
                0xa1: GloverLevel.EnemySetAttentionBbox,
                0xba: GloverLevel.Enemy0xba,
                0x84: GloverLevel.EnemyFinalize,
                0x9a: GloverLevel.EnemyNormalInstruction,
                0x9b: GloverLevel.EnemyConditionalInstruction,
                0x9c: GloverLevel.EnemyAttackInstruction,
                0x7d00: GloverLevel.EndLevelData,
                0x0: GloverLevel.Noop,
                None: GloverLevel.Unknown,
            },
            'type-to-code': {
                GloverLevel.UnknownSound0xbd: 0xbd,
                GloverLevel.EnvironmentalSound: 0xbe,
                GloverLevel.Unknown0xa9: 0xa9,
                GloverLevel.MrTip: 0xbb,
                GloverLevel.DiffuseLight: 0x97,
                GloverLevel.AmbientLight: 0x98,
                GloverLevel.GloverSpawnPoint: 0x1,
                GloverLevel.BallSpawnPoint: 0x2,
                GloverLevel.CameraSpawnPoint: 0x3,
                GloverLevel.FogConfiguration: 0xa5,
                GloverLevel.Actor0xbf: 0xbf,
                GloverLevel.AnimatedBackgroundActor: 0xbc,
                GloverLevel.BackgroundActor: 0x91,
                GloverLevel.LandActor: 0x92,
                GloverLevel.SetActorRotation: 0x93,
                GloverLevel.SetActorScale: 0x94,
                GloverLevel.Wind: 0x8c,
                GloverLevel.Water: 0xa0,
                GloverLevel.Backdrop: 0x99,
                GloverLevel.Cameo: 0xaa,
                GloverLevel.CameoInst: 0xab,
                GloverLevel.Puzzle: 0x4,
                GloverLevel.PuzzleAnd: 0x5,
                GloverLevel.PuzzleOr: 0x6,
                GloverLevel.PuzzleNumtimes: 0x7,
                GloverLevel.PuzzleAny: 0x8,
                GloverLevel.PuzzleCond: 0x95,
                GloverLevel.PuzzleAction: 0x96,
                GloverLevel.GaribGroup: 0x85,
                GloverLevel.Garib: 0x86,
                GloverLevel.Powerup: 0x87,
                GloverLevel.PlatMvspn0x58: 0x58,
                GloverLevel.PlatMvspn0x59: 0x59,
                GloverLevel.PlatMvspn0x5a: 0x5a,
                GloverLevel.PlatSetParent: 0x71,
                GloverLevel.PlatMvspn0x73: 0x73,
                GloverLevel.PlatMvspn0x74: 0x74,
                GloverLevel.PlatCopySpinFromParent: 0x7b,
                GloverLevel.PlatSpecial0xb8: 0xb8,
                GloverLevel.PlatActorEnableWaterAnimation: 0xb3,
                GloverLevel.SetGlobal0xb7: 0xb7,
                GloverLevel.Buzzer: 0xb5,
                GloverLevel.BuzzerDutyCycle: 0xb6,
                GloverLevel.SetObjectSparkle: 0xb4,
                GloverLevel.PlatSpecial0xb9: 0xb9,
                GloverLevel.SetExit: 0xa8,
                GloverLevel.PlatCat0x69: 0x69,
                GloverLevel.PlatformConveyor: 0x68,
                GloverLevel.PlatSpecial0x9e: 0x9e,
                GloverLevel.SetTeleport: 0x89,
                GloverLevel.PlatFan0x8a: 0x8a,
                GloverLevel.PlatMagnet0x8b: 0x8b,
                GloverLevel.PlatCheckpoint: 0x63,
                GloverLevel.PlatCrumb0x67: 0x67,
                GloverLevel.PlatSpecial0xc7: 0xc7,
                GloverLevel.PlatSpecial0x6e: 0x6e,
                GloverLevel.PlatSpecial0x8e: 0x8e,
                GloverLevel.PlatPush0x5b: 0x5b,
                GloverLevel.PlatConf0x72: 0x72,
                GloverLevel.PlatOrbitSound0xc4: 0xc4,
                GloverLevel.Plat0xc6: 0xc6,
                GloverLevel.PlatOrbitAroundPoint: 0x75,
                GloverLevel.PlatOrbitPause: 0x76,
                GloverLevel.PlatOrbitFlip0x77: 0x77,
                GloverLevel.Plat0xc3: 0xc3,
                GloverLevel.PlatSpinSound0xc5: 0xc5,
                GloverLevel.Plat0x9f: 0x9f,
                GloverLevel.PlatSpinPause0x7c: 0x7c,
                GloverLevel.PlatSpinFlip: 0x7d,
                GloverLevel.Plat0x7e: 0x7e,
                GloverLevel.PlatConstantSpin: 0x7f,
                GloverLevel.PlatSpin0x80: 0x80,
                GloverLevel.PlatTopple0x81: 0x81,
                GloverLevel.LookAtHand0x60: 0x60,
                GloverLevel.LookAtBall0x61: 0x61,
                GloverLevel.PlatRocking: 0x70,
                GloverLevel.Plat0x78: 0x78,
                GloverLevel.PlatSound0xc1: 0xc1,
                GloverLevel.PlatSound0xc2: 0xc2,
                GloverLevel.PlatTurnTowardsPathPoint: 0x5e,
                GloverLevel.PlatGoForwards0x5f: 0x5f,
                GloverLevel.PlatPathPoint: 0x6b,
                GloverLevel.PlatMaxVelocity: 0x6c,
                GloverLevel.PlatPathAcceleration: 0x6d,
                GloverLevel.PlatPos0xa7: 0xa7,
                GloverLevel.PlatSetInitialPos: 0xa6,
                GloverLevel.PlatPlayObjectAnimation: 0xc0,
                GloverLevel.Plat0xa4: 0xa4,
                GloverLevel.PlatVentAdvanceFrames: 0x5c,
                GloverLevel.PlatNoClip: 0x64,
                GloverLevel.PlatDestructible: 0x65,
                GloverLevel.PlatDestructibleSound: 0xc8,
                GloverLevel.Plat0x9d: 0x9d,
                GloverLevel.Plat0x66: 0x66,
                GloverLevel.PlatActorSurfaceType: 0x6a,
                GloverLevel.PlatSetTag: 0x6f,
                GloverLevel.PlatSpike: 0x82,
                GloverLevel.PlatScale: 0x79,
                GloverLevel.PlatStr0x7a: 0x7a,
                GloverLevel.Rope: 0x8d,
                GloverLevel.PlatSine: 0x90,
                GloverLevel.PlatOrbit: 0x8f,
                GloverLevel.Vent: 0xa2,
                GloverLevel.VentDutyCycle: 0xa3,
                GloverLevel.Platform: 0x62,
                GloverLevel.NullPlatform: 0x5d,
                GloverLevel.Enemy: 0x83,
                GloverLevel.EnemySetAttentionBbox: 0xa1,
                GloverLevel.Enemy0xba: 0xba,
                GloverLevel.EnemyFinalize: 0x84,
                GloverLevel.EnemyNormalInstruction: 0x9a,
                GloverLevel.EnemyConditionalInstruction: 0x9b,
                GloverLevel.EnemyAttackInstruction: 0x9c,
                GloverLevel.EndLevelData: 0x7d00,
                GloverLevel.Noop: 0x0,
                GloverLevel.Unknown: None,
            }
        },
    },
    'GloverLevel.CameoInst': {
        'body': {
            'field': 'inst_type',
            'code-to-type': {
                0x0: GloverLevel.CameoInst0,
                0x1: GloverLevel.CameoInst1,
                0x2: GloverLevel.CameoInst2,
                0x3: GloverLevel.CameoInst3,
                0x4: GloverLevel.CameoInst4,
                0x5: GloverLevel.CameoInst5,
                0x6: GloverLevel.CameoInst6,
                None: GloverLevel.CameoInstDefault,
            },
            'type-to-code': {
                GloverLevel.CameoInst0: 0x0,
                GloverLevel.CameoInst1: 0x1,
                GloverLevel.CameoInst2: 0x2,
                GloverLevel.CameoInst3: 0x3,
                GloverLevel.CameoInst4: 0x4,
                GloverLevel.CameoInst5: 0x5,
                GloverLevel.CameoInst6: 0x6,
                GloverLevel.CameoInstDefault: None,
            }
        },
    },
    'GloverLevel.PuzzleCond': {
        'body': {
            'field': 'cond_type',
            'code-to-type': {
                0x22: GloverLevel.PuzzleCondB,
                0x23: GloverLevel.PuzzleCondC,
                0x25: GloverLevel.PuzzleCondC,
                0x27: GloverLevel.PuzzleCondC,
                0x24: GloverLevel.PuzzleCondD,
                0x26: GloverLevel.PuzzleCondD,
                0x28: GloverLevel.PuzzleCondD,
                0x29: GloverLevel.PuzzleCondE,
                None: GloverLevel.PuzzleCondA,
            },
            'type-to-code': {
                GloverLevel.PuzzleCondB: 0x22,
                GloverLevel.PuzzleCondC: [35, 37, 39],
                GloverLevel.PuzzleCondD: [36, 38, 40],
                GloverLevel.PuzzleCondE: 0x29,
                GloverLevel.PuzzleCondA: None,
            }
        },
    },
    'GloverLevel.PuzzleAction': {
        'body': {
            'field': 'action_type',
            'code-to-type': {
                0x35: GloverLevel.PuzzleAction0x350x3b0x3c0x3d0x3e0x3f0x40,
                0x3b: GloverLevel.PuzzleAction0x350x3b0x3c0x3d0x3e0x3f0x40,
                0x3c: GloverLevel.PuzzleAction0x350x3b0x3c0x3d0x3e0x3f0x40,
                0x3d: GloverLevel.PuzzleAction0x350x3b0x3c0x3d0x3e0x3f0x40,
                0x3e: GloverLevel.PuzzleAction0x350x3b0x3c0x3d0x3e0x3f0x40,
                0x3f: GloverLevel.PuzzleAction0x350x3b0x3c0x3d0x3e0x3f0x40,
                0x40: GloverLevel.PuzzleAction0x350x3b0x3c0x3d0x3e0x3f0x40,
                0x4f: GloverLevel.PuzzleAction0x4f,
                0x46: GloverLevel.PuzzleAction0x460x470x48,
                0x47: GloverLevel.PuzzleAction0x460x470x48,
                0x48: GloverLevel.PuzzleAction0x460x470x48,
                0x49: GloverLevel.PuzzleAction0x490x4d,
                0x4d: GloverLevel.PuzzleAction0x490x4d,
                0x4a: GloverLevel.PuzzleAction0x4a,
                0x4b: GloverLevel.PuzzleAction0x4b0x4c,
                0x4c: GloverLevel.PuzzleAction0x4b0x4c,
                0x54: GloverLevel.PuzzleAction0x54,
                0x55: GloverLevel.PuzzleAction0x55,
                0x56: GloverLevel.PuzzleAction0x56,
                None: GloverLevel.PuzzleActionDefault,
            },
            'type-to-code': {
                GloverLevel.PuzzleAction0x350x3b0x3c0x3d0x3e0x3f0x40: [53, 59, 60, 61, 62, 63, 64],
                GloverLevel.PuzzleAction0x4f: 0x4f,
                GloverLevel.PuzzleAction0x460x470x48: [70, 71, 72],
                GloverLevel.PuzzleAction0x490x4d: [73, 77],
                GloverLevel.PuzzleAction0x4a: 0x4a,
                GloverLevel.PuzzleAction0x4b0x4c: [75, 76],
                GloverLevel.PuzzleAction0x54: 0x54,
                GloverLevel.PuzzleAction0x55: 0x55,
                GloverLevel.PuzzleAction0x56: 0x56,
                GloverLevel.PuzzleActionDefault: None,
            }
        },
    },
    'GloverLevel.EnemyInstruction': {
        'params': {
            'field': 'instr_type',
            'code-to-type': {
                0x0: GloverLevel.EnemyInstructionMove,
                0x1: GloverLevel.EnemyInstructionDash,
                0x2: GloverLevel.EnemyInstructionTurn,
                0x9: GloverLevel.EnemyInstructionA,
                0xa: GloverLevel.EnemyInstructionA,
                0xb: GloverLevel.EnemyInstructionA,
                0xd: GloverLevel.EnemyInstructionA,
                0x16: GloverLevel.EnemyInstructionA,
                0x17: GloverLevel.EnemyInstructionA,
                0x3: GloverLevel.EnemyInstructionRandomWalk,
                0x4: GloverLevel.EnemyInstructionRest,
                0x5: GloverLevel.EnemyInstructionC,
                0x6: GloverLevel.EnemyInstructionC,
                0x7: GloverLevel.EnemyInstructionPlayAnimation,
                0x8: GloverLevel.EnemyInstructionC,
                0xc: GloverLevel.EnemyInstructionC,
                0xe: GloverLevel.EnemyInstructionC,
                0xf: GloverLevel.EnemyInstructionAttack,
                0x10: GloverLevel.EnemyInstructionC,
                0x11: GloverLevel.EnemyInstructionC,
                0x12: GloverLevel.EnemyInstructionGoto,
                0x13: GloverLevel.EnemyInstructionC,
                0x14: GloverLevel.EnemyInstructionC,
                0x15: GloverLevel.EnemyInstructionC,
                0x18: GloverLevel.EnemyInstructionC,
                None: GloverLevel.EnemyInstructionError,
            },
            'type-to-code': {
                GloverLevel.EnemyInstructionMove: 0x0,
                GloverLevel.EnemyInstructionDash: 0x1,
                GloverLevel.EnemyInstructionTurn: 0x2,
                GloverLevel.EnemyInstructionA: [9, 10, 11, 13, 22, 23],
                GloverLevel.EnemyInstructionRandomWalk: 0x3,
                GloverLevel.EnemyInstructionRest: 0x4,
                GloverLevel.EnemyInstructionC: [5, 6, 8, 12, 14, 16, 17, 19, 20, 21, 24],
                GloverLevel.EnemyInstructionPlayAnimation: 0x7,
                GloverLevel.EnemyInstructionAttack: 0xf,
                GloverLevel.EnemyInstructionGoto: 0x12,
                GloverLevel.EnemyInstructionError: None,
            }
        },
    },
}
original_names = {
    'GloverLevel': 'glover_level',
    'GloverLevel.Cmd': 'glover_level.cmd',
    'GloverLevel.UnknownSound0xbd': 'glover_level.unknown_sound_0xbd',
    'GloverLevel.EnvironmentalSound': 'glover_level.environmental_sound',
    'GloverLevel.Unknown0xa9': 'glover_level.unknown_0xa9',
    'GloverLevel.MrTip': 'glover_level.mr_tip',
    'GloverLevel.DiffuseLight': 'glover_level.diffuse_light',
    'GloverLevel.AmbientLight': 'glover_level.ambient_light',
    'GloverLevel.GloverSpawnPoint': 'glover_level.glover_spawn_point',
    'GloverLevel.BallSpawnPoint': 'glover_level.ball_spawn_point',
    'GloverLevel.CameraSpawnPoint': 'glover_level.camera_spawn_point',
    'GloverLevel.FogConfiguration': 'glover_level.fog_configuration',
    'GloverLevel.Actor0xbf': 'glover_level.actor_0xbf',
    'GloverLevel.AnimatedBackgroundActor': 'glover_level.animated_background_actor',
    'GloverLevel.BackgroundActor': 'glover_level.background_actor',
    'GloverLevel.LandActor': 'glover_level.land_actor',
    'GloverLevel.SetActorRotation': 'glover_level.set_actor_rotation',
    'GloverLevel.SetActorScale': 'glover_level.set_actor_scale',
    'GloverLevel.Wind': 'glover_level.wind',
    'GloverLevel.Water': 'glover_level.water',
    'GloverLevel.Backdrop': 'glover_level.backdrop',
    'GloverLevel.Cameo': 'glover_level.cameo',
    'GloverLevel.CameoInst': 'glover_level.cameo_inst',
    'GloverLevel.CameoInst0': 'glover_level.cameo_inst_0',
    'GloverLevel.CameoInst1': 'glover_level.cameo_inst_1',
    'GloverLevel.CameoInst2': 'glover_level.cameo_inst_2',
    'GloverLevel.CameoInst3': 'glover_level.cameo_inst_3',
    'GloverLevel.CameoInst4': 'glover_level.cameo_inst_4',
    'GloverLevel.CameoInst5': 'glover_level.cameo_inst_5',
    'GloverLevel.CameoInst6': 'glover_level.cameo_inst_6',
    'GloverLevel.CameoInstDefault': 'glover_level.cameo_inst_default',
    'GloverLevel.Puzzle': 'glover_level.puzzle',
    'GloverLevel.PuzzleAnd': 'glover_level.puzzle_and',
    'GloverLevel.PuzzleOr': 'glover_level.puzzle_or',
    'GloverLevel.PuzzleNumtimes': 'glover_level.puzzle_numtimes',
    'GloverLevel.PuzzleAny': 'glover_level.puzzle_any',
    'GloverLevel.PuzzleCond': 'glover_level.puzzle_cond',
    'GloverLevel.PuzzleCondA': 'glover_level.puzzle_cond_a',
    'GloverLevel.PuzzleCondB': 'glover_level.puzzle_cond_b',
    'GloverLevel.PuzzleCondC': 'glover_level.puzzle_cond_c',
    'GloverLevel.PuzzleCondD': 'glover_level.puzzle_cond_d',
    'GloverLevel.PuzzleCondE': 'glover_level.puzzle_cond_e',
    'GloverLevel.PuzzleAction': 'glover_level.puzzle_action',
    'GloverLevel.PuzzleAction0x4f': 'glover_level.puzzle_action_0x4f',
    'GloverLevel.PuzzleAction0x350x3b0x3c0x3d0x3e0x3f0x40': 'glover_level.puzzle_action_0x35_0x3b_0x3c_0x3d_0x3e_0x3f_0x40',
    'GloverLevel.PuzzleActionDefault': 'glover_level.puzzle_action_default',
    'GloverLevel.PuzzleAction0x460x470x48': 'glover_level.puzzle_action_0x46_0x47_0x48',
    'GloverLevel.PuzzleAction0x490x4d': 'glover_level.puzzle_action_0x49_0x4d',
    'GloverLevel.PuzzleAction0x4a': 'glover_level.puzzle_action_0x4a',
    'GloverLevel.PuzzleAction0x54': 'glover_level.puzzle_action_0x54',
    'GloverLevel.PuzzleAction0x55': 'glover_level.puzzle_action_0x55',
    'GloverLevel.PuzzleAction0x56': 'glover_level.puzzle_action_0x56',
    'GloverLevel.PuzzleAction0x4b0x4c': 'glover_level.puzzle_action_0x4b_0x4c',
    'GloverLevel.GaribGroup': 'glover_level.garib_group',
    'GloverLevel.Garib': 'glover_level.garib',
    'GloverLevel.Powerup': 'glover_level.powerup',
    'GloverLevel.PlatMvspn0x58': 'glover_level.plat_mvspn_0x58',
    'GloverLevel.PlatMvspn0x59': 'glover_level.plat_mvspn_0x59',
    'GloverLevel.PlatMvspn0x5a': 'glover_level.plat_mvspn_0x5a',
    'GloverLevel.PlatSetParent': 'glover_level.plat_set_parent',
    'GloverLevel.PlatMvspn0x73': 'glover_level.plat_mvspn_0x73',
    'GloverLevel.PlatMvspn0x74': 'glover_level.plat_mvspn_0x74',
    'GloverLevel.PlatCopySpinFromParent': 'glover_level.plat_copy_spin_from_parent',
    'GloverLevel.PlatSpecial0xb8': 'glover_level.plat_special_0xb8',
    'GloverLevel.PlatActorEnableWaterAnimation': 'glover_level.plat_actor_enable_water_animation',
    'GloverLevel.SetGlobal0xb7': 'glover_level.set_global_0xb7',
    'GloverLevel.Buzzer': 'glover_level.buzzer',
    'GloverLevel.BuzzerDutyCycle': 'glover_level.buzzer_duty_cycle',
    'GloverLevel.SetObjectSparkle': 'glover_level.set_object_sparkle',
    'GloverLevel.PlatSpecial0xb9': 'glover_level.plat_special_0xb9',
    'GloverLevel.SetExit': 'glover_level.set_exit',
    'GloverLevel.PlatCat0x69': 'glover_level.plat_cat_0x69',
    'GloverLevel.PlatformConveyor': 'glover_level.platform_conveyor',
    'GloverLevel.PlatSpecial0x9e': 'glover_level.plat_special_0x9e',
    'GloverLevel.SetTeleport': 'glover_level.set_teleport',
    'GloverLevel.PlatFan0x8a': 'glover_level.plat_fan_0x8a',
    'GloverLevel.PlatMagnet0x8b': 'glover_level.plat_magnet_0x8b',
    'GloverLevel.PlatCheckpoint': 'glover_level.plat_checkpoint',
    'GloverLevel.PlatCrumb0x67': 'glover_level.plat_crumb_0x67',
    'GloverLevel.PlatSpecial0xc7': 'glover_level.plat_special_0xc7',
    'GloverLevel.PlatSpecial0x6e': 'glover_level.plat_special_0x6e',
    'GloverLevel.PlatSpecial0x8e': 'glover_level.plat_special_0x8e',
    'GloverLevel.PlatPush0x5b': 'glover_level.plat_push_0x5b',
    'GloverLevel.PlatConf0x72': 'glover_level.plat_conf_0x72',
    'GloverLevel.PlatOrbitSound0xc4': 'glover_level.plat_orbit_sound_0xc4',
    'GloverLevel.Plat0xc6': 'glover_level.plat_0xc6',
    'GloverLevel.PlatOrbitAroundPoint': 'glover_level.plat_orbit_around_point',
    'GloverLevel.PlatOrbitPause': 'glover_level.plat_orbit_pause',
    'GloverLevel.PlatOrbitFlip0x77': 'glover_level.plat_orbit_flip_0x77',
    'GloverLevel.Plat0xc3': 'glover_level.plat_0xc3',
    'GloverLevel.PlatSpinSound0xc5': 'glover_level.plat_spin_sound_0xc5',
    'GloverLevel.Plat0x9f': 'glover_level.plat_0x9f',
    'GloverLevel.PlatSpinPause0x7c': 'glover_level.plat_spin_pause_0x7c',
    'GloverLevel.PlatSpinFlip': 'glover_level.plat_spin_flip',
    'GloverLevel.Plat0x7e': 'glover_level.plat_0x7e',
    'GloverLevel.PlatConstantSpin': 'glover_level.plat_constant_spin',
    'GloverLevel.PlatSpin0x80': 'glover_level.plat_spin_0x80',
    'GloverLevel.PlatTopple0x81': 'glover_level.plat_topple_0x81',
    'GloverLevel.LookAtHand0x60': 'glover_level.look_at_hand_0x60',
    'GloverLevel.LookAtBall0x61': 'glover_level.look_at_ball_0x61',
    'GloverLevel.PlatRocking': 'glover_level.plat_rocking',
    'GloverLevel.Plat0x78': 'glover_level.plat_0x78',
    'GloverLevel.PlatSound0xc1': 'glover_level.plat_sound_0xc1',
    'GloverLevel.PlatSound0xc2': 'glover_level.plat_sound_0xc2',
    'GloverLevel.PlatTurnTowardsPathPoint': 'glover_level.plat_turn_towards_path_point',
    'GloverLevel.PlatGoForwards0x5f': 'glover_level.plat_go_forwards_0x5f',
    'GloverLevel.PlatPathPoint': 'glover_level.plat_path_point',
    'GloverLevel.PlatMaxVelocity': 'glover_level.plat_max_velocity',
    'GloverLevel.PlatPathAcceleration': 'glover_level.plat_path_acceleration',
    'GloverLevel.PlatPos0xa7': 'glover_level.plat_pos_0xa7',
    'GloverLevel.PlatSetInitialPos': 'glover_level.plat_set_initial_pos',
    'GloverLevel.PlatPlayObjectAnimation': 'glover_level.plat_play_object_animation',
    'GloverLevel.Plat0xa4': 'glover_level.plat_0xa4',
    'GloverLevel.PlatVentAdvanceFrames': 'glover_level.plat_vent_advance_frames',
    'GloverLevel.PlatNoClip': 'glover_level.plat_no_clip',
    'GloverLevel.PlatDestructible': 'glover_level.plat_destructible',
    'GloverLevel.PlatDestructibleSound': 'glover_level.plat_destructible_sound',
    'GloverLevel.Plat0x9d': 'glover_level.plat_0x9d',
    'GloverLevel.Plat0x66': 'glover_level.plat_0x66',
    'GloverLevel.PlatActorSurfaceType': 'glover_level.plat_actor_surface_type',
    'GloverLevel.PlatSetTag': 'glover_level.plat_set_tag',
    'GloverLevel.PlatSpike': 'glover_level.plat_spike',
    'GloverLevel.PlatScale': 'glover_level.plat_scale',
    'GloverLevel.PlatStr0x7a': 'glover_level.plat_str_0x7a',
    'GloverLevel.Rope': 'glover_level.rope',
    'GloverLevel.PlatSine': 'glover_level.plat_sine',
    'GloverLevel.PlatOrbit': 'glover_level.plat_orbit',
    'GloverLevel.Vent': 'glover_level.vent',
    'GloverLevel.VentDutyCycle': 'glover_level.vent_duty_cycle',
    'GloverLevel.Platform': 'glover_level.platform',
    'GloverLevel.NullPlatform': 'glover_level.null_platform',
    'GloverLevel.Enemy': 'glover_level.enemy',
    'GloverLevel.EnemySetAttentionBbox': 'glover_level.enemy_set_attention_bbox',
    'GloverLevel.Enemy0xba': 'glover_level.enemy_0xba',
    'GloverLevel.EnemyFinalize': 'glover_level.enemy_finalize',
    'GloverLevel.EnemyNormalInstruction': 'glover_level.enemy_normal_instruction',
    'GloverLevel.EnemyConditionalInstruction': 'glover_level.enemy_conditional_instruction',
    'GloverLevel.EnemyAttackInstruction': 'glover_level.enemy_attack_instruction',
    'GloverLevel.EnemyInstruction': 'glover_level.enemy_instruction',
    'GloverLevel.EnemyInstructionA': 'glover_level.enemy_instruction_a',
    'GloverLevel.EnemyInstructionDash': 'glover_level.enemy_instruction_dash',
    'GloverLevel.EnemyInstructionMove': 'glover_level.enemy_instruction_move',
    'GloverLevel.EnemyInstructionTurn': 'glover_level.enemy_instruction_turn',
    'GloverLevel.EnemyInstructionGoto': 'glover_level.enemy_instruction_goto',
    'GloverLevel.EnemyInstructionRandomWalk': 'glover_level.enemy_instruction_random_walk',
    'GloverLevel.EnemyInstructionPlayAnimation': 'glover_level.enemy_instruction_play_animation',
    'GloverLevel.EnemyInstructionRest': 'glover_level.enemy_instruction_rest',
    'GloverLevel.EnemyInstructionAttack': 'glover_level.enemy_instruction_attack',
    'GloverLevel.EnemyInstructionC': 'glover_level.enemy_instruction_c',
    'GloverLevel.EnemyInstructionError': 'glover_level.enemy_instruction_error',
    'GloverLevel.EndLevelData': 'glover_level.end_level_data',
    'GloverLevel.Noop': 'glover_level.noop',
    'GloverLevel.Unknown': 'glover_level.unknown',
}
private_fields = {
    'GloverLevel.Actor0xbf': {'semantic': {'modifies': ['LAND_ACTOR', 'BG_ACTOR', 'ANIMATED_BG_ACTOR']}},
    'GloverLevel.AnimatedBackgroundActor': {'semantic': {'declares': 'ANIMATED_BG_ACTOR'}, '_annotated_children': ['GloverLevel.AnimatedBackgroundActor.Seq[0]']},
    'GloverLevel.AnimatedBackgroundActor.Seq[0]': {'semantic': {'hash-namespace': 'object'}},
    'GloverLevel.BackgroundActor': {'semantic': {'declares': 'BG_ACTOR'}, '_annotated_children': ['GloverLevel.BackgroundActor.Seq[0]']},
    'GloverLevel.BackgroundActor.Seq[0]': {'semantic': {'hash-namespace': 'object'}},
    'GloverLevel.LandActor': {'semantic': {'declares': 'LAND_ACTOR'}, '_annotated_children': ['GloverLevel.LandActor.Seq[0]']},
    'GloverLevel.LandActor.Seq[0]': {'semantic': {'hash-namespace': 'object'}},
    'GloverLevel.SetActorRotation': {'semantic': {'modifies': ['LAND_ACTOR', 'BG_ACTOR', 'ANIMATED_BG_ACTOR']}},
    'GloverLevel.SetActorScale': {'semantic': {'modifies': ['LAND_ACTOR', 'BG_ACTOR', 'ANIMATED_BG_ACTOR']}},
    'GloverLevel.Water.Seq[10]': {'semantic': {'hash-namespace': 'object'}},
    'GloverLevel.Backdrop.Seq[0]': {'semantic': {'hash-namespace': 'texture'}},
    'GloverLevel.Cameo': {'semantic': {'declares': 'CAMEO'}},
    'GloverLevel.CameoInst': {'semantic': {'modifies': 'CAMEO'}},
    'GloverLevel.Puzzle': {'semantic': {'declares': 'PUZZLE'}},
    'GloverLevel.PuzzleAnd': {'semantic': {'modifies': 'PUZZLE'}},
    'GloverLevel.PuzzleOr': {'semantic': {'modifies': 'PUZZLE'}},
    'GloverLevel.PuzzleNumtimes': {'semantic': {'modifies': 'PUZZLE'}},
    'GloverLevel.PuzzleAny': {'semantic': {'modifies': 'PUZZLE'}},
    'GloverLevel.PuzzleCond': {'semantic': {'modifies': 'PUZZLE'}},
    'GloverLevel.PuzzleAction': {'semantic': {'modifies': 'PUZZLE'}},
    'GloverLevel.GaribGroup': {'semantic': {'declares': 'GARIB_GROUP'}},
    'GloverLevel.Garib': {'semantic': {'modifies': 'GARIB_GROUP'}},
    'GloverLevel.PlatMvspn0x58': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatMvspn0x59': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatMvspn0x5a': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatSetParent': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatMvspn0x73': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatMvspn0x74': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatCopySpinFromParent': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatSpecial0xb8': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatActorEnableWaterAnimation': {'semantic': {'modifies': ['PLATFORM', 'LAND_ACTOR', 'BG_ACTOR', 'ANIMATED_BG_ACTOR']}},
    'GloverLevel.Buzzer': {'semantic': {'declares': 'BUZZER'}},
    'GloverLevel.BuzzerDutyCycle': {'semantic': {'modifies': 'BUZZER'}},
    'GloverLevel.SetObjectSparkle': {'semantic': {'modifies': ['PLATFORM', 'LAND_ACTOR']}},
    'GloverLevel.PlatSpecial0xb9': {'semantic': {'modifies': ['PLATFORM', 'LAND_ACTOR']}},
    'GloverLevel.SetExit': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatCat0x69': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatformConveyor': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatSpecial0x9e': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.SetTeleport': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatFan0x8a': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatMagnet0x8b': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatCheckpoint': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatCrumb0x67': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatSpecial0xc7': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatSpecial0x6e': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatSpecial0x8e': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatPush0x5b': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatConf0x72': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatOrbitSound0xc4': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.Plat0xc6': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatOrbitAroundPoint': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatOrbitPause': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatOrbitFlip0x77': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.Plat0xc3': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatSpinSound0xc5': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.Plat0x9f': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatSpinPause0x7c': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatSpinFlip': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.Plat0x7e': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatConstantSpin': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatSpin0x80': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatTopple0x81': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.LookAtHand0x60': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.LookAtBall0x61': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatRocking': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.Plat0x78': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatSound0xc1': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatSound0xc2': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatTurnTowardsPathPoint': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatGoForwards0x5f': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatPathPoint': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatMaxVelocity': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatPathAcceleration': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatPos0xa7': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatSetInitialPos': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatPlayObjectAnimation': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.Plat0xa4': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatVentAdvanceFrames': {'semantic': {'modifies': ['PLATFORM', 'VENT']}},
    'GloverLevel.PlatNoClip': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatDestructible': {'semantic': {'modifies': 'PLATFORM'}, '_annotated_children': ['GloverLevel.PlatDestructible.Seq[2]']},
    'GloverLevel.PlatDestructible.Seq[2]': {'semantic': {'hash-namespace': 'object'}},
    'GloverLevel.PlatDestructibleSound': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.Plat0x9d': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.Plat0x66': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatActorSurfaceType': {'semantic': {'modifies': ['PLATFORM', 'LAND_ACTOR', 'BG_ACTOR', 'ANIMATED_BG_ACTOR']}},
    'GloverLevel.PlatSetTag': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatSpike': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatScale': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.Vent': {'semantic': {'declares': 'VENT'}},
    'GloverLevel.VentDutyCycle': {'semantic': {'modifies': 'VENT'}},
    'GloverLevel.Platform': {'semantic': {'declares': 'PLATFORM'}, '_annotated_children': ['GloverLevel.Platform.Seq[0]']},
    'GloverLevel.Platform.Seq[0]': {'semantic': {'hash-namespace': 'object'}},
    'GloverLevel.NullPlatform': {'semantic': {'declares': 'PLATFORM'}},
    'GloverLevel.Enemy': {'semantic': {'declares': 'ENEMY'}},
    'GloverLevel.EnemySetAttentionBbox': {'semantic': {'modifies': 'ENEMY'}},
    'GloverLevel.Enemy0xba': {'semantic': {'modifies': 'ENEMY'}},
    'GloverLevel.EnemyFinalize': {'semantic': {'modifies': 'ENEMY'}},
    'GloverLevel.EnemyNormalInstruction': {'semantic': {'modifies': 'ENEMY', 'groups-into': 'normal_instructions'}},
    'GloverLevel.EnemyConditionalInstruction': {'semantic': {'modifies': 'ENEMY', 'groups-into': 'conditional_instructions'}},
    'GloverLevel.EnemyAttackInstruction': {'semantic': {'modifies': 'ENEMY', 'groups-into': 'attack_instructions'}},
    'GloverLevel': {'_annotated_children': ['GloverLevel.Actor0xbf', 'GloverLevel.AnimatedBackgroundActor', 'GloverLevel.BackgroundActor', 'GloverLevel.LandActor', 'GloverLevel.SetActorRotation', 'GloverLevel.SetActorScale', 'GloverLevel.Cameo', 'GloverLevel.CameoInst', 'GloverLevel.Puzzle', 'GloverLevel.PuzzleAnd', 'GloverLevel.PuzzleOr', 'GloverLevel.PuzzleNumtimes', 'GloverLevel.PuzzleAny', 'GloverLevel.PuzzleCond', 'GloverLevel.PuzzleAction', 'GloverLevel.GaribGroup', 'GloverLevel.Garib', 'GloverLevel.PlatMvspn0x58', 'GloverLevel.PlatMvspn0x59', 'GloverLevel.PlatMvspn0x5a', 'GloverLevel.PlatSetParent', 'GloverLevel.PlatMvspn0x73', 'GloverLevel.PlatMvspn0x74', 'GloverLevel.PlatCopySpinFromParent', 'GloverLevel.PlatSpecial0xb8', 'GloverLevel.PlatActorEnableWaterAnimation', 'GloverLevel.Buzzer', 'GloverLevel.BuzzerDutyCycle', 'GloverLevel.SetObjectSparkle', 'GloverLevel.PlatSpecial0xb9', 'GloverLevel.SetExit', 'GloverLevel.PlatCat0x69', 'GloverLevel.PlatformConveyor', 'GloverLevel.PlatSpecial0x9e', 'GloverLevel.SetTeleport', 'GloverLevel.PlatFan0x8a', 'GloverLevel.PlatMagnet0x8b', 'GloverLevel.PlatCheckpoint', 'GloverLevel.PlatCrumb0x67', 'GloverLevel.PlatSpecial0xc7', 'GloverLevel.PlatSpecial0x6e', 'GloverLevel.PlatSpecial0x8e', 'GloverLevel.PlatPush0x5b', 'GloverLevel.PlatConf0x72', 'GloverLevel.PlatOrbitSound0xc4', 'GloverLevel.Plat0xc6', 'GloverLevel.PlatOrbitAroundPoint', 'GloverLevel.PlatOrbitPause', 'GloverLevel.PlatOrbitFlip0x77', 'GloverLevel.Plat0xc3', 'GloverLevel.PlatSpinSound0xc5', 'GloverLevel.Plat0x9f', 'GloverLevel.PlatSpinPause0x7c', 'GloverLevel.PlatSpinFlip', 'GloverLevel.Plat0x7e', 'GloverLevel.PlatConstantSpin', 'GloverLevel.PlatSpin0x80', 'GloverLevel.PlatTopple0x81', 'GloverLevel.LookAtHand0x60', 'GloverLevel.LookAtBall0x61', 'GloverLevel.PlatRocking', 'GloverLevel.Plat0x78', 'GloverLevel.PlatSound0xc1', 'GloverLevel.PlatSound0xc2', 'GloverLevel.PlatTurnTowardsPathPoint', 'GloverLevel.PlatGoForwards0x5f', 'GloverLevel.PlatPathPoint', 'GloverLevel.PlatMaxVelocity', 'GloverLevel.PlatPathAcceleration', 'GloverLevel.PlatPos0xa7', 'GloverLevel.PlatSetInitialPos', 'GloverLevel.PlatPlayObjectAnimation', 'GloverLevel.Plat0xa4', 'GloverLevel.PlatVentAdvanceFrames', 'GloverLevel.PlatNoClip', 'GloverLevel.PlatDestructible', 'GloverLevel.PlatDestructibleSound', 'GloverLevel.Plat0x9d', 'GloverLevel.Plat0x66', 'GloverLevel.PlatActorSurfaceType', 'GloverLevel.PlatSetTag', 'GloverLevel.PlatSpike', 'GloverLevel.PlatScale', 'GloverLevel.Vent', 'GloverLevel.VentDutyCycle', 'GloverLevel.Platform', 'GloverLevel.NullPlatform', 'GloverLevel.Enemy', 'GloverLevel.EnemySetAttentionBbox', 'GloverLevel.Enemy0xba', 'GloverLevel.EnemyFinalize', 'GloverLevel.EnemyNormalInstruction', 'GloverLevel.EnemyConditionalInstruction', 'GloverLevel.EnemyAttackInstruction']},
    'GloverLevel.Water': {'_annotated_children': ['GloverLevel.Water.Seq[10]']},
    'GloverLevel.Backdrop': {'_annotated_children': ['GloverLevel.Backdrop.Seq[0]']},
}

import importlib
import re
import sys

_module_cache = {}
_cls_cache = {}
@classmethod
def getConstructType(cls):
    global _module_cache
    global _cls_cache
    if cls.__qualname__ not in _cls_cache:
        if __name__ not in _module_cache:
            module_tokens = __name__.split(".")
            package_name = ".".join(module_tokens[:-1])
            module_name = module_tokens[-1]
            _module_cache[__name__] = importlib.import_module(".construct.{:}".format(module_name), package_name)
        construct_mod = _module_cache[__name__]
        type_name = cls.getOriginalName().replace(".", "__")
        _cls_cache[cls.__qualname__] = getattr(construct_mod, type_name)
    return _cls_cache[cls.__qualname__]
KaitaiStruct.getConstructType = getConstructType

@classmethod
def getOriginalName(cls):
    original_names = sys.modules[cls.__module__].original_names
    return original_names[cls.__qualname__]
KaitaiStruct.getOriginalName = getOriginalName

@classmethod
def getPrivate(cls, field_name, default=None):
    try:
        private_fields = sys.modules[cls.__module__].private_fields
    except AttributeError:
        return default
    if "." not in field_name:
        qualname = cls.__qualname__
    else:
        parent_field, field_name = field_name.split(".")
        try:
            seq_idx = cls.SEQ_FIELDS.index(parent_field)
        except ValueError:
            return default
        qualname = "{:}.Seq[{:}]".format(cls.__qualname__, seq_idx)
    return private_fields.get(qualname, {}).get(field_name, default)
KaitaiStruct.getPrivate = getPrivate

@classmethod
def getAnnotatedChildren(cls):
    try:
        private_fields = sys.modules[cls.__module__].private_fields
    except AttributeError:
        raise StopIteration()
    children = cls.getPrivate("_annotated_children", [])
    for child_key in children:
        subscript_suffix = re.findall(r"\[([0-9]+)\]$", child_key)
        if len(subscript_suffix) > 0:
            field_idx = int(re.findall(r"\[([0-9]+)\]$", child_key)[-1])
            child_name = cls.SEQ_FIELDS[field_idx]
        else:
            child_name = child_key
        yield child_name, private_fields[child_key]
KaitaiStruct.getAnnotatedChildren = getAnnotatedChildren

@classmethod
def getSwitches(cls):
    try:
        switch_fields = sys.modules[cls.__module__].switch_fields
    except AttributeError:
        return None
    return switch_fields.get(cls.__qualname__, {})
KaitaiStruct.getSwitches = getSwitches

ksy_hash = '903403fab83eb57e6cb63ee282643610e70f743a'
#############

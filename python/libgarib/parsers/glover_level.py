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

    class PuzzleCondGloverChangedTouchingPlatform(KaitaiStruct):
        SEQ_FIELDS = ["plat_tag", "started_or_stopped"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['started_or_stopped']['start'] = self._io.pos()
            self.started_or_stopped = self._io.read_s2be()
            self._debug['started_or_stopped']['end'] = self._io.pos()


    class EnemyInstructionSetTimer(KaitaiStruct):
        SEQ_FIELDS = ["value", "unused"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_s4be()
            self._debug['value']['end'] = self._io.pos()
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_u4be()
            self._debug['unused']['end'] = self._io.pos()


    class EnemyInstructionCatapult(KaitaiStruct):
        SEQ_FIELDS = ["vel_x", "vel_y", "vel_z", "unused"]
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
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_s4be()
            self._debug['unused']['end'] = self._io.pos()


    class PuzzleCondBallChangedTouchingPlatform(KaitaiStruct):
        SEQ_FIELDS = ["plat_tag", "started_or_stopped"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['started_or_stopped']['start'] = self._io.pos()
            self.started_or_stopped = self._io.read_s2be()
            self._debug['started_or_stopped']['end'] = self._io.pos()


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


    class PuzzleActionCameraFlyTowardsPoint(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z", "activation_delay"]
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
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()


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


    class PuzzleActionHidePlatform(KaitaiStruct):
        SEQ_FIELDS = ["hide_enabled", "platform_tag", "activation_delay", "flags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['hide_enabled']['start'] = self._io.pos()
            self.hide_enabled = self._io.read_u4be()
            self._debug['hide_enabled']['end'] = self._io.pos()
            self._debug['platform_tag']['start'] = self._io.pos()
            self.platform_tag = self._io.read_s2be()
            self._debug['platform_tag']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.GenericFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


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


    class PuzzleCondPlatformDoesntExist(KaitaiStruct):
        SEQ_FIELDS = ["plat_tag", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_u2be()
            self._debug['reserved']['end'] = self._io.pos()


    class PuzzleActionCameraTweenDistance(KaitaiStruct):
        SEQ_FIELDS = ["distance", "activation_delay"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['distance']['start'] = self._io.pos()
            self.distance = self._io.read_f4be()
            self._debug['distance']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()


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


    class PuzzleActionCameraLookAtPoint2(KaitaiStruct):
        SEQ_FIELDS = ["lookat_x", "lookat_y", "lookat_z", "duration", "reserved", "activation_delay", "flags"]
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
            self._debug['duration']['start'] = self._io.pos()
            self.duration = self._io.read_f4be()
            self._debug['duration']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_u2be()
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.CameraFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


    class EnemyInstructionBullet0x5(KaitaiStruct):
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
                self.body = GloverLevel.CameoPlayAnimation(self._io, self, self._root)
            elif _on == 4:
                self.body = GloverLevel.CameoGrabTodo(self._io, self, self._root)
            elif _on == 6:
                self.body = GloverLevel.CameoLightningFlash(self._io, self, self._root)
            elif _on == 1:
                self.body = GloverLevel.CameoSetCameraAttention(self._io, self, self._root)
            elif _on == 3:
                self.body = GloverLevel.CameoSpin(self._io, self, self._root)
            elif _on == 5:
                self.body = GloverLevel.CameoSetEnemyFlagTodo(self._io, self, self._root)
            elif _on == 2:
                self.body = GloverLevel.CameoInst2(self._io, self, self._root)
            else:
                self.body = GloverLevel.CameoInstDefault(self._io, self, self._root)
            self._debug['body']['end'] = self._io.pos()


    class PuzzleCondDefault(KaitaiStruct):
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


    class PuzzleActionRegSet(KaitaiStruct):
        SEQ_FIELDS = ["imm_val_or_src_reg", "dst_reg", "activation_delay", "flags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['imm_val_or_src_reg']['start'] = self._io.pos()
            self.imm_val_or_src_reg = self._io.read_f4be()
            self._debug['imm_val_or_src_reg']['end'] = self._io.pos()
            self._debug['dst_reg']['start'] = self._io.pos()
            self.dst_reg = self._io.read_u2be()
            self._debug['dst_reg']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.RegisterFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


    class PuzzleActionPlatformConfigOrbit(KaitaiStruct):
        SEQ_FIELDS = ["velocity", "platform_tag", "activation_delay", "flags"]
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
            self._debug['platform_tag']['start'] = self._io.pos()
            self.platform_tag = self._io.read_s2be()
            self._debug['platform_tag']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.PlatformMovementFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


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


    class PuzzleCondPlatformOrbitTodo(KaitaiStruct):
        SEQ_FIELDS = ["plat_tag", "idx"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['idx']['start'] = self._io.pos()
            self.idx = self._io.read_s2be()
            self._debug['idx']['end'] = self._io.pos()


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


    class PuzzleActionPlatformNudge(KaitaiStruct):
        SEQ_FIELDS = ["velocity", "platform_tag", "activation_delay", "flags"]
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
            self._debug['platform_tag']['start'] = self._io.pos()
            self.platform_tag = self._io.read_s2be()
            self._debug['platform_tag']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.PlatformMovementFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


    class EnemyInstructionGlom(KaitaiStruct):
        SEQ_FIELDS = ["u32_0x02", "u32_0x06", "u32_0x0a", "u32_0x0e"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u32_0x02']['start'] = self._io.pos()
            self.u32_0x02 = self._io.read_f4be()
            self._debug['u32_0x02']['end'] = self._io.pos()
            self._debug['u32_0x06']['start'] = self._io.pos()
            self.u32_0x06 = self._io.read_f4be()
            self._debug['u32_0x06']['end'] = self._io.pos()
            self._debug['u32_0x0a']['start'] = self._io.pos()
            self.u32_0x0a = self._io.read_f4be()
            self._debug['u32_0x0a']['end'] = self._io.pos()
            self._debug['u32_0x0e']['start'] = self._io.pos()
            self.u32_0x0e = self._io.read_s4be()
            self._debug['u32_0x0e']['end'] = self._io.pos()


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


    class PlatReverseAtEndsOfPath(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class PuzzleCondCameraWithinVolume(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z", "l", "w", "h"]
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
            self._debug['l']['start'] = self._io.pos()
            self.l = self._io.read_f4be()
            self._debug['l']['end'] = self._io.pos()
            self._debug['w']['start'] = self._io.pos()
            self.w = self._io.read_f4be()
            self._debug['w']['end'] = self._io.pos()
            self._debug['h']['start'] = self._io.pos()
            self.h = self._io.read_f4be()
            self._debug['h']['end'] = self._io.pos()


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


    class CameoSetEnemyFlagTodo(KaitaiStruct):
        SEQ_FIELDS = ["enemy_idx", "frame_count", "preceding_instr_idx"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['enemy_idx']['start'] = self._io.pos()
            self.enemy_idx = self._io.read_u2be()
            self._debug['enemy_idx']['end'] = self._io.pos()
            self._debug['frame_count']['start'] = self._io.pos()
            self.frame_count = self._io.read_s2be()
            self._debug['frame_count']['end'] = self._io.pos()
            self._debug['preceding_instr_idx']['start'] = self._io.pos()
            self.preceding_instr_idx = self._io.read_s2be()
            self._debug['preceding_instr_idx']['end'] = self._io.pos()


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


    class EnemyImpulseForward(KaitaiStruct):

        class AnimationBehaviorFlags(Enum):
            force_animation = 0
            do_not_force_animation = 16384
        SEQ_FIELDS = ["unused", "vel_y", "vel_forward", "animation_behavior"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_f4be()
            self._debug['unused']['end'] = self._io.pos()
            self._debug['vel_y']['start'] = self._io.pos()
            self.vel_y = self._io.read_f4be()
            self._debug['vel_y']['end'] = self._io.pos()
            self._debug['vel_forward']['start'] = self._io.pos()
            self.vel_forward = self._io.read_f4be()
            self._debug['vel_forward']['end'] = self._io.pos()
            self._debug['animation_behavior']['start'] = self._io.pos()
            self.animation_behavior = KaitaiStream.resolve_enum(GloverLevel.EnemyImpulseForward.AnimationBehaviorFlags, self._io.read_u4be())
            self._debug['animation_behavior']['end'] = self._io.pos()


    class PuzzleActionStartCameo(KaitaiStruct):
        SEQ_FIELDS = ["reserved", "cameo_idx", "activation_delay", "flags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_u4be()
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['cameo_idx']['start'] = self._io.pos()
            self.cameo_idx = self._io.read_s2be()
            self._debug['cameo_idx']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.GenericFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


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


    class PuzzleCondPlatformSpin2Todo(KaitaiStruct):
        SEQ_FIELDS = ["plat_tag", "arg2"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['arg2']['start'] = self._io.pos()
            self.arg2 = self._io.read_s2be()
            self._debug['arg2']['end'] = self._io.pos()


    class PuzzleCondEnemyIsTouchingPlatform(KaitaiStruct):
        SEQ_FIELDS = ["plat_tag", "invert_result"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['invert_result']['start'] = self._io.pos()
            self.invert_result = self._io.read_s2be()
            self._debug['invert_result']['end'] = self._io.pos()


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


    class PuzzleActionPlatformSpinAlongAxis(KaitaiStruct):
        SEQ_FIELDS = ["axis_idx", "platform_tag", "activation_delay", "flags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['axis_idx']['start'] = self._io.pos()
            self.axis_idx = self._io.read_u4be()
            self._debug['axis_idx']['end'] = self._io.pos()
            self._debug['platform_tag']['start'] = self._io.pos()
            self.platform_tag = self._io.read_s2be()
            self._debug['platform_tag']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.GenericFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


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


    class PlatPathSoundAtPointHit(KaitaiStruct):
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


    class SetGravity(KaitaiStruct):
        SEQ_FIELDS = ["strength"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['strength']['start'] = self._io.pos()
            self.strength = self._io.read_f4be()
            self._debug['strength']['end'] = self._io.pos()


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


    class PuzzleCondEnemyStandingOnPlatform(KaitaiStruct):
        SEQ_FIELDS = ["plat_tag", "invert_result"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['invert_result']['start'] = self._io.pos()
            self.invert_result = self._io.read_s2be()
            self._debug['invert_result']['end'] = self._io.pos()


    class PuzzleActionPlatformMoveToPointIdxMinusOne(KaitaiStruct):
        SEQ_FIELDS = ["point_idx", "platform_tag", "activation_delay", "flags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['point_idx']['start'] = self._io.pos()
            self.point_idx = self._io.read_u4be()
            self._debug['point_idx']['end'] = self._io.pos()
            self._debug['platform_tag']['start'] = self._io.pos()
            self.platform_tag = self._io.read_s2be()
            self._debug['platform_tag']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.GenericFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


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


    class EnemyInstructionFleePlayer(KaitaiStruct):
        SEQ_FIELDS = ["panic_radius", "unused"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['panic_radius']['start'] = self._io.pos()
            self.panic_radius = self._io.read_f4be()
            self._debug['panic_radius']['end'] = self._io.pos()
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_u4be()
            self._debug['unused']['end'] = self._io.pos()


    class PuzzleActionCameraLookAtGlover(KaitaiStruct):
        SEQ_FIELDS = ["angle", "distance", "activation_delay"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['angle']['start'] = self._io.pos()
            self.angle = self._io.read_f4be()
            self._debug['angle']['end'] = self._io.pos()
            self._debug['distance']['start'] = self._io.pos()
            self.distance = self._io.read_f4be()
            self._debug['distance']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()


    class PlatFan0x8a(KaitaiStruct):
        SEQ_FIELDS = ["enabled", "force_vector_x", "force_vector_y", "force_vector_z", "u32_0x10", "force_min_threshold", "u32_0x18", "force_vector_magnitude"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['enabled']['start'] = self._io.pos()
            self.enabled = self._io.read_u2be()
            self._debug['enabled']['end'] = self._io.pos()
            self._debug['force_vector_x']['start'] = self._io.pos()
            self.force_vector_x = self._io.read_f4be()
            self._debug['force_vector_x']['end'] = self._io.pos()
            self._debug['force_vector_y']['start'] = self._io.pos()
            self.force_vector_y = self._io.read_f4be()
            self._debug['force_vector_y']['end'] = self._io.pos()
            self._debug['force_vector_z']['start'] = self._io.pos()
            self.force_vector_z = self._io.read_f4be()
            self._debug['force_vector_z']['end'] = self._io.pos()
            self._debug['u32_0x10']['start'] = self._io.pos()
            self.u32_0x10 = self._io.read_u4be()
            self._debug['u32_0x10']['end'] = self._io.pos()
            self._debug['force_min_threshold']['start'] = self._io.pos()
            self.force_min_threshold = self._io.read_f4be()
            self._debug['force_min_threshold']['end'] = self._io.pos()
            self._debug['u32_0x18']['start'] = self._io.pos()
            self.u32_0x18 = self._io.read_u4be()
            self._debug['u32_0x18']['end'] = self._io.pos()
            self._debug['force_vector_magnitude']['start'] = self._io.pos()
            self.force_vector_magnitude = self._io.read_f4be()
            self._debug['force_vector_magnitude']['end'] = self._io.pos()


    class PuzzleActionRegAdd(KaitaiStruct):
        SEQ_FIELDS = ["imm_val_or_src_reg", "dst_reg", "activation_delay", "flags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['imm_val_or_src_reg']['start'] = self._io.pos()
            self.imm_val_or_src_reg = self._io.read_f4be()
            self._debug['imm_val_or_src_reg']['end'] = self._io.pos()
            self._debug['dst_reg']['start'] = self._io.pos()
            self.dst_reg = self._io.read_u2be()
            self._debug['dst_reg']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.RegisterFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


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


    class CameoLightningFlash(KaitaiStruct):
        SEQ_FIELDS = ["reserved", "duration_min", "duration_range"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_u2be()
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['duration_min']['start'] = self._io.pos()
            self.duration_min = self._io.read_u2be()
            self._debug['duration_min']['end'] = self._io.pos()
            self._debug['duration_range']['start'] = self._io.pos()
            self.duration_range = self._io.read_u2be()
            self._debug['duration_range']['end'] = self._io.pos()


    class PuzzleCondEnemyChangedStandingOnPlatform(KaitaiStruct):
        SEQ_FIELDS = ["plat_tag", "invert_result"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['invert_result']['start'] = self._io.pos()
            self.invert_result = self._io.read_s2be()
            self._debug['invert_result']['end'] = self._io.pos()


    class PuzzleActionEnemySetAiInstruction(KaitaiStruct):
        SEQ_FIELDS = ["instruction_idx", "puzzle_tag", "activation_delay", "flags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['instruction_idx']['start'] = self._io.pos()
            self.instruction_idx = self._io.read_u4be()
            self._debug['instruction_idx']['end'] = self._io.pos()
            self._debug['puzzle_tag']['start'] = self._io.pos()
            self.puzzle_tag = self._io.read_s2be()
            self._debug['puzzle_tag']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.GenericFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


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


    class PuzzleCondGloverWithinRangeOfPoint2(KaitaiStruct):
        SEQ_FIELDS = ["x", "z", "range", "max_y", "min_y"]
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
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()
            self._debug['range']['start'] = self._io.pos()
            self.range = self._io.read_f4be()
            self._debug['range']['end'] = self._io.pos()
            self._debug['max_y']['start'] = self._io.pos()
            self.max_y = self._io.read_f4be()
            self._debug['max_y']['end'] = self._io.pos()
            self._debug['min_y']['start'] = self._io.pos()
            self.min_y = self._io.read_f4be()
            self._debug['min_y']['end'] = self._io.pos()


    class PuzzleCondBallWithinRangeOfPoint(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z", "range"]
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
            self._debug['range']['start'] = self._io.pos()
            self.range = self._io.read_f4be()
            self._debug['range']['end'] = self._io.pos()


    class PuzzleActionCameraFlyTowardsPointRelativeToGlover(KaitaiStruct):
        SEQ_FIELDS = ["x", "z", "distance", "activation_delay"]
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
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()
            self._debug['distance']['start'] = self._io.pos()
            self.distance = self._io.read_f4be()
            self._debug['distance']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()


    class EnemyInstructionFacePlayer(KaitaiStruct):
        SEQ_FIELDS = ["randomize", "unused"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['randomize']['start'] = self._io.pos()
            self.randomize = self._io.read_u4be()
            self._debug['randomize']['end'] = self._io.pos()
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_u4be()
            self._debug['unused']['end'] = self._io.pos()


    class AmbientSoundAtPoint(KaitaiStruct):
        SEQ_FIELDS = ["sound_id", "volume", "flags", "h_0x06", "h_0x08", "h_0x0a", "platform_tag", "puzzle_tag", "x", "y", "z", "radius"]
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
            self._debug['platform_tag']['start'] = self._io.pos()
            self.platform_tag = self._io.read_u2be()
            self._debug['platform_tag']['end'] = self._io.pos()
            self._debug['puzzle_tag']['start'] = self._io.pos()
            self.puzzle_tag = self._io.read_u2be()
            self._debug['puzzle_tag']['end'] = self._io.pos()
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


    class PuzzleActionSoundControl(KaitaiStruct):
        SEQ_FIELDS = ["sound_id", "volume", "u32_0x18", "u32_0x1a", "u32_0x1c", "u32_0x1e", "platform_tag", "sound_tag", "pos_x", "pos_y", "pos_z", "activation_delay"]
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
            self.volume = self._io.read_s2be()
            self._debug['volume']['end'] = self._io.pos()
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
            self._debug['platform_tag']['start'] = self._io.pos()
            self.platform_tag = self._io.read_u2be()
            self._debug['platform_tag']['end'] = self._io.pos()
            self._debug['sound_tag']['start'] = self._io.pos()
            self.sound_tag = self._io.read_u2be()
            self._debug['sound_tag']['end'] = self._io.pos()
            self._debug['pos_x']['start'] = self._io.pos()
            self.pos_x = self._io.read_f4be()
            self._debug['pos_x']['end'] = self._io.pos()
            self._debug['pos_y']['start'] = self._io.pos()
            self.pos_y = self._io.read_f4be()
            self._debug['pos_y']['end'] = self._io.pos()
            self._debug['pos_z']['start'] = self._io.pos()
            self.pos_z = self._io.read_f4be()
            self._debug['pos_z']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()


    class PuzzleActionCameraTurnTowardsFocus(KaitaiStruct):
        SEQ_FIELDS = ["reserved", "activation_delay"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_f4be()
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()


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


    class PuzzleActionSetFog(KaitaiStruct):
        SEQ_FIELDS = ["r", "g", "b", "min_z", "u16_0x1c", "activation_delay"]
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
            self._debug['min_z']['start'] = self._io.pos()
            self.min_z = self._io.read_u2be()
            self._debug['min_z']['end'] = self._io.pos()
            self._debug['u16_0x1c']['start'] = self._io.pos()
            self.u16_0x1c = self._io.read_u2be()
            self._debug['u16_0x1c']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()


    class PuzzleActionPlatformConfigSpin(KaitaiStruct):
        SEQ_FIELDS = ["velocity", "platform_tag", "activation_delay", "flags"]
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
            self._debug['platform_tag']['start'] = self._io.pos()
            self.platform_tag = self._io.read_s2be()
            self._debug['platform_tag']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.PlatformMovementFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


    class Vent(KaitaiStruct):
        SEQ_FIELDS = ["type", "puzzle_tag", "parent_tag", "origin_x", "origin_y", "origin_z", "particle_velocity_x", "particle_velocity_y", "particle_velocity_z"]
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
            self._debug['puzzle_tag']['start'] = self._io.pos()
            self.puzzle_tag = self._io.read_u2be()
            self._debug['puzzle_tag']['end'] = self._io.pos()
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
            if _on == 14:
                self.body = GloverLevel.PuzzleCondPlatformOrbit2Todo(self._io, self, self._root)
            elif _on == 10:
                self.body = GloverLevel.PuzzleCondPlatformSpinTodo(self._io, self, self._root)
            elif _on == 17:
                self.body = GloverLevel.PuzzleCondBallStandingOnPlatform(self._io, self, self._root)
            elif _on == 42:
                self.body = GloverLevel.PuzzleCondPlatformDoesntExist(self._io, self, self._root)
            elif _on == 39:
                self.body = GloverLevel.PuzzleCondCameraWithinVolume(self._io, self, self._root)
            elif _on == 24:
                self.body = GloverLevel.PuzzleCondBallChangedTouchingPlatform(self._io, self, self._root)
            elif _on == 35:
                self.body = GloverLevel.PuzzleCondGloverWithinVolume(self._io, self, self._root)
            elif _on == 20:
                self.body = GloverLevel.PuzzleCondEnemyChangedStandingOnPlatform(self._io, self, self._root)
            elif _on == 32:
                self.body = GloverLevel.PuzzleCondPlatformCloseToConfBoundaryEdge(self._io, self, self._root)
            elif _on == 27:
                self.body = GloverLevel.PuzzleCondRegEq(self._io, self, self._root)
            elif _on == 13:
                self.body = GloverLevel.PuzzleCondPlatformSpin2Todo(self._io, self, self._root)
            elif _on == 11:
                self.body = GloverLevel.PuzzleCondPlatformOrbitTodo(self._io, self, self._root)
            elif _on == 12:
                self.body = GloverLevel.PuzzleCondPlatformPathAtPoint2(self._io, self, self._root)
            elif _on == 33:
                self.body = GloverLevel.PuzzleCondSpecificEnemyExists(self._io, self, self._root)
            elif _on == 19:
                self.body = GloverLevel.PuzzleCondEnemyStandingOnPlatform(self._io, self, self._root)
            elif _on == 23:
                self.body = GloverLevel.PuzzleCondBallIsTouchingPlatform(self._io, self, self._root)
            elif _on == 15:
                self.body = GloverLevel.PuzzleCondGloverStandingOnPlatform(self._io, self, self._root)
            elif _on == 38:
                self.body = GloverLevel.PuzzleCondBallWithinRangeOfPoint(self._io, self, self._root)
            elif _on == 40:
                self.body = GloverLevel.PuzzleCondCameraWithinRangeOfPoint(self._io, self, self._root)
            elif _on == 9:
                self.body = GloverLevel.PuzzleCondPlatformPathAtPointAtRest(self._io, self, self._root)
            elif _on == 21:
                self.body = GloverLevel.PuzzleCondGloverIsTouchingPlatform(self._io, self, self._root)
            elif _on == 37:
                self.body = GloverLevel.PuzzleCondBallWithinVolume(self._io, self, self._root)
            elif _on == 41:
                self.body = GloverLevel.PuzzleCondGloverWithinRangeOfPoint2(self._io, self, self._root)
            elif _on == 36:
                self.body = GloverLevel.PuzzleCondGloverWithinRangeOfPoint(self._io, self, self._root)
            elif _on == 28:
                self.body = GloverLevel.PuzzleCondRegNe(self._io, self, self._root)
            elif _on == 16:
                self.body = GloverLevel.PuzzleCondGloverChangedStandingOnPlatform(self._io, self, self._root)
            elif _on == 18:
                self.body = GloverLevel.PuzzleCondBallChangedStandingOnPlatform(self._io, self, self._root)
            elif _on == 26:
                self.body = GloverLevel.PuzzleCondEnemyChangedTouchingPlatform(self._io, self, self._root)
            elif _on == 31:
                self.body = GloverLevel.PuzzleCondPlatformTouchingConfBoundaryEdge(self._io, self, self._root)
            elif _on == 34:
                self.body = GloverLevel.PuzzleCond0x22(self._io, self, self._root)
            elif _on == 29:
                self.body = GloverLevel.PuzzleCondRegGt(self._io, self, self._root)
            elif _on == 25:
                self.body = GloverLevel.PuzzleCondEnemyIsTouchingPlatform(self._io, self, self._root)
            elif _on == 22:
                self.body = GloverLevel.PuzzleCondGloverChangedTouchingPlatform(self._io, self, self._root)
            elif _on == 30:
                self.body = GloverLevel.PuzzleCondRegLt(self._io, self, self._root)
            else:
                self.body = GloverLevel.PuzzleCondDefault(self._io, self, self._root)
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


    class PuzzleActionSetPlatformPathDirection(KaitaiStruct):
        SEQ_FIELDS = ["direction", "puzzle_tag", "activation_delay", "flags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['direction']['start'] = self._io.pos()
            self.direction = self._io.read_u4be()
            self._debug['direction']['end'] = self._io.pos()
            self._debug['puzzle_tag']['start'] = self._io.pos()
            self.puzzle_tag = self._io.read_u2be()
            self._debug['puzzle_tag']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.PlatformMovementFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


    class PlatStrobe(KaitaiStruct):
        SEQ_FIELDS = ["scale_x", "scale_y", "scale_z", "tween_factor", "pause_frames"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['scale_x']['start'] = self._io.pos()
            self.scale_x = self._io.read_f4be()
            self._debug['scale_x']['end'] = self._io.pos()
            self._debug['scale_y']['start'] = self._io.pos()
            self.scale_y = self._io.read_f4be()
            self._debug['scale_y']['end'] = self._io.pos()
            self._debug['scale_z']['start'] = self._io.pos()
            self.scale_z = self._io.read_f4be()
            self._debug['scale_z']['end'] = self._io.pos()
            self._debug['tween_factor']['start'] = self._io.pos()
            self.tween_factor = self._io.read_s2be()
            self._debug['tween_factor']['end'] = self._io.pos()
            self._debug['pause_frames']['start'] = self._io.pos()
            self.pause_frames = self._io.read_s2be()
            self._debug['pause_frames']['end'] = self._io.pos()


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
        SEQ_FIELDS = ["subcommand", "i_0x02", "i_0x06", "i_0x0a", "i_0x0e", "frame_count", "preceding_instr_idx"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['subcommand']['start'] = self._io.pos()
            self.subcommand = self._io.read_s2be()
            self._debug['subcommand']['end'] = self._io.pos()
            self._debug['i_0x02']['start'] = self._io.pos()
            self.i_0x02 = self._io.read_f4be()
            self._debug['i_0x02']['end'] = self._io.pos()
            self._debug['i_0x06']['start'] = self._io.pos()
            self.i_0x06 = self._io.read_f4be()
            self._debug['i_0x06']['end'] = self._io.pos()
            self._debug['i_0x0a']['start'] = self._io.pos()
            self.i_0x0a = self._io.read_f4be()
            self._debug['i_0x0a']['end'] = self._io.pos()
            self._debug['i_0x0e']['start'] = self._io.pos()
            self.i_0x0e = self._io.read_u4be()
            self._debug['i_0x0e']['end'] = self._io.pos()
            self._debug['frame_count']['start'] = self._io.pos()
            self.frame_count = self._io.read_s2be()
            self._debug['frame_count']['end'] = self._io.pos()
            self._debug['preceding_instr_idx']['start'] = self._io.pos()
            self.preceding_instr_idx = self._io.read_s2be()
            self._debug['preceding_instr_idx']['end'] = self._io.pos()


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


    class PuzzleCondPlatformPathAtPoint2(KaitaiStruct):
        SEQ_FIELDS = ["plat_tag", "arg2"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['arg2']['start'] = self._io.pos()
            self.arg2 = self._io.read_s2be()
            self._debug['arg2']['end'] = self._io.pos()


    class SetExit(KaitaiStruct):

        class ExitType(Enum):
            loading_zone = 0
            solid_platform = 1
        SEQ_FIELDS = ["behavior", "type"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['behavior']['start'] = self._io.pos()
            self.behavior = self._io.read_u2be()
            self._debug['behavior']['end'] = self._io.pos()
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(GloverLevel.SetExit.ExitType, self._io.read_s2be())
            self._debug['type']['end'] = self._io.pos()


    class PuzzleCondPlatformTouchingConfBoundaryEdge(KaitaiStruct):

        class EdgeType(Enum):
            x = 0
            y = 1
            z = 2
            x_plus_w = 3
            y_plus_h = 4
            z_plus_d = 5
        SEQ_FIELDS = ["plat_tag", "edge"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['edge']['start'] = self._io.pos()
            self.edge = KaitaiStream.resolve_enum(GloverLevel.PuzzleCondPlatformTouchingConfBoundaryEdge.EdgeType, self._io.read_u2be())
            self._debug['edge']['end'] = self._io.pos()


    class PuzzleActionSetPlatformVelocity(KaitaiStruct):
        SEQ_FIELDS = ["vel_x", "vel_y", "vel_z", "reserved", "puzzle_tag", "activation_delay", "flags"]
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
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_u4be()
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['puzzle_tag']['start'] = self._io.pos()
            self.puzzle_tag = self._io.read_u2be()
            self._debug['puzzle_tag']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.PlatformMovementFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


    class PuzzleCondRegEq(KaitaiStruct):
        SEQ_FIELDS = ["reg_a", "imm_or_reg_b"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['reg_a']['start'] = self._io.pos()
            self.reg_a = self._io.read_s2be()
            self._debug['reg_a']['end'] = self._io.pos()
            self._debug['imm_or_reg_b']['start'] = self._io.pos()
            self.imm_or_reg_b = self._io.read_s2be()
            self._debug['imm_or_reg_b']['end'] = self._io.pos()


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


    class EnemyInstructionNoop(KaitaiStruct):
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


    class PuzzleActionRegSub(KaitaiStruct):
        SEQ_FIELDS = ["imm_val_or_src_reg", "dst_reg", "activation_delay", "flags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['imm_val_or_src_reg']['start'] = self._io.pos()
            self.imm_val_or_src_reg = self._io.read_f4be()
            self._debug['imm_val_or_src_reg']['end'] = self._io.pos()
            self._debug['dst_reg']['start'] = self._io.pos()
            self.dst_reg = self._io.read_u2be()
            self._debug['dst_reg']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.RegisterFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


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


    class PuzzleActionCameraSetDistance(KaitaiStruct):
        SEQ_FIELDS = ["distance", "reserved", "activation_delay", "flags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['distance']['start'] = self._io.pos()
            self.distance = self._io.read_f4be()
            self._debug['distance']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_u2be()
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.CameraFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


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


    class PuzzleCondBallWithinVolume(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z", "l", "w", "h"]
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
            self._debug['l']['start'] = self._io.pos()
            self.l = self._io.read_f4be()
            self._debug['l']['end'] = self._io.pos()
            self._debug['w']['start'] = self._io.pos()
            self.w = self._io.read_f4be()
            self._debug['w']['end'] = self._io.pos()
            self._debug['h']['start'] = self._io.pos()
            self.h = self._io.read_f4be()
            self._debug['h']['end'] = self._io.pos()


    class PuzzleActionTogglePlatformPhysics(KaitaiStruct):
        SEQ_FIELDS = ["physics_enabled", "platform_tag", "activation_delay", "flags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['physics_enabled']['start'] = self._io.pos()
            self.physics_enabled = self._io.read_u4be()
            self._debug['physics_enabled']['end'] = self._io.pos()
            self._debug['platform_tag']['start'] = self._io.pos()
            self.platform_tag = self._io.read_s2be()
            self._debug['platform_tag']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.GenericFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


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


    class PlatPathSetStartingPoint(KaitaiStruct):
        SEQ_FIELDS = ["point_idx"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['point_idx']['start'] = self._io.pos()
            self.point_idx = self._io.read_u2be()
            self._debug['point_idx']['end'] = self._io.pos()


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
        SEQ_FIELDS = ["target_tag", "out_framecount", "in_framecount", "u16_0x12", "u32_0x00", "u32_0x04", "u32_0x08"]
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
            self._debug['out_framecount']['start'] = self._io.pos()
            self.out_framecount = self._io.read_u2be()
            self._debug['out_framecount']['end'] = self._io.pos()
            self._debug['in_framecount']['start'] = self._io.pos()
            self.in_framecount = self._io.read_u2be()
            self._debug['in_framecount']['end'] = self._io.pos()
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
                self.params = GloverLevel.PlatPathSoundAtPointHit(self._io, self, self._root)
            elif _on == 184:
                self.params = GloverLevel.PlatCollision0xb8Todo(self._io, self, self._root)
            elif _on == 105:
                self.params = GloverLevel.PlatCat0x69(self._io, self, self._root)
            elif _on == 142:
                self.params = GloverLevel.PlatCauseDamage(self._io, self, self._root)
            elif _on == 112:
                self.params = GloverLevel.PlatRocking(self._io, self, self._root)
            elif _on == 163:
                self.params = GloverLevel.VentDutyCycle(self._io, self, self._root)
            elif _on == 131:
                self.params = GloverLevel.Enemy(self._io, self, self._root)
            elif _on == 0:
                self.params = GloverLevel.Noop(self._io, self, self._root)
            elif _on == 167:
                self.params = GloverLevel.PlatPathSetStartingPoint(self._io, self, self._root)
            elif _on == 146:
                self.params = GloverLevel.LandActor(self._io, self, self._root)
            elif _on == 4:
                self.params = GloverLevel.Puzzle(self._io, self, self._root)
            elif _on == 169:
                self.params = GloverLevel.SetGravity(self._io, self, self._root)
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
                self.params = GloverLevel.PlatConfBoundaryVolume(self._io, self, self._root)
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
                self.params = GloverLevel.PlatStrobe(self._io, self, self._root)
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
                self.params = GloverLevel.PlatInteractsWithWater(self._io, self, self._root)
            elif _on == 182:
                self.params = GloverLevel.BuzzerDutyCycle(self._io, self, self._root)
            elif _on == 108:
                self.params = GloverLevel.PlatMaxVelocity(self._io, self, self._root)
            elif _on == 189:
                self.params = GloverLevel.AmbientSound(self._io, self, self._root)
            elif _on == 168:
                self.params = GloverLevel.SetExit(self._io, self, self._root)
            elif _on == 171:
                self.params = GloverLevel.CameoInst(self._io, self, self._root)
            elif _on == 193:
                self.params = GloverLevel.PlatMovementSound(self._io, self, self._root)
            elif _on == 133:
                self.params = GloverLevel.GaribGroup(self._io, self, self._root)
            elif _on == 129:
                self.params = GloverLevel.PlatTopple0x81(self._io, self, self._root)
            elif _on == 151:
                self.params = GloverLevel.DiffuseLight(self._io, self, self._root)
            elif _on == 157:
                self.params = GloverLevel.PlatHasPhysics(self._io, self, self._root)
            elif _on == 147:
                self.params = GloverLevel.SetActorRotation(self._io, self, self._root)
            elif _on == 134:
                self.params = GloverLevel.Garib(self._io, self, self._root)
            elif _on == 102:
                self.params = GloverLevel.PlatReverseAtEndsOfPath(self._io, self, self._root)
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
                self.params = GloverLevel.AmbientSoundAtPoint(self._io, self, self._root)
            elif _on == 196:
                self.params = GloverLevel.PlatOrbitSound0xc4(self._io, self, self._root)
            elif _on == 183:
                self.params = GloverLevel.PlatSetCollisionYOffset(self._io, self, self._root)
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


    class PuzzleCondEnemyChangedTouchingPlatform(KaitaiStruct):
        SEQ_FIELDS = ["plat_tag", "started_or_stopped"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['started_or_stopped']['start'] = self._io.pos()
            self.started_or_stopped = self._io.read_s2be()
            self._debug['started_or_stopped']['end'] = self._io.pos()


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


    class PuzzleCond0x22(KaitaiStruct):
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


    class PlatDestructible(KaitaiStruct):

        class DestructibleFlags(Enum):
            spawn_particles_on_destruction = 4
        SEQ_FIELDS = ["flags", "num_fragments", "fragment_object_id", "name"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PlatDestructible.DestructibleFlags, self._io.read_u2be())
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

        class GenericFlags(Enum):
            puzzle_action_random_activation_delay = 512

        class CameraFlags(Enum):
            puzzle_camera_freeze_player = 1
            puzzle_camera_freeze_particles = 2
            puzzle_camera_freeze_enemies = 4
            puzzle_action_random_activation_delay = 512

        class PlatformMovementFlags(Enum):
            puzzle_platform_halt_at_end_of_first_segment_only = 1
            puzzle_platform_halt_at_segment_end = 2
            puzzle_platform_clip_current_velocity = 4
            puzzle_action_random_activation_delay = 512

        class PlatformToggleFlags(Enum):
            puzzle_action_include_fans_and_magnets = 8
            puzzle_action_include_teleports = 16
            puzzle_action_include_catapults = 32
            puzzle_action_include_damage_platforms = 64
            puzzle_action_include_vents = 256
            puzzle_action_random_activation_delay = 512
            puzzle_action_include_buzzers = 1024

        class RegisterFlags(Enum):
            puzzle_register_indirect_argument = 128
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
                self.body = GloverLevel.PuzzleActionSetPlatformVelocity(self._io, self, self._root)
            elif _on == 47:
                self.body = GloverLevel.PuzzleActionPlatformConfigOrbit(self._io, self, self._root)
            elif _on == 73:
                self.body = GloverLevel.PuzzleActionCameraFlyTowardsPoint(self._io, self, self._root)
            elif _on == 46:
                self.body = GloverLevel.PuzzleActionPlatformConfigSpin(self._io, self, self._root)
            elif _on == 81:
                self.body = GloverLevel.PuzzleActionStartCameo(self._io, self, self._root)
            elif _on == 60:
                self.body = GloverLevel.PuzzleActionSpawnEnemy(self._io, self, self._root)
            elif _on == 62:
                self.body = GloverLevel.PuzzleActionCameraLookAtPlatform(self._io, self, self._root)
            elif _on == 55:
                self.body = GloverLevel.PuzzleActionTogglePlatformPhysics(self._io, self, self._root)
            elif _on == 77:
                self.body = GloverLevel.PuzzleActionCameraFlyTowardsPointRelativeToGlover(self._io, self, self._root)
            elif _on == 52:
                self.body = GloverLevel.PuzzleActionControlActiveElements(self._io, self, self._root)
            elif _on == 56:
                self.body = GloverLevel.PuzzleActionRegSet(self._io, self, self._root)
            elif _on == 45:
                self.body = GloverLevel.PuzzleActionPlatformNudge(self._io, self, self._root)
            elif _on == 85:
                self.body = GloverLevel.PuzzleActionSetBackground(self._io, self, self._root)
            elif _on == 67:
                self.body = GloverLevel.PuzzleActionEnemySetAiInstruction(self._io, self, self._root)
            elif _on == 69:
                self.body = GloverLevel.PuzzleActionSpawnGaribGroup(self._io, self, self._root)
            elif _on == 59:
                self.body = GloverLevel.PuzzleActionSpawnPowerup(self._io, self, self._root)
            elif _on == 58:
                self.body = GloverLevel.PuzzleActionRegSub(self._io, self, self._root)
            elif _on == 82:
                self.body = GloverLevel.PuzzleActionSetPlatformPathDirection(self._io, self, self._root)
            elif _on == 86:
                self.body = GloverLevel.PuzzleActionSetFog(self._io, self, self._root)
            elif _on == 84:
                self.body = GloverLevel.PuzzleActionSoundControl(self._io, self, self._root)
            elif _on == 63:
                self.body = GloverLevel.PuzzleActionCameraLookAtPoint2(self._io, self, self._root)
            elif _on == 51:
                self.body = GloverLevel.PuzzleActionPlatformSpinAlongAxis(self._io, self, self._root)
            elif _on == 83:
                self.body = GloverLevel.PuzzleActionMakeBallInteractive(self._io, self, self._root)
            elif _on == 48:
                self.body = GloverLevel.PuzzleActionPlatformMoveToPointIdxMinusOne(self._io, self, self._root)
            elif _on == 78:
                self.body = GloverLevel.PuzzleActionChangeWaterHeight(self._io, self, self._root)
            elif _on == 53:
                self.body = GloverLevel.PuzzleActionSetConveyor(self._io, self, self._root)
            elif _on == 64:
                self.body = GloverLevel.PuzzleActionCameraLookAtPoint1(self._io, self, self._root)
            elif _on == 65:
                self.body = GloverLevel.PuzzleActionCameraSetDistance(self._io, self, self._root)
            elif _on == 76:
                self.body = GloverLevel.PuzzleAction0x4b0x4c(self._io, self, self._root)
            elif _on == 79:
                self.body = GloverLevel.PuzzleAction0x4f(self._io, self, self._root)
            elif _on == 57:
                self.body = GloverLevel.PuzzleActionRegAdd(self._io, self, self._root)
            elif _on == 72:
                self.body = GloverLevel.PuzzleActionCameraTurnTowardsFocus(self._io, self, self._root)
            elif _on == 71:
                self.body = GloverLevel.PuzzleActionCameraTweenDistance(self._io, self, self._root)
            elif _on == 70:
                self.body = GloverLevel.PuzzleActionCameraTweenYAdjust(self._io, self, self._root)
            elif _on == 74:
                self.body = GloverLevel.PuzzleActionCameraLookAtGlover(self._io, self, self._root)
            elif _on == 80:
                self.body = GloverLevel.PuzzleActionSetGravity(self._io, self, self._root)
            elif _on == 68:
                self.body = GloverLevel.PuzzleActionToggleWind(self._io, self, self._root)
            elif _on == 54:
                self.body = GloverLevel.PuzzleActionHidePlatform(self._io, self, self._root)
            elif _on == 75:
                self.body = GloverLevel.PuzzleAction0x4b0x4c(self._io, self, self._root)
            else:
                self.body = GloverLevel.PuzzleActionDefault(self._io, self, self._root)
            self._debug['body']['end'] = self._io.pos()


    class PuzzleActionSpawnPowerup(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z", "u32_0x10", "type", "activation_delay", "u32_0x20"]
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
            self._debug['u32_0x10']['start'] = self._io.pos()
            self.u32_0x10 = self._io.read_f4be()
            self._debug['u32_0x10']['end'] = self._io.pos()
            self._debug['type']['start'] = self._io.pos()
            self.type = self._io.read_u2be()
            self._debug['type']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['u32_0x20']['start'] = self._io.pos()
            self.u32_0x20 = self._io.read_u4be()
            self._debug['u32_0x20']['end'] = self._io.pos()


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
        SEQ_FIELDS = ["left", "top", "front", "width", "bottom", "depth", "surface_y", "current_x", "current_z", "puzzle_tag", "object_id", "name", "x", "y", "z"]
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
            self._debug['puzzle_tag']['start'] = self._io.pos()
            self.puzzle_tag = self._io.read_u2be()
            self._debug['puzzle_tag']['end'] = self._io.pos()
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


    class PuzzleActionSpawnEnemy(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z", "reserved", "puzzle_tag", "activation_delay", "flags"]
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
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_u4be()
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['puzzle_tag']['start'] = self._io.pos()
            self.puzzle_tag = self._io.read_u2be()
            self._debug['puzzle_tag']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.GenericFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


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


    class PuzzleActionSetBackground(KaitaiStruct):
        SEQ_FIELDS = ["texture_id", "activation_delay"]
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
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()


    class PuzzleCondPlatformCloseToConfBoundaryEdge(KaitaiStruct):

        class EdgeType(Enum):
            x = 0
            y = 1
            z = 2
            x_plus_w = 3
            y_plus_h = 4
            z_plus_d = 5
        SEQ_FIELDS = ["plat_tag", "edge"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['edge']['start'] = self._io.pos()
            self.edge = KaitaiStream.resolve_enum(GloverLevel.PuzzleCondPlatformCloseToConfBoundaryEdge.EdgeType, self._io.read_u2be())
            self._debug['edge']['end'] = self._io.pos()


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


    class PuzzleCondBallIsTouchingPlatform(KaitaiStruct):
        SEQ_FIELDS = ["plat_tag", "invert_result"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['invert_result']['start'] = self._io.pos()
            self.invert_result = self._io.read_s2be()
            self._debug['invert_result']['end'] = self._io.pos()


    class EnemyInstructionFollowPlayer(KaitaiStruct):
        SEQ_FIELDS = ["offset_x", "offset_y", "offset_z", "vel_magnitude"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['offset_x']['start'] = self._io.pos()
            self.offset_x = self._io.read_f4be()
            self._debug['offset_x']['end'] = self._io.pos()
            self._debug['offset_y']['start'] = self._io.pos()
            self.offset_y = self._io.read_f4be()
            self._debug['offset_y']['end'] = self._io.pos()
            self._debug['offset_z']['start'] = self._io.pos()
            self.offset_z = self._io.read_f4be()
            self._debug['offset_z']['end'] = self._io.pos()
            self._debug['vel_magnitude']['start'] = self._io.pos()
            self.vel_magnitude = self._io.read_f4be()
            self._debug['vel_magnitude']['end'] = self._io.pos()


    class CameoGrabTodo(KaitaiStruct):
        SEQ_FIELDS = ["grabbing_enemy_idx", "grabbed_enemy_idx", "linkage_point_idx", "frame_count", "preceding_instr_idx"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['grabbing_enemy_idx']['start'] = self._io.pos()
            self.grabbing_enemy_idx = self._io.read_u2be()
            self._debug['grabbing_enemy_idx']['end'] = self._io.pos()
            self._debug['grabbed_enemy_idx']['start'] = self._io.pos()
            self.grabbed_enemy_idx = self._io.read_u2be()
            self._debug['grabbed_enemy_idx']['end'] = self._io.pos()
            self._debug['linkage_point_idx']['start'] = self._io.pos()
            self.linkage_point_idx = self._io.read_u2be()
            self._debug['linkage_point_idx']['end'] = self._io.pos()
            self._debug['frame_count']['start'] = self._io.pos()
            self.frame_count = self._io.read_s2be()
            self._debug['frame_count']['end'] = self._io.pos()
            self._debug['preceding_instr_idx']['start'] = self._io.pos()
            self.preceding_instr_idx = self._io.read_s2be()
            self._debug['preceding_instr_idx']['end'] = self._io.pos()


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
        SEQ_FIELDS = ["type", "puzzle_tag", "x", "y", "z", "y_rotation"]
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
            self._debug['puzzle_tag']['start'] = self._io.pos()
            self.puzzle_tag = self._io.read_u2be()
            self._debug['puzzle_tag']['end'] = self._io.pos()
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


    class PuzzleCondPlatformOrbit2Todo(KaitaiStruct):
        SEQ_FIELDS = ["plat_tag", "arg2"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['arg2']['start'] = self._io.pos()
            self.arg2 = self._io.read_s2be()
            self._debug['arg2']['end'] = self._io.pos()


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


    class PuzzleCondSpecificEnemyExists(KaitaiStruct):
        SEQ_FIELDS = ["puzzle_tag", "invert_result"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['puzzle_tag']['start'] = self._io.pos()
            self.puzzle_tag = self._io.read_u2be()
            self._debug['puzzle_tag']['end'] = self._io.pos()
            self._debug['invert_result']['start'] = self._io.pos()
            self.invert_result = self._io.read_s2be()
            self._debug['invert_result']['end'] = self._io.pos()


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
        SEQ_FIELDS = ["field_0", "field_1", "activation_delay", "flags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['field_0']['start'] = self._io.pos()
            self.field_0 = self._io.read_u4be()
            self._debug['field_0']['end'] = self._io.pos()
            self._debug['field_1']['start'] = self._io.pos()
            self.field_1 = self._io.read_s2be()
            self._debug['field_1']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.GenericFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


    class AmbientSound(KaitaiStruct):
        SEQ_FIELDS = ["sound_id", "volume", "flags"]
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


    class PlatCauseDamage(KaitaiStruct):
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


    class PuzzleActionMakeBallInteractive(KaitaiStruct):
        SEQ_FIELDS = ["reserved", "reserved_2", "activation_delay", "flags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_u4be()
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['reserved_2']['start'] = self._io.pos()
            self.reserved_2 = self._io.read_u2be()
            self._debug['reserved_2']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.GenericFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


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


    class CameoSpin(KaitaiStruct):
        SEQ_FIELDS = ["enemy_idx", "speed", "frame_count", "preceding_instr_idx"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['enemy_idx']['start'] = self._io.pos()
            self.enemy_idx = self._io.read_u2be()
            self._debug['enemy_idx']['end'] = self._io.pos()
            self._debug['speed']['start'] = self._io.pos()
            self.speed = self._io.read_f4be()
            self._debug['speed']['end'] = self._io.pos()
            self._debug['frame_count']['start'] = self._io.pos()
            self.frame_count = self._io.read_s2be()
            self._debug['frame_count']['end'] = self._io.pos()
            self._debug['preceding_instr_idx']['start'] = self._io.pos()
            self.preceding_instr_idx = self._io.read_s2be()
            self._debug['preceding_instr_idx']['end'] = self._io.pos()


    class PuzzleCondRegGt(KaitaiStruct):
        SEQ_FIELDS = ["reg_a", "imm_or_reg_b"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['reg_a']['start'] = self._io.pos()
            self.reg_a = self._io.read_s2be()
            self._debug['reg_a']['end'] = self._io.pos()
            self._debug['imm_or_reg_b']['start'] = self._io.pos()
            self.imm_or_reg_b = self._io.read_s2be()
            self._debug['imm_or_reg_b']['end'] = self._io.pos()


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


    class PuzzleCondBallChangedStandingOnPlatform(KaitaiStruct):
        SEQ_FIELDS = ["plat_tag", "invert_result"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['invert_result']['start'] = self._io.pos()
            self.invert_result = self._io.read_s2be()
            self._debug['invert_result']['end'] = self._io.pos()


    class PuzzleActionToggleWind(KaitaiStruct):
        SEQ_FIELDS = ["enabled", "puzzle_tag", "activation_delay", "flags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['enabled']['start'] = self._io.pos()
            self.enabled = self._io.read_u4be()
            self._debug['enabled']['end'] = self._io.pos()
            self._debug['puzzle_tag']['start'] = self._io.pos()
            self.puzzle_tag = self._io.read_s2be()
            self._debug['puzzle_tag']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.GenericFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


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


    class EnemyInstructionSteer(KaitaiStruct):
        SEQ_FIELDS = ["dst_x", "dst_y", "dst_z", "turn_damping"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['dst_x']['start'] = self._io.pos()
            self.dst_x = self._io.read_f4be()
            self._debug['dst_x']['end'] = self._io.pos()
            self._debug['dst_y']['start'] = self._io.pos()
            self.dst_y = self._io.read_f4be()
            self._debug['dst_y']['end'] = self._io.pos()
            self._debug['dst_z']['start'] = self._io.pos()
            self.dst_z = self._io.read_f4be()
            self._debug['dst_z']['end'] = self._io.pos()
            self._debug['turn_damping']['start'] = self._io.pos()
            self.turn_damping = self._io.read_f4be()
            self._debug['turn_damping']['end'] = self._io.pos()


    class PuzzleCondGloverIsTouchingPlatform(KaitaiStruct):
        SEQ_FIELDS = ["plat_tag", "invert_result"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['invert_result']['start'] = self._io.pos()
            self.invert_result = self._io.read_s2be()
            self._debug['invert_result']['end'] = self._io.pos()


    class PlatMovementSound(KaitaiStruct):
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


    class PuzzleActionControlActiveElements(KaitaiStruct):
        SEQ_FIELDS = ["value", "puzzle_tag", "activation_delay", "flags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_f4be()
            self._debug['value']['end'] = self._io.pos()
            self._debug['puzzle_tag']['start'] = self._io.pos()
            self.puzzle_tag = self._io.read_u2be()
            self._debug['puzzle_tag']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.PlatformToggleFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


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


    class PuzzleCondBallStandingOnPlatform(KaitaiStruct):
        SEQ_FIELDS = ["plat_tag", "invert_result"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['invert_result']['start'] = self._io.pos()
            self.invert_result = self._io.read_s2be()
            self._debug['invert_result']['end'] = self._io.pos()


    class EnemyInstructionBullet0x6(KaitaiStruct):
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


    class CameoPlayAnimation(KaitaiStruct):
        SEQ_FIELDS = ["enemy_idx", "anim_idx", "start_playing", "playback_speed", "frame_count", "preceding_instr_idx"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['enemy_idx']['start'] = self._io.pos()
            self.enemy_idx = self._io.read_u2be()
            self._debug['enemy_idx']['end'] = self._io.pos()
            self._debug['anim_idx']['start'] = self._io.pos()
            self.anim_idx = self._io.read_u2be()
            self._debug['anim_idx']['end'] = self._io.pos()
            self._debug['start_playing']['start'] = self._io.pos()
            self.start_playing = self._io.read_u2be()
            self._debug['start_playing']['end'] = self._io.pos()
            self._debug['playback_speed']['start'] = self._io.pos()
            self.playback_speed = self._io.read_f4be()
            self._debug['playback_speed']['end'] = self._io.pos()
            self._debug['frame_count']['start'] = self._io.pos()
            self.frame_count = self._io.read_s2be()
            self._debug['frame_count']['end'] = self._io.pos()
            self._debug['preceding_instr_idx']['start'] = self._io.pos()
            self.preceding_instr_idx = self._io.read_s2be()
            self._debug['preceding_instr_idx']['end'] = self._io.pos()


    class PuzzleCondRegNe(KaitaiStruct):
        SEQ_FIELDS = ["reg_a", "imm_or_reg_b"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['reg_a']['start'] = self._io.pos()
            self.reg_a = self._io.read_s2be()
            self._debug['reg_a']['end'] = self._io.pos()
            self._debug['imm_or_reg_b']['start'] = self._io.pos()
            self.imm_or_reg_b = self._io.read_s2be()
            self._debug['imm_or_reg_b']['end'] = self._io.pos()


    class PlatInteractsWithWater(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class PuzzleActionSetConveyor(KaitaiStruct):
        SEQ_FIELDS = ["vel_x", "vel_y", "vel_z", "reserved", "puzzle_tag", "activation_delay", "flags"]
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
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_u4be()
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['puzzle_tag']['start'] = self._io.pos()
            self.puzzle_tag = self._io.read_u2be()
            self._debug['puzzle_tag']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.CameraFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


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


    class PuzzleCondGloverWithinVolume(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z", "l", "w", "h"]
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
            self._debug['l']['start'] = self._io.pos()
            self.l = self._io.read_f4be()
            self._debug['l']['end'] = self._io.pos()
            self._debug['w']['start'] = self._io.pos()
            self.w = self._io.read_f4be()
            self._debug['w']['end'] = self._io.pos()
            self._debug['h']['start'] = self._io.pos()
            self.h = self._io.read_f4be()
            self._debug['h']['end'] = self._io.pos()


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
            modulate_velocity_with_turns = 1
            modulate_acceleration = 2
            slow_down_close_to_destination = 4
            pitch = 8
            yaw = 16
            roll = 32
            proximity_of_player = 64
            proximity_of_ball = 128
            proximity_of_closer_of_player_or_ball = 256
            mirror_angle = 1024
            prevent_conditinoal_transition = 2048
            dont_turn_towards_movement_direction = 4096
            movement_roll_into_turn = 8192
            dont_animate = 16384
            dont_interrupt_animation = 65536
            anim_switch_todo_0x40000 = 262144
            face_player = 1048576
            face_ball = 2097152
            face_closer_of_player_or_ball = 4194304
            slow_down_towards_target = 8388608
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
                self.params = GloverLevel.EnemyInstructionSetTimer(self._io, self, self._root)
            elif _on == 10:
                self.params = GloverLevel.EnemyInstructionGlom(self._io, self, self._root)
            elif _on == 17:
                self.params = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 0:
                self.params = GloverLevel.EnemyInstructionMove(self._io, self, self._root)
            elif _on == 4:
                self.params = GloverLevel.EnemyInstructionRest(self._io, self, self._root)
            elif _on == 24:
                self.params = GloverLevel.EnemyKill(self._io, self, self._root)
            elif _on == 6:
                self.params = GloverLevel.EnemyInstructionBullet0x6(self._io, self, self._root)
            elif _on == 20:
                self.params = GloverLevel.EnemyInstructionC(self._io, self, self._root)
            elif _on == 7:
                self.params = GloverLevel.EnemyInstructionPlayAnimation(self._io, self, self._root)
            elif _on == 1:
                self.params = GloverLevel.EnemyInstructionDash(self._io, self, self._root)
            elif _on == 13:
                self.params = GloverLevel.EnemyInstructionSteer(self._io, self, self._root)
            elif _on == 11:
                self.params = GloverLevel.EnemyInstructionCatapult(self._io, self, self._root)
            elif _on == 12:
                self.params = GloverLevel.EnemyInstructionFleePlayer(self._io, self, self._root)
            elif _on == 3:
                self.params = GloverLevel.EnemyInstructionRandomWalk(self._io, self, self._root)
            elif _on == 5:
                self.params = GloverLevel.EnemyInstructionBullet0x5(self._io, self, self._root)
            elif _on == 19:
                self.params = GloverLevel.EnemyInstructionNoop(self._io, self, self._root)
            elif _on == 23:
                self.params = GloverLevel.EnemyImpulseForward(self._io, self, self._root)
            elif _on == 15:
                self.params = GloverLevel.EnemyInstructionAttack(self._io, self, self._root)
            elif _on == 8:
                self.params = GloverLevel.EnemyInstructionFacePlayer(self._io, self, self._root)
            elif _on == 9:
                self.params = GloverLevel.EnemyInstructionFollowPlayer(self._io, self, self._root)
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


    class PuzzleCondPlatformSpinTodo(KaitaiStruct):
        SEQ_FIELDS = ["plat_tag", "idx"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['idx']['start'] = self._io.pos()
            self.idx = self._io.read_s2be()
            self._debug['idx']['end'] = self._io.pos()


    class PuzzleActionCameraTweenYAdjust(KaitaiStruct):
        SEQ_FIELDS = ["y_adjust", "activation_delay"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['y_adjust']['start'] = self._io.pos()
            self.y_adjust = self._io.read_f4be()
            self._debug['y_adjust']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()


    class PuzzleCondRegLt(KaitaiStruct):
        SEQ_FIELDS = ["reg_a", "imm_or_reg_b"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['reg_a']['start'] = self._io.pos()
            self.reg_a = self._io.read_s2be()
            self._debug['reg_a']['end'] = self._io.pos()
            self._debug['imm_or_reg_b']['start'] = self._io.pos()
            self.imm_or_reg_b = self._io.read_s2be()
            self._debug['imm_or_reg_b']['end'] = self._io.pos()


    class PuzzleCondGloverChangedStandingOnPlatform(KaitaiStruct):
        SEQ_FIELDS = ["plat_tag", "invert_result"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['invert_result']['start'] = self._io.pos()
            self.invert_result = self._io.read_s2be()
            self._debug['invert_result']['end'] = self._io.pos()


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


    class PuzzleActionCameraLookAtPlatform(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z", "duration", "platform_tag", "activation_delay", "flags"]
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
            self._debug['duration']['start'] = self._io.pos()
            self.duration = self._io.read_f4be()
            self._debug['duration']['end'] = self._io.pos()
            self._debug['platform_tag']['start'] = self._io.pos()
            self.platform_tag = self._io.read_u2be()
            self._debug['platform_tag']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.CameraFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


    class PlatConfBoundaryVolume(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z", "w", "h", "d"]
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
            self._debug['w']['start'] = self._io.pos()
            self.w = self._io.read_f4be()
            self._debug['w']['end'] = self._io.pos()
            self._debug['h']['start'] = self._io.pos()
            self.h = self._io.read_f4be()
            self._debug['h']['end'] = self._io.pos()
            self._debug['d']['start'] = self._io.pos()
            self.d = self._io.read_f4be()
            self._debug['d']['end'] = self._io.pos()


    class PlatCollision0xb8Todo(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


    class PuzzleActionSpawnGaribGroup(KaitaiStruct):
        SEQ_FIELDS = ["y", "group_id", "activation_delay", "num_spawns"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['group_id']['start'] = self._io.pos()
            self.group_id = self._io.read_s2be()
            self._debug['group_id']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['num_spawns']['start'] = self._io.pos()
            self.num_spawns = self._io.read_s4be()
            self._debug['num_spawns']['end'] = self._io.pos()


    class PuzzleActionSetGravity(KaitaiStruct):
        SEQ_FIELDS = ["value", "reserved", "activation_delay", "flags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_f4be()
            self._debug['value']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_u2be()
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.GenericFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


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


    class PuzzleCondCameraWithinRangeOfPoint(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z", "range"]
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
            self._debug['range']['start'] = self._io.pos()
            self.range = self._io.read_f4be()
            self._debug['range']['end'] = self._io.pos()


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


    class PuzzleCondPlatformPathAtPointAtRest(KaitaiStruct):
        SEQ_FIELDS = ["plat_tag", "path_point_idx"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['path_point_idx']['start'] = self._io.pos()
            self.path_point_idx = self._io.read_s2be()
            self._debug['path_point_idx']['end'] = self._io.pos()


    class PlatSetCollisionYOffset(KaitaiStruct):
        SEQ_FIELDS = ["y_offset"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['y_offset']['start'] = self._io.pos()
            self.y_offset = self._io.read_f4be()
            self._debug['y_offset']['end'] = self._io.pos()


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


    class PuzzleCondGloverStandingOnPlatform(KaitaiStruct):
        SEQ_FIELDS = ["plat_tag", "invert_result"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['plat_tag']['start'] = self._io.pos()
            self.plat_tag = self._io.read_u2be()
            self._debug['plat_tag']['end'] = self._io.pos()
            self._debug['invert_result']['start'] = self._io.pos()
            self.invert_result = self._io.read_s2be()
            self._debug['invert_result']['end'] = self._io.pos()


    class PuzzleCondGloverWithinRangeOfPoint(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "z", "range"]
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
            self._debug['range']['start'] = self._io.pos()
            self.range = self._io.read_f4be()
            self._debug['range']['end'] = self._io.pos()


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


    class CameoSetCameraAttention(KaitaiStruct):
        SEQ_FIELDS = ["enemy_idx", "x", "y", "z", "frame_count", "preceding_instr_idx"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['enemy_idx']['start'] = self._io.pos()
            self.enemy_idx = self._io.read_u2be()
            self._debug['enemy_idx']['end'] = self._io.pos()
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_f4be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_f4be()
            self._debug['z']['end'] = self._io.pos()
            self._debug['frame_count']['start'] = self._io.pos()
            self.frame_count = self._io.read_s2be()
            self._debug['frame_count']['end'] = self._io.pos()
            self._debug['preceding_instr_idx']['start'] = self._io.pos()
            self.preceding_instr_idx = self._io.read_s2be()
            self._debug['preceding_instr_idx']['end'] = self._io.pos()


    class EnemyKill(KaitaiStruct):
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


    class PlatHasPhysics(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


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


    class PuzzleActionChangeWaterHeight(KaitaiStruct):
        SEQ_FIELDS = ["y", "puzzle_tag", "activation_delay", "flags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_f4be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['puzzle_tag']['start'] = self._io.pos()
            self.puzzle_tag = self._io.read_s2be()
            self._debug['puzzle_tag']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.GenericFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()


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


    class PuzzleActionCameraLookAtPoint1(KaitaiStruct):
        SEQ_FIELDS = ["cam_x", "cam_y", "cam_z", "reserved", "reserved_2", "activation_delay", "flags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['cam_x']['start'] = self._io.pos()
            self.cam_x = self._io.read_f4be()
            self._debug['cam_x']['end'] = self._io.pos()
            self._debug['cam_y']['start'] = self._io.pos()
            self.cam_y = self._io.read_f4be()
            self._debug['cam_y']['end'] = self._io.pos()
            self._debug['cam_z']['start'] = self._io.pos()
            self.cam_z = self._io.read_f4be()
            self._debug['cam_z']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_u4be()
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['reserved_2']['start'] = self._io.pos()
            self.reserved_2 = self._io.read_u2be()
            self._debug['reserved_2']['end'] = self._io.pos()
            self._debug['activation_delay']['start'] = self._io.pos()
            self.activation_delay = self._io.read_u2be()
            self._debug['activation_delay']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = KaitaiStream.resolve_enum(GloverLevel.PuzzleAction.CameraFlags, self._io.read_u4be())
            self._debug['flags']['end'] = self._io.pos()




#############
# PATCHED BY ./python/scripts/ksy-patcher.py

switch_fields = {
    'GloverLevel.Cmd': {
        'params': {
            'field': 'type_code',
            'code-to-type': {
                0xbd: GloverLevel.AmbientSound,
                0xbe: GloverLevel.AmbientSoundAtPoint,
                0xa9: GloverLevel.SetGravity,
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
                0xb8: GloverLevel.PlatCollision0xb8Todo,
                0xb3: GloverLevel.PlatActorEnableWaterAnimation,
                0xb7: GloverLevel.PlatSetCollisionYOffset,
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
                0x8e: GloverLevel.PlatCauseDamage,
                0x5b: GloverLevel.PlatPush0x5b,
                0x72: GloverLevel.PlatConfBoundaryVolume,
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
                0xc1: GloverLevel.PlatMovementSound,
                0xc2: GloverLevel.PlatPathSoundAtPointHit,
                0x5e: GloverLevel.PlatTurnTowardsPathPoint,
                0x5f: GloverLevel.PlatGoForwards0x5f,
                0x6b: GloverLevel.PlatPathPoint,
                0x6c: GloverLevel.PlatMaxVelocity,
                0x6d: GloverLevel.PlatPathAcceleration,
                0xa7: GloverLevel.PlatPathSetStartingPoint,
                0xa6: GloverLevel.PlatSetInitialPos,
                0xc0: GloverLevel.PlatPlayObjectAnimation,
                0xa4: GloverLevel.PlatInteractsWithWater,
                0x5c: GloverLevel.PlatVentAdvanceFrames,
                0x64: GloverLevel.PlatNoClip,
                0x65: GloverLevel.PlatDestructible,
                0xc8: GloverLevel.PlatDestructibleSound,
                0x9d: GloverLevel.PlatHasPhysics,
                0x66: GloverLevel.PlatReverseAtEndsOfPath,
                0x6a: GloverLevel.PlatActorSurfaceType,
                0x6f: GloverLevel.PlatSetTag,
                0x82: GloverLevel.PlatSpike,
                0x79: GloverLevel.PlatScale,
                0x7a: GloverLevel.PlatStrobe,
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
                GloverLevel.AmbientSound: 0xbd,
                GloverLevel.AmbientSoundAtPoint: 0xbe,
                GloverLevel.SetGravity: 0xa9,
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
                GloverLevel.PlatCollision0xb8Todo: 0xb8,
                GloverLevel.PlatActorEnableWaterAnimation: 0xb3,
                GloverLevel.PlatSetCollisionYOffset: 0xb7,
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
                GloverLevel.PlatCauseDamage: 0x8e,
                GloverLevel.PlatPush0x5b: 0x5b,
                GloverLevel.PlatConfBoundaryVolume: 0x72,
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
                GloverLevel.PlatMovementSound: 0xc1,
                GloverLevel.PlatPathSoundAtPointHit: 0xc2,
                GloverLevel.PlatTurnTowardsPathPoint: 0x5e,
                GloverLevel.PlatGoForwards0x5f: 0x5f,
                GloverLevel.PlatPathPoint: 0x6b,
                GloverLevel.PlatMaxVelocity: 0x6c,
                GloverLevel.PlatPathAcceleration: 0x6d,
                GloverLevel.PlatPathSetStartingPoint: 0xa7,
                GloverLevel.PlatSetInitialPos: 0xa6,
                GloverLevel.PlatPlayObjectAnimation: 0xc0,
                GloverLevel.PlatInteractsWithWater: 0xa4,
                GloverLevel.PlatVentAdvanceFrames: 0x5c,
                GloverLevel.PlatNoClip: 0x64,
                GloverLevel.PlatDestructible: 0x65,
                GloverLevel.PlatDestructibleSound: 0xc8,
                GloverLevel.PlatHasPhysics: 0x9d,
                GloverLevel.PlatReverseAtEndsOfPath: 0x66,
                GloverLevel.PlatActorSurfaceType: 0x6a,
                GloverLevel.PlatSetTag: 0x6f,
                GloverLevel.PlatSpike: 0x82,
                GloverLevel.PlatScale: 0x79,
                GloverLevel.PlatStrobe: 0x7a,
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
                0x0: GloverLevel.CameoPlayAnimation,
                0x1: GloverLevel.CameoSetCameraAttention,
                0x2: GloverLevel.CameoInst2,
                0x3: GloverLevel.CameoSpin,
                0x4: GloverLevel.CameoGrabTodo,
                0x5: GloverLevel.CameoSetEnemyFlagTodo,
                0x6: GloverLevel.CameoLightningFlash,
                None: GloverLevel.CameoInstDefault,
            },
            'type-to-code': {
                GloverLevel.CameoPlayAnimation: 0x0,
                GloverLevel.CameoSetCameraAttention: 0x1,
                GloverLevel.CameoInst2: 0x2,
                GloverLevel.CameoSpin: 0x3,
                GloverLevel.CameoGrabTodo: 0x4,
                GloverLevel.CameoSetEnemyFlagTodo: 0x5,
                GloverLevel.CameoLightningFlash: 0x6,
                GloverLevel.CameoInstDefault: None,
            }
        },
    },
    'GloverLevel.PuzzleCond': {
        'body': {
            'field': 'cond_type',
            'code-to-type': {
                0x9: GloverLevel.PuzzleCondPlatformPathAtPointAtRest,
                0xa: GloverLevel.PuzzleCondPlatformSpinTodo,
                0xb: GloverLevel.PuzzleCondPlatformOrbitTodo,
                0xc: GloverLevel.PuzzleCondPlatformPathAtPoint2,
                0xd: GloverLevel.PuzzleCondPlatformSpin2Todo,
                0xe: GloverLevel.PuzzleCondPlatformOrbit2Todo,
                0xf: GloverLevel.PuzzleCondGloverStandingOnPlatform,
                0x10: GloverLevel.PuzzleCondGloverChangedStandingOnPlatform,
                0x11: GloverLevel.PuzzleCondBallStandingOnPlatform,
                0x12: GloverLevel.PuzzleCondBallChangedStandingOnPlatform,
                0x13: GloverLevel.PuzzleCondEnemyStandingOnPlatform,
                0x14: GloverLevel.PuzzleCondEnemyChangedStandingOnPlatform,
                0x15: GloverLevel.PuzzleCondGloverIsTouchingPlatform,
                0x16: GloverLevel.PuzzleCondGloverChangedTouchingPlatform,
                0x17: GloverLevel.PuzzleCondBallIsTouchingPlatform,
                0x18: GloverLevel.PuzzleCondBallChangedTouchingPlatform,
                0x19: GloverLevel.PuzzleCondEnemyIsTouchingPlatform,
                0x1a: GloverLevel.PuzzleCondEnemyChangedTouchingPlatform,
                0x1b: GloverLevel.PuzzleCondRegEq,
                0x1c: GloverLevel.PuzzleCondRegNe,
                0x1d: GloverLevel.PuzzleCondRegGt,
                0x1e: GloverLevel.PuzzleCondRegLt,
                0x1f: GloverLevel.PuzzleCondPlatformTouchingConfBoundaryEdge,
                0x20: GloverLevel.PuzzleCondPlatformCloseToConfBoundaryEdge,
                0x21: GloverLevel.PuzzleCondSpecificEnemyExists,
                0x22: GloverLevel.PuzzleCond0x22,
                0x23: GloverLevel.PuzzleCondGloverWithinVolume,
                0x24: GloverLevel.PuzzleCondGloverWithinRangeOfPoint,
                0x25: GloverLevel.PuzzleCondBallWithinVolume,
                0x26: GloverLevel.PuzzleCondBallWithinRangeOfPoint,
                0x27: GloverLevel.PuzzleCondCameraWithinVolume,
                0x28: GloverLevel.PuzzleCondCameraWithinRangeOfPoint,
                0x29: GloverLevel.PuzzleCondGloverWithinRangeOfPoint2,
                0x2a: GloverLevel.PuzzleCondPlatformDoesntExist,
                None: GloverLevel.PuzzleCondDefault,
            },
            'type-to-code': {
                GloverLevel.PuzzleCondPlatformPathAtPointAtRest: 0x9,
                GloverLevel.PuzzleCondPlatformSpinTodo: 0xa,
                GloverLevel.PuzzleCondPlatformOrbitTodo: 0xb,
                GloverLevel.PuzzleCondPlatformPathAtPoint2: 0xc,
                GloverLevel.PuzzleCondPlatformSpin2Todo: 0xd,
                GloverLevel.PuzzleCondPlatformOrbit2Todo: 0xe,
                GloverLevel.PuzzleCondGloverStandingOnPlatform: 0xf,
                GloverLevel.PuzzleCondGloverChangedStandingOnPlatform: 0x10,
                GloverLevel.PuzzleCondBallStandingOnPlatform: 0x11,
                GloverLevel.PuzzleCondBallChangedStandingOnPlatform: 0x12,
                GloverLevel.PuzzleCondEnemyStandingOnPlatform: 0x13,
                GloverLevel.PuzzleCondEnemyChangedStandingOnPlatform: 0x14,
                GloverLevel.PuzzleCondGloverIsTouchingPlatform: 0x15,
                GloverLevel.PuzzleCondGloverChangedTouchingPlatform: 0x16,
                GloverLevel.PuzzleCondBallIsTouchingPlatform: 0x17,
                GloverLevel.PuzzleCondBallChangedTouchingPlatform: 0x18,
                GloverLevel.PuzzleCondEnemyIsTouchingPlatform: 0x19,
                GloverLevel.PuzzleCondEnemyChangedTouchingPlatform: 0x1a,
                GloverLevel.PuzzleCondRegEq: 0x1b,
                GloverLevel.PuzzleCondRegNe: 0x1c,
                GloverLevel.PuzzleCondRegGt: 0x1d,
                GloverLevel.PuzzleCondRegLt: 0x1e,
                GloverLevel.PuzzleCondPlatformTouchingConfBoundaryEdge: 0x1f,
                GloverLevel.PuzzleCondPlatformCloseToConfBoundaryEdge: 0x20,
                GloverLevel.PuzzleCondSpecificEnemyExists: 0x21,
                GloverLevel.PuzzleCond0x22: 0x22,
                GloverLevel.PuzzleCondGloverWithinVolume: 0x23,
                GloverLevel.PuzzleCondGloverWithinRangeOfPoint: 0x24,
                GloverLevel.PuzzleCondBallWithinVolume: 0x25,
                GloverLevel.PuzzleCondBallWithinRangeOfPoint: 0x26,
                GloverLevel.PuzzleCondCameraWithinVolume: 0x27,
                GloverLevel.PuzzleCondCameraWithinRangeOfPoint: 0x28,
                GloverLevel.PuzzleCondGloverWithinRangeOfPoint2: 0x29,
                GloverLevel.PuzzleCondPlatformDoesntExist: 0x2a,
                GloverLevel.PuzzleCondDefault: None,
            }
        },
    },
    'GloverLevel.PuzzleAction': {
        'body': {
            'field': 'action_type',
            'code-to-type': {
                0x2d: GloverLevel.PuzzleActionPlatformNudge,
                0x2e: GloverLevel.PuzzleActionPlatformConfigSpin,
                0x2f: GloverLevel.PuzzleActionPlatformConfigOrbit,
                0x30: GloverLevel.PuzzleActionPlatformMoveToPointIdxMinusOne,
                0x33: GloverLevel.PuzzleActionPlatformSpinAlongAxis,
                0x34: GloverLevel.PuzzleActionControlActiveElements,
                0x35: GloverLevel.PuzzleActionSetConveyor,
                0x36: GloverLevel.PuzzleActionHidePlatform,
                0x37: GloverLevel.PuzzleActionTogglePlatformPhysics,
                0x38: GloverLevel.PuzzleActionRegSet,
                0x39: GloverLevel.PuzzleActionRegAdd,
                0x3a: GloverLevel.PuzzleActionRegSub,
                0x3b: GloverLevel.PuzzleActionSpawnPowerup,
                0x3c: GloverLevel.PuzzleActionSpawnEnemy,
                0x3d: GloverLevel.PuzzleActionSetPlatformVelocity,
                0x3e: GloverLevel.PuzzleActionCameraLookAtPlatform,
                0x3f: GloverLevel.PuzzleActionCameraLookAtPoint2,
                0x40: GloverLevel.PuzzleActionCameraLookAtPoint1,
                0x41: GloverLevel.PuzzleActionCameraSetDistance,
                0x43: GloverLevel.PuzzleActionEnemySetAiInstruction,
                0x44: GloverLevel.PuzzleActionToggleWind,
                0x45: GloverLevel.PuzzleActionSpawnGaribGroup,
                0x46: GloverLevel.PuzzleActionCameraTweenYAdjust,
                0x47: GloverLevel.PuzzleActionCameraTweenDistance,
                0x48: GloverLevel.PuzzleActionCameraTurnTowardsFocus,
                0x49: GloverLevel.PuzzleActionCameraFlyTowardsPoint,
                0x4a: GloverLevel.PuzzleActionCameraLookAtGlover,
                0x4b: GloverLevel.PuzzleAction0x4b0x4c,
                0x4c: GloverLevel.PuzzleAction0x4b0x4c,
                0x4d: GloverLevel.PuzzleActionCameraFlyTowardsPointRelativeToGlover,
                0x4e: GloverLevel.PuzzleActionChangeWaterHeight,
                0x4f: GloverLevel.PuzzleAction0x4f,
                0x50: GloverLevel.PuzzleActionSetGravity,
                0x51: GloverLevel.PuzzleActionStartCameo,
                0x52: GloverLevel.PuzzleActionSetPlatformPathDirection,
                0x53: GloverLevel.PuzzleActionMakeBallInteractive,
                0x54: GloverLevel.PuzzleActionSoundControl,
                0x55: GloverLevel.PuzzleActionSetBackground,
                0x56: GloverLevel.PuzzleActionSetFog,
                None: GloverLevel.PuzzleActionDefault,
            },
            'type-to-code': {
                GloverLevel.PuzzleActionPlatformNudge: 0x2d,
                GloverLevel.PuzzleActionPlatformConfigSpin: 0x2e,
                GloverLevel.PuzzleActionPlatformConfigOrbit: 0x2f,
                GloverLevel.PuzzleActionPlatformMoveToPointIdxMinusOne: 0x30,
                GloverLevel.PuzzleActionPlatformSpinAlongAxis: 0x33,
                GloverLevel.PuzzleActionControlActiveElements: 0x34,
                GloverLevel.PuzzleActionSetConveyor: 0x35,
                GloverLevel.PuzzleActionHidePlatform: 0x36,
                GloverLevel.PuzzleActionTogglePlatformPhysics: 0x37,
                GloverLevel.PuzzleActionRegSet: 0x38,
                GloverLevel.PuzzleActionRegAdd: 0x39,
                GloverLevel.PuzzleActionRegSub: 0x3a,
                GloverLevel.PuzzleActionSpawnPowerup: 0x3b,
                GloverLevel.PuzzleActionSpawnEnemy: 0x3c,
                GloverLevel.PuzzleActionSetPlatformVelocity: 0x3d,
                GloverLevel.PuzzleActionCameraLookAtPlatform: 0x3e,
                GloverLevel.PuzzleActionCameraLookAtPoint2: 0x3f,
                GloverLevel.PuzzleActionCameraLookAtPoint1: 0x40,
                GloverLevel.PuzzleActionCameraSetDistance: 0x41,
                GloverLevel.PuzzleActionEnemySetAiInstruction: 0x43,
                GloverLevel.PuzzleActionToggleWind: 0x44,
                GloverLevel.PuzzleActionSpawnGaribGroup: 0x45,
                GloverLevel.PuzzleActionCameraTweenYAdjust: 0x46,
                GloverLevel.PuzzleActionCameraTweenDistance: 0x47,
                GloverLevel.PuzzleActionCameraTurnTowardsFocus: 0x48,
                GloverLevel.PuzzleActionCameraFlyTowardsPoint: 0x49,
                GloverLevel.PuzzleActionCameraLookAtGlover: 0x4a,
                GloverLevel.PuzzleAction0x4b0x4c: [75, 76],
                GloverLevel.PuzzleActionCameraFlyTowardsPointRelativeToGlover: 0x4d,
                GloverLevel.PuzzleActionChangeWaterHeight: 0x4e,
                GloverLevel.PuzzleAction0x4f: 0x4f,
                GloverLevel.PuzzleActionSetGravity: 0x50,
                GloverLevel.PuzzleActionStartCameo: 0x51,
                GloverLevel.PuzzleActionSetPlatformPathDirection: 0x52,
                GloverLevel.PuzzleActionMakeBallInteractive: 0x53,
                GloverLevel.PuzzleActionSoundControl: 0x54,
                GloverLevel.PuzzleActionSetBackground: 0x55,
                GloverLevel.PuzzleActionSetFog: 0x56,
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
                0x3: GloverLevel.EnemyInstructionRandomWalk,
                0x4: GloverLevel.EnemyInstructionRest,
                0x5: GloverLevel.EnemyInstructionBullet0x5,
                0x6: GloverLevel.EnemyInstructionBullet0x6,
                0x7: GloverLevel.EnemyInstructionPlayAnimation,
                0x8: GloverLevel.EnemyInstructionFacePlayer,
                0x9: GloverLevel.EnemyInstructionFollowPlayer,
                0xa: GloverLevel.EnemyInstructionGlom,
                0xb: GloverLevel.EnemyInstructionCatapult,
                0xc: GloverLevel.EnemyInstructionFleePlayer,
                0xd: GloverLevel.EnemyInstructionSteer,
                0xe: GloverLevel.EnemyInstructionSetTimer,
                0xf: GloverLevel.EnemyInstructionAttack,
                0x10: GloverLevel.EnemyInstructionC,
                0x11: GloverLevel.EnemyInstructionC,
                0x12: GloverLevel.EnemyInstructionGoto,
                0x13: GloverLevel.EnemyInstructionNoop,
                0x14: GloverLevel.EnemyInstructionC,
                0x15: GloverLevel.EnemyInstructionC,
                0x16: GloverLevel.EnemyInstructionA,
                0x17: GloverLevel.EnemyImpulseForward,
                0x18: GloverLevel.EnemyKill,
                None: GloverLevel.EnemyInstructionError,
            },
            'type-to-code': {
                GloverLevel.EnemyInstructionMove: 0x0,
                GloverLevel.EnemyInstructionDash: 0x1,
                GloverLevel.EnemyInstructionTurn: 0x2,
                GloverLevel.EnemyInstructionRandomWalk: 0x3,
                GloverLevel.EnemyInstructionRest: 0x4,
                GloverLevel.EnemyInstructionBullet0x5: 0x5,
                GloverLevel.EnemyInstructionBullet0x6: 0x6,
                GloverLevel.EnemyInstructionPlayAnimation: 0x7,
                GloverLevel.EnemyInstructionFacePlayer: 0x8,
                GloverLevel.EnemyInstructionFollowPlayer: 0x9,
                GloverLevel.EnemyInstructionGlom: 0xa,
                GloverLevel.EnemyInstructionCatapult: 0xb,
                GloverLevel.EnemyInstructionFleePlayer: 0xc,
                GloverLevel.EnemyInstructionSteer: 0xd,
                GloverLevel.EnemyInstructionSetTimer: 0xe,
                GloverLevel.EnemyInstructionAttack: 0xf,
                GloverLevel.EnemyInstructionC: [16, 17, 20, 21],
                GloverLevel.EnemyInstructionGoto: 0x12,
                GloverLevel.EnemyInstructionNoop: 0x13,
                GloverLevel.EnemyInstructionA: 0x16,
                GloverLevel.EnemyImpulseForward: 0x17,
                GloverLevel.EnemyKill: 0x18,
                GloverLevel.EnemyInstructionError: None,
            }
        },
    },
}
original_names = {
    'GloverLevel': 'glover_level',
    'GloverLevel.Cmd': 'glover_level.cmd',
    'GloverLevel.AmbientSound': 'glover_level.ambient_sound',
    'GloverLevel.AmbientSoundAtPoint': 'glover_level.ambient_sound_at_point',
    'GloverLevel.SetGravity': 'glover_level.set_gravity',
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
    'GloverLevel.CameoPlayAnimation': 'glover_level.cameo_play_animation',
    'GloverLevel.CameoSetCameraAttention': 'glover_level.cameo_set_camera_attention',
    'GloverLevel.CameoInst2': 'glover_level.cameo_inst_2',
    'GloverLevel.CameoSpin': 'glover_level.cameo_spin',
    'GloverLevel.CameoGrabTodo': 'glover_level.cameo_grab_todo',
    'GloverLevel.CameoSetEnemyFlagTodo': 'glover_level.cameo_set_enemy_flag_todo',
    'GloverLevel.CameoLightningFlash': 'glover_level.cameo_lightning_flash',
    'GloverLevel.CameoInstDefault': 'glover_level.cameo_inst_default',
    'GloverLevel.Puzzle': 'glover_level.puzzle',
    'GloverLevel.PuzzleAnd': 'glover_level.puzzle_and',
    'GloverLevel.PuzzleOr': 'glover_level.puzzle_or',
    'GloverLevel.PuzzleNumtimes': 'glover_level.puzzle_numtimes',
    'GloverLevel.PuzzleAny': 'glover_level.puzzle_any',
    'GloverLevel.PuzzleCond': 'glover_level.puzzle_cond',
    'GloverLevel.PuzzleCondPlatformPathAtPointAtRest': 'glover_level.puzzle_cond_platform_path_at_point_at_rest',
    'GloverLevel.PuzzleCondPlatformSpinTodo': 'glover_level.puzzle_cond_platform_spin_todo',
    'GloverLevel.PuzzleCondPlatformOrbitTodo': 'glover_level.puzzle_cond_platform_orbit_todo',
    'GloverLevel.PuzzleCondPlatformPathAtPoint2': 'glover_level.puzzle_cond_platform_path_at_point_2',
    'GloverLevel.PuzzleCondPlatformSpin2Todo': 'glover_level.puzzle_cond_platform_spin_2_todo',
    'GloverLevel.PuzzleCondPlatformOrbit2Todo': 'glover_level.puzzle_cond_platform_orbit_2_todo',
    'GloverLevel.PuzzleCondGloverStandingOnPlatform': 'glover_level.puzzle_cond_glover_standing_on_platform',
    'GloverLevel.PuzzleCondGloverChangedStandingOnPlatform': 'glover_level.puzzle_cond_glover_changed_standing_on_platform',
    'GloverLevel.PuzzleCondBallStandingOnPlatform': 'glover_level.puzzle_cond_ball_standing_on_platform',
    'GloverLevel.PuzzleCondBallChangedStandingOnPlatform': 'glover_level.puzzle_cond_ball_changed_standing_on_platform',
    'GloverLevel.PuzzleCondEnemyStandingOnPlatform': 'glover_level.puzzle_cond_enemy_standing_on_platform',
    'GloverLevel.PuzzleCondEnemyChangedStandingOnPlatform': 'glover_level.puzzle_cond_enemy_changed_standing_on_platform',
    'GloverLevel.PuzzleCondGloverIsTouchingPlatform': 'glover_level.puzzle_cond_glover_is_touching_platform',
    'GloverLevel.PuzzleCondGloverChangedTouchingPlatform': 'glover_level.puzzle_cond_glover_changed_touching_platform',
    'GloverLevel.PuzzleCondBallIsTouchingPlatform': 'glover_level.puzzle_cond_ball_is_touching_platform',
    'GloverLevel.PuzzleCondBallChangedTouchingPlatform': 'glover_level.puzzle_cond_ball_changed_touching_platform',
    'GloverLevel.PuzzleCondEnemyIsTouchingPlatform': 'glover_level.puzzle_cond_enemy_is_touching_platform',
    'GloverLevel.PuzzleCondEnemyChangedTouchingPlatform': 'glover_level.puzzle_cond_enemy_changed_touching_platform',
    'GloverLevel.PuzzleCondPlatformTouchingConfBoundaryEdge': 'glover_level.puzzle_cond_platform_touching_conf_boundary_edge',
    'GloverLevel.PuzzleCondPlatformCloseToConfBoundaryEdge': 'glover_level.puzzle_cond_platform_close_to_conf_boundary_edge',
    'GloverLevel.PuzzleCondSpecificEnemyExists': 'glover_level.puzzle_cond_specific_enemy_exists',
    'GloverLevel.PuzzleCondRegEq': 'glover_level.puzzle_cond_reg_eq',
    'GloverLevel.PuzzleCondRegNe': 'glover_level.puzzle_cond_reg_ne',
    'GloverLevel.PuzzleCondRegGt': 'glover_level.puzzle_cond_reg_gt',
    'GloverLevel.PuzzleCondRegLt': 'glover_level.puzzle_cond_reg_lt',
    'GloverLevel.PuzzleCondDefault': 'glover_level.puzzle_cond_default',
    'GloverLevel.PuzzleCond0x22': 'glover_level.puzzle_cond_0x22',
    'GloverLevel.PuzzleCondGloverWithinVolume': 'glover_level.puzzle_cond_glover_within_volume',
    'GloverLevel.PuzzleCondBallWithinVolume': 'glover_level.puzzle_cond_ball_within_volume',
    'GloverLevel.PuzzleCondCameraWithinVolume': 'glover_level.puzzle_cond_camera_within_volume',
    'GloverLevel.PuzzleCondGloverWithinRangeOfPoint': 'glover_level.puzzle_cond_glover_within_range_of_point',
    'GloverLevel.PuzzleCondBallWithinRangeOfPoint': 'glover_level.puzzle_cond_ball_within_range_of_point',
    'GloverLevel.PuzzleCondCameraWithinRangeOfPoint': 'glover_level.puzzle_cond_camera_within_range_of_point',
    'GloverLevel.PuzzleCondGloverWithinRangeOfPoint2': 'glover_level.puzzle_cond_glover_within_range_of_point_2',
    'GloverLevel.PuzzleCondPlatformDoesntExist': 'glover_level.puzzle_cond_platform_doesnt_exist',
    'GloverLevel.PuzzleAction': 'glover_level.puzzle_action',
    'GloverLevel.PuzzleActionRegSet': 'glover_level.puzzle_action_reg_set',
    'GloverLevel.PuzzleActionRegAdd': 'glover_level.puzzle_action_reg_add',
    'GloverLevel.PuzzleActionRegSub': 'glover_level.puzzle_action_reg_sub',
    'GloverLevel.PuzzleAction0x4f': 'glover_level.puzzle_action_0x4f',
    'GloverLevel.PuzzleActionSpawnPowerup': 'glover_level.puzzle_action_spawn_powerup',
    'GloverLevel.PuzzleActionSpawnEnemy': 'glover_level.puzzle_action_spawn_enemy',
    'GloverLevel.PuzzleActionCameraLookAtPlatform': 'glover_level.puzzle_action_camera_look_at_platform',
    'GloverLevel.PuzzleActionCameraLookAtPoint1': 'glover_level.puzzle_action_camera_look_at_point_1',
    'GloverLevel.PuzzleActionCameraLookAtPoint2': 'glover_level.puzzle_action_camera_look_at_point_2',
    'GloverLevel.PuzzleActionSetConveyor': 'glover_level.puzzle_action_set_conveyor',
    'GloverLevel.PuzzleActionSetPlatformVelocity': 'glover_level.puzzle_action_set_platform_velocity',
    'GloverLevel.PuzzleActionSetPlatformPathDirection': 'glover_level.puzzle_action_set_platform_path_direction',
    'GloverLevel.PuzzleActionControlActiveElements': 'glover_level.puzzle_action_control_active_elements',
    'GloverLevel.PuzzleActionPlatformNudge': 'glover_level.puzzle_action_platform_nudge',
    'GloverLevel.PuzzleActionPlatformConfigSpin': 'glover_level.puzzle_action_platform_config_spin',
    'GloverLevel.PuzzleActionPlatformConfigOrbit': 'glover_level.puzzle_action_platform_config_orbit',
    'GloverLevel.PuzzleActionHidePlatform': 'glover_level.puzzle_action_hide_platform',
    'GloverLevel.PuzzleActionTogglePlatformPhysics': 'glover_level.puzzle_action_toggle_platform_physics',
    'GloverLevel.PuzzleActionPlatformMoveToPointIdxMinusOne': 'glover_level.puzzle_action_platform_move_to_point_idx_minus_one',
    'GloverLevel.PuzzleActionPlatformSpinAlongAxis': 'glover_level.puzzle_action_platform_spin_along_axis',
    'GloverLevel.PuzzleActionEnemySetAiInstruction': 'glover_level.puzzle_action_enemy_set_ai_instruction',
    'GloverLevel.PuzzleActionToggleWind': 'glover_level.puzzle_action_toggle_wind',
    'GloverLevel.PuzzleActionSpawnGaribGroup': 'glover_level.puzzle_action_spawn_garib_group',
    'GloverLevel.PuzzleActionCameraSetDistance': 'glover_level.puzzle_action_camera_set_distance',
    'GloverLevel.PuzzleActionChangeWaterHeight': 'glover_level.puzzle_action_change_water_height',
    'GloverLevel.PuzzleActionSetGravity': 'glover_level.puzzle_action_set_gravity',
    'GloverLevel.PuzzleActionStartCameo': 'glover_level.puzzle_action_start_cameo',
    'GloverLevel.PuzzleActionMakeBallInteractive': 'glover_level.puzzle_action_make_ball_interactive',
    'GloverLevel.PuzzleActionDefault': 'glover_level.puzzle_action_default',
    'GloverLevel.PuzzleActionCameraTweenYAdjust': 'glover_level.puzzle_action_camera_tween_y_adjust',
    'GloverLevel.PuzzleActionCameraTweenDistance': 'glover_level.puzzle_action_camera_tween_distance',
    'GloverLevel.PuzzleActionCameraTurnTowardsFocus': 'glover_level.puzzle_action_camera_turn_towards_focus',
    'GloverLevel.PuzzleActionCameraFlyTowardsPoint': 'glover_level.puzzle_action_camera_fly_towards_point',
    'GloverLevel.PuzzleActionCameraFlyTowardsPointRelativeToGlover': 'glover_level.puzzle_action_camera_fly_towards_point_relative_to_glover',
    'GloverLevel.PuzzleActionCameraLookAtGlover': 'glover_level.puzzle_action_camera_look_at_glover',
    'GloverLevel.PuzzleActionSoundControl': 'glover_level.puzzle_action_sound_control',
    'GloverLevel.PuzzleActionSetBackground': 'glover_level.puzzle_action_set_background',
    'GloverLevel.PuzzleActionSetFog': 'glover_level.puzzle_action_set_fog',
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
    'GloverLevel.PlatCollision0xb8Todo': 'glover_level.plat_collision_0xb8_todo',
    'GloverLevel.PlatActorEnableWaterAnimation': 'glover_level.plat_actor_enable_water_animation',
    'GloverLevel.PlatSetCollisionYOffset': 'glover_level.plat_set_collision_y_offset',
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
    'GloverLevel.PlatCauseDamage': 'glover_level.plat_cause_damage',
    'GloverLevel.PlatPush0x5b': 'glover_level.plat_push_0x5b',
    'GloverLevel.PlatConfBoundaryVolume': 'glover_level.plat_conf_boundary_volume',
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
    'GloverLevel.PlatMovementSound': 'glover_level.plat_movement_sound',
    'GloverLevel.PlatPathSoundAtPointHit': 'glover_level.plat_path_sound_at_point_hit',
    'GloverLevel.PlatTurnTowardsPathPoint': 'glover_level.plat_turn_towards_path_point',
    'GloverLevel.PlatGoForwards0x5f': 'glover_level.plat_go_forwards_0x5f',
    'GloverLevel.PlatPathPoint': 'glover_level.plat_path_point',
    'GloverLevel.PlatMaxVelocity': 'glover_level.plat_max_velocity',
    'GloverLevel.PlatPathAcceleration': 'glover_level.plat_path_acceleration',
    'GloverLevel.PlatPathSetStartingPoint': 'glover_level.plat_path_set_starting_point',
    'GloverLevel.PlatSetInitialPos': 'glover_level.plat_set_initial_pos',
    'GloverLevel.PlatPlayObjectAnimation': 'glover_level.plat_play_object_animation',
    'GloverLevel.PlatInteractsWithWater': 'glover_level.plat_interacts_with_water',
    'GloverLevel.PlatVentAdvanceFrames': 'glover_level.plat_vent_advance_frames',
    'GloverLevel.PlatNoClip': 'glover_level.plat_no_clip',
    'GloverLevel.PlatDestructible': 'glover_level.plat_destructible',
    'GloverLevel.PlatDestructibleSound': 'glover_level.plat_destructible_sound',
    'GloverLevel.PlatHasPhysics': 'glover_level.plat_has_physics',
    'GloverLevel.PlatReverseAtEndsOfPath': 'glover_level.plat_reverse_at_ends_of_path',
    'GloverLevel.PlatActorSurfaceType': 'glover_level.plat_actor_surface_type',
    'GloverLevel.PlatSetTag': 'glover_level.plat_set_tag',
    'GloverLevel.PlatSpike': 'glover_level.plat_spike',
    'GloverLevel.PlatScale': 'glover_level.plat_scale',
    'GloverLevel.PlatStrobe': 'glover_level.plat_strobe',
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
    'GloverLevel.EnemyImpulseForward': 'glover_level.enemy_impulse_forward',
    'GloverLevel.EnemyInstructionSteer': 'glover_level.enemy_instruction_steer',
    'GloverLevel.EnemyInstructionCatapult': 'glover_level.enemy_instruction_catapult',
    'GloverLevel.EnemyInstructionGlom': 'glover_level.enemy_instruction_glom',
    'GloverLevel.EnemyInstructionFollowPlayer': 'glover_level.enemy_instruction_follow_player',
    'GloverLevel.EnemyInstructionDash': 'glover_level.enemy_instruction_dash',
    'GloverLevel.EnemyInstructionMove': 'glover_level.enemy_instruction_move',
    'GloverLevel.EnemyInstructionTurn': 'glover_level.enemy_instruction_turn',
    'GloverLevel.EnemyInstructionGoto': 'glover_level.enemy_instruction_goto',
    'GloverLevel.EnemyInstructionRandomWalk': 'glover_level.enemy_instruction_random_walk',
    'GloverLevel.EnemyInstructionPlayAnimation': 'glover_level.enemy_instruction_play_animation',
    'GloverLevel.EnemyInstructionRest': 'glover_level.enemy_instruction_rest',
    'GloverLevel.EnemyInstructionAttack': 'glover_level.enemy_instruction_attack',
    'GloverLevel.EnemyInstructionBullet0x5': 'glover_level.enemy_instruction_bullet_0x5',
    'GloverLevel.EnemyInstructionBullet0x6': 'glover_level.enemy_instruction_bullet_0x6',
    'GloverLevel.EnemyInstructionFacePlayer': 'glover_level.enemy_instruction_face_player',
    'GloverLevel.EnemyInstructionFleePlayer': 'glover_level.enemy_instruction_flee_player',
    'GloverLevel.EnemyInstructionSetTimer': 'glover_level.enemy_instruction_set_timer',
    'GloverLevel.EnemyKill': 'glover_level.enemy_kill',
    'GloverLevel.EnemyInstructionNoop': 'glover_level.enemy_instruction_noop',
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
    'GloverLevel.Wind.Seq[12]': {'semantic': {'tag-namespace': 'wind'}},
    'GloverLevel.Water.Seq[9]': {'semantic': {'tag-namespace': 'water'}},
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
    'GloverLevel.PlatCollision0xb8Todo': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatActorEnableWaterAnimation': {'semantic': {'modifies': ['PLATFORM', 'LAND_ACTOR', 'BG_ACTOR', 'ANIMATED_BG_ACTOR']}},
    'GloverLevel.PlatSetCollisionYOffset': {'semantic': {'modifies': 'PLATFORM'}},
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
    'GloverLevel.PlatCauseDamage': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatPush0x5b': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatConfBoundaryVolume': {'semantic': {'modifies': 'PLATFORM'}},
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
    'GloverLevel.PlatMovementSound': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatPathSoundAtPointHit': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatTurnTowardsPathPoint': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatGoForwards0x5f': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatPathPoint': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatMaxVelocity': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatPathAcceleration': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatPathSetStartingPoint': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatSetInitialPos': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatPlayObjectAnimation': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatInteractsWithWater': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatVentAdvanceFrames': {'semantic': {'modifies': ['PLATFORM', 'VENT']}},
    'GloverLevel.PlatNoClip': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatDestructible': {'semantic': {'modifies': 'PLATFORM'}, '_annotated_children': ['GloverLevel.PlatDestructible.Seq[2]']},
    'GloverLevel.PlatDestructible.Seq[2]': {'semantic': {'hash-namespace': 'object'}},
    'GloverLevel.PlatDestructibleSound': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatHasPhysics': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatReverseAtEndsOfPath': {'semantic': {'modifies': 'PLATFORM'}},
    'GloverLevel.PlatActorSurfaceType': {'semantic': {'modifies': ['PLATFORM', 'LAND_ACTOR', 'BG_ACTOR', 'ANIMATED_BG_ACTOR']}},
    'GloverLevel.PlatSetTag': {'semantic': {'modifies': 'PLATFORM'}, '_annotated_children': ['GloverLevel.PlatSetTag.Seq[0]']},
    'GloverLevel.PlatSetTag.Seq[0]': {'semantic': {'tag-namespace': 'platform'}},
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
    'GloverLevel': {'_annotated_children': ['GloverLevel.Actor0xbf', 'GloverLevel.AnimatedBackgroundActor', 'GloverLevel.BackgroundActor', 'GloverLevel.LandActor', 'GloverLevel.SetActorRotation', 'GloverLevel.SetActorScale', 'GloverLevel.Cameo', 'GloverLevel.CameoInst', 'GloverLevel.Puzzle', 'GloverLevel.PuzzleAnd', 'GloverLevel.PuzzleOr', 'GloverLevel.PuzzleNumtimes', 'GloverLevel.PuzzleAny', 'GloverLevel.PuzzleCond', 'GloverLevel.PuzzleAction', 'GloverLevel.GaribGroup', 'GloverLevel.Garib', 'GloverLevel.PlatMvspn0x58', 'GloverLevel.PlatMvspn0x59', 'GloverLevel.PlatMvspn0x5a', 'GloverLevel.PlatSetParent', 'GloverLevel.PlatMvspn0x73', 'GloverLevel.PlatMvspn0x74', 'GloverLevel.PlatCopySpinFromParent', 'GloverLevel.PlatCollision0xb8Todo', 'GloverLevel.PlatActorEnableWaterAnimation', 'GloverLevel.PlatSetCollisionYOffset', 'GloverLevel.Buzzer', 'GloverLevel.BuzzerDutyCycle', 'GloverLevel.SetObjectSparkle', 'GloverLevel.PlatSpecial0xb9', 'GloverLevel.SetExit', 'GloverLevel.PlatCat0x69', 'GloverLevel.PlatformConveyor', 'GloverLevel.PlatSpecial0x9e', 'GloverLevel.SetTeleport', 'GloverLevel.PlatFan0x8a', 'GloverLevel.PlatMagnet0x8b', 'GloverLevel.PlatCheckpoint', 'GloverLevel.PlatCrumb0x67', 'GloverLevel.PlatSpecial0xc7', 'GloverLevel.PlatSpecial0x6e', 'GloverLevel.PlatCauseDamage', 'GloverLevel.PlatPush0x5b', 'GloverLevel.PlatConfBoundaryVolume', 'GloverLevel.PlatOrbitSound0xc4', 'GloverLevel.Plat0xc6', 'GloverLevel.PlatOrbitAroundPoint', 'GloverLevel.PlatOrbitPause', 'GloverLevel.PlatOrbitFlip0x77', 'GloverLevel.Plat0xc3', 'GloverLevel.PlatSpinSound0xc5', 'GloverLevel.Plat0x9f', 'GloverLevel.PlatSpinPause0x7c', 'GloverLevel.PlatSpinFlip', 'GloverLevel.Plat0x7e', 'GloverLevel.PlatConstantSpin', 'GloverLevel.PlatSpin0x80', 'GloverLevel.PlatTopple0x81', 'GloverLevel.LookAtHand0x60', 'GloverLevel.LookAtBall0x61', 'GloverLevel.PlatRocking', 'GloverLevel.Plat0x78', 'GloverLevel.PlatMovementSound', 'GloverLevel.PlatPathSoundAtPointHit', 'GloverLevel.PlatTurnTowardsPathPoint', 'GloverLevel.PlatGoForwards0x5f', 'GloverLevel.PlatPathPoint', 'GloverLevel.PlatMaxVelocity', 'GloverLevel.PlatPathAcceleration', 'GloverLevel.PlatPathSetStartingPoint', 'GloverLevel.PlatSetInitialPos', 'GloverLevel.PlatPlayObjectAnimation', 'GloverLevel.PlatInteractsWithWater', 'GloverLevel.PlatVentAdvanceFrames', 'GloverLevel.PlatNoClip', 'GloverLevel.PlatDestructible', 'GloverLevel.PlatDestructibleSound', 'GloverLevel.PlatHasPhysics', 'GloverLevel.PlatReverseAtEndsOfPath', 'GloverLevel.PlatActorSurfaceType', 'GloverLevel.PlatSetTag', 'GloverLevel.PlatSpike', 'GloverLevel.PlatScale', 'GloverLevel.Vent', 'GloverLevel.VentDutyCycle', 'GloverLevel.Platform', 'GloverLevel.NullPlatform', 'GloverLevel.Enemy', 'GloverLevel.EnemySetAttentionBbox', 'GloverLevel.Enemy0xba', 'GloverLevel.EnemyFinalize', 'GloverLevel.EnemyNormalInstruction', 'GloverLevel.EnemyConditionalInstruction', 'GloverLevel.EnemyAttackInstruction']},
    'GloverLevel.Wind': {'_annotated_children': ['GloverLevel.Wind.Seq[12]']},
    'GloverLevel.Water': {'_annotated_children': ['GloverLevel.Water.Seq[9]', 'GloverLevel.Water.Seq[10]']},
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

ksy_hash = '31166ff98fef376ec8c3396a9c60e94389a2edf9'
#############

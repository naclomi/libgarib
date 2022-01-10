# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class GloverObjbank(KaitaiStruct):
    SEQ_FIELDS = ["directory"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['directory']['start'] = self._io.pos()
        self.directory = []
        i = 0
        while True:
            if not 'arr' in self._debug['directory']:
                self._debug['directory']['arr'] = []
            self._debug['directory']['arr'].append({'start': self._io.pos()})
            _ = GloverObjbank.DirectoryEntry(self._io, self, self._root)
            self.directory.append(_)
            self._debug['directory']['arr'][len(self.directory) - 1]['end'] = self._io.pos()
            if _.obj_id == 0:
                break
            i += 1
        self._debug['directory']['end'] = self._io.pos()

    class Uv(KaitaiStruct):
        SEQ_FIELDS = ["u1", "v1", "u2", "v2", "u3", "v3"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['u1']['start'] = self._io.pos()
            self.u1 = GloverObjbank.Fixed115(self._io, self, self._root)
            self._debug['u1']['end'] = self._io.pos()
            self._debug['v1']['start'] = self._io.pos()
            self.v1 = GloverObjbank.Fixed115(self._io, self, self._root)
            self._debug['v1']['end'] = self._io.pos()
            self._debug['u2']['start'] = self._io.pos()
            self.u2 = GloverObjbank.Fixed115(self._io, self, self._root)
            self._debug['u2']['end'] = self._io.pos()
            self._debug['v2']['start'] = self._io.pos()
            self.v2 = GloverObjbank.Fixed115(self._io, self, self._root)
            self._debug['v2']['end'] = self._io.pos()
            self._debug['u3']['start'] = self._io.pos()
            self.u3 = GloverObjbank.Fixed115(self._io, self, self._root)
            self._debug['u3']['end'] = self._io.pos()
            self._debug['v3']['start'] = self._io.pos()
            self.v3 = GloverObjbank.Fixed115(self._io, self, self._root)
            self._debug['v3']['end'] = self._io.pos()


    class Vertex(KaitaiStruct):
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


    class ObjectRoot(KaitaiStruct):
        SEQ_FIELDS = ["obj_id", "bank_base_addr", "u2", "mesh_ptr", "u3", "u4", "animation_ptr"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['obj_id']['start'] = self._io.pos()
            self.obj_id = self._io.read_u4be()
            self._debug['obj_id']['end'] = self._io.pos()
            self._debug['bank_base_addr']['start'] = self._io.pos()
            self.bank_base_addr = self._io.read_u4be()
            self._debug['bank_base_addr']['end'] = self._io.pos()
            self._debug['u2']['start'] = self._io.pos()
            self.u2 = self._io.read_u4be()
            self._debug['u2']['end'] = self._io.pos()
            self._debug['mesh_ptr']['start'] = self._io.pos()
            self.mesh_ptr = self._io.read_u4be()
            self._debug['mesh_ptr']['end'] = self._io.pos()
            self._debug['u3']['start'] = self._io.pos()
            self.u3 = self._io.read_u4be()
            self._debug['u3']['end'] = self._io.pos()
            self._debug['u4']['start'] = self._io.pos()
            self.u4 = self._io.read_u4be()
            self._debug['u4']['end'] = self._io.pos()
            self._debug['animation_ptr']['start'] = self._io.pos()
            self.animation_ptr = self._io.read_u4be()
            self._debug['animation_ptr']['end'] = self._io.pos()

        @property
        def mesh(self):
            if hasattr(self, '_m_mesh'):
                return self._m_mesh if hasattr(self, '_m_mesh') else None

            if self.mesh_ptr != 0:
                _pos = self._io.pos()
                self._io.seek(self.mesh_ptr)
                self._debug['_m_mesh']['start'] = self._io.pos()
                self._m_mesh = GloverObjbank.Mesh(self._io, self, self._root)
                self._debug['_m_mesh']['end'] = self._io.pos()
                self._io.seek(_pos)

            return self._m_mesh if hasattr(self, '_m_mesh') else None

        @property
        def animation(self):
            if hasattr(self, '_m_animation'):
                return self._m_animation if hasattr(self, '_m_animation') else None

            if self.animation_ptr != 0:
                _pos = self._io.pos()
                self._io.seek(self.animation_ptr)
                self._debug['_m_animation']['start'] = self._io.pos()
                self._m_animation = GloverObjbank.Animation(self._io, self, self._root)
                self._debug['_m_animation']['end'] = self._io.pos()
                self._io.seek(_pos)

            return self._m_animation if hasattr(self, '_m_animation') else None


    class DisplayListCmd(KaitaiStruct):
        SEQ_FIELDS = ["cmd", "params"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['cmd']['start'] = self._io.pos()
            self.cmd = self._io.read_u1()
            self._debug['cmd']['end'] = self._io.pos()
            self._debug['params']['start'] = self._io.pos()
            self.params = self._io.read_bytes(7)
            self._debug['params']['end'] = self._io.pos()


    class DirectoryEntry(KaitaiStruct):
        SEQ_FIELDS = ["obj_id", "ptr"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['obj_id']['start'] = self._io.pos()
            self.obj_id = self._io.read_u4be()
            self._debug['obj_id']['end'] = self._io.pos()
            self._debug['ptr']['start'] = self._io.pos()
            self.ptr = self._io.read_u4be()
            self._debug['ptr']['end'] = self._io.pos()

        @property
        def obj_root(self):
            if hasattr(self, '_m_obj_root'):
                return self._m_obj_root if hasattr(self, '_m_obj_root') else None

            if self.ptr != 0:
                _pos = self._io.pos()
                self._io.seek(self.ptr)
                self._debug['_m_obj_root']['start'] = self._io.pos()
                self._m_obj_root = GloverObjbank.ObjectRoot(self._io, self, self._root)
                self._debug['_m_obj_root']['end'] = self._io.pos()
                self._io.seek(_pos)

            return self._m_obj_root if hasattr(self, '_m_obj_root') else None


    class AffineFrame(KaitaiStruct):
        SEQ_FIELDS = ["v1", "v2", "v3", "v4", "t"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['v1']['start'] = self._io.pos()
            self.v1 = self._io.read_f4be()
            self._debug['v1']['end'] = self._io.pos()
            self._debug['v2']['start'] = self._io.pos()
            self.v2 = self._io.read_f4be()
            self._debug['v2']['end'] = self._io.pos()
            self._debug['v3']['start'] = self._io.pos()
            self.v3 = self._io.read_f4be()
            self._debug['v3']['end'] = self._io.pos()
            self._debug['v4']['start'] = self._io.pos()
            self.v4 = self._io.read_f4be()
            self._debug['v4']['end'] = self._io.pos()
            self._debug['t']['start'] = self._io.pos()
            self.t = self._io.read_u4be()
            self._debug['t']['end'] = self._io.pos()


    class AnimationDefinition(KaitaiStruct):
        SEQ_FIELDS = ["start_time", "end_time", "playback_speed", "u1"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['start_time']['start'] = self._io.pos()
            self.start_time = self._io.read_s2be()
            self._debug['start_time']['end'] = self._io.pos()
            self._debug['end_time']['start'] = self._io.pos()
            self.end_time = self._io.read_s2be()
            self._debug['end_time']['end'] = self._io.pos()
            self._debug['playback_speed']['start'] = self._io.pos()
            self.playback_speed = self._io.read_f4be()
            self._debug['playback_speed']['end'] = self._io.pos()
            self._debug['u1']['start'] = self._io.pos()
            self.u1 = self._io.read_u4be()
            self._debug['u1']['end'] = self._io.pos()


    class Face(KaitaiStruct):
        SEQ_FIELDS = ["v0", "v1", "v2"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['v0']['start'] = self._io.pos()
            self.v0 = self._io.read_u2be()
            self._debug['v0']['end'] = self._io.pos()
            self._debug['v1']['start'] = self._io.pos()
            self.v1 = self._io.read_u2be()
            self._debug['v1']['end'] = self._io.pos()
            self._debug['v2']['start'] = self._io.pos()
            self.v2 = self._io.read_u2be()
            self._debug['v2']['end'] = self._io.pos()


    class Sprite(KaitaiStruct):
        SEQ_FIELDS = ["texture_id", "u2", "x", "y", "z", "width", "height", "u5", "u6", "u7"]
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
            self._debug['u2']['start'] = self._io.pos()
            self.u2 = self._io.read_u4be()
            self._debug['u2']['end'] = self._io.pos()
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_u2be()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_u2be()
            self._debug['y']['end'] = self._io.pos()
            self._debug['z']['start'] = self._io.pos()
            self.z = self._io.read_u2be()
            self._debug['z']['end'] = self._io.pos()
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u2be()
            self._debug['width']['end'] = self._io.pos()
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u2be()
            self._debug['height']['end'] = self._io.pos()
            self._debug['u5']['start'] = self._io.pos()
            self.u5 = self._io.read_u2be()
            self._debug['u5']['end'] = self._io.pos()
            self._debug['u6']['start'] = self._io.pos()
            self.u6 = self._io.read_u2be()
            self._debug['u6']['end'] = self._io.pos()
            self._debug['u7']['start'] = self._io.pos()
            self.u7 = self._io.read_u2be()
            self._debug['u7']['end'] = self._io.pos()


    class Animation(KaitaiStruct):
        SEQ_FIELDS = ["num_animation_definitions", "current_animation_idx", "u3", "is_playing", "time_delta", "next_anim_idx", "pad", "next_is_playing", "next_time_delta", "next_anim_slot_idx", "u15", "animation_definitions_ptr", "cur_time"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_animation_definitions']['start'] = self._io.pos()
            self.num_animation_definitions = self._io.read_s2be()
            self._debug['num_animation_definitions']['end'] = self._io.pos()
            self._debug['current_animation_idx']['start'] = self._io.pos()
            self.current_animation_idx = self._io.read_s2be()
            self._debug['current_animation_idx']['end'] = self._io.pos()
            self._debug['u3']['start'] = self._io.pos()
            self.u3 = self._io.read_u4be()
            self._debug['u3']['end'] = self._io.pos()
            self._debug['is_playing']['start'] = self._io.pos()
            self.is_playing = self._io.read_u4be()
            self._debug['is_playing']['end'] = self._io.pos()
            self._debug['time_delta']['start'] = self._io.pos()
            self.time_delta = self._io.read_f4be()
            self._debug['time_delta']['end'] = self._io.pos()
            self._debug['next_anim_idx']['start'] = self._io.pos()
            self.next_anim_idx = [None] * (5)
            for i in range(5):
                if not 'arr' in self._debug['next_anim_idx']:
                    self._debug['next_anim_idx']['arr'] = []
                self._debug['next_anim_idx']['arr'].append({'start': self._io.pos()})
                self.next_anim_idx[i] = self._io.read_s2be()
                self._debug['next_anim_idx']['arr'][i]['end'] = self._io.pos()

            self._debug['next_anim_idx']['end'] = self._io.pos()
            self._debug['pad']['start'] = self._io.pos()
            self.pad = self._io.read_u2be()
            self._debug['pad']['end'] = self._io.pos()
            self._debug['next_is_playing']['start'] = self._io.pos()
            self.next_is_playing = [None] * (5)
            for i in range(5):
                if not 'arr' in self._debug['next_is_playing']:
                    self._debug['next_is_playing']['arr'] = []
                self._debug['next_is_playing']['arr'].append({'start': self._io.pos()})
                self.next_is_playing[i] = self._io.read_u4be()
                self._debug['next_is_playing']['arr'][i]['end'] = self._io.pos()

            self._debug['next_is_playing']['end'] = self._io.pos()
            self._debug['next_time_delta']['start'] = self._io.pos()
            self.next_time_delta = [None] * (5)
            for i in range(5):
                if not 'arr' in self._debug['next_time_delta']:
                    self._debug['next_time_delta']['arr'] = []
                self._debug['next_time_delta']['arr'].append({'start': self._io.pos()})
                self.next_time_delta[i] = self._io.read_u4be()
                self._debug['next_time_delta']['arr'][i]['end'] = self._io.pos()

            self._debug['next_time_delta']['end'] = self._io.pos()
            self._debug['next_anim_slot_idx']['start'] = self._io.pos()
            self.next_anim_slot_idx = self._io.read_s2be()
            self._debug['next_anim_slot_idx']['end'] = self._io.pos()
            self._debug['u15']['start'] = self._io.pos()
            self.u15 = self._io.read_u2be()
            self._debug['u15']['end'] = self._io.pos()
            self._debug['animation_definitions_ptr']['start'] = self._io.pos()
            self.animation_definitions_ptr = self._io.read_u4be()
            self._debug['animation_definitions_ptr']['end'] = self._io.pos()
            self._debug['cur_time']['start'] = self._io.pos()
            self.cur_time = self._io.read_f4be()
            self._debug['cur_time']['end'] = self._io.pos()

        @property
        def animation_definitions(self):
            if hasattr(self, '_m_animation_definitions'):
                return self._m_animation_definitions if hasattr(self, '_m_animation_definitions') else None

            if self.animation_definitions_ptr != 0:
                _pos = self._io.pos()
                self._io.seek(self.animation_definitions_ptr)
                self._debug['_m_animation_definitions']['start'] = self._io.pos()
                self._m_animation_definitions = [None] * (self.num_animation_definitions)
                for i in range(self.num_animation_definitions):
                    if not 'arr' in self._debug['_m_animation_definitions']:
                        self._debug['_m_animation_definitions']['arr'] = []
                    self._debug['_m_animation_definitions']['arr'].append({'start': self._io.pos()})
                    self._m_animation_definitions[i] = GloverObjbank.AnimationDefinition(self._io, self, self._root)
                    self._debug['_m_animation_definitions']['arr'][i]['end'] = self._io.pos()

                self._debug['_m_animation_definitions']['end'] = self._io.pos()
                self._io.seek(_pos)

            return self._m_animation_definitions if hasattr(self, '_m_animation_definitions') else None


    class Mesh(KaitaiStruct):
        SEQ_FIELDS = ["id", "name", "alpha", "num_scale", "num_translation", "num_rotation", "geometry_ptr", "display_list_ptr", "scale_ptr", "translation_ptr", "rotation_ptr", "num_sprites", "sprites_ptr", "num_children", "render_mode", "child_ptr", "sibling_ptr", "u15"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['id']['start'] = self._io.pos()
            self.id = self._io.read_u4be()
            self._debug['id']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(8)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['alpha']['start'] = self._io.pos()
            self.alpha = self._io.read_u2be()
            self._debug['alpha']['end'] = self._io.pos()
            self._debug['num_scale']['start'] = self._io.pos()
            self.num_scale = self._io.read_u2be()
            self._debug['num_scale']['end'] = self._io.pos()
            self._debug['num_translation']['start'] = self._io.pos()
            self.num_translation = self._io.read_u2be()
            self._debug['num_translation']['end'] = self._io.pos()
            self._debug['num_rotation']['start'] = self._io.pos()
            self.num_rotation = self._io.read_u2be()
            self._debug['num_rotation']['end'] = self._io.pos()
            self._debug['geometry_ptr']['start'] = self._io.pos()
            self.geometry_ptr = self._io.read_u4be()
            self._debug['geometry_ptr']['end'] = self._io.pos()
            self._debug['display_list_ptr']['start'] = self._io.pos()
            self.display_list_ptr = self._io.read_u4be()
            self._debug['display_list_ptr']['end'] = self._io.pos()
            self._debug['scale_ptr']['start'] = self._io.pos()
            self.scale_ptr = self._io.read_u4be()
            self._debug['scale_ptr']['end'] = self._io.pos()
            self._debug['translation_ptr']['start'] = self._io.pos()
            self.translation_ptr = self._io.read_u4be()
            self._debug['translation_ptr']['end'] = self._io.pos()
            self._debug['rotation_ptr']['start'] = self._io.pos()
            self.rotation_ptr = self._io.read_u4be()
            self._debug['rotation_ptr']['end'] = self._io.pos()
            self._debug['num_sprites']['start'] = self._io.pos()
            self.num_sprites = self._io.read_u4be()
            self._debug['num_sprites']['end'] = self._io.pos()
            self._debug['sprites_ptr']['start'] = self._io.pos()
            self.sprites_ptr = self._io.read_u4be()
            self._debug['sprites_ptr']['end'] = self._io.pos()
            self._debug['num_children']['start'] = self._io.pos()
            self.num_children = self._io.read_u2be()
            self._debug['num_children']['end'] = self._io.pos()
            self._debug['render_mode']['start'] = self._io.pos()
            self.render_mode = self._io.read_u2be()
            self._debug['render_mode']['end'] = self._io.pos()
            self._debug['child_ptr']['start'] = self._io.pos()
            self.child_ptr = self._io.read_u4be()
            self._debug['child_ptr']['end'] = self._io.pos()
            self._debug['sibling_ptr']['start'] = self._io.pos()
            self.sibling_ptr = self._io.read_u4be()
            self._debug['sibling_ptr']['end'] = self._io.pos()
            self._debug['u15']['start'] = self._io.pos()
            self.u15 = self._io.read_u4be()
            self._debug['u15']['end'] = self._io.pos()

        @property
        def rotation(self):
            if hasattr(self, '_m_rotation'):
                return self._m_rotation if hasattr(self, '_m_rotation') else None

            if self.rotation_ptr != 0:
                _pos = self._io.pos()
                self._io.seek(self.rotation_ptr)
                self._debug['_m_rotation']['start'] = self._io.pos()
                self._m_rotation = [None] * (self.num_rotation)
                for i in range(self.num_rotation):
                    if not 'arr' in self._debug['_m_rotation']:
                        self._debug['_m_rotation']['arr'] = []
                    self._debug['_m_rotation']['arr'].append({'start': self._io.pos()})
                    self._m_rotation[i] = GloverObjbank.AffineFrame(self._io, self, self._root)
                    self._debug['_m_rotation']['arr'][i]['end'] = self._io.pos()

                self._debug['_m_rotation']['end'] = self._io.pos()
                self._io.seek(_pos)

            return self._m_rotation if hasattr(self, '_m_rotation') else None

        @property
        def geometry(self):
            if hasattr(self, '_m_geometry'):
                return self._m_geometry if hasattr(self, '_m_geometry') else None

            if self.geometry_ptr != 0:
                _pos = self._io.pos()
                self._io.seek(self.geometry_ptr)
                self._debug['_m_geometry']['start'] = self._io.pos()
                self._m_geometry = GloverObjbank.Geometry(self._io, self, self._root)
                self._debug['_m_geometry']['end'] = self._io.pos()
                self._io.seek(_pos)

            return self._m_geometry if hasattr(self, '_m_geometry') else None

        @property
        def scale(self):
            if hasattr(self, '_m_scale'):
                return self._m_scale if hasattr(self, '_m_scale') else None

            if self.scale_ptr != 0:
                _pos = self._io.pos()
                self._io.seek(self.scale_ptr)
                self._debug['_m_scale']['start'] = self._io.pos()
                self._m_scale = [None] * (self.num_scale)
                for i in range(self.num_scale):
                    if not 'arr' in self._debug['_m_scale']:
                        self._debug['_m_scale']['arr'] = []
                    self._debug['_m_scale']['arr'].append({'start': self._io.pos()})
                    self._m_scale[i] = GloverObjbank.AffineFrame(self._io, self, self._root)
                    self._debug['_m_scale']['arr'][i]['end'] = self._io.pos()

                self._debug['_m_scale']['end'] = self._io.pos()
                self._io.seek(_pos)

            return self._m_scale if hasattr(self, '_m_scale') else None

        @property
        def translation(self):
            if hasattr(self, '_m_translation'):
                return self._m_translation if hasattr(self, '_m_translation') else None

            if self.translation_ptr != 0:
                _pos = self._io.pos()
                self._io.seek(self.translation_ptr)
                self._debug['_m_translation']['start'] = self._io.pos()
                self._m_translation = [None] * (self.num_translation)
                for i in range(self.num_translation):
                    if not 'arr' in self._debug['_m_translation']:
                        self._debug['_m_translation']['arr'] = []
                    self._debug['_m_translation']['arr'].append({'start': self._io.pos()})
                    self._m_translation[i] = GloverObjbank.AffineFrame(self._io, self, self._root)
                    self._debug['_m_translation']['arr'][i]['end'] = self._io.pos()

                self._debug['_m_translation']['end'] = self._io.pos()
                self._io.seek(_pos)

            return self._m_translation if hasattr(self, '_m_translation') else None

        @property
        def child(self):
            if hasattr(self, '_m_child'):
                return self._m_child if hasattr(self, '_m_child') else None

            if self.child_ptr != 0:
                _pos = self._io.pos()
                self._io.seek(self.child_ptr)
                self._debug['_m_child']['start'] = self._io.pos()
                self._m_child = GloverObjbank.Mesh(self._io, self, self._root)
                self._debug['_m_child']['end'] = self._io.pos()
                self._io.seek(_pos)

            return self._m_child if hasattr(self, '_m_child') else None

        @property
        def sibling(self):
            if hasattr(self, '_m_sibling'):
                return self._m_sibling if hasattr(self, '_m_sibling') else None

            if self.sibling_ptr != 0:
                _pos = self._io.pos()
                self._io.seek(self.sibling_ptr)
                self._debug['_m_sibling']['start'] = self._io.pos()
                self._m_sibling = GloverObjbank.Mesh(self._io, self, self._root)
                self._debug['_m_sibling']['end'] = self._io.pos()
                self._io.seek(_pos)

            return self._m_sibling if hasattr(self, '_m_sibling') else None

        @property
        def display_list(self):
            if hasattr(self, '_m_display_list'):
                return self._m_display_list if hasattr(self, '_m_display_list') else None

            if self.display_list_ptr != 0:
                _pos = self._io.pos()
                self._io.seek(self.display_list_ptr)
                self._debug['_m_display_list']['start'] = self._io.pos()
                self._m_display_list = []
                i = 0
                while True:
                    if not 'arr' in self._debug['_m_display_list']:
                        self._debug['_m_display_list']['arr'] = []
                    self._debug['_m_display_list']['arr'].append({'start': self._io.pos()})
                    _ = GloverObjbank.DisplayListCmd(self._io, self, self._root)
                    self._m_display_list.append(_)
                    self._debug['_m_display_list']['arr'][len(self._m_display_list) - 1]['end'] = self._io.pos()
                    if _.cmd == 184:
                        break
                    i += 1
                self._debug['_m_display_list']['end'] = self._io.pos()
                self._io.seek(_pos)

            return self._m_display_list if hasattr(self, '_m_display_list') else None

        @property
        def sprites(self):
            if hasattr(self, '_m_sprites'):
                return self._m_sprites if hasattr(self, '_m_sprites') else None

            if self.sprites_ptr != 0:
                _pos = self._io.pos()
                self._io.seek(self.sprites_ptr)
                self._debug['_m_sprites']['start'] = self._io.pos()
                self._m_sprites = [None] * (self.num_sprites)
                for i in range(self.num_sprites):
                    if not 'arr' in self._debug['_m_sprites']:
                        self._debug['_m_sprites']['arr'] = []
                    self._debug['_m_sprites']['arr'].append({'start': self._io.pos()})
                    self._m_sprites[i] = GloverObjbank.Sprite(self._io, self, self._root)
                    self._debug['_m_sprites']['arr'][i]['end'] = self._io.pos()

                self._debug['_m_sprites']['end'] = self._io.pos()
                self._io.seek(_pos)

            return self._m_sprites if hasattr(self, '_m_sprites') else None


    class Fixed115(KaitaiStruct):
        SEQ_FIELDS = ["raw"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['raw']['start'] = self._io.pos()
            self.raw = self._io.read_u2be()
            self._debug['raw']['end'] = self._io.pos()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value if hasattr(self, '_m_value') else None

            self._m_value = (self.raw / 32.0)
            return self._m_value if hasattr(self, '_m_value') else None


    class Geometry(KaitaiStruct):
        SEQ_FIELDS = ["num_faces", "num_vertices", "vertices_ptr", "faces_ptr", "u1_ptr", "uvs_ptr", "u3", "colors_norms_ptr", "u5_ptr", "texture_ids_ptr"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_faces']['start'] = self._io.pos()
            self.num_faces = self._io.read_u2be()
            self._debug['num_faces']['end'] = self._io.pos()
            self._debug['num_vertices']['start'] = self._io.pos()
            self.num_vertices = self._io.read_u2be()
            self._debug['num_vertices']['end'] = self._io.pos()
            self._debug['vertices_ptr']['start'] = self._io.pos()
            self.vertices_ptr = self._io.read_u4be()
            self._debug['vertices_ptr']['end'] = self._io.pos()
            self._debug['faces_ptr']['start'] = self._io.pos()
            self.faces_ptr = self._io.read_u4be()
            self._debug['faces_ptr']['end'] = self._io.pos()
            self._debug['u1_ptr']['start'] = self._io.pos()
            self.u1_ptr = self._io.read_u4be()
            self._debug['u1_ptr']['end'] = self._io.pos()
            self._debug['uvs_ptr']['start'] = self._io.pos()
            self.uvs_ptr = self._io.read_u4be()
            self._debug['uvs_ptr']['end'] = self._io.pos()
            self._debug['u3']['start'] = self._io.pos()
            self.u3 = self._io.read_u4be()
            self._debug['u3']['end'] = self._io.pos()
            self._debug['colors_norms_ptr']['start'] = self._io.pos()
            self.colors_norms_ptr = self._io.read_u4be()
            self._debug['colors_norms_ptr']['end'] = self._io.pos()
            self._debug['u5_ptr']['start'] = self._io.pos()
            self.u5_ptr = self._io.read_u4be()
            self._debug['u5_ptr']['end'] = self._io.pos()
            self._debug['texture_ids_ptr']['start'] = self._io.pos()
            self.texture_ids_ptr = self._io.read_u4be()
            self._debug['texture_ids_ptr']['end'] = self._io.pos()

        @property
        def texture_ids(self):
            if hasattr(self, '_m_texture_ids'):
                return self._m_texture_ids if hasattr(self, '_m_texture_ids') else None

            if self.texture_ids_ptr != 0:
                _pos = self._io.pos()
                self._io.seek(self.texture_ids_ptr)
                self._debug['_m_texture_ids']['start'] = self._io.pos()
                self._m_texture_ids = [None] * (self.num_faces)
                for i in range(self.num_faces):
                    if not 'arr' in self._debug['_m_texture_ids']:
                        self._debug['_m_texture_ids']['arr'] = []
                    self._debug['_m_texture_ids']['arr'].append({'start': self._io.pos()})
                    self._m_texture_ids[i] = self._io.read_u4be()
                    self._debug['_m_texture_ids']['arr'][i]['end'] = self._io.pos()

                self._debug['_m_texture_ids']['end'] = self._io.pos()
                self._io.seek(_pos)

            return self._m_texture_ids if hasattr(self, '_m_texture_ids') else None

        @property
        def u5(self):
            if hasattr(self, '_m_u5'):
                return self._m_u5 if hasattr(self, '_m_u5') else None

            if self.u5_ptr != 0:
                _pos = self._io.pos()
                self._io.seek(self.u5_ptr)
                self._debug['_m_u5']['start'] = self._io.pos()
                self._m_u5 = [None] * (self.num_faces)
                for i in range(self.num_faces):
                    if not 'arr' in self._debug['_m_u5']:
                        self._debug['_m_u5']['arr'] = []
                    self._debug['_m_u5']['arr'].append({'start': self._io.pos()})
                    self._m_u5[i] = self._io.read_u1()
                    self._debug['_m_u5']['arr'][i]['end'] = self._io.pos()

                self._debug['_m_u5']['end'] = self._io.pos()
                self._io.seek(_pos)

            return self._m_u5 if hasattr(self, '_m_u5') else None

        @property
        def faces(self):
            if hasattr(self, '_m_faces'):
                return self._m_faces if hasattr(self, '_m_faces') else None

            if self.faces_ptr != 0:
                _pos = self._io.pos()
                self._io.seek(self.faces_ptr)
                self._debug['_m_faces']['start'] = self._io.pos()
                self._m_faces = [None] * (self.num_faces)
                for i in range(self.num_faces):
                    if not 'arr' in self._debug['_m_faces']:
                        self._debug['_m_faces']['arr'] = []
                    self._debug['_m_faces']['arr'].append({'start': self._io.pos()})
                    self._m_faces[i] = GloverObjbank.Face(self._io, self, self._root)
                    self._debug['_m_faces']['arr'][i]['end'] = self._io.pos()

                self._debug['_m_faces']['end'] = self._io.pos()
                self._io.seek(_pos)

            return self._m_faces if hasattr(self, '_m_faces') else None

        @property
        def vertices(self):
            if hasattr(self, '_m_vertices'):
                return self._m_vertices if hasattr(self, '_m_vertices') else None

            if self.vertices_ptr != 0:
                _pos = self._io.pos()
                self._io.seek(self.vertices_ptr)
                self._debug['_m_vertices']['start'] = self._io.pos()
                self._m_vertices = [None] * (self.num_vertices)
                for i in range(self.num_vertices):
                    if not 'arr' in self._debug['_m_vertices']:
                        self._debug['_m_vertices']['arr'] = []
                    self._debug['_m_vertices']['arr'].append({'start': self._io.pos()})
                    self._m_vertices[i] = GloverObjbank.Vertex(self._io, self, self._root)
                    self._debug['_m_vertices']['arr'][i]['end'] = self._io.pos()

                self._debug['_m_vertices']['end'] = self._io.pos()
                self._io.seek(_pos)

            return self._m_vertices if hasattr(self, '_m_vertices') else None

        @property
        def u1(self):
            if hasattr(self, '_m_u1'):
                return self._m_u1 if hasattr(self, '_m_u1') else None

            if self.u1_ptr != 0:
                _pos = self._io.pos()
                self._io.seek(self.u1_ptr)
                self._debug['_m_u1']['start'] = self._io.pos()
                self._m_u1 = [None] * (self.num_faces)
                for i in range(self.num_faces):
                    if not 'arr' in self._debug['_m_u1']:
                        self._debug['_m_u1']['arr'] = []
                    self._debug['_m_u1']['arr'].append({'start': self._io.pos()})
                    self._m_u1[i] = self._io.read_u4be()
                    self._debug['_m_u1']['arr'][i]['end'] = self._io.pos()

                self._debug['_m_u1']['end'] = self._io.pos()
                self._io.seek(_pos)

            return self._m_u1 if hasattr(self, '_m_u1') else None

        @property
        def uvs(self):
            if hasattr(self, '_m_uvs'):
                return self._m_uvs if hasattr(self, '_m_uvs') else None

            if self.uvs_ptr != 0:
                _pos = self._io.pos()
                self._io.seek(self.uvs_ptr)
                self._debug['_m_uvs']['start'] = self._io.pos()
                self._m_uvs = [None] * (self.num_faces)
                for i in range(self.num_faces):
                    if not 'arr' in self._debug['_m_uvs']:
                        self._debug['_m_uvs']['arr'] = []
                    self._debug['_m_uvs']['arr'].append({'start': self._io.pos()})
                    self._m_uvs[i] = GloverObjbank.Uv(self._io, self, self._root)
                    self._debug['_m_uvs']['arr'][i]['end'] = self._io.pos()

                self._debug['_m_uvs']['end'] = self._io.pos()
                self._io.seek(_pos)

            return self._m_uvs if hasattr(self, '_m_uvs') else None

        @property
        def colors_norms(self):
            if hasattr(self, '_m_colors_norms'):
                return self._m_colors_norms if hasattr(self, '_m_colors_norms') else None

            if self.colors_norms_ptr != 0:
                _pos = self._io.pos()
                self._io.seek(self.colors_norms_ptr)
                self._debug['_m_colors_norms']['start'] = self._io.pos()
                self._m_colors_norms = [None] * (self.num_vertices)
                for i in range(self.num_vertices):
                    if not 'arr' in self._debug['_m_colors_norms']:
                        self._debug['_m_colors_norms']['arr'] = []
                    self._debug['_m_colors_norms']['arr'].append({'start': self._io.pos()})
                    self._m_colors_norms[i] = self._io.read_u4be()
                    self._debug['_m_colors_norms']['arr'][i]['end'] = self._io.pos()

                self._debug['_m_colors_norms']['end'] = self._io.pos()
                self._io.seek(_pos)

            return self._m_colors_norms if hasattr(self, '_m_colors_norms') else None




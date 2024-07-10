# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class GloverTexbank(KaitaiStruct):

    class TextureCompressionFormat(Enum):
        ci4 = 0
        ci8 = 1
        uncompressed_16b = 2
        uncompressed_32b = 3

    class TextureColorFormat(Enum):
        rgba = 0
        yuv = 1
        ci = 2
        ia = 3
        i = 4
    SEQ_FIELDS = ["n_textures", "assets", "filenames"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['n_textures']['start'] = self._io.pos()
        self.n_textures = self._io.read_u4be()
        self._debug['n_textures']['end'] = self._io.pos()
        self._debug['assets']['start'] = self._io.pos()
        self.assets = [None] * (self.n_textures)
        for i in range(self.n_textures):
            if not 'arr' in self._debug['assets']:
                self._debug['assets']['arr'] = []
            self._debug['assets']['arr'].append({'start': self._io.pos()})
            self.assets[i] = GloverTexbank.Texture(self._io, self, self._root)
            self._debug['assets']['arr'][i]['end'] = self._io.pos()

        self._debug['assets']['end'] = self._io.pos()
        self._debug['filenames']['start'] = self._io.pos()
        self.filenames = [None] * (self.n_textures)
        for i in range(self.n_textures):
            if not 'arr' in self._debug['filenames']:
                self._debug['filenames']['arr'] = []
            self._debug['filenames']['arr'].append({'start': self._io.pos()})
            self.filenames[i] = (self._io.read_bytes_term(0, False, True, False)).decode(u"UTF-8")
            self._debug['filenames']['arr'][i]['end'] = self._io.pos()

        self._debug['filenames']['end'] = self._io.pos()

    class Texture(KaitaiStruct):
        SEQ_FIELDS = ["id", "palette_anim_idx_min", "palette_anim_idx_max", "flags", "frame_increment", "frame_counter", "width", "height", "masks", "maskt", "length", "color_format", "compression_format", "data_ptr", "palette_offset", "data"]
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
            self._debug['palette_anim_idx_min']['start'] = self._io.pos()
            self.palette_anim_idx_min = self._io.read_u1()
            self._debug['palette_anim_idx_min']['end'] = self._io.pos()
            self._debug['palette_anim_idx_max']['start'] = self._io.pos()
            self.palette_anim_idx_max = self._io.read_u1()
            self._debug['palette_anim_idx_max']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u2be()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['frame_increment']['start'] = self._io.pos()
            self.frame_increment = self._io.read_s2be()
            self._debug['frame_increment']['end'] = self._io.pos()
            self._debug['frame_counter']['start'] = self._io.pos()
            self.frame_counter = self._io.read_s2be()
            self._debug['frame_counter']['end'] = self._io.pos()
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u2be()
            self._debug['width']['end'] = self._io.pos()
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u2be()
            self._debug['height']['end'] = self._io.pos()
            self._debug['masks']['start'] = self._io.pos()
            self.masks = self._io.read_u2be()
            self._debug['masks']['end'] = self._io.pos()
            self._debug['maskt']['start'] = self._io.pos()
            self.maskt = self._io.read_u2be()
            self._debug['maskt']['end'] = self._io.pos()
            self._debug['length']['start'] = self._io.pos()
            self.length = self._io.read_u4be()
            self._debug['length']['end'] = self._io.pos()
            self._debug['color_format']['start'] = self._io.pos()
            self.color_format = KaitaiStream.resolve_enum(GloverTexbank.TextureColorFormat, self._io.read_u2be())
            self._debug['color_format']['end'] = self._io.pos()
            self._debug['compression_format']['start'] = self._io.pos()
            self.compression_format = KaitaiStream.resolve_enum(GloverTexbank.TextureCompressionFormat, self._io.read_u2be())
            self._debug['compression_format']['end'] = self._io.pos()
            self._debug['data_ptr']['start'] = self._io.pos()
            self.data_ptr = self._io.read_u4be()
            self._debug['data_ptr']['end'] = self._io.pos()
            self._debug['palette_offset']['start'] = self._io.pos()
            self.palette_offset = self._io.read_u4be()
            self._debug['palette_offset']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes((self.length - 36))
            self._debug['data']['end'] = self._io.pos()




#############
# PATCHED BY ./python/ksy-patcher.py

type_fields = {
}
type_codes = {
}
inverse_type_codes = {
}
original_names = {
    'GloverTexbank.Texture': 'glover_texbank.texture',
}
private_fields = {
}

import sys
import importlib

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
    return private_fields.get(cls.__qualname__, {}).get(field_name, default)
KaitaiStruct.getPrivate = getPrivate

@classmethod
def getTypeField(cls):
    type_fields = sys.modules[cls.__module__].type_fields
    return type_fields[cls.__qualname__]
KaitaiStruct.getTypeField = getTypeField

@classmethod
def typeCodeToValue(cls, code):
    all_type_codes = sys.modules[cls.__module__].type_codes
    type_codes = all_type_codes[cls.__qualname__]
    val = type_codes.get(code, None)
    if val is None:
        val = type_codes[None]
    return val
KaitaiStruct.typeCodeToValue = typeCodeToValue

@classmethod
def typeValueToCode(cls, val):
    all_type_values = sys.modules[cls.__module__].inverse_type_codes
    type_values = all_type_values[cls.__qualname__]
    return type_values[val]
KaitaiStruct.typeValueToCode = typeValueToCode

ksy_hash = '2776e1c28dc8064e0cdce4b74e72e4280b82eea4'
#############

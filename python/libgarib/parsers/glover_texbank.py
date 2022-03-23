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
    SEQ_FIELDS = ["n_textures", "asset"]
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
        self._debug['asset']['start'] = self._io.pos()
        self.asset = [None] * (self.n_textures)
        for i in range(self.n_textures):
            if not 'arr' in self._debug['asset']:
                self._debug['asset']['arr'] = []
            self._debug['asset']['arr'].append({'start': self._io.pos()})
            self.asset[i] = GloverTexbank.Texture(self._io, self, self._root)
            self._debug['asset']['arr'][i]['end'] = self._io.pos()

        self._debug['asset']['end'] = self._io.pos()

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




from construct import *
from construct.lib import *

def glover_texbank__texture_compression_format(subcon):
	return Enum(subcon,
		ci4=0,
		ci8=1,
		uncompressed_16b=2,
		uncompressed_32b=3,
	)

def glover_texbank__texture_color_format(subcon):
	return Enum(subcon,
		rgba=0,
		yuv=1,
		ci=2,
		ia=3,
		i=4,
	)

glover_texbank__texture = Struct(
	'id' / Int32ub,
	'palette_anim_idx_min' / Int8ub,
	'palette_anim_idx_max' / Int8ub,
	'flags' / Int16ub,
	'frame_increment' / Int16sb,
	'frame_counter' / Int16sb,
	'width' / Int16ub,
	'height' / Int16ub,
	'masks' / Int16ub,
	'maskt' / Int16ub,
	'length' / Int32ub,
	'color_format' / glover_texbank__texture_color_format(Int16ub),
	'compression_format' / glover_texbank__texture_compression_format(Int16ub),
	'data_ptr' / Int32ub,
	'palette_offset' / Int32ub,
	'data' / FixedSized((this.length - 36), GreedyBytes),
)

glover_texbank = Struct(
	'n_textures' / Int32ub,
	'assets' / Array(this.n_textures, LazyBound(lambda: glover_texbank__texture)),
	'filenames' / Array(this.n_textures, NullTerminated(GreedyString(encoding='UTF-8'), term=b'\x00', include=False, consume=True)),
)

_schema = glover_texbank

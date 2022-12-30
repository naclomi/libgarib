from construct import *
from construct.lib import *

glover_objbank__uv = Struct(
	'u1' / LazyBound(lambda: glover_objbank__fixed_11_5),
	'v1' / LazyBound(lambda: glover_objbank__fixed_11_5),
	'u2' / LazyBound(lambda: glover_objbank__fixed_11_5),
	'v2' / LazyBound(lambda: glover_objbank__fixed_11_5),
	'u3' / LazyBound(lambda: glover_objbank__fixed_11_5),
	'v3' / LazyBound(lambda: glover_objbank__fixed_11_5),
)

glover_objbank__vertex = Struct(
	'x' / Float32b,
	'y' / Float32b,
	'z' / Float32b,
)

glover_objbank__object_root = Struct(
	'obj_id' / Int32ub,
	'bank_base_addr' / Int32ub,
	'u2' / Int32ub,
	'mesh_ptr' / Int32ub,
	'u3' / Int32ub,
	'u4' / Int32ub,
	'animation_ptr' / Int32ub,
	'mesh' / Pointer(this.mesh_ptr, If(this.mesh_ptr != 0, LazyBound(lambda: glover_objbank__mesh))),
	'animation' / Pointer(this.animation_ptr, If(this.animation_ptr != 0, LazyBound(lambda: glover_objbank__animation))),
)

glover_objbank__display_list_cmd = Struct(
	'w1' / Int32ub,
	'w0' / Int32ub,
	'cmd' / Computed(lambda this: ((this.w1 >> 24) & 255)),
)

glover_objbank__directory_entry = Struct(
	'obj_id' / Int32ub,
	'ptr' / Int32ub,
	'obj_root' / Pointer(this.ptr, If(this.ptr != 0, LazyBound(lambda: glover_objbank__object_root))),
)

glover_objbank__affine_frame = Struct(
	'v1' / Float32b,
	'v2' / Float32b,
	'v3' / Float32b,
	'v4' / Float32b,
	't' / Int32ub,
)

glover_objbank__animation_definition = Struct(
	'start_time' / Int16sb,
	'end_time' / Int16sb,
	'playback_speed' / Float32b,
	'unused' / Int32ub,
)

glover_objbank__face = Struct(
	'v0' / Int16ub,
	'v1' / Int16ub,
	'v2' / Int16ub,
)

glover_objbank__sprite = Struct(
	'texture_id' / Int32ub,
	'runtime_data_ptr' / Int32ub,
	'x' / Int16ub,
	'y' / Int16ub,
	'z' / Int16ub,
	'width' / Int16ub,
	'height' / Int16ub,
	'u5' / Int16sb,
	'u6' / Int16sb,
	'flags' / Int16ub,
)

glover_objbank__animation = Struct(
	'num_animation_definitions' / Int16sb,
	'current_animation_idx' / Int16sb,
	'u3' / Int32ub,
	'is_playing' / Int32ub,
	'time_delta' / Float32b,
	'next_anim_idx' / Array(5, Int16sb),
	'pad' / Int16ub,
	'next_is_playing' / Array(5, Int32ub),
	'next_time_delta' / Array(5, Int32ub),
	'next_anim_slot_idx' / Int16sb,
	'u15' / Int16ub,
	'animation_definitions_ptr' / Int32ub,
	'cur_time' / Float32b,
	'animation_definitions' / Pointer(this.animation_definitions_ptr, If(this.animation_definitions_ptr != 0, Array(this.num_animation_definitions, LazyBound(lambda: glover_objbank__animation_definition)))),
)

glover_objbank__mesh = Struct(
	'id' / Int32ub,
	'name' / FixedSized(8, GreedyString(encoding='ASCII')),
	'mesh_alpha' / Int8ub,
	'sprite_alpha' / Int8ub,
	'num_scale' / Int16ub,
	'num_translation' / Int16ub,
	'num_rotation' / Int16ub,
	'geometry_ptr' / Int32ub,
	'display_list_ptr' / Int32ub,
	'scale_ptr' / Int32ub,
	'translation_ptr' / Int32ub,
	'rotation_ptr' / Int32ub,
	'num_sprites' / Int32ub,
	'sprites_ptr' / Int32ub,
	'num_children' / Int16ub,
	'render_mode' / Int16ub,
	'child_ptr' / Int32ub,
	'sibling_ptr' / Int32ub,
	'runtime_collision_data_ptr' / Int32ub,
	'rotation' / Pointer(this.rotation_ptr, If(this.rotation_ptr != 0, Array(this.num_rotation, LazyBound(lambda: glover_objbank__affine_frame)))),
	'geometry' / Pointer(this.geometry_ptr, If(this.geometry_ptr != 0, LazyBound(lambda: glover_objbank__geometry))),
	'scale' / Pointer(this.scale_ptr, If(this.scale_ptr != 0, Array(this.num_scale, LazyBound(lambda: glover_objbank__affine_frame)))),
	'translation' / Pointer(this.translation_ptr, If(this.translation_ptr != 0, Array(this.num_translation, LazyBound(lambda: glover_objbank__affine_frame)))),
	'child' / Pointer(this.child_ptr, If(this.child_ptr != 0, LazyBound(lambda: glover_objbank__mesh))),
	'sibling' / Pointer(this.sibling_ptr, If(this.sibling_ptr != 0, LazyBound(lambda: glover_objbank__mesh))),
	'display_list' / Pointer(this.display_list_ptr, If(this.display_list_ptr != 0, RepeatUntil(lambda obj_, list_, this: obj_.cmd == 184, LazyBound(lambda: glover_objbank__display_list_cmd)))),
	'sprites' / Pointer(this.sprites_ptr, If(this.sprites_ptr != 0, Array(this.num_sprites, LazyBound(lambda: glover_objbank__sprite)))),
)

glover_objbank__fixed_11_5 = Struct(
	'raw' / Int16ub,
	'value' / Computed(lambda this: (this.raw / 32.0)),
)

glover_objbank__geometry = Struct(
	'num_faces' / Int16ub,
	'num_vertices' / Int16ub,
	'vertices_ptr' / Int32ub,
	'faces_ptr' / Int32ub,
	'face_cn_ptr' / Int32ub,
	'uvs_ptr' / Int32ub,
	'uvs_unmodified_ptr' / Int32ub,
	'vertex_cn_ptr' / Int32ub,
	'flags_ptr' / Int32ub,
	'texture_ids_ptr' / Int32ub,
	'texture_ids' / Pointer(this.texture_ids_ptr, If(this.texture_ids_ptr != 0, Array(this.num_faces, Int32ub))),
	'faces' / Pointer(this.faces_ptr, If(this.faces_ptr != 0, Array(this.num_faces, LazyBound(lambda: glover_objbank__face)))),
	'vertex_cn' / Pointer(this.vertex_cn_ptr, If(this.vertex_cn_ptr != 0, Array(this.num_vertices, Int32ub))),
	'uvs_unmodified' / Pointer(this.uvs_unmodified_ptr, If(this.uvs_unmodified_ptr != 0, Array(this.num_faces, LazyBound(lambda: glover_objbank__uv)))),
	'flags' / Pointer(this.flags_ptr, If(this.flags_ptr != 0, Array(this.num_faces, Int8ub))),
	'vertices' / Pointer(this.vertices_ptr, If(this.vertices_ptr != 0, Array(this.num_vertices, LazyBound(lambda: glover_objbank__vertex)))),
	'uvs' / Pointer(this.uvs_ptr, If(this.uvs_ptr != 0, Array(this.num_faces, LazyBound(lambda: glover_objbank__uv)))),
	'face_cn' / Pointer(this.face_cn_ptr, If(this.face_cn_ptr != 0, Array(this.num_faces, Int32ub))),
)

glover_objbank = Struct(
	'directory' / RepeatUntil(lambda obj_, list_, this: obj_.obj_id == 0, LazyBound(lambda: glover_objbank__directory_entry)),
)

_schema = glover_objbank

meta:
  id: glover_objbank
  file-extension: obj
  endian: be
seq:
  - id: directory
    type: directory_entry
    repeat: until
    repeat-until: _.obj_id == 0x00000000
types:
  directory_entry:
    seq:
      - id: obj_id
        type: u4
      - id: ptr
        type: u4
    instances:
      obj_root:
        pos: ptr
        type: object_root
        if: ptr != 0
  object_root:
    seq:
      - id: obj_id
        type: u4
      - id: bank_base_addr
        type: u4
      - id: u2
        type: u4
      - id: mesh_ptr
        type: u4
      - id: u3
        type: u4
      - id: u4
        type: u4
      - id: animation_ptr
        type: u4
    instances:
      mesh:
        pos: mesh_ptr
        type: mesh
        if: mesh_ptr != 0
      animation:
        pos: animation_ptr
        type: animation
        if: animation_ptr != 0

  mesh:
    seq:
      - id: id
        type: u4
      - id: name
        type: str
        encoding: ASCII
        size: 8
      - id: mesh_alpha
        type: u1
      - id: sprite_alpha
        type: u1
      - id: num_scale
        type: u2
      - id: num_translation
        type: u2
      - id: num_rotation
        type: u2
      - id: geometry_ptr
        type: u4
      - id: display_list_ptr
        type: u4
      - id: scale_ptr
        type: u4
      - id: translation_ptr
        type: u4
      - id: rotation_ptr
        type: u4
      - id: num_sprites
        type: u4
      - id: sprites_ptr
        type: u4
      - id: num_children
        type: u2
      - id: render_mode
        type: u2
      - id: child_ptr
        type: u4
      - id: sibling_ptr
        type: u4
      - id: runtime_collision_data_ptr
        type: u4
    instances:
      geometry:
        pos: geometry_ptr
        type: geometry
        if: geometry_ptr != 0
      sprites:
        pos: sprites_ptr
        type: sprite
        repeat: expr
        repeat-expr: num_sprites
        if: sprites_ptr != 0
      scale:
        pos: scale_ptr
        type: affine_frame
        repeat: expr
        repeat-expr: num_scale
        if: scale_ptr != 0
      translation:
        pos: translation_ptr
        type: affine_frame
        repeat: expr
        repeat-expr: num_translation
        if: translation_ptr != 0
      rotation:
        pos: rotation_ptr
        type: affine_frame
        repeat: expr
        repeat-expr: num_rotation
        if: rotation_ptr != 0
      sibling:
        pos: sibling_ptr
        type: mesh
        if: sibling_ptr != 0
      child:
        pos: child_ptr
        type: mesh
        if: child_ptr != 0
      display_list:
        pos: display_list_ptr
        type: display_list_cmd
        repeat: until
        repeat-until: _.cmd == 0xB8
        if: display_list_ptr != 0
  geometry:
    seq:
      - id: num_faces
        type: u2
      - id: num_vertices
        type: u2
      - id: vertices_ptr
        type: u4
      - id: faces_ptr
        type: u4
      - id: face_cn_ptr
        type: u4
      - id: uvs_ptr
        type: u4
      - id: uvs_unmodified_ptr
        type: u4
      - id: vertex_cn_ptr
        type: u4
      - id: flags_ptr
        type: u4
      - id: texture_ids_ptr
        type: u4
    instances:
      face_cn:
        pos: face_cn_ptr
        type: u4
        repeat: expr
        repeat-expr: num_faces
        if: face_cn_ptr != 0
      vertices:
        pos: vertices_ptr
        type: vertex
        repeat: expr
        repeat-expr: num_vertices
        if: vertices_ptr != 0
      faces:
        pos: faces_ptr
        type: face
        repeat: expr
        repeat-expr: num_faces
        if: faces_ptr != 0
      uvs:
        pos: uvs_ptr
        type: uv
        repeat: expr
        repeat-expr: num_faces
        if: uvs_ptr != 0
      uvs_unmodified:
        pos: uvs_unmodified_ptr
        type: uv
        repeat: expr
        repeat-expr: num_faces
        if: uvs_unmodified_ptr != 0
      vertex_cn:
        pos: vertex_cn_ptr
        type: u4
        repeat: expr
        repeat-expr: num_vertices
        if: vertex_cn_ptr != 0
      flags:
        pos: flags_ptr
        type: u1
        repeat: expr
        repeat-expr: num_faces
        if: flags_ptr != 0
      texture_ids:
        pos: texture_ids_ptr
        type: u4
        repeat: expr
        repeat-expr: num_faces
        if: texture_ids_ptr != 0
  vertex:
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4
  face:
    seq:
      - id: v0
        type: u2
      - id: v1
        type: u2
      - id: v2
        type: u2
  uv:
    seq:
      - id: u1
        type: fixed_11_5
      - id: v1
        type: fixed_11_5
      - id: u2
        type: fixed_11_5
      - id: v2
        type: fixed_11_5
      - id: u3
        type: fixed_11_5
      - id: v3
        type: fixed_11_5

  fixed_11_5:
    seq:
      - id: raw
        type: u2
    instances:
      value:
        value: raw / 32.0

  sprite:
    seq:
      - id: texture_id
        type: u4
      - id: runtime_data_ptr
        type: u4
      - id: x
        type: u2
      - id: y
        type: u2
      - id: z
        type: u2
      - id: width
        type: u2
      - id: height
        type: u2
      - id: u5
        type: u2
      - id: u6
        type: u2
      - id: flags
        type: u2

  affine_frame:
    seq:
      - id: v1
        type: f4
      - id: v2
        type: f4
      - id: v3
        type: f4
      - id: v4
        type: f4
      - id: t
        type: u4
  display_list_cmd:
    seq:
      - id: w1
        type: u4
      - id: w0
        type: u4
    instances:
      cmd:
        value: (w1 >> 24) & 0xFF
  animation:
    seq:
      - id: num_animation_definitions
        type: s2
      - id: current_animation_idx
        type: s2
      - id: u3
        type: u4
      - id: is_playing
        type: u4
      - id: time_delta
        type: f4
      - id: next_anim_idx
        type: s2
        repeat: expr
        repeat-expr: 5
      - id: pad
        type: u2
      - id: next_is_playing
        type: u4
        repeat: expr
        repeat-expr: 5
      - id: next_time_delta
        type: u4
        repeat: expr
        repeat-expr: 5
      - id: next_anim_slot_idx
        type: s2
      - id: u15
        type: u2
      - id: animation_definitions_ptr
        type: u4
      - id: cur_time
        type: f4
    instances:
      animation_definitions:
        pos: animation_definitions_ptr
        type: animation_definition
        repeat: expr
        repeat-expr: num_animation_definitions
        if: animation_definitions_ptr != 0
  animation_definition:
    seq:
      - id: start_time
        type: s2
      - id: end_time
        type: s2
      - id: playback_speed
        type: f4
      - id: u1
        type: u4

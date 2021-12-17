meta:
  id: glover_texbank
  endian: be
  file-extension: .tex.bin
seq:
  - id: n_textures
    type: u4
  - id: asset
    type: texture
    repeat: expr
    repeat-expr: n_textures
types:
  texture:
    seq:
      - id: id
        type: u4
      - id: palette_anim_idx_min
        type: u1
      - id: palette_anim_idx_max
        type: u1
      - id: flags
        type: u2
      - id: frame_increment
        type: s2
      - id: frame_counter
        type: s2
      - id: width
        type: u2
      - id: height
        type: u2
      - id: masks
        type: u2
      - id: maskt
        type: u2
      - id: length
        type: u4
      - id: color_format
        type: u2
        enum: texture_color_format
      - id: compression_format
        type: u2
        enum: texture_compression_format
      - id: data_ptr
        type: u4
      - id: palette_offset
        type: u4
      - id: data
        size: length - 36
enums:
  texture_compression_format:
    0: ci4
    1: ci8
    2: uncompressed_16b
    3: uncompressed_32b
  texture_color_format:
    0: rgba
    1: yuv
    2: ci
    3: ia
    4: i

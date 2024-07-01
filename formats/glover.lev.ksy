meta:
  id: glover_level
  file-extension: lev
  endian: be
seq:
  - id: length
    type: u4
  - id: name
    type: str
    encoding: ASCII
    terminator: 0
  - id: body
    repeat: eos
    type: cmd
types:
  cmd:
    seq:
      - id: type_code
        type: u2
      - id: params
        type:
          switch-on: type_code
          cases:
            0xBD: unknown_sound_0xbd
            0xBE: environmental_sound
            0xA9: unknown_0xa9
            0xBB: mr_tip
            0x97: diffuse_light
            0x98: ambient_light
            0x01: glover_spawn_point
            0x02: ball_spawn_point
            0x03: camera_spawn_point
            0xA5: fog_configuration
            0xBF: actor_0xbf
            0xBC: animated_background_actor
            0x91: background_actor
            0x92: land_actor
            0x93: set_actor_rotation
            0x94: set_actor_scale
            0x8C: wind
            0xA0: water
            0x99: backdrop
            
            0xAA: cameo
            0xAB: cameo_inst
            
            0x04: puzzle
            0x05: puzzle_and
            0x06: puzzle_or
            0x07: puzzle_numtimes
            0x08: puzzle_any
            0x95: puzzle_cond
            0x96: puzzle_action

            0x85: garib_group
            0x86: garib
            0x87: powerup

            0x58: plat_mvspn_0x58
            0x59: plat_mvspn_0x59
            0x5a: plat_mvspn_0x5a
            0x71: plat_set_parent
            0x73: plat_mvspn_0x73
            0x74: plat_mvspn_0x74
            0x7b: plat_copy_spin_from_parent

            0xb8: plat_special_0xb8
            0xb3: plat_actor_enable_water_animation
            0xb7: set_global_0xb7

            0xb5: buzzer
            0xb6: buzzer_duty_cycle

            0xb4: set_object_sparkle
            0xb9: plat_special_0xb9
            0xa8: set_exit
            0x69: plat_cat_0x69
            0x68: platform_conveyor
            0x9e: plat_special_0x9e
            0x89: set_teleport
            0x8a: plat_fan_0x8a
            0x8b: plat_magnet_0x8b
            0x63: plat_checkpoint
            0x67: plat_crumb_0x67
            0xc7: plat_special_0xc7
            0x6e: plat_special_0x6e
            0x8e: plat_special_0x8e
            0x5b: plat_push_0x5b
            0x72: plat_conf_0x72

            0xc4: plat_orbit_sound_0xc4
            0xc6: plat_0xc6
            0x75: plat_orbit_around_point
            0x76: plat_orbit_pause
            0x77: plat_orbit_flip_0x77

            0xc3: plat_0xc3
            0xc5: plat_spin_sound_0xc5
            0x9f: plat_0x9f
            0x7c: plat_spin_pause_0x7c
            0x7d: plat_spin_flip
            0x7e: plat_0x7e
            0x7f: plat_constant_spin
            0x80: plat_spin_0x80
            0x81: plat_topple_0x81
            0x60: look_at_hand_0x60
            0x61: look_at_ball_0x61
            0x70: plat_rocking
            0x78: plat_0x78

            0xc1: plat_sound_0xc1
            0xc2: plat_sound_0xc2
            0x5e: plat_turn_towards_path_point
            0x5f: plat_go_forwards_0x5f
            0x6b: plat_path_point
            0x6c: plat_max_velocity
            0x6d: plat_path_acceleration
            0xa7: plat_pos_0xa7
            0xa6: plat_set_initial_pos

            0xc0: plat_play_object_animation
            0xa4: plat_0xa4
            0x5c: plat_vent_advance_frames
            0x64: plat_no_clip
            0x65: plat_destructible
            0xc8: plat_destructible_sound
            0x9d: plat_0x9d
            0x66: plat_0x66
            0x6a: plat_actor_surface_type
            0x6f: plat_set_tag
            0x82: plat_spike
            0x79: plat_scale
            0x7a: plat_str_0x7a

            0x8d: rope
            0x90: plat_sine
            0x8f: plat_orbit

            0xa2: vent
            0xa3: vent_duty_cycle

            0x62: platform
            0x5d: null_platform

            0x83: enemy
            0xa1: enemy_set_attention_bbox
            0xba: enemy_0xba
            0x84: enemy_finalize
            0x9a: enemy_normal_instruction
            0x9b: enemy_conditional_instruction
            0x9c: enemy_attack_instruction

            0x7D00: end_level_data

            # 0x00: noop
            # _: unknown
            _: unrecognized

# TODO: custom metadata is indicated by, immediately following
#       header:
#       0x0098 FFxx yyyyyyyy
#       where xx is the metadata type and yyyyyyyy is a type-defined data word
#       the following types are currently defined:
#       FF00 - pointer to unstructured ascii text at offset y from start of landscape file
#       FF01 - pointer to loading sequence information at offset y from start of landscape file
#
#       loading sequence format:
#       a series of commands to set up level assets, of the format:
#       nndddddd
#       where nn is a command byte and dddddd is a 3-byte unsigned number.
#       the following commands are defined:
#       00 - end sequence
#       01 - latch d as beginning ROM offset
#       02 - latch d as ending ROM offset
#       03 - load object bank between latched ROM offsets
#       04 - load texture bank between latched ROM offsets
#       05 - load object bank with internal id d
#       06 - load texture bank with internal id d
#       07 - load sound bank with internal id d
#       08 - load song with internal id d
#       09 - load song between latched ROM offsets
#       TODO: are absolute offsets actually useful? consider "yet another lookup table"

###############################################################
### Landscape

  unknown_sound_0xbd:
    # TODO
    seq:
      - id: h_0x00
        type: u2
      - id: h_0x02
        type: u2
      - id: h_0x04
        type: u2

  environmental_sound:
    # TODO: unclear how flags works, or any of the unknown halfs
    seq:
      - id: sound_id
        type: u2
      - id: volume
        type: u2
      - id: flags
        type: u2
      - id: h_0x06
        type: u2
      - id: h_0x08
        type: u2
      - id: h_0x0a
        type: u2
      - id: h_0x0c
        type: u2
      - id: h_0x0e
        type: u2
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4
      - id: radius
        type: f4

  unknown_0xa9:
    # TODO
    seq:
      - id: i_0x00
        type: u4

  mr_tip:
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4
      - id: message_id
        type: u2

  diffuse_light:
    seq:
      - id: r
        type: u2
      - id: g
        type: u2
      - id: b
        type: u2
      - id: theta_x
        type: f4
      - id: theta_y
        type: f4

  ambient_light:
    # notes: each H is cast to a B at runtime
    seq:
      - id: r
        type: u2
      - id: g
        type: u2
      - id: b
        type: u2

  glover_spawn_point:
    seq:
      - id: x
        type: f4
      - id: y
        type: f4  
      - id: z
        type: f4

  ball_spawn_point:
    #
    # 'type' encodes how this ball affects overall game progress.
    #   0: ball can contribute to game completion progress
    #   1: unknown (TODO: seems to only be used in prehistoric 1, maybe it
    #               means frozen-in-ice-cube?)
    #   2: ball represents an in-transit ball between defeating a boss and
    #      returning to the castle cave
    #   3: ball does not contribute to game completion progress
    #      (eg, bonus stages and cutscenes)
    #       
    # If missing, Glover will start level holding ball
    #
    # TODO: on rare occasions based on the type field and internal parser state,
    #       this struct is JUST h_0x00 without the 3f. more analysis of the code
    #       and level data is needed to figure out what the rules around this are.
    #       so gross.
    seq:
      - id: type
        type: u2
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4

  camera_spawn_point:
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4
      - id: pitch
        type: f4
      - id: yaw
        type: f4

  fog_configuration:
    seq:
      - id: fog_enabled
        type: u1
      - id: r
        type: u1
      - id: g
        type: u1
      - id: b
        type: u1
      - id: fog_distance
        type: u2
      - id: near_clip
        type: u2

  actor_0xbf:
    # TODO
    # Used a lot in cutscenes. Searches current actor for a child with the
    # specified mesh, and then modifies it based on the value of 'mode'.
    #     0 seems to be a 'start' command and 2 seems to be an 'append'
    seq:
      - id: mode
        type: u2
      - id: child_mesh_id
        type: u4

  animated_background_actor:
    # Sets up a background actor and queues it to play
    # anim idx 0. Hard-coded to start paused on the intro
    # and outro cutscenes and carnival boss, otherwise
    # starts playing immediately.
    seq:
      - id: object_id
        type: u4
      - id: name
        type: str
        encoding: ASCII
        size: 8
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4

  background_actor:
    seq:
      - id: object_id
        type: u4
      - id: name
        type: str
        encoding: ASCII
        size: 8
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4

  land_actor:
    seq:
      - id: object_id
        type: u4
      - id: name
        type: str
        encoding: ASCII
        size: 8
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4

  set_actor_rotation:
    # x/y/z are axis rotation angles, in radians
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4

  set_actor_scale:
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4

  wind:
    # TODO: figure out exactly what unknown_0x2c does,
    #       seems to have something to do with effect distance
    seq:
      - id: left
        type: f4
      - id: top
        type: f4
      - id: front
        type: f4

      - id: width
        type: f4
      - id: height
        type: f4
      - id: depth
        type: f4

      - id: vel_x
        type: f4
      - id: vel_y
        type: f4
      - id: vel_z
        type: f4

      - id: turbulence
        type: f4

      - id: unknown_0x2c
        type: u4

      - id: active
        type: u4

      - id: tag
        type: u4


  water:
    # lol dear lord
    seq:
      - id: left
        type: f4
      - id: top
        type: f4
      - id: front
        type: f4
      - id: width
        type: f4
      - id: bottom
        type: f4
      - id: depth
        type: f4
      - id: surface_y
        type: f4
      - id: current_x
        type: f4
      - id: current_z
        type: f4
      - id: unknown_1
        type: u2
      - id: object_id
        type: u4
      - id: name
        type: str
        encoding: ASCII
        size: 8
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4

  backdrop:
    seq:
      - id: texture_id
        type: u4

      - id: decal_pos_x
        type: u2
      - id: decal_pos_y
        type: u2
      - id: sort_key
        type: u2

      - id: offset_y
        type: s2
      - id: scale_x
        type: u2
      - id: scale_y
        type: u2
      - id: flip_x
        type: u2
      - id: flip_y
        type: u2
      - id: scroll_speed_x
        type: u2
      - id: unused
        type: u2

      - id: decal_parent_idx
        type: u2

###############################################################
### Cameo
# TODO: understand what these are

  cameo:
    seq: []

  cameo_inst:
    seq:
      - id: inst_type
        type: u2
      - id: body
        type:
          switch-on: inst_type
          cases:
            0x00: cameo_inst_0
            0x01: cameo_inst_1
            0x02: cameo_inst_2
            0x03: cameo_inst_3
            0x04: cameo_inst_4
            0x05: cameo_inst_5
            0x06: cameo_inst_6
            _: cameo_inst_default

  cameo_inst_0:
    seq:
      - id: h_0x00
        type: u2
      - id: h_0x02
        type: u2
      - id: h_0x04
        type: u2
      - id: i_0x06
        type: u4
      - id: h_0x0a
        type: u2
      - id: h_0x0c
        type: u2

  cameo_inst_1:
    seq:
      - id: h_0x00
        type: u2
      - id: i_0x02
        type: u4
      - id: i_0x06
        type: u4
      - id: i_0x0a
        type: u4
      - id: h_0x0e
        type: u2
      - id: h_0x10
        type: u2

  cameo_inst_2:
    seq:
      - id: h_0x00
        type: u2
      - id: i_0x02
        type: u4
      - id: i_0x06
        type: u4
      - id: i_0x0a
        type: u4
      - id: i_0x0e
        type: u4
      - id: h_0x12
        type: u2
      - id: h_0x14
        type: u2

  cameo_inst_3:
    seq:
      - id: h_0x00
        type: u2
      - id: i_0x02
        type: u4
      - id: h_0x06
        type: u2
      - id: h_0x08
        type: u2

  cameo_inst_4:
    seq:
      - id: h_0x00
        type: u2
      - id: h_0x02
        type: u2
      - id: h_0x04
        type: u2
      - id: h_0x06
        type: u2
      - id: h_0x08
        type: u2

  cameo_inst_5:
    seq:
      - id: h_0x00
        type: u2
      - id: h_0x02
        type: u2
      - id: h_0x04
        type: u2

  cameo_inst_6:
    seq:
      - id: h_0x00
        type: u2
      - id: h_0x02
        type: u2
      - id: h_0x04
        type: u2
      - id: h_0x06
        type: u2

  cameo_inst_default:
    seq:
      - id: h_0x00
        type: u2
      - id: h_0x02
        type: u2

###############################################################
### Puzzles

# TODO: investigate how these work

  puzzle:
    seq: []

  puzzle_and:
    seq: []

  puzzle_or:
    seq: []

  puzzle_numtimes:
    seq:
      - id: n
        type: u2

  puzzle_any:
    seq:
      - id: op
        type: u2

  puzzle_cond:
    seq:
      - id: cond_type
        type: u2
      - id: body
        type:
          switch-on: cond_type
          cases:
            0x22: puzzle_cond_b

            0x23: puzzle_cond_c
            0x25: puzzle_cond_c
            0x27: puzzle_cond_c

            0x24: puzzle_cond_d
            0x26: puzzle_cond_d
            0x28: puzzle_cond_d

            0x29: puzzle_cond_e

            _: puzzle_cond_a


  puzzle_cond_a:
    seq:
      - id: u32_0x24
        type: u2
      - id: u16_0x0a
        type: u2

  puzzle_cond_b:
    seq:
      - id: i_0x00
        type: u4
      - id: i_0x04
        type: u4
      - id: i_0x08
        type: u4

      - id: i_0x0c
        type: u4
      - id: i_0x10
        type: u4
      - id: i_0x14
        type: u4

      - id: i_0x18
        type: u4

  puzzle_cond_c:
    seq:
      - id: i_0x00
        type: u4
      - id: i_0x04
        type: u4
      - id: i_0x08
        type: u4

      - id: i_0x0c
        type: u4
      - id: i_0x10
        type: u4
      - id: i_0x14
        type: u4

  puzzle_cond_d:
    seq:
      - id: i_0x00
        type: u4
      - id: i_0x04
        type: u4
      - id: i_0x08
        type: u4

      - id: i_0x0c
        type: u4

  puzzle_cond_e:
    seq:
      - id: i_0x00
        type: u4
      - id: i_0x04
        type: u4
      - id: i_0x08
        type: u4

      - id: i_0x0c
        type: u4
      - id: i_0x10
        type: u4

  puzzle_action:
    seq:
      - id: action_type
        type: u2
      - id: body
        type:
          switch-on: action_type
          cases:
            0x35: puzzle_action_0x35_0x3b_0x3c_0x3d_0x3e_0x3f_0x40
            0x3b: puzzle_action_0x35_0x3b_0x3c_0x3d_0x3e_0x3f_0x40
            0x3c: puzzle_action_0x35_0x3b_0x3c_0x3d_0x3e_0x3f_0x40
            0x3d: puzzle_action_0x35_0x3b_0x3c_0x3d_0x3e_0x3f_0x40
            0x3e: puzzle_action_0x35_0x3b_0x3c_0x3d_0x3e_0x3f_0x40
            0x3f: puzzle_action_0x35_0x3b_0x3c_0x3d_0x3e_0x3f_0x40
            0x40: puzzle_action_0x35_0x3b_0x3c_0x3d_0x3e_0x3f_0x40

            0x4F:  puzzle_action_0x4f

            0x46: puzzle_action_0x46_0x47_0x48
            0x47: puzzle_action_0x46_0x47_0x48
            0x48: puzzle_action_0x46_0x47_0x48

            0x49: puzzle_action_0x49_0x4d
            0x4D: puzzle_action_0x49_0x4d

            0x4A: puzzle_action_0x4a

            0x4B: puzzle_action_0x4b_0x4c
            0x4C: puzzle_action_0x4b_0x4c

            0x54: puzzle_action_0x54

            0x55: puzzle_action_0x55

            0x56: puzzle_action_0x56

            _:  puzzle_action_default

  puzzle_action_0x4f:
    seq:
      - id: u32_0x14
        type: u4
      - id: u32_0x18
        type: u4

      - id: u32_0x10
        type: u4

      - id: u16_0x0e
        type: u2

      - id: u16_0x0a
        type: u2

      - id: u32_0x20
        type: u4


  puzzle_action_0x35_0x3b_0x3c_0x3d_0x3e_0x3f_0x40:
    seq:
      - id: u32_0x14
        type: u4
      - id: u32_0x18
        type: u4
      - id: u32_0x1c
        type: u4

      - id: u32_0x10
        type: u4

      - id: u16_0x0e
        type: u2

      - id: u16_0x0a
        type: u2

      - id: u32_0x20
        type: u4

  puzzle_action_default:
    seq:
      - id: u32_0x10
        type: u4

      - id: u16_0x0e
        type: u2

      - id: u16_0x0a
        type: u2

      - id: u32_0x20
        type: u4

  puzzle_action_0x46_0x47_0x48:
    seq:
      - id: u32_0x24
        type: u4
      - id: u16_0x0a
        type: u2 

  puzzle_action_0x49_0x4d:
    seq:
      - id: u32_0x24
        type: u4
      - id: u32_0x28
        type: u4
      - id: u32_0x2c
        type: u4
      - id: u16_0x0a
        type: u2 

  puzzle_action_0x4a:
    seq:
      - id: u32_0x24
        type: u4
      - id: u32_0x24_0x0c
        type: u4
      - id: u16_0x0a
        type: u2 


  puzzle_action_0x54:
    seq:
      - id: u32_0x14
        type: u2
      - id: u32_0x16
        type: u2
      - id: u32_0x18
        type: u2
      - id: u32_0x1a
        type: u2
      - id: u32_0x1c
        type: u2
      - id: u32_0x1e
        type: u2
      - id: u32_0x10
        type: u2
      - id: u16_0x0e
        type: u2 
      - id: u32_0x24
        type: u4
      - id: u32_0x28
        type: u4
      - id: u32_0x2c
        type: u4
      - id: u16_0x0a
        type: u2 

  puzzle_action_0x55:
    seq:
      - id: u32_0x24
        type: u4
      - id: u16_0x0a
        type: u2 

  puzzle_action_0x56:
    seq:
      - id: u32_0x14
        type: u4
      - id: u32_0x18
        type: u4
      - id: u16_0x1c
        type: u2

      - id: u16_0x0a
        type: u2 

  puzzle_action_0x4b_0x4c:
    seq:
      - id: u16_0x0a
        type: u2 

###############################################################
### Collectibles

  garib_group:
    # TODO: investigate further
    # initial_state:
    #   <0: visible, not collectable
    #   ==0: invisible, uncollectable
    #   >0: visible, collectable
    seq:
      - id: group_id
        type: u2 
      - id: initial_state
        type: s2 

  garib:
    # type: {"0": "garib", "1": "500pt-bang", "2": "extra-life", "3": "mad-garib"}
    seq:
      - id: x
        type: f4 
      - id: y
        type: f4 
      - id: z
        type: f4 
      - id: type
        type: u2 
      - id: dynamic_shadow
        type: u2 

  powerup:
    seq:
      - id: type
        type: u2
      - id: u16_0x02
        type: u2
      - id: u16_0x04
        type: u2
      - id: x
        type: f4 
      - id: y
        type: f4 
      - id: z
        type: f4 


###############################################################
### Platform movement

  plat_mvspn_0x58:
    seq:
      - id: u16_0x14
        type: u2
      - id: u32_0x10
        type: u4

  plat_mvspn_0x59:
    seq:
      - id: u16_0x24
        type: u2
      - id: u32_0x20
        type: u4

      - id: u32_0x28
        type: u4
      - id: u32_0x2c
        type: u4
      - id: u32_0x30
        type: u4

  plat_mvspn_0x5a:
    seq:
      - id: u16_0x1c
        type: u2
      - id: u32_0x18
        type: u4

  plat_set_parent:
    seq:
      - id: tag
        type: u2

  plat_mvspn_0x73:
    seq:
      - id: u16_0x0c
        type: u2
      - id: u32_0x34
        type: u4
      - id: u32_0x38
        type: u4
      - id: u32_0x3c
        type: u4

  plat_mvspn_0x74:
    seq:
      - id: u32_0x34
        type: u4
      - id: u32_0x38
        type: u4
      - id: u32_0x3c
        type: u4

  plat_copy_spin_from_parent:
    seq: []

###############################################################
### Platform special

  plat_special_0xb8: # 0xb8
    seq: []

  plat_actor_enable_water_animation: # 0xb3
    seq: []

  set_global_0xb7: # 0xb7
    # TODO: writes value to RAM 0x801efcf4, only use is to set some behavior for setting platform's initial position
    seq:
      - id: value
        type: u4

  buzzer: # 0xb5
    # Creates a linear electric arc enemy
    #
    # If a non-zero platform tag is specified, the
    # arc uses that platform's position as the respective
    # endpoint. Otherwise, it uses the coordinates specified
    # here.
    #
    # TODO: document draw flags
    seq:
      - id: tag
        type: u2

      - id: platform_1_tag
        type: u2

      - id: platform_2_tag
        type: u2

      - id: draw_flags
        type: u2

      - id: r
        type: u2
      - id: g
        type: u2
      - id: b
        type: u2
      - id: color_jitter
        type: u2

      - id: end_1_x
        type: f4
      - id: end_1_y
        type: f4
      - id: end_1_z
        type: f4

      - id: end_2_x
        type: f4
      - id: end_2_y
        type: f4
      - id: end_2_z
        type: f4

      - id: draw_diameter
        type: f4

      - id: draw_thickness
        type: f4

  buzzer_duty_cycle: # 0xb6
    seq:
      - id: frames_off
        type: u2
      - id: frames_on
        type: u2

  set_object_sparkle: # 0xb4
    # Works on active actor or platform
    seq:
      - id: period
        type: u2

  plat_special_0xb9: # 0xb9
    # TODO: ORs 0x20000000 into a flags field of active  platform or actor
    #       affects physics calculations in FUN_80157708
    seq: []

  set_exit: # 0xa8
    seq:
      - id: type # TODO: enumerate types
        type: u2
      - id: visible
        type: u2

  plat_cat_0x69: # 0x69
    seq:
      - id: u16_0x20
        type: u2

      - id: u32_0x00
        type: u4
      - id: u32_0x04
        type: u4
      - id: u32_0x08
        type: u4

      - id: u32_0x0c
        type: u4

      - id: u32_0x10
        type: u4

      - id: u32_0x1c
        type: u4

  platform_conveyor: # 0x68
    seq:
      - id: vel_x
        type: f4
      - id: vel_y
        type: f4
      - id: vel_z
        type: f4

  plat_special_0x9e: # 0x9e
    seq:
      - id: u32_0x5c
        type: u4
      - id: u32_0x60
        type: u4
      - id: u32_0x65
        type: u4

      - id: u32_0x68
        type: u4

  set_teleport: # 0x89
    seq:
      - id: target_tag
        type: u2
      - id: u16_0x0c
        type: u2
      - id: u16_0x10
        type: u2
      - id: u16_0x12
        type: u2

      - id: u32_0x00
        type: u4
      - id: u32_0x04
        type: u4
      - id: u32_0x08
        type: u4

  plat_fan_0x8a: # 0x8a
    seq:
      - id: u16_0x0c
        type: u2

      - id: u32_0x48
        type: u4
      - id: u32_0x4c
        type: u4
      - id: u32_0x50
        type: u4


      - id: u32_0x10
        type: u4

      - id: u32_0x14
        type: u4

      - id: u32_0x18
        type: u4

      - id: u32_0x1c
        type: u4

  plat_magnet_0x8b: # 0x8b
    seq:
      - id: u16_0x0c
        type: u2

      - id: u32_0x48
        type: u4
      - id: u32_0x4c
        type: u4
      - id: u32_0x50
        type: u4

      - id: u32_0x10
        type: u4

      - id: u32_0x14
        type: u4

      - id: u32_0x18
        type: u4

      - id: u32_0x1c
        type: u4

  plat_checkpoint: # 0x63
    # TODO: input seems to influence camera angle on spawn?
    # theta is in radians
    seq:
      - id: u16_0x17
        type: u2
      - id: theta
        type: f4

  plat_crumb_0x67: # 0x67
    seq:
      - id: u16_0x02
        type: u2
      - id: u16_0x04
        type: u2
      - id: u16_0x08
        type: u4

  plat_special_0xc7: # 0xc7
    seq:
      - id: u16_0x2a
        type: u2
      - id: u16_0x1c_and_0x24
        type: u2
      - id: u16_0x28
        type: u2

  plat_special_0x6e: # 0x6e
    # TODO: bits 0-2 are valid flags, figure out what they do
    seq:
      - id: flags
        type: u2
      - id: u32_0x70
        type: u4

  plat_special_0x8e: # 0x8e
    # TODO: if enable is nonzero, ORs 0x4000 into plat->u32_0x14
    #       figure out what this does
    seq:
      - id: enable
        type: u2

  plat_push_0x5b: # 0x5b
    # TODO: bits 0-2 are valid flags, figure out what they do
    seq:
      - id: flags
        type: u2
      - id: u32_0x04
        type: u4
      - id: actor_f_0x70
        type: f4
      - id: u32_0x1c
        type: u4

  plat_conf_0x72: # 0x72
    seq:
      - id: u32_0x00
        type: u4
      - id: u32_0x04
        type: u4
      - id: u32_0x08
        type: u4

      - id: u32_0x0c
        type: u4
      - id: u32_0x10
        type: u4
      - id: u32_0x14
        type: u4

###############################################################
### Platform Orbit

  plat_orbit_sound_0xc4: # 0xc4
    seq:
      - id: u16_0x3a
        type: u2
      - id: u16_0x2c_and_0x34
        type: u2
      - id: u16_0x38
        type: u2

  plat_0xc6: # 0xc6
    seq:
      - id: u16_0x4a
        type: u2
      - id: u16_0x44
        type: u2
      - id: u16_0x48
        type: u2

  plat_orbit_around_point: # 0x75
    # TODO: the parser doesn't consume bytes for everything after idx
    #       when the platform already has a point to orbit,
    #       but it's hard to detect this in a grammar because it
    #       relies on parser state. blah. probably fine to not model
    #       this behavior, but it's ugly.
    seq:
      - id: axis
        type: u2

      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4

      - id: speed
        type: f4

  plat_orbit_pause: # 0x76
    # TODO: the parser doesn't consume these bytes if the platform already
    #       "has ORBITFLIP specified".
    seq:
      - id: num_frames
        type: u2
      - id: num_pauses
        type: u2


  plat_orbit_flip_0x77: # 0x77
    # TODO: the parser doesn't consume these bytes if the platform already
    #       "has ORBITPAUSE specified".
    seq:
      - id: u16_0x08
        type: u2
      - id: u16_0x10
        type: u2



###############################################################
### Platform Misc Spin

  plat_0xc3: # 0xc3
    seq:
      - id: u16_0x86
        type: u2
      - id: u32_0x78_0x80
        type: u2
      - id: u16_0x84
        type: u2

  plat_spin_sound_0xc5: # 0xc5
    seq:
      - id: sound_id
        type: u2
      - id: volume
        type: u2
      - id: pitch
        type: u2

  plat_0x9f: # 0x9f
    seq:
      - id: u32_0x6c
        type: u4
      - id: u32_0x70
        type: u4
      - id: u32_0x1c
        type: u4
      - id: u32_0x28
        type: u4

  plat_spin_pause_0x7c: # 0x7c
    seq:
      - id: u16_0x0c
        type: u2
      - id: u16_0x0a
        type: u2

  plat_spin_flip: # 0x7d
    # Only parses when SPINPAUSE is not specified
    seq:
      - id: cooldown_timer
        type: u2
      - id: theta
        type: f4

  plat_0x7e: # 0x7e
    seq:
      - id: u32_0x28
        type: u4

  plat_constant_spin: # 0x7f
    # TODO: axis is enum: {"0": "x", "1": "y", "2": "z"}
    seq:
      - id: axis
        type: u2
      - id: initial_theta
        type: f4
      - id: speed
        type: f4

  plat_spin_0x80: # 0x80
    seq:
      - id: idx
        type: u2
      - id: f_0x1c
        type: f4
      - id: u32_0x28
        type: u4
      - id: u32_ustack56
        type: u4
      - id: u32_0x2c
        type: u4
      - id: f_0x6c
        type: f4
      - id: f_0x70
        type: u2

  plat_topple_0x81: # 0x81
    seq:
      - id: idx
        type: u2
      - id: f_0x1c
        type: f4
      - id: f_0x28
        type: f4
      - id: f_0x24
        type: f4
      - id: f_0x2c
        type: f4
      - id: f_0x6c
        type: f4
      - id: f_0x70_pivot_height
        type: f4
      - id: u16_0x10
        type: u2

  look_at_hand_0x60: # 0x60
    # TODO: doesn't parse if error, yadda yadda yadda
    seq:
      - id: u32_0x6c
        type: u4
      - id: u32_0x1c
        type: u4

  look_at_ball_0x61: # 0x61
    # TODO: doesn't parse if error, yadda yadda yadda
    seq:
      - id: u32_0x6c
        type: u4
      - id: u32_0x1c
        type: u4

  plat_rocking: # 0x70
    seq:
      - id: axis
        type: u2
      - id: theta
        type: f4
      - id: deceleration
        type: f4
      - id: blur_height
        type: f4
      - id: frame_advance
        type: u2

  plat_0x78: # 0x78
    seq:
      - id: u16_0x08
        type: u2


###############################################################
### Platform misc properties

  plat_sound_0xc1: # 0xc1
    seq:
      - id: sound_id
        type: u2
      - id: volume
        type: u2
      - id: pitch
        type: u2

  plat_sound_0xc2: # 0xc2
    seq:
      - id: sound_id
        type: u2
      - id: volume
        type: u2
      - id: pitch
        type: u2

  plat_turn_towards_path_point: # 0x5e
    seq:
      - id: input_1
        type: u4
      - id: input_2
        type: u4

  plat_go_forwards_0x5f: # 0x5f
    # TODO: empty seq if there isn't an active
    #       platform
    # does some sort of thing with radians
    seq:
      - id: u32_0x2c_0x6c
        type: u4
      - id: u32_0x2c_0x1c
        type: u4
      - id: u32_0xf0
        type: u4
      - id: u32_0x2c_0x34
        type: u4

  plat_path_point: # 0x6b
    seq:
      - id: duration
        type: s2
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4

  plat_max_velocity: # 0x6c
    seq:
      - id: velocity
        type: f4

  plat_path_acceleration: # 0x6d
    seq:
      - id: acceleration
        type: f4

  plat_pos_0xa7: # 0xa7
    seq:
      - id: u8_idx
        type: u2

  plat_set_initial_pos: # 0xa6
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4


  plat_play_object_animation: # 0xc0
    # Plays the skeletal animation at index 0 in the platform actor's
    # animation data
    seq: []

  plat_0xa4: # 0xa4
    seq: []

  plat_vent_advance_frames: # 0x5c
    seq:
      - id: num_frames
        type: u2
    meta:
      xref: [platform, vent]

  plat_no_clip: # 0x64
    seq: []

  plat_destructible: # 0x65
    # TODO: figure flags out
    # valid flag bits are 0, 1, and 2
    # flag bit 0 means glover can fist-pound it apart
    seq:
      - id: flags 
        type: u2
      - id: num_fragments 
        type: u4
      - id: fragment_object_id
        type: u4
      - id: name
        type: str
        encoding: ASCII
        size: 8

  plat_destructible_sound: # 0xc8
    seq:
      - id: sound_id
        type: u2
      - id: volume
        type: u2
      - id: pitch
        type: u2
    
  plat_0x9d: # 0x9d
    seq: []

  plat_0x66: # 0x66
    seq: []

  plat_actor_surface_type: # 0x6a
    # TODO: figure out what value means. 6 = insta-death on contact
    seq:
      - id: value
        type: u2
    

  plat_set_tag: # 0x6f
    seq:
      - id: tag
        type: u2

  plat_spike: # 0x82
    seq: []

  plat_scale: # 0x79
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4
    
  plat_str_0x7a: # 0x7a
    seq:
      - id: u32_0x0c
        type: u4
      - id: u32_0x10
        type: u4
      - id: u32_0x14
        type: u4

      - id: u16_0x18
        type: u2

      - id: u16_0x1c
        type: u2

###############################################################
### Special objects

  rope: # 0x8d
    seq:
      - id: num_components
        type: u4

      - id: wiggle_axis
        type: u2

      - id: component_obj_id
        type: u4

      - id: name
        encoding: ASCII
        type: str
        size: 8

      - id: puzzle_unknown_1
        type: f4
      - id: sway_unknown_1
        type: f4
      - id: sway_unknown_2
        type: f4
      - id: sway_unknown_3
        type: f4
      - id: sway_rocking_theta
        type: u4
      - id: sway_unknown_4
        type: u4
      - id: sway_unknown_5
        type: f4

      - id: x
        type: f4

      - id: y
        type: f4

      - id: z
        type: f4

      - id: component_w
        type: f4

      - id: component_h
        type: f4

      - id: component_d
        type: f4


  plat_sine: # 0x90
    seq:
      - id: u32_count
        type: u4

      - id: u32_116
        type: u4

      - id: name
        encoding: ASCII
        type: str
        size: 8

      - id: f_108
        type: f4

      - id: f_104
        type: f4

      - id: f_100
        type: f4

      - id: f_96
        type: f4

      - id: f_92
        type: f4

      - id: f_88
        type: f4

      - id: f_84
        type: f4

      - id: f_80
        type: f4

      - id: u32_176
        type: u4

      - id: u32_172
        type: u4

  plat_orbit: # 0x8f
    seq:
      - id: u16_120
        type: u2

      - id: u16_136
        type: u2
      - id: u16_134
        type: u2
      - id: u16_132
        type: u2

      - id: u32_116
        type: u4

      - id: name
        encoding: ASCII
        type: str
        size: 8

      - id: f_112
        type: f4
      - id: f_108
        type: f4
      - id: f_104
        type: f4
      - id: f_100
        type: f4
      - id: f_96
        type: f4
      - id: f_92
        type: f4
      - id: f_88
        type: f4
      - id: f_84
        type: f4
      - id: f_80
        type: f4

      - id: u32_176
        type: u4



###############################################################
### Misc

  vent: # 0xa2
    seq:
      - id: type
        type: u2
      - id: u16_0x0a
        type: u2
      - id: parent_tag
        type: u2

      - id: origin_x
        type: f4
      - id: origin_y
        type: f4
      - id: origin_z
        type: f4

      - id: particle_velocity_x
        type: f4
      - id: particle_velocity_y
        type: f4
      - id: particle_velocity_z
        type: f4

  vent_duty_cycle: # 0xa3
    seq:
      - id: frames_off
        type: s2
      - id: frames_on
        type: s2

  platform: # 0x62
    seq:
      - id: object_id
        type: u4
      - id: name
        encoding: ASCII
        type: str
        size: 8


  null_platform: # 0x5d
    seq: []

  enemy: # 0x83
    seq:
      - id: type
        type: u2
        enum: enemy_type
      - id: u1
        type: u2

      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4

      - id: y_rotation
        type: f4
    enums:
      enemy_type:
        7: bovva
        8: cannon
        9: samtex
        10: mallet
        11: generalw
        12: lionfish
        13: chester
        14: keg
        15: reggie
        16: swish
        17: thrice
        18: robes
        19: fumble
        20: mike
        21: raptor
        22: crumpet
        23: tracey
        24: yoofow
        25: opec
        26: cymon
        27: sucker
        28: bugle
        29: dennis
        30: chuck
        31: hubchicken1
        32: frankie2
        33: kloset
        34: willy
        35: joff
        36: cancer
        37: kirk
        38: robot
        39: evilrobot
        40: spank
        41: babyspk2
        42: evilglove
        43: dibber
        44: brundle
        45: malcom
        46: spotty
        47: gordon
        48: sidney
        49: weevil
        50: chopstik
        51: butterfly
        52: spider
        53: bat
        54: frog
        55: dragfly
        56: boxthing
        57: bug
        58: nmefrog

  enemy_set_attention_bbox: # 0xa1
    seq:
      - id: left
        type: f4
      - id: top
        type: f4
      - id: front
        type: f4
      - id: width
        type: f4
      - id: height
        type: f4
      - id: depth
        type: f4

  enemy_0xba: # 0xba
    seq: []

  enemy_finalize: # 0x84
    seq: []

  enemy_normal_instruction: # 0x9a
    seq:
      - id: instr
        type: enemy_instruction

  enemy_conditional_instruction: # 0x9b
    seq:
      - id: instr
        type: enemy_instruction

  enemy_attack_instruction: # 0x9c
    seq:
      - id: instr
        type: enemy_instruction


  enemy_instruction:
    seq:
      - id: instr_type
        type: u2
      - id: lifetime
        type: s2
      - id: params
        type:
          switch-on: instr_type
          cases:
            0: enemy_instruction_move
            1: enemy_instruction_dash
            2: enemy_instruction_turn
            9: enemy_instruction_a # TODO
            0x0a: enemy_instruction_a # TODO
            0x0b: enemy_instruction_a # TODO
            0x0d: enemy_instruction_a # TODO
            0x16: enemy_instruction_a # TODO
            0x17: enemy_instruction_a # TODO

            0x3: enemy_instruction_random_walk

            4: enemy_instruction_rest
            5: enemy_instruction_c # TODO
            6: enemy_instruction_c # TODO
            7: enemy_instruction_play_animation
            8: enemy_instruction_c # TODO
            0xc: enemy_instruction_c # TODO
            0xe: enemy_instruction_c # TODO
            0xf: enemy_instruction_attack
            0x10: enemy_instruction_c # TODO
            0x11: enemy_instruction_c # TODO
            0x12: enemy_instruction_goto
            0x13: enemy_instruction_c # TODO
            0x14: enemy_instruction_c # TODO
            0x15: enemy_instruction_c # TODO
            0x18: enemy_instruction_c # TODO

            _: enemy_instruction_error
      - id: execution_condition_param_a
        type: f4
      - id: execution_condition_param_b
        type: f4
      - id: flags
        type: u4
        enum: instruction_flags
      - id: execution_condition
        type: u2
        enum: execution_condition_type
    enums:
      execution_condition_type:
        0: ball_within_range
        1: ball_within_ground_range
        2: glover_within_range
        3: glover_within_ground_range
        4: ball_or_glover_within_range
        5: ball_or_glover_within_ground_range
        6: ball_within_angle_of_view
        7: glover_within_angle_of_view
        8: ball_or_glover_within_angle_of_view
        9: periodic
        10: roll_angle_within_range_and_periodic
        11: glover_holding_ball
        12: glover_not_holding_ball
        13: enemy_holding_ball
        14: enemy_not_holding_ball
        15: glover_holding_enemy
        16: glover_not_holding_enemy
        17: on_ball
        18: on_glover
        19: enemy_within_attention_bbox
        20: always
        21: never
        22: random_chance_param_a_over_1000
      instruction_flags:
        0x100000: face_player
        0x200000: face_ball
        0x400000: face_closer_of_player_or_ball


  enemy_instruction_a:
    seq:
      - id: u32_0x02
        type: u4
      - id: u32_0x06
        type: u4
      - id: u32_0x0a
        type: u4

      - id: u32_0x0e
        type: u4

  enemy_instruction_dash:
    seq:
      - id: destination_x
        type: f4
      - id: destination_y
        type: f4
      - id: destination_z
        type: f4
      - id: vel_magnitude
        type: f4

  enemy_instruction_move:
    seq:
      - id: destination_x
        type: f4
      - id: destination_y
        type: f4
      - id: destination_z
        type: f4
      - id: vel_magnitude
        type: f4

  enemy_instruction_turn:
    seq:
      - id: lookat_x
        type: f4
      - id: lookat_y
        type: f4
      - id: lookat_z
        type: f4
      - id: choose_random_direction
        type: u4


  enemy_instruction_goto:
    seq:
      - id: instr_idx
        type: u4
      - id: unused
        type: u4

  enemy_instruction_random_walk:
    seq:
      - id: home_x
        type: f4
      - id: home_y
        type: f4
      - id: home_z
        type: f4

      - id: extent_x
        type: f4
      - id: extent_y
        type: f4
      - id: extent_z
        type: f4

      - id: min_travel_distance
        type: f4

  enemy_instruction_play_animation:
    seq:
      - id: anim_idx_1
        type: s4
      - id: anim_idx_2
        type: s4
 
  enemy_instruction_rest:
    seq:
      - id: flags
        type: u4
      - id: anim_start_playing
        type: u4

  enemy_instruction_attack:
    seq:
      - id: unused_1
        type: u4
      - id: unused_2
        type: u4

  enemy_instruction_c:
    seq:
      - id: u32_0x02
        type: u4

      - id: u32_0x0e
        type: u4


  enemy_instruction_error:
    seq: []

###############################################################
### Control

  end_level_data:
    seq: []

  unrecognized:
    seq: []

  # noop:
  #   seq: []

  # unknown:
  #   seq:
  #     - id: body
  #       size-eos: true
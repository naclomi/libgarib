from construct import *
from construct.lib import *

glover_level__puzzle_action_0x54 = Struct(
	'u32_0x14' / Int16ub,
	'u32_0x16' / Int16ub,
	'u32_0x18' / Int16ub,
	'u32_0x1a' / Int16ub,
	'u32_0x1c' / Int16ub,
	'u32_0x1e' / Int16ub,
	'u32_0x10' / Int16ub,
	'u16_0x0e' / Int16ub,
	'u32_0x24' / Int32ub,
	'u32_0x28' / Int32ub,
	'u32_0x2c' / Int32ub,
	'u16_0x0a' / Int16ub,
)

glover_level__puzzle_action_0x46_0x47_0x48 = Struct(
	'u32_0x24' / Int32ub,
	'u16_0x0a' / Int16ub,
)

glover_level__plat_sound_0xc2 = Struct(
	'sound_id' / Int16ub,
	'volume' / Int16ub,
	'pitch' / Int16ub,
)

glover_level__plat_spin_pause_0x7c = Struct(
	'u16_0x0c' / Int16ub,
	'u16_0x0a' / Int16ub,
)

glover_level__plat_magnet_0x8b = Struct(
	'u16_0x0c' / Int16ub,
	'u32_0x48' / Int32ub,
	'u32_0x4c' / Int32ub,
	'u32_0x50' / Int32ub,
	'u32_0x10' / Int32ub,
	'u32_0x14' / Int32ub,
	'u32_0x18' / Int32ub,
	'u32_0x1c' / Int32ub,
)

glover_level__enemy_instruction_error = Struct(
)

glover_level__backdrop = Struct(
	'texture_id' / Int32ub,
	'decal_pos_x' / Int16ub,
	'decal_pos_y' / Int16ub,
	'sort_key' / Int16ub,
	'offset_y' / Int16sb,
	'scale_x' / Int16ub,
	'scale_y' / Int16ub,
	'flip_x' / Int16ub,
	'flip_y' / Int16ub,
	'scroll_speed_x' / Int16ub,
	'unused' / Int16ub,
	'decal_parent_idx' / Int16ub,
)

glover_level__diffuse_light = Struct(
	'r' / Int16ub,
	'g' / Int16ub,
	'b' / Int16ub,
	'theta_x' / Float32b,
	'theta_y' / Float32b,
)

glover_level__plat_path_acceleration = Struct(
	'acceleration' / Float32b,
)

glover_level__buzzer = Struct(
	'tag' / Int16ub,
	'platform_1_tag' / Int16ub,
	'platform_2_tag' / Int16ub,
	'draw_flags' / Int16ub,
	'r' / Int16ub,
	'g' / Int16ub,
	'b' / Int16ub,
	'color_jitter' / Int16ub,
	'end_1_x' / Float32b,
	'end_1_y' / Float32b,
	'end_1_z' / Float32b,
	'end_2_x' / Float32b,
	'end_2_y' / Float32b,
	'end_2_z' / Float32b,
	'draw_diameter' / Float32b,
	'draw_thickness' / Float32b,
)

glover_level__puzzle_any = Struct(
	'op' / Int16ub,
)

glover_level__set_actor_rotation = Struct(
	'x' / Float32b,
	'y' / Float32b,
	'z' / Float32b,
)

glover_level__cameo_inst = Struct(
	'inst_type' / Int16ub,
	'body' / Switch(this.inst_type, {0: LazyBound(lambda: glover_level__cameo_inst_0), 4: LazyBound(lambda: glover_level__cameo_inst_4), 6: LazyBound(lambda: glover_level__cameo_inst_6), 1: LazyBound(lambda: glover_level__cameo_inst_1), 3: LazyBound(lambda: glover_level__cameo_inst_3), 5: LazyBound(lambda: glover_level__cameo_inst_5), 2: LazyBound(lambda: glover_level__cameo_inst_2), }, default=LazyBound(lambda: glover_level__cameo_inst_default)),
)

glover_level__plat_turn_towards_path_point = Struct(
	'input_1' / Int32ub,
	'input_2' / Int32ub,
)

glover_level__plat_mvspn_0x5a = Struct(
	'u16_0x1c' / Int16ub,
	'u32_0x18' / Int32ub,
)

glover_level__plat_mvspn_0x74 = Struct(
	'u32_0x34' / Int32ub,
	'u32_0x38' / Int32ub,
	'u32_0x3c' / Int32ub,
)

glover_level__plat_orbit = Struct(
	'u16_120' / Int16ub,
	'u16_136' / Int16ub,
	'u16_134' / Int16ub,
	'u16_132' / Int16ub,
	'u32_116' / Int32ub,
	'name' / FixedSized(8, GreedyString(encoding='ASCII')),
	'f_112' / Float32b,
	'f_108' / Float32b,
	'f_104' / Float32b,
	'f_100' / Float32b,
	'f_96' / Float32b,
	'f_92' / Float32b,
	'f_88' / Float32b,
	'f_84' / Float32b,
	'f_80' / Float32b,
	'u32_176' / Int32ub,
)

glover_level__plat_spike = Struct(
)

glover_level__plat_special_0x8e = Struct(
	'enable' / Int16ub,
)

glover_level__plat_actor_surface_type = Struct(
	'value' / Int16ub,
)

glover_level__plat_0x9f = Struct(
	'u32_0x6c' / Int32ub,
	'u32_0x70' / Int32ub,
	'u32_0x1c' / Int32ub,
	'u32_0x28' / Int32ub,
)

glover_level__enemy_instruction_dash = Struct(
	'destination_x' / Float32b,
	'destination_y' / Float32b,
	'destination_z' / Float32b,
	'vel_magnitude' / Float32b,
)

glover_level__environmental_sound = Struct(
	'sound_id' / Int16ub,
	'volume' / Int16ub,
	'flags' / Int16ub,
	'h_0x06' / Int16ub,
	'h_0x08' / Int16ub,
	'h_0x0a' / Int16ub,
	'h_0x0c' / Int16ub,
	'h_0x0e' / Int16ub,
	'x' / Float32b,
	'y' / Float32b,
	'z' / Float32b,
	'radius' / Float32b,
)

glover_level__plat_set_initial_pos = Struct(
	'x' / Float32b,
	'y' / Float32b,
	'z' / Float32b,
)

glover_level__actor_0xbf = Struct(
	'mode' / Int16ub,
	'child_mesh_id' / Int32ub,
)

glover_level__plat_max_velocity = Struct(
	'velocity' / Float32b,
)

glover_level__enemy_finalize = Struct(
)

glover_level__plat_mvspn_0x59 = Struct(
	'u16_0x24' / Int16ub,
	'u32_0x20' / Int32ub,
	'u32_0x28' / Int32ub,
	'u32_0x2c' / Int32ub,
	'u32_0x30' / Int32ub,
)

glover_level__cameo = Struct(
)

glover_level__plat_constant_spin = Struct(
	'axis' / Int16ub,
	'initial_theta' / Float32b,
	'speed' / Float32b,
)

glover_level__vent_duty_cycle = Struct(
	'frames_off' / Int16sb,
	'frames_on' / Int16sb,
)

glover_level__plat_0xc3 = Struct(
	'u16_0x86' / Int16ub,
	'u32_0x78_0x80' / Int16ub,
	'u16_0x84' / Int16ub,
)

glover_level__end_level_data = Struct(
)

glover_level__set_object_sparkle = Struct(
	'period' / Int16ub,
)

glover_level__plat_fan_0x8a = Struct(
	'u16_0x0c' / Int16ub,
	'u32_0x48' / Int32ub,
	'u32_0x4c' / Int32ub,
	'u32_0x50' / Int32ub,
	'u32_0x10' / Int32ub,
	'u32_0x14' / Int32ub,
	'u32_0x18' / Int32ub,
	'u32_0x1c' / Int32ub,
)

glover_level__plat_spin_sound_0xc5 = Struct(
	'sound_id' / Int16ub,
	'volume' / Int16ub,
	'pitch' / Int16ub,
)

glover_level__puzzle_cond_c = Struct(
	'i_0x00' / Int32ub,
	'i_0x04' / Int32ub,
	'i_0x08' / Int32ub,
	'i_0x0c' / Int32ub,
	'i_0x10' / Int32ub,
	'i_0x14' / Int32ub,
)

glover_level__enemy_instruction_turn = Struct(
	'lookat_x' / Float32b,
	'lookat_y' / Float32b,
	'lookat_z' / Float32b,
	'choose_random_direction' / Int32ub,
)

glover_level__puzzle_action_0x4a = Struct(
	'u32_0x24' / Int32ub,
	'u32_0x24_0x0c' / Int32ub,
	'u16_0x0a' / Int16ub,
)

glover_level__enemy_conditional_instruction = Struct(
	'instr' / LazyBound(lambda: glover_level__enemy_instruction),
)

glover_level__plat_set_tag = Struct(
	'tag' / Int16ub,
)

glover_level__plat_copy_spin_from_parent = Struct(
)

glover_level__vent = Struct(
	'type' / Int16ub,
	'u16_0x0a' / Int16ub,
	'parent_tag' / Int16ub,
	'origin_x' / Float32b,
	'origin_y' / Float32b,
	'origin_z' / Float32b,
	'particle_velocity_x' / Float32b,
	'particle_velocity_y' / Float32b,
	'particle_velocity_z' / Float32b,
)

glover_level__puzzle_cond = Struct(
	'cond_type' / Int16ub,
	'body' / Switch(this.cond_type, {39: LazyBound(lambda: glover_level__puzzle_cond_c), 35: LazyBound(lambda: glover_level__puzzle_cond_c), 38: LazyBound(lambda: glover_level__puzzle_cond_d), 40: LazyBound(lambda: glover_level__puzzle_cond_d), 37: LazyBound(lambda: glover_level__puzzle_cond_c), 41: LazyBound(lambda: glover_level__puzzle_cond_e), 36: LazyBound(lambda: glover_level__puzzle_cond_d), 34: LazyBound(lambda: glover_level__puzzle_cond_b), }, default=LazyBound(lambda: glover_level__puzzle_cond_a)),
)

glover_level__plat_mvspn_0x73 = Struct(
	'u16_0x0c' / Int16ub,
	'u32_0x34' / Int32ub,
	'u32_0x38' / Int32ub,
	'u32_0x3c' / Int32ub,
)

glover_level__enemy_instruction_attack = Struct(
	'unused_1' / Int32ub,
	'unused_2' / Int32ub,
)

glover_level__enemy_instruction_rest = Struct(
	'flags' / Int32ub,
	'anim_start_playing' / Int32ub,
)

glover_level__look_at_ball_0x61 = Struct(
	'u32_0x6c' / Int32ub,
	'u32_0x1c' / Int32ub,
)

glover_level__look_at_hand_0x60 = Struct(
	'u32_0x6c' / Int32ub,
	'u32_0x1c' / Int32ub,
)

glover_level__cameo_inst_2 = Struct(
	'h_0x00' / Int16ub,
	'i_0x02' / Int32ub,
	'i_0x06' / Int32ub,
	'i_0x0a' / Int32ub,
	'i_0x0e' / Int32ub,
	'h_0x12' / Int16ub,
	'h_0x14' / Int16ub,
)

glover_level__unknown_0xa9 = Struct(
	'i_0x00' / Int32ub,
)

glover_level__plat_vent_advance_frames = Struct(
	'num_frames' / Int16ub,
)

glover_level__set_exit = Struct(
	'type' / Int16ub,
	'plat_flags' / Int16ub,
)

glover_level__plat_sound_0xc1 = Struct(
	'sound_id' / Int16ub,
	'volume' / Int16ub,
	'pitch' / Int16ub,
)

glover_level__plat_actor_enable_water_animation = Struct(
)

glover_level__enemy_instruction_c = Struct(
	'u32_0x02' / Int32ub,
	'u32_0x0e' / Int32ub,
)

glover_level__puzzle_and = Struct(
)

glover_level__plat_0x66 = Struct(
)

glover_level__plat_special_0xc7 = Struct(
	'u16_0x2a' / Int16ub,
	'u16_0x1c_and_0x24' / Int16ub,
	'u16_0x28' / Int16ub,
)

glover_level__null_platform = Struct(
)

glover_level__powerup = Struct(
	'type' / Int16ub,
	'u16_0x02' / Int16ub,
	'u16_0x04' / Int16ub,
	'x' / Float32b,
	'y' / Float32b,
	'z' / Float32b,
)

glover_level__platform_conveyor = Struct(
	'vel_x' / Float32b,
	'vel_y' / Float32b,
	'vel_z' / Float32b,
)

glover_level__set_teleport = Struct(
	'target_tag' / Int16ub,
	'u16_0x0c' / Int16ub,
	'u16_0x10' / Int16ub,
	'u16_0x12' / Int16ub,
	'u32_0x00' / Int32ub,
	'u32_0x04' / Int32ub,
	'u32_0x08' / Int32ub,
)

glover_level__puzzle_cond_d = Struct(
	'i_0x00' / Int32ub,
	'i_0x04' / Int32ub,
	'i_0x08' / Int32ub,
	'i_0x0c' / Int32ub,
)

glover_level__unknown_sound_0xbd = Struct(
	'h_0x00' / Int16ub,
	'h_0x02' / Int16ub,
	'h_0x04' / Int16ub,
)

glover_level__plat_checkpoint = Struct(
	'u16_0x17' / Int16ub,
	'theta' / Float32b,
)

glover_level__cameo_inst_4 = Struct(
	'h_0x00' / Int16ub,
	'h_0x02' / Int16ub,
	'h_0x04' / Int16ub,
	'h_0x06' / Int16ub,
	'h_0x08' / Int16ub,
)

glover_level__ball_spawn_point = Struct(
	'type' / Int16ub,
	'x' / Float32b,
	'y' / Float32b,
	'z' / Float32b,
)

glover_level__plat_set_parent = Struct(
	'tag' / Int16ub,
)

glover_level__puzzle_or = Struct(
)

glover_level__puzzle_action_0x56 = Struct(
	'u32_0x14' / Int32ub,
	'u32_0x18' / Int32ub,
	'u16_0x1c' / Int16ub,
	'u16_0x0a' / Int16ub,
)

glover_level__cmd = Struct(
	'type_code' / Int16ub,
	'params' / Switch(this.type_code, {120: LazyBound(lambda: glover_level__plat_0x78), 141: LazyBound(lambda: glover_level__rope), 93: LazyBound(lambda: glover_level__null_platform), 118: LazyBound(lambda: glover_level__plat_orbit_pause), 159: LazyBound(lambda: glover_level__plat_0x9f), 194: LazyBound(lambda: glover_level__plat_sound_0xc2), 184: LazyBound(lambda: glover_level__plat_special_0xb8), 105: LazyBound(lambda: glover_level__plat_cat_0x69), 142: LazyBound(lambda: glover_level__plat_special_0x8e), 112: LazyBound(lambda: glover_level__plat_rocking), 163: LazyBound(lambda: glover_level__vent_duty_cycle), 131: LazyBound(lambda: glover_level__enemy), 167: LazyBound(lambda: glover_level__plat_pos_0xa7), 146: LazyBound(lambda: glover_level__land_actor), 4: LazyBound(lambda: glover_level__puzzle), 169: LazyBound(lambda: glover_level__unknown_0xa9), 162: LazyBound(lambda: glover_level__vent), 116: LazyBound(lambda: glover_level__plat_mvspn_0x74), 119: LazyBound(lambda: glover_level__plat_orbit_flip_0x77), 6: LazyBound(lambda: glover_level__puzzle_or), 7: LazyBound(lambda: glover_level__puzzle_numtimes), 113: LazyBound(lambda: glover_level__plat_set_parent), 121: LazyBound(lambda: glover_level__plat_scale), 96: LazyBound(lambda: glover_level__look_at_hand_0x60), 191: LazyBound(lambda: glover_level__actor_0xbf), 1: LazyBound(lambda: glover_level__glover_spawn_point), 150: LazyBound(lambda: glover_level__puzzle_action), 97: LazyBound(lambda: glover_level__look_at_ball_0x61), 106: LazyBound(lambda: glover_level__plat_actor_surface_type), 145: LazyBound(lambda: glover_level__background_actor), 101: LazyBound(lambda: glover_level__plat_destructible), 144: LazyBound(lambda: glover_level__plat_sine), 127: LazyBound(lambda: glover_level__plat_constant_spin), 100: LazyBound(lambda: glover_level__plat_no_clip), 149: LazyBound(lambda: glover_level__puzzle_cond), 115: LazyBound(lambda: glover_level__plat_mvspn_0x73), 91: LazyBound(lambda: glover_level__plat_push_0x5b), 107: LazyBound(lambda: glover_level__plat_path_point), 143: LazyBound(lambda: glover_level__plat_orbit), 89: LazyBound(lambda: glover_level__plat_mvspn_0x59), 104: LazyBound(lambda: glover_level__platform_conveyor), 98: LazyBound(lambda: glover_level__platform), 197: LazyBound(lambda: glover_level__plat_spin_sound_0xc5), 95: LazyBound(lambda: glover_level__plat_go_forwards_0x5f), 137: LazyBound(lambda: glover_level__set_teleport), 88: LazyBound(lambda: glover_level__plat_mvspn_0x58), 161: LazyBound(lambda: glover_level__enemy_set_attention_bbox), 138: LazyBound(lambda: glover_level__plat_fan_0x8a), 3: LazyBound(lambda: glover_level__camera_spawn_point), 192: LazyBound(lambda: glover_level__plat_play_object_animation), 126: LazyBound(lambda: glover_level__plat_0x7e), 165: LazyBound(lambda: glover_level__fog_configuration), 5: LazyBound(lambda: glover_level__puzzle_and), 103: LazyBound(lambda: glover_level__plat_crumb_0x67), 99: LazyBound(lambda: glover_level__plat_checkpoint), 185: LazyBound(lambda: glover_level__plat_special_0xb9), 180: LazyBound(lambda: glover_level__set_object_sparkle), 156: LazyBound(lambda: glover_level__enemy_attack_instruction), 125: LazyBound(lambda: glover_level__plat_spin_flip), 186: LazyBound(lambda: glover_level__enemy_0xba), 188: LazyBound(lambda: glover_level__animated_background_actor), 153: LazyBound(lambda: glover_level__backdrop), 123: LazyBound(lambda: glover_level__plat_copy_spin_from_parent), 160: LazyBound(lambda: glover_level__water), 8: LazyBound(lambda: glover_level__puzzle_any), 166: LazyBound(lambda: glover_level__plat_set_initial_pos), 114: LazyBound(lambda: glover_level__plat_conf_0x72), 181: LazyBound(lambda: glover_level__buzzer), 148: LazyBound(lambda: glover_level__set_actor_scale), 158: LazyBound(lambda: glover_level__plat_special_0x9e), 117: LazyBound(lambda: glover_level__plat_orbit_around_point), 152: LazyBound(lambda: glover_level__ambient_light), 94: LazyBound(lambda: glover_level__plat_turn_towards_path_point), 109: LazyBound(lambda: glover_level__plat_path_acceleration), 32000: LazyBound(lambda: glover_level__end_level_data), 140: LazyBound(lambda: glover_level__wind), 122: LazyBound(lambda: glover_level__plat_str_0x7a), 179: LazyBound(lambda: glover_level__plat_actor_enable_water_animation), 195: LazyBound(lambda: glover_level__plat_0xc3), 130: LazyBound(lambda: glover_level__plat_spike), 187: LazyBound(lambda: glover_level__mr_tip), 170: LazyBound(lambda: glover_level__cameo), 199: LazyBound(lambda: glover_level__plat_special_0xc7), 164: LazyBound(lambda: glover_level__plat_0xa4), 182: LazyBound(lambda: glover_level__buzzer_duty_cycle), 108: LazyBound(lambda: glover_level__plat_max_velocity), 189: LazyBound(lambda: glover_level__unknown_sound_0xbd), 168: LazyBound(lambda: glover_level__set_exit), 171: LazyBound(lambda: glover_level__cameo_inst), 193: LazyBound(lambda: glover_level__plat_sound_0xc1), 133: LazyBound(lambda: glover_level__garib_group), 129: LazyBound(lambda: glover_level__plat_topple_0x81), 151: LazyBound(lambda: glover_level__diffuse_light), 157: LazyBound(lambda: glover_level__plat_0x9d), 147: LazyBound(lambda: glover_level__set_actor_rotation), 134: LazyBound(lambda: glover_level__garib), 102: LazyBound(lambda: glover_level__plat_0x66), 110: LazyBound(lambda: glover_level__plat_special_0x6e), 139: LazyBound(lambda: glover_level__plat_magnet_0x8b), 155: LazyBound(lambda: glover_level__enemy_conditional_instruction), 2: LazyBound(lambda: glover_level__ball_spawn_point), 135: LazyBound(lambda: glover_level__powerup), 124: LazyBound(lambda: glover_level__plat_spin_pause_0x7c), 200: LazyBound(lambda: glover_level__plat_destructible_sound), 132: LazyBound(lambda: glover_level__enemy_finalize), 92: LazyBound(lambda: glover_level__plat_vent_advance_frames), 198: LazyBound(lambda: glover_level__plat_0xc6), 111: LazyBound(lambda: glover_level__plat_set_tag), 190: LazyBound(lambda: glover_level__environmental_sound), 196: LazyBound(lambda: glover_level__plat_orbit_sound_0xc4), 183: LazyBound(lambda: glover_level__set_global_0xb7), 128: LazyBound(lambda: glover_level__plat_spin_0x80), 90: LazyBound(lambda: glover_level__plat_mvspn_0x5a), 154: LazyBound(lambda: glover_level__enemy_normal_instruction), }, default=LazyBound(lambda: glover_level__unrecognized)),
)

glover_level__plat_0xc6 = Struct(
	'u16_0x4a' / Int16ub,
	'u16_0x44' / Int16ub,
	'u16_0x48' / Int16ub,
)

glover_level__wind = Struct(
	'left' / Float32b,
	'top' / Float32b,
	'front' / Float32b,
	'width' / Float32b,
	'height' / Float32b,
	'depth' / Float32b,
	'vel_x' / Float32b,
	'vel_y' / Float32b,
	'vel_z' / Float32b,
	'turbulence' / Float32b,
	'unknown_0x2c' / Int32ub,
	'active' / Int32ub,
	'tag' / Int32ub,
)

glover_level__puzzle = Struct(
)

glover_level__plat_push_0x5b = Struct(
	'flags' / Int16ub,
	'u32_0x04' / Int32ub,
	'actor_f_0x70' / Float32b,
	'u32_0x1c' / Int32ub,
)

glover_level__plat_mvspn_0x58 = Struct(
	'u16_0x14' / Int16ub,
	'u32_0x10' / Int32ub,
)

glover_level__plat_destructible = Struct(
	'flags' / Int16ub,
	'num_fragments' / Int32ub,
	'fragment_object_id' / Int32ub,
	'name' / FixedSized(8, GreedyString(encoding='ASCII')),
)

glover_level__puzzle_action = Struct(
	'action_type' / Int16ub,
	'body' / Switch(this.action_type, {61: LazyBound(lambda: glover_level__puzzle_action_0x35_0x3b_0x3c_0x3d_0x3e_0x3f_0x40), 73: LazyBound(lambda: glover_level__puzzle_action_0x49_0x4d), 60: LazyBound(lambda: glover_level__puzzle_action_0x35_0x3b_0x3c_0x3d_0x3e_0x3f_0x40), 62: LazyBound(lambda: glover_level__puzzle_action_0x35_0x3b_0x3c_0x3d_0x3e_0x3f_0x40), 77: LazyBound(lambda: glover_level__puzzle_action_0x49_0x4d), 85: LazyBound(lambda: glover_level__puzzle_action_0x55), 59: LazyBound(lambda: glover_level__puzzle_action_0x35_0x3b_0x3c_0x3d_0x3e_0x3f_0x40), 86: LazyBound(lambda: glover_level__puzzle_action_0x56), 84: LazyBound(lambda: glover_level__puzzle_action_0x54), 63: LazyBound(lambda: glover_level__puzzle_action_0x35_0x3b_0x3c_0x3d_0x3e_0x3f_0x40), 53: LazyBound(lambda: glover_level__puzzle_action_0x35_0x3b_0x3c_0x3d_0x3e_0x3f_0x40), 64: LazyBound(lambda: glover_level__puzzle_action_0x35_0x3b_0x3c_0x3d_0x3e_0x3f_0x40), 76: LazyBound(lambda: glover_level__puzzle_action_0x4b_0x4c), 79: LazyBound(lambda: glover_level__puzzle_action_0x4f), 72: LazyBound(lambda: glover_level__puzzle_action_0x46_0x47_0x48), 71: LazyBound(lambda: glover_level__puzzle_action_0x46_0x47_0x48), 70: LazyBound(lambda: glover_level__puzzle_action_0x46_0x47_0x48), 74: LazyBound(lambda: glover_level__puzzle_action_0x4a), 75: LazyBound(lambda: glover_level__puzzle_action_0x4b_0x4c), }, default=LazyBound(lambda: glover_level__puzzle_action_default)),
)

glover_level__water = Struct(
	'left' / Float32b,
	'top' / Float32b,
	'front' / Float32b,
	'width' / Float32b,
	'bottom' / Float32b,
	'depth' / Float32b,
	'surface_y' / Float32b,
	'current_x' / Float32b,
	'current_z' / Float32b,
	'unknown_1' / Int16ub,
	'object_id' / Int32ub,
	'name' / FixedSized(8, GreedyString(encoding='ASCII')),
	'x' / Float32b,
	'y' / Float32b,
	'z' / Float32b,
)

glover_level__puzzle_action_0x4f = Struct(
	'u32_0x14' / Int32ub,
	'u32_0x18' / Int32ub,
	'u32_0x10' / Int32ub,
	'u16_0x0e' / Int16ub,
	'u16_0x0a' / Int16ub,
	'u32_0x20' / Int32ub,
)

glover_level__unrecognized = Struct(
)

glover_level__plat_no_clip = Struct(
)

glover_level__plat_scale = Struct(
	'x' / Float32b,
	'y' / Float32b,
	'z' / Float32b,
)

glover_level__puzzle_action_0x4b_0x4c = Struct(
	'u16_0x0a' / Int16ub,
)

glover_level__set_actor_scale = Struct(
	'x' / Float32b,
	'y' / Float32b,
	'z' / Float32b,
)

glover_level__plat_special_0xb8 = Struct(
)

glover_level__plat_orbit_sound_0xc4 = Struct(
	'u16_0x3a' / Int16ub,
	'u16_0x2c_and_0x34' / Int16ub,
	'u16_0x38' / Int16ub,
)

glover_level__plat_orbit_flip_0x77 = Struct(
	'u16_0x08' / Int16ub,
	'u16_0x10' / Int16ub,
)

glover_level__plat_destructible_sound = Struct(
	'sound_id' / Int16ub,
	'volume' / Int16ub,
	'pitch' / Int16ub,
)

glover_level__ambient_light = Struct(
	'r' / Int16ub,
	'g' / Int16ub,
	'b' / Int16ub,
)

def glover_level__enemy__enemy_type(subcon):
	return Enum(subcon,
		bovva=7,
		cannon=8,
		samtex=9,
		mallet=10,
		generalw=11,
		lionfish=12,
		chester=13,
		keg=14,
		reggie=15,
		swish=16,
		thrice=17,
		robes=18,
		fumble=19,
		mike=20,
		raptor=21,
		crumpet=22,
		tracey=23,
		yoofow=24,
		opec=25,
		cymon=26,
		sucker=27,
		bugle=28,
		dennis=29,
		chuck=30,
		hubchicken1=31,
		frankie2=32,
		kloset=33,
		willy=34,
		joff=35,
		cancer=36,
		kirk=37,
		robot=38,
		evilrobot=39,
		spank=40,
		babyspk2=41,
		evilglove=42,
		dibber=43,
		brundle=44,
		malcom=45,
		spotty=46,
		gordon=47,
		sidney=48,
		weevil=49,
		chopstik=50,
		butterfly=51,
		spider=52,
		bat=53,
		frog=54,
		dragfly=55,
		boxthing=56,
		bug=57,
		nmefrog=58,
	)

glover_level__enemy = Struct(
	'type' / glover_level__enemy__enemy_type(Int16ub),
	'u1' / Int16ub,
	'x' / Float32b,
	'y' / Float32b,
	'z' / Float32b,
	'y_rotation' / Float32b,
)

glover_level__plat_0xa4 = Struct(
)

glover_level__plat_orbit_pause = Struct(
	'num_frames' / Int16ub,
	'num_pauses' / Int16ub,
)

glover_level__plat_crumb_0x67 = Struct(
	'u16_0x02' / Int16ub,
	'u16_0x04' / Int16ub,
	'u16_0x08' / Int32ub,
)

glover_level__puzzle_action_default = Struct(
	'u32_0x10' / Int32ub,
	'u16_0x0e' / Int16ub,
	'u16_0x0a' / Int16ub,
	'u32_0x20' / Int32ub,
)

glover_level__garib = Struct(
	'x' / Float32b,
	'y' / Float32b,
	'z' / Float32b,
	'type' / Int16ub,
	'dynamic_shadow' / Int16ub,
)

glover_level__garib_group = Struct(
	'group_id' / Int16ub,
	'initial_state' / Int16sb,
)

glover_level__cameo_inst_6 = Struct(
	'h_0x00' / Int16ub,
	'h_0x02' / Int16ub,
	'h_0x04' / Int16ub,
	'h_0x06' / Int16ub,
)

glover_level__animated_background_actor = Struct(
	'object_id' / Int32ub,
	'name' / FixedSized(8, GreedyString(encoding='ASCII')),
	'x' / Float32b,
	'y' / Float32b,
	'z' / Float32b,
)

glover_level__background_actor = Struct(
	'object_id' / Int32ub,
	'name' / FixedSized(8, GreedyString(encoding='ASCII')),
	'x' / Float32b,
	'y' / Float32b,
	'z' / Float32b,
)

glover_level__enemy_instruction_move = Struct(
	'destination_x' / Float32b,
	'destination_y' / Float32b,
	'destination_z' / Float32b,
	'vel_magnitude' / Float32b,
)

glover_level__plat_path_point = Struct(
	'duration' / Int16sb,
	'x' / Float32b,
	'y' / Float32b,
	'z' / Float32b,
)

glover_level__plat_0x78 = Struct(
	'u16_0x08' / Int16ub,
)

glover_level__enemy_0xba = Struct(
)

glover_level__puzzle_cond_a = Struct(
	'u32_0x24' / Int16ub,
	'u16_0x0a' / Int16ub,
)

glover_level__plat_sine = Struct(
	'u32_count' / Int32ub,
	'u32_116' / Int32ub,
	'name' / FixedSized(8, GreedyString(encoding='ASCII')),
	'f_108' / Float32b,
	'f_104' / Float32b,
	'f_100' / Float32b,
	'f_96' / Float32b,
	'f_92' / Float32b,
	'f_88' / Float32b,
	'f_84' / Float32b,
	'f_80' / Float32b,
	'u32_176' / Int32ub,
	'u32_172' / Int32ub,
)

glover_level__plat_cat_0x69 = Struct(
	'u16_0x20' / Int16ub,
	'u32_0x00' / Int32ub,
	'u32_0x04' / Int32ub,
	'u32_0x08' / Int32ub,
	'u32_0x0c' / Int32ub,
	'u32_0x10' / Int32ub,
	'u32_0x1c' / Int32ub,
)

glover_level__puzzle_numtimes = Struct(
	'n' / Int16ub,
)

glover_level__plat_spin_0x80 = Struct(
	'idx' / Int16ub,
	'f_0x1c' / Float32b,
	'u32_0x28' / Int32ub,
	'u32_ustack56' / Int32ub,
	'u32_0x2c' / Int32ub,
	'f_0x6c' / Float32b,
	'f_0x70' / Int16ub,
)

glover_level__plat_rocking = Struct(
	'axis' / Int16ub,
	'theta' / Float32b,
	'deceleration' / Float32b,
	'blur_height' / Float32b,
	'frame_advance' / Int16ub,
)

glover_level__plat_0x7e = Struct(
	'u32_0x28' / Int32ub,
)

glover_level__glover_spawn_point = Struct(
	'x' / Float32b,
	'y' / Float32b,
	'z' / Float32b,
)

glover_level__cameo_inst_1 = Struct(
	'h_0x00' / Int16ub,
	'i_0x02' / Int32ub,
	'i_0x06' / Int32ub,
	'i_0x0a' / Int32ub,
	'h_0x0e' / Int16ub,
	'h_0x10' / Int16ub,
)

glover_level__plat_0x9d = Struct(
)

glover_level__enemy_normal_instruction = Struct(
	'instr' / LazyBound(lambda: glover_level__enemy_instruction),
)

glover_level__fog_configuration = Struct(
	'fog_enabled' / Int8ub,
	'r' / Int8ub,
	'g' / Int8ub,
	'b' / Int8ub,
	'fog_distance' / Int16ub,
	'near_clip' / Int16ub,
)

glover_level__buzzer_duty_cycle = Struct(
	'frames_off' / Int16ub,
	'frames_on' / Int16ub,
)

glover_level__cameo_inst_5 = Struct(
	'h_0x00' / Int16ub,
	'h_0x02' / Int16ub,
	'h_0x04' / Int16ub,
)

glover_level__plat_play_object_animation = Struct(
)

glover_level__plat_topple_0x81 = Struct(
	'idx' / Int16ub,
	'f_0x1c' / Float32b,
	'f_0x28' / Float32b,
	'f_0x24' / Float32b,
	'f_0x2c' / Float32b,
	'f_0x6c' / Float32b,
	'f_0x70_pivot_height' / Float32b,
	'u16_0x10' / Int16ub,
)

glover_level__enemy_instruction_play_animation = Struct(
	'anim_idx_1' / Int32sb,
	'anim_idx_2' / Int32sb,
)

glover_level__enemy_instruction_random_walk = Struct(
	'home_x' / Float32b,
	'home_y' / Float32b,
	'home_z' / Float32b,
	'extent_x' / Float32b,
	'extent_y' / Float32b,
	'extent_z' / Float32b,
	'min_travel_distance' / Float32b,
)

glover_level__puzzle_action_0x55 = Struct(
	'u32_0x24' / Int32ub,
	'u16_0x0a' / Int16ub,
)

glover_level__cameo_inst_3 = Struct(
	'h_0x00' / Int16ub,
	'i_0x02' / Int32ub,
	'h_0x06' / Int16ub,
	'h_0x08' / Int16ub,
)

glover_level__plat_go_forwards_0x5f = Struct(
	'u32_0x2c_0x6c' / Int32ub,
	'u32_0x2c_0x1c' / Int32ub,
	'u32_0xf0' / Int32ub,
	'u32_0x2c_0x34' / Int32ub,
)

glover_level__plat_special_0x9e = Struct(
	'u32_0x5c' / Int32ub,
	'u32_0x60' / Int32ub,
	'u32_0x65' / Int32ub,
	'u32_0x68' / Int32ub,
)

def glover_level__enemy_instruction__execution_condition_type(subcon):
	return Enum(subcon,
		ball_within_range=0,
		ball_within_ground_range=1,
		glover_within_range=2,
		glover_within_ground_range=3,
		ball_or_glover_within_range=4,
		ball_or_glover_within_ground_range=5,
		ball_within_angle_of_view=6,
		glover_within_angle_of_view=7,
		ball_or_glover_within_angle_of_view=8,
		periodic=9,
		roll_angle_within_range_and_periodic=10,
		glover_holding_ball=11,
		glover_not_holding_ball=12,
		enemy_holding_ball=13,
		enemy_not_holding_ball=14,
		glover_holding_enemy=15,
		glover_not_holding_enemy=16,
		on_ball=17,
		on_glover=18,
		enemy_within_attention_bbox=19,
		always=20,
		never=21,
		random_chance_param_a_over_1000=22,
	)

def glover_level__enemy_instruction__instruction_flags(subcon):
	return Enum(subcon,
		face_player=1048576,
		face_ball=2097152,
		face_closer_of_player_or_ball=4194304,
	)

glover_level__enemy_instruction = Struct(
	'instr_type' / Int16ub,
	'lifetime' / Int16sb,
	'params' / Switch(this.instr_type, {14: LazyBound(lambda: glover_level__enemy_instruction_c), 10: LazyBound(lambda: glover_level__enemy_instruction_a), 17: LazyBound(lambda: glover_level__enemy_instruction_c), 0: LazyBound(lambda: glover_level__enemy_instruction_move), 4: LazyBound(lambda: glover_level__enemy_instruction_rest), 24: LazyBound(lambda: glover_level__enemy_instruction_c), 6: LazyBound(lambda: glover_level__enemy_instruction_c), 20: LazyBound(lambda: glover_level__enemy_instruction_c), 7: LazyBound(lambda: glover_level__enemy_instruction_play_animation), 1: LazyBound(lambda: glover_level__enemy_instruction_dash), 13: LazyBound(lambda: glover_level__enemy_instruction_a), 11: LazyBound(lambda: glover_level__enemy_instruction_a), 12: LazyBound(lambda: glover_level__enemy_instruction_c), 3: LazyBound(lambda: glover_level__enemy_instruction_random_walk), 5: LazyBound(lambda: glover_level__enemy_instruction_c), 19: LazyBound(lambda: glover_level__enemy_instruction_c), 23: LazyBound(lambda: glover_level__enemy_instruction_a), 15: LazyBound(lambda: glover_level__enemy_instruction_attack), 8: LazyBound(lambda: glover_level__enemy_instruction_c), 9: LazyBound(lambda: glover_level__enemy_instruction_a), 21: LazyBound(lambda: glover_level__enemy_instruction_c), 16: LazyBound(lambda: glover_level__enemy_instruction_c), 18: LazyBound(lambda: glover_level__enemy_instruction_goto), 2: LazyBound(lambda: glover_level__enemy_instruction_turn), 22: LazyBound(lambda: glover_level__enemy_instruction_a), }, default=LazyBound(lambda: glover_level__enemy_instruction_error)),
	'execution_condition_param_a' / Float32b,
	'execution_condition_param_b' / Float32b,
	'flags' / glover_level__enemy_instruction__instruction_flags(Int32ub),
	'execution_condition' / glover_level__enemy_instruction__execution_condition_type(Int16ub),
)

glover_level__set_global_0xb7 = Struct(
	'value' / Int32ub,
)

glover_level__plat_conf_0x72 = Struct(
	'u32_0x00' / Int32ub,
	'u32_0x04' / Int32ub,
	'u32_0x08' / Int32ub,
	'u32_0x0c' / Int32ub,
	'u32_0x10' / Int32ub,
	'u32_0x14' / Int32ub,
)

glover_level__puzzle_cond_e = Struct(
	'i_0x00' / Int32ub,
	'i_0x04' / Int32ub,
	'i_0x08' / Int32ub,
	'i_0x0c' / Int32ub,
	'i_0x10' / Int32ub,
)

glover_level__platform = Struct(
	'object_id' / Int32ub,
	'name' / FixedSized(8, GreedyString(encoding='ASCII')),
)

glover_level__plat_pos_0xa7 = Struct(
	'u8_idx' / Int16ub,
)

glover_level__plat_special_0x6e = Struct(
	'flags' / Int16ub,
	'u32_0x70' / Int32ub,
)

glover_level__cameo_inst_default = Struct(
	'h_0x00' / Int16ub,
	'h_0x02' / Int16ub,
)

glover_level__puzzle_action_0x35_0x3b_0x3c_0x3d_0x3e_0x3f_0x40 = Struct(
	'u32_0x14' / Int32ub,
	'u32_0x18' / Int32ub,
	'u32_0x1c' / Int32ub,
	'u32_0x10' / Int32ub,
	'u16_0x0e' / Int16ub,
	'u16_0x0a' / Int16ub,
	'u32_0x20' / Int32ub,
)

glover_level__plat_orbit_around_point = Struct(
	'axis' / Int16ub,
	'x' / Float32b,
	'y' / Float32b,
	'z' / Float32b,
	'speed' / Float32b,
)

glover_level__rope = Struct(
	'num_components' / Int32ub,
	'wiggle_axis' / Int16ub,
	'component_obj_id' / Int32ub,
	'name' / FixedSized(8, GreedyString(encoding='ASCII')),
	'puzzle_unknown_1' / Float32b,
	'sway_unknown_1' / Float32b,
	'sway_unknown_2' / Float32b,
	'sway_unknown_3' / Float32b,
	'sway_rocking_theta' / Int32ub,
	'sway_unknown_4' / Int32ub,
	'sway_unknown_5' / Float32b,
	'x' / Float32b,
	'y' / Float32b,
	'z' / Float32b,
	'component_w' / Float32b,
	'component_h' / Float32b,
	'component_d' / Float32b,
)

glover_level__puzzle_cond_b = Struct(
	'i_0x00' / Int32ub,
	'i_0x04' / Int32ub,
	'i_0x08' / Int32ub,
	'i_0x0c' / Int32ub,
	'i_0x10' / Int32ub,
	'i_0x14' / Int32ub,
	'i_0x18' / Int32ub,
)

glover_level__plat_str_0x7a = Struct(
	'u32_0x0c' / Int32ub,
	'u32_0x10' / Int32ub,
	'u32_0x14' / Int32ub,
	'u16_0x18' / Int16ub,
	'u16_0x1c' / Int16ub,
)

glover_level__enemy_instruction_goto = Struct(
	'instr_idx' / Int32ub,
	'unused' / Int32ub,
)

glover_level__enemy_instruction_a = Struct(
	'u32_0x02' / Int32ub,
	'u32_0x06' / Int32ub,
	'u32_0x0a' / Int32ub,
	'u32_0x0e' / Int32ub,
)

glover_level__plat_special_0xb9 = Struct(
)

glover_level__enemy_attack_instruction = Struct(
	'instr' / LazyBound(lambda: glover_level__enemy_instruction),
)

glover_level__land_actor = Struct(
	'object_id' / Int32ub,
	'name' / FixedSized(8, GreedyString(encoding='ASCII')),
	'x' / Float32b,
	'y' / Float32b,
	'z' / Float32b,
)

glover_level__mr_tip = Struct(
	'x' / Float32b,
	'y' / Float32b,
	'z' / Float32b,
	'message_id' / Int16ub,
)

glover_level__puzzle_action_0x49_0x4d = Struct(
	'u32_0x24' / Int32ub,
	'u32_0x28' / Int32ub,
	'u32_0x2c' / Int32ub,
	'u16_0x0a' / Int16ub,
)

glover_level__cameo_inst_0 = Struct(
	'h_0x00' / Int16ub,
	'h_0x02' / Int16ub,
	'h_0x04' / Int16ub,
	'i_0x06' / Int32ub,
	'h_0x0a' / Int16ub,
	'h_0x0c' / Int16ub,
)

glover_level__camera_spawn_point = Struct(
	'x' / Float32b,
	'y' / Float32b,
	'z' / Float32b,
	'pitch' / Float32b,
	'yaw' / Float32b,
)

glover_level__plat_spin_flip = Struct(
	'cooldown_timer' / Int16ub,
	'theta' / Float32b,
)

glover_level__enemy_set_attention_bbox = Struct(
	'left' / Float32b,
	'top' / Float32b,
	'front' / Float32b,
	'width' / Float32b,
	'height' / Float32b,
	'depth' / Float32b,
)

glover_level = Struct(
	'length' / Int32ub,
	'name' / NullTerminated(GreedyString(encoding='ASCII'), term=b'\x00', include=False, consume=True),
	'body' / GreedyRange(LazyBound(lambda: glover_level__cmd)),
)

_schema = glover_level

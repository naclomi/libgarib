# Glover landscape format

## Introduction

Landscape files effectively specify a single Glover level. In the vanilla
game, all landscapes are stored in one contiguous array. The game engine
identifies a level by its index in this array, and for the rest of this
documentation we'll refer to that index as the **level ID**.

A landscape file includes the following information:
- A level name, which goes unused except for debugging output
- The position and layout of _everything_ in the level's 3D space (terrain,
  collectibles, enemies, level exits/loading zones, positional sound sources,
  etc.)
- Atmospheric settings (lighting, fog, backdrops)
- Scripts to govern puzzles and interactive level elements
- Per-enemy AI scripts
- Cutscene scripts
- Level exit destination (TODO, confirm if this is true)

Notably, this does _not_ include the following:
- Actual graphical and collision data (meshes, animations and textures)
    - This is all stored in the _object data_ being referenced by the
      landscape layout. That data is in the game's object banks.
- Mr. Tip message text
- Which object banks and texture banks need to be loaded for the landscape to
  function
- Which background music track should be playing

Also notably, most levels have some special-case logic hardcoded into the game
engine that is triggered based solely on the active level ID. This behavior
can't be modified or disabled without patching the game code itself.

The rest of this document is divided into these sections:
1. **Landscape Components**: A description of what the building blocks of a
   level are, and how they interact.
2. **File Format**: The details of how those building blocks are *specified*
   in a landscape file.
3. **Special Cases**: Level-ID-dependent engine behaviors

## Landscape Components

Glover levels are built out of a small handful of different building blocks.
Where possible this document refers to these components by their official
names recovered from symbols left in the game engine, though in many cases
these names can be counter-intuitive.

### Terrain

The most _concrete_ building blocks are "actors" and "platforms":

- **Land actors**: Collidable objects at fixed locations in 3D space. Does not
  support object (skeletal) animation. Cannot be altered by puzzles or player
  interaction. Most of the level's landmass are actually "land actors".
- **Background actors**: Non-collidable objects at fixed locations in 3D
  space. **Can** play object (skeletal) animations. Cannot be altered by
  puzzles or player interaction. Used for decorative elements like the gushing
  water spouts in Atlantis.
- **Platforms**: Collidable objects at _changing_ locations in 3D space. Does
  not support object (skeletal) animation. **Can** be altered by puzzles and
  player interaction. Almost all parts of the level that physically move,
  aside from enemies and particle effects, are platforms. This includes
  buttons, breakable blocks, doors, checkpoints, exits and loading zones.

[TODO: double-check skeletal animation details for all of the above. Exit cones rotate using skeletal animation, and those are platforms]

These components are all placed in the level by specifying an _object ID_ and
a _location_. The object ID refers to an object in one of the loaded object
banks, which contains some combination of display meshes, collision meshes,
F3DEX display lists, and skeletal animations. _Any_ object can be used for
_any_ of the above component types; if the water spouts in Atlantis 1 were
changed from background actors to land actors without any changes to the
underlying object, you would be able to hop around on them.


### Physical Volumes

There are also a couple of components that define **volumes** in 3D space
which alter game physics:

- **Water**: Defines an axis-aligned rectangular column of water in 3D space.
  This column has a surface level on the Y axis and an extent on the XZ plane.
  Although landscapes can specify a "bottom" plane for the water volume, the
  game **ignores this value** and extends the water [TODO: infinitely down or
  just to the lowest collidable mesh in the column?].

  Any regions of the water volume that don't have a collidable land actor or
  platform beneath them are considered _outside_ of the water volume and just
  empty space. This is the **only way** to specify non-rectangular volumes of
  water. This is how, for example, the jagged edge waterfall in Atlantis 1 is
  implemented.

  Each water volume has an implicit background actor associated with it that
  renders the water's "surface", though this actor does not have to correspond
  with the actual volume in any way and does not affect game physics at all.
  
- **Wind**: Defines an axis-aligned rectangular volume of 3D space inside of
  which a "wind current" that can move Glover and the ball. The velocity of
  the wind can be specified independently for each axis. Wind volumes are
  actually invisible, but are often paired with a "vent" (particle emitter) to
  visually represent their presence.

### Miscellaneous terrain elements

- **Vents** (particle emitters): Vents specify a position in 3D space from
  which particles are emitted. There are a very wide variety of particle
  types, ranging from purely aesthetic (eg. bubbles in a pool of water) to
  collidable obstacles (eg. the tumbling boulders in Prehistoric 1 and 2).
  Vents can be turned on and off dynamically or be given a periodic duty
  cycle. A given vent can only emit a single particle type, and that type
  fully specifies the particles' appearance and behavior.
- **Mr. Tip**: An instance of Mr. Tip, specified by a 3D location and a
  message ID.
- **Environmental sounds**: A point in 3D space from which a specific sound
  effect is played. As the player move closer to the sound's origin, it gets
  louder.
- **Backgrounds**: TODO

### Collectibles

### Enemies

### Misc

<!-- 
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
 -->



## File Format

### Overview

Landscape files take the form of a linear stream of commands that instruct the
engine to load and configure various game structures in memory. This stream
is read and executed from start to finish without any jumps or branches. That
said, because the level loading code is stateful, in some cases the order of
these commands does matter.

In all cases, the endianness of the data in a landscape file match the
endianness of the host system. For the N64 game, this is big-endian. For the
PC CD-ROM game, this is little-endian [^1].

Before the command stream, the level begins with a simple header:
- A uint32 indicating the length of the level file in bytes (TODO: what is inclusive)
- A null-terminated string containing the level name

After the header comes the command stream. Each command begins with a unique
two-byte opcode. __Most__ commands are fixed-length, with a few complex and
unfortunate exceptions.

The stream ends with the "end" command, after which the level loader will stop
reading the file and begin playing the level. Because the overall file length
is specified in the header, it is possible to store arbitrary data between
the "end" command and the actual end-of-file, although the vanilla game does
not do this.

## Libgarib tools



## Special cases



[^1] Much of what was learned about this format initially came from a differential analysis of the same level data across these two game editions, which facilitated the identification of word boundaries.

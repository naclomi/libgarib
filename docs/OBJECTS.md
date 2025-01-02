# Glover object format

## Introduction
Glover "object" assets consist of 3D models and (optionally) their associated animations. All 3D models that appear in the game are stored as an object, whether it's the terrain for a level, a piece of rock rubble from a smashable wall, the vertical "Glover" text in the main menu, or Glover himself. These objects do not have any innate behaviors or interactive properties associated with them -- the object used for a smashable box could just as easily be swapped with the object used for a dinosaur enemy. 3D models and animations are the _only_ data stored here.

The rest of this document describes how objects are stored and used in-game, as well as how libgarib's tools translate these objects to/from GlTF files for editing. Binary formats are described as C structures that are assumed to be big-endian unless stated otherwise.

## Object banks

Objects are inherently grouped into object banks, rather than standalone files. These banks are loaded and unloaded automatically by the game engine depending on which active level or menu screen is selected. 

The game then uses specifc objects by referring to them with their unique 32-bit ID numbers, which are used very similarly to filenames. When a level references an object ID, the game will load it by linearly searching every ID in every loaded object bank for a match.

Object banks start with a "directory" listing all objects in the bank and their byte offsets. The directory ends when a record of all null bytes is encountered.

```c

struct {
    uint32_t object_id;
    ObjectRoot * object_offset;
} ObjbankDirectoryEntry;

struct {
    ObjbankDirectoryEntry entries[];
    uint32_t null_entry; // All 0s 
} ObjbankDirectory;

```

The directory is the only part of an object bank that must be at a fixed location in the file (the very beginning). All other data in the file can be arbitrarily located provided it's aligned to an 8 byte boundary [TODO: or is it 4?]. In practice, objects are interleaved with each other throughout the bank file rather than being arranged sequentially.

## Objects

An object consists of several different types of structure and data blocks spread throughout the bank file which connect to each other using pointers (or put another way, byte offsets into the file). Practically, this means to find a single object's data you start with the object's root pointer in the bank directory and then follow child pointers around depending on the structures you encounter. Those structures are described throughout the rest of this section.

The game engine loads these structures directly into RAM and doesn't modify them aside from changing file-based offsets to RAM addresses. As a result, many of these structures have "reserved fields" that serve no purpose when stored in the cartridge but are used as space for runtime variables while the game is running. These fields are also marked in the subsequent sections where their purposes are known, but in practice should be left as 0s.

TODO: describe which pointers can/can't be NULL

TODO: describe what UNUSED annotation means

### Roots

The directory at the top of an object bank points to an object's "root" structure. The root contains the object ID, a pointer to a heirarchical tree of meshes, and a pointer to animation metadata (though most of the animation data itself actually in the mesh tree). There are also several reserved fields that go mostly unused, aside from a pointer to the bank's base address (0 in-file, overwritten to the appropriate RAM address at load time)

```c
struct {
    uint32_t object_id;
    /* [[RESERVED]] */ void * __bank_base_addr;
    /* [[RESERVED]] */ uint32_t __unused_0x08;
    Mesh * mesh_tree;
    /* [[RESERVED]] */ uint32_t __unused_0x14;
    /* [[RESERVED]] */ uint32_t __unused_0x18;
    AnimationMetadata * animations;
} ObjectRoot;

```

### Meshes

```c
struct {
    uint32_t mesh_id;
    char name[8];

    uint16_t alpha; // TODO: ????

    uint16_t num_scale_keyframes;
    uint16_t num_translation_keyframes;
    uint16_t num_rotation_keyframes;

    Geometry *geo;
    DisplayListF3DEX *dl;

    TransformKeyframe (*scale_keyframes)[num_scale_keyframes];
    TransformKeyframe (*translation_keyframes)[num_translation_keyframes];
    TransformKeyframe (*rotation_keyframes)[num_rotation_keyframes];

    uint32_t num_sprites;
    Sprite (*sprites)[num_sprites];

    uint16_t num_children;

    uint16_t render_mode; // TODO: datatype

    Mesh *first_child;
    Mesh *sibling;

    /* [[RESERVED]] */ void * __runtime_collision_data;
} Mesh;

struct {
    float v[4];
    uint32_t t;
} TransformKeyframe;


```

#### Geometry

```c

struct {
    float x, y, z;
} Vertex;

struct {
    uint16_t v_idx[3];
} Face;

union {
    struct {
        uint8_t r, g, b;
    };
    struct {
        int8_t x, y, z;
    };
    /* [[RESERVED]] */ uint8_t __unused; // TODO: is this used as alpha?
} ColorNormal;

typedef s10_5_t int16_t;
struct {
    s10_5_t u, v;
} UV;
struct {
    UV coords[3];
} FaceUVs;

struct {
    uint16_t num_faces;
    uint16_t num_vertices;

    Vertex (*vertices)[num_vertices];
    Face (*faces)[num_faces];
    ColorNormal (*face_cn)[num_faces];
    FaceUVs (*uvs)[num_faces];
    /* [[RESERVED]] */ FaceUVs (* __unmodified_uvs)[num_faces] // TODO: is this allocated at runtime?
    ColorNormal (*vert_cn)[num_vertices];
    /* [[UNUSED]] */ uint8_t texture_flags; // TODO: confirm actually unused
    uint32_t (*texture_ids)[num_faces];
} Geometry;
```

#### Display lists

TODO:
- F3DEX display lists.
- Texture addresses are texture IDs and are updated at runtime.
- Describe what state is set up in advance

#### Sprites

TODO: describe incomplete engine implementation

```c
struct {
    uint32_t texture_id;
    // - id: runtime_data_ptr
    //   type: u4
    // - id: x
    //   type: u2
    // - id: y
    //   type: u2
    // - id: z
    //   type: u2
    // - id: width
    //   type: u2
    // - id: height
    //   type: u2
    // - id: u5
    //   type: s2
    // - id: u6
    //   type: s2
    // - id: flags
    //   type: u2
} Sprite;
```

### Animation Metadata

```c
struct {
    // - id: num_animation_definitions
    //   type: s2
    // - id: current_animation_idx
    //   type: s2
    // - id: u3
    //   type: u4
    // - id: is_playing
    //   type: u4
    // - id: time_delta
    //   type: f4
    // - id: next_anim_idx
    //   type: s2
    //   repeat: expr
    //   repeat-expr: 5
    // - id: pad
    //   type: u2
    // - id: next_is_playing
    //   type: u4
    //   repeat: expr
    //   repeat-expr: 5
    // - id: next_time_delta
    //   type: u4
    //   repeat: expr
    //   repeat-expr: 5
    // - id: next_anim_slot_idx
    //   type: s2
    // - id: u15
    //   type: u2
    // - id: animation_definitions_ptr
    //   type: u4
    // - id: cur_time
    //   type: f4
} AnimationMetadata;
```

```c
struct {
    // - id: start_time
    //   type: s2
    // - id: end_time
    //   type: s2
    // - id: playback_speed
    //   type: f4
    // - id: unused
    //   # this value is 0 everywhere except:
    //   #   - glover anims 12, 24, 42
    //   #   - FF boss actor "parento" (pillar elctricity)
    //   # where it is 1. the value is never read by the
    //   # game at runtime.
    //   type: u4
} AnimationDefinition;
```

## Libgarib GlTF format

### Conceptual

### Reference


# objbank-tool

## dumping
- mesh+sprite alpha
- enumerate/clarify render mode bits
    - determine alpha blending options from material
    - from reverse engineering notes:
        ```
        // TODO: 0x1 -- something to do with mesh generation?

        #define MESH_OPACITY        0x2
        #define MESH_OPAQUE         0
        #define MESH_TRANSPARENT    MESH_OPACITY

        #define MESH_TEXTURING      0x4
        #define MESH_UNTEXTURED     0
        #define MESH_TEXTURED       MESH_TEXTURING

        #define MESH_LIGHTING       0x8
        #define MESH_LIT            0
        #define MESH_UNLIT          MESH_LIGHTING

        // TODO: 0x10 -- ???
        // TODO: 0x20 -- animate water UVs
        // TODO: 0x40 -- lock animation time for rotation and all subsequent child TSR animations to (global level timer % 40) (wtf?)
        // TODO: 0x80 -- something to do with render order?
        ```
- deal with vertex clamp attributes

## packing
- compile new display lists
- gltf meshes

# actor-metadata-editor
- choose UI toolkit
- allow structured editing of gltf metadata

# fla2.c
- write C implementation
- set up python bindings
    - auto-fallback to python impl
- set up build system

# level editor

# level harness (ROM patch)
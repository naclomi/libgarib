# texbank-tool
- there used to be a creepy bug in IA tex packing whereby every other X coordinate
  was skipped. investigate what this was about (see git diff right after 07cd5e369246c5a4712edfd164c24698713df0cb)

# objbank-tool

## dumping
- don't repeat properties on child meshes when they're identical 
- mesh+sprite alpha
- enumerate/clarify render mode bits
    - determine alpha blending options from material
    - from reverse engineering notes:
        ```
        // bit -- 0 / 1
        // 0x1 -- TODO: something to do with mesh generation?
        // 0x2 -- opaque / transparent
        // 0x4 -- untextured / textured 
        // 0x8 -- lit / unlit
        // 0x10 -- ??? TODO
        // 0x20 -- _ / animate water UVs
        // 0x40 -- _ / lock animation time for rotation and all subsequent child TSR animations to (global level timer % 40) (wtf?)
        // 0x80 -- TODO: something to do with render order?
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
# texbank-tool
- there used to be a creepy bug in IA tex packing whereby every other X coordinate
  was skipped. investigate what this was about (see git diff right after 07cd5e369246c5a4712edfd164c24698713df0cb)

# objbank-tool

## dumping
- don't repeat properties on child meshes when they're identical 
- mesh+sprite alpha
- finish enumerating/clarifying render mode bits
- deal with vertex clamp attributes
- vertex compressor

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
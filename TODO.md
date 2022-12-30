# texbank-tool
- there used to be a creepy bug in IA tex packing whereby every other X coordinate
  was skipped. investigate what this was about (see git diff right after 07cd5e369246c5a4712edfd164c24698713df0cb)

# objbank-tool

## dumping
- animation: instead of just saving playback_time as a property,
             scale time timeline with it (it's only used to determine u16
             time code precision)
- sometimes, blender exporter crashes on material export and causes the skeleton to become ALL screwed up
- don't repeat properties on child meshes when they're identical 
- deal with collision vs dlist
- deal with vertex clamp attributes
- vertex UVs are off on pool entry for 0xcd048e58-at1land
- vertex compressor?
- animations should have slot as a property rather than just in name
- use a dict to map slot names?
- control export of global animation track via cmdline arg

## packing
- compile new display lists
- gltf meshes

# fla2.c
- write C implementation
- set up python bindings
    - auto-fallback to python impl
- set up build system

# level editor

# level harness (ROM patch)
# test rom
- when modified mupen is hanging on patched roms it seems to be
  getting stuck in the audio subsystem, I think there is more
  to asset patching than is currently being handled by the tool

# texbank-tool
- there used to be a creepy bug in IA tex packing whereby every other X coordinate
  was skipped. investigate what this was about (see git diff right after 07cd5e369246c5a4712edfd164c24698713df0cb)

# objbank-tool
## common
- Refactor pack list so it is less prone to silent errors
- Try turning an extracted display list into a packed geo object and viewing it in model viewer

## dumping
- make sure metadata is placed consistently in heirarchy
- animation: instead of just saving playback_time as a property,
             scale time timeline with it (it's only used to determine u16
             time code precision)
- sometimes, blender exporter crashes on material export and causes the skeleton to become ALL screwed up
- don't repeat properties on child meshes when they're identical 
- deal with collision vs dlist
- deal with vertex clamp attributes
- vertex UVs are off on pool entry for 0xcd048e58-at1land
- use a dict to map animation slot names?
- control export of global animation track via cmdline arg

## packing
- Test:
    - Animation
    - Child/sib nodes
    - Alpha
    - Geopacking: Multiple materials
- compile new display lists
- vertex compressor
- better validation
- look for missing properties in parent nodes

## mapping
- The "padding" at the end of each file seems
  to almost always be (72b * total_meshses), or very
  very slightly less than that.
  Unclear what it's for -- doesn't seem to be accessed
  by game code during normal operation


# fla2.c
- write C implementation
    - set up python bindings
        - auto-fallback to python impl
    - set up build system

# level editor

# level harness (ROM patch)
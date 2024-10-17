
# general

- current kaitai format seems to produce broken construct code by introducing
  enum too late into file. file bug with kaitai and patch in temporary fix.

# rom-asset-tool

# texbank-tool
- there used to be a creepy bug in IA tex packing whereby every other X coordinate
  was skipped. investigate what this was about (see git diff right after 07cd5e369246c5a4712edfd164c24698713df0cb)
- embed version info into output (for both packing and unpacking)

# objbank-tool
## common
- Refactor pack list so it is less prone to silent errors
- store extra surface attribute as either a secondary texture or
  third texture coordinate?
- new api:
  - all top-level nodes in a gltf scene are individual objects
  - instead of pack-list being required, it's display list by default,
    dynamic if ripple or conveyor belt are enabled, override if
    pack list specified
  - level-tool has a mode that consumes a gltf and spits out a
    boilerplate landscape that lays the objects out relative to 
    eachother properly
  - both DL and collision are derived from the same node UNLESS
    there is a sibling node named `{:}.geo`, in which case
    the latter is used for geo packing
      - how does dumping work with this? by default dump both, conrollable by flag?

## blender plugins
- New plugin that can auto-create materials from texure banks?
- Plugin that makes a UI element to graphically manage mesh
  properties. ARTISTS SHOULD NOT HAVE TO MANUALLY MANAGE PACK LISTS
  - See: https://docs.blender.org/api/current/info_quickstart.html#example-panel

## dumping
- only split vertices when their uvs/materials differ
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
- embed version info into output


## packing
- Test:
    - Animation
    - Child/sib nodes
    - Alpha
- better validation
- look for missing properties in parent nodes
- embed version info into output
- presently, the algorithm for ordering faces within an F3DEX batch is totally
  broken. it should be replaced with features in the global optimizer that:
  - optimize across materials
  - optimize which variant is "default" based on which other variants it often
    appears with


## mapping
- The "padding" at the end of each file seems
  to almost always be (72b * total_meshses), or very
  very slightly less than that.
  Unclear what it's for -- doesn't seem to be accessed
  by game code during normal operation
  Possibly an accumulation of boundary paddings across
  multiple modifications of the asset pack?

# fla2.c

# level-tool

## disassemble
- add "raw" mode that doesn't trim padding or nest tags

## assemble

# level editor

# rom patches

## kaizo level harness

## stdout
- how to do this easily with emulators?

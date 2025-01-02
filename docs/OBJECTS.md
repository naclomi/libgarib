# Glover object format

## Introduction
Glover "object" assets consist of 3D models and (optionally) their associated animations. All 3D models that appear in the game are stored as an object, whether it's the terrain for a level, a piece of rock rubble from a smashable wall, the vertical "Glover" text in the main menu, or Glover himself. These objects do not have any innate behaviors or interactive properties associated with them -- the object used for a smashable box could just as easily be swapped with the object used for a dinosaur enemy. 3D models and animations are the _only_ data stored here.

The rest of this document describes how objects are stored and used in-game, as well as how libgarib's tools translate these objects to/from GlTF files for editing. Binary formats are described as C structures that are assumed to be big-endian unless stated otherwise.

## Object banks

### Conceptual

Objects are inherently grouped into object banks, rather than standalone files. These banks are loaded and unloaded automatically by the game engine depending on which active level or menu screen is selected. 

The game then uses specifc objects by referring to them with their unique 32-bit ID numbers, which are used very similarly to filenames. When a level references an object ID, the game will load it by linearly searching every ID in every loaded object bank for a match.

### Binary format

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

### Roots

The directory at the top of an object bank points to an object's "root" structure. The root contains the object ID, a pointer to a heirarchical tree of meshes, and a pointer to animation metadata (though most of the animation data itself actually in the mesh tree). There are also several reserved fields used as reference pointers during gameplay.

```c
// todo
```

### Meshes
A mesh 

```c
// todo
```

#### Geometry

#### Display lists


### Animation Metadata



## Libgarib GlTF format

### Conceptual

### Reference

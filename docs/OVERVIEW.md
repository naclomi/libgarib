# Glover asset structure overview

## Data overview

Glover is built out of four main kinds of data ("assets"):

1. Game code
2. Textures
3. Objects (3D models)
4. Landscapes (level layouts)

Generally, these assets are grouped up into collections called "banks", which can optionally be compressed with a variant of LZAA compression called "FLA2". At any given time, one or more of these banks are loaded into memory and can thus refer to assets in eachother. _Landscapes_ are filled with _objects_, which are covered in _textures_.

Almost _all_ game sequences (including the intro logos, title screen, cutscenes, and bonus levels) are stored as landscapes. The only sections that aren't are the main menu, level completion screens and copyright screen. That said, even these sections store their graphical data in texture and object banks.

Additionally, game audio is stored in the following standard N64 formats:

5. MIDI song sequences
6. Audio banks (sound metadata)
7. Wave tables (sound samples)

Libgarib presently provides tools to mod textures, objects and landscapes. Modding game code has to be done by hand, and is much trickier.

## Loading sequence

In the vanilla ROM, much of the orchestration concerning how levels are loaded is hard-coded into the game code. The process usually looks like this:

- The game engine decides to load a given level
- It will load generic object and texture banks that store data common to all levels (eg, the Glover player model, ball models, garib textures, bitmap fonts etc)
- It will load an object bank and texture bank specific to the _world_ the level is located in (eg, one for Atlantis, one for Carnival, one for the hub world, etc)
- It will load an object bank specific to the _level_ (eg, Atlantis 1, Atlantis Boss, ...)
- It will load the landscape file associated with the level. In loading the landscape file, it sets up all aspects of the game engine needed to actually play the game.
- Finally, the game starts running

Whenever there is a scene transition (whether it's a level being completed, moving from the hub world to the castle cave, or exiting the title screen), the game unloads all the previous object/texture banks and starts this loading process again for the new one.


## Using libgarib tools

Libgarib comes packaged with several command-line tools for manipulating assets. Their general M.O. is to act as "translators" between the binary game data in Glover's custom formats and common file formats that you can edit with modern third-party art tools (like Blender or Photoshop).

Here's a rundown of the type of data each tool works with:
- `rom-asset-tool` takes a Glover ROM and splits it into its constituent data banks. These banks are still binary files that you can't do much with. The tool can also make a ROM _from_ data banks.
- `texbank-tool` translates between texture banks and PNG image files. Extra metadata about each texture is stored in the PNG file's "comments" data.
- `objbank-tool` translates between object banks and GlTF files. These models contain the 3D models themselves, as well as any skeletons, animations, and miscellaneous game-specific metadata. They also potentially contain embedded N64 display lists.
- `level-tool` translates landscape files between their binary form that the game can read, and an XML representation intended to be human-readable.
- `tip-tool` translates Mr. Tip text between the game's binary format and an editable YAML file

In theory, it's all that "simple". In practice, getting modern editing tools to _keep_ all the required metadata around that the game needs can be difficult. Understanding that metadata yourself and editing it where appropriate is an art. In subsequent documentation files, each asset format (and the nuances of editing it) is explained in detail.


## Asset names

Rather than filenames, the game refers to assets using unique **ID numbers** in the form of arbitrary-looking 32-bit integers. That integer is actually hashed version of the asset's original full filename, but in practice we don't know what those filenames were and so just refer to assets by their IDs. In-game, when a model or texture is requested, the relevant ID is provided and the game performs a linear search through all loaded assets looking for it.

In a few cases, the game intentionally uses the same IDs for different assets. Most notably, the body texture for the dibbers (the little wind-up toy enemies) is stored in each world's texture bank with the ID 0x5607992A.

When extracting data, libgarib tools will generally use this ID as the asset's filename. When _packing_ data, libgarib will treat the filename in one of these ways:

- If the filename (ignoring extension) is an 8-digit hex number starting with 0x, libgarib will treat this number as the object's ID and pack the asset into the game using said ID
- Otherwise, libgarib will hash the _whole_ filename (including extension) using the same hashing algorithm the game engine uses, and use this hash as the object's ID

Thankfully, the game's hashing algorithm is identical to a free and open-source CRC function found [here](http://www.mrob.com/pub/comp/crc-all.html) and released under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
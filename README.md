# libgarib v0.01

Tools for reading and manipulating data from the 1999 N64 release of the video game Glover.

## Repo contents

- `docs`: Human-language specifications and descriptions of game file formats
- `formats`: Rom memory maps and Kaitai Struct descriptions of game file formats
- `js`: Format parsers and convenience code for Javascript/Typescript
- `python`: Format parsers and convenience classes for Python 3
- `tools`: Stand-alone modding and inspection tools
    - `checksum.py`: Tool to recalculate N64 rom checksums
    - `fla2.py`: Tool to compress/decompress game assets
    - `hash.py`: Tool to produce string hashes equivalent to in-game hashing algorithm
    - `objbank-tool.py`: Tool to inspect and edit object banks (3D model archives) 
    - `texbank-tool.py`: Tool to edit texture banks
    - `rom-asset-tool.py`: Tool to split and edit ROM assets
    - `tip-tool.py`: Tool to edit Mr. Tip messages

## License

See `LICENSE.md`
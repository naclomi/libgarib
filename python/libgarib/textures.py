import struct
import sys

import json
import PIL.Image

from .parsers.glover_texbank import GloverTexbank
from .parsers.construct import glover_texbank as texbank_writer

def decodeRGBA16(raw):
    raw = struct.unpack(">H", raw)[0]
    r = int((((raw & 0xf800) >> 11)/32) * 255)
    g = int((((raw & 0x07C0) >> 6)/32) * 255)
    b = int((((raw & 0x003E) >> 1)/32) * 255)
    a = int((raw & 0x1) * 255)
    return (r,g,b,a)

class TextureDecodeException(Exception):
    pass

def imToTex(im, tex_id):
    
    metadata = {}
    if "Comment" in im.info:
        metadata = json.loads(im.info["Comment"])

    flags = metadata.get("flags", 0)

    # Set palette animation flag based on other metadata
    if metadata.get("palette_anim_idx_min", 0) != metadata.get("palette_anim_idx_max", 0):
        flags |= 4
    else:
        flags &= ~4 & 0xFFFF

    # TODO: if not filled out, guess based on image data
    metadata["color_format"] = metadata.get("color_format", 0)
    metadata["compression_format"] = metadata.get("compression_format", 0)

    pixels = []
    palette = []


    return texbank_writer.glover_texbank__texture.build({
        "id": tex_id,
        "palette_anim_idx_min": metadata.get("palette_anim_idx_min", 0),
        "palette_anim_idx_max": metadata.get("palette_anim_idx_max", 0),
        "frame_increment": metadata.get("frame_increment", 0),
        "frame_counter": metadata.get("frame_counter", 0),
        "flags": flags,
        "width": im.size[0],
        "height": im.size[1],
        "masks": 0, # TODO
        "maskt": 0, # TODO
        "color_format": metadata["color_format"],
        "compression_format": metadata["compression_format"], 
        "data_ptr": 36,
        "palette_offset": 36 + len(pixels),
        "length": 36 + len(pixels) + len(palette),
        "data": b"" # TODO
    })

def texToIm(texture: GloverTexbank):
    size = (texture.width, texture.height)
    decoded_pixels = []
    palette = []
    if texture.color_format is GloverTexbank.TextureColorFormat.ia:
        if texture.compression_format is GloverTexbank.TextureCompressionFormat.uncompressed_16b:
            mode = "RGBA"
            for cursor in range(0, size[0]*size[1]*2, 2):
                raw = struct.unpack(">BB", texture.data[cursor:cursor+2])
                decoded_pixels.append((raw[0], raw[0], raw[0], raw[1]))
    else:
        if texture.compression_format is GloverTexbank.TextureCompressionFormat.ci4:
            mode = "P"
            for indices in texture.data[:size[0]*size[1]//2]:
                decoded_pixels.append((indices & 0xF0) >> 4)
                decoded_pixels.append(indices & 0xF)
            for cursor in range(texture.palette_offset - 36, len(texture.data), 2):
                palette.extend(decodeRGBA16(texture.data[cursor:cursor+2]))
        elif texture.compression_format is GloverTexbank.TextureCompressionFormat.ci8:
            mode = "P"
            for index in texture.data[:size[0]*size[1]]:
                decoded_pixels.append(index)
            for cursor in range(texture.palette_offset - 36, len(texture.data), 2):
                palette.extend(decodeRGBA16(texture.data[cursor:cursor+2]))
        elif texture.compression_format is GloverTexbank.TextureCompressionFormat.uncompressed_16b:
            mode = "RGBA"
            for cursor in range(0, size[0]*size[1]*2, 2):
                decoded_pixels.append(decodeRGBA16(texture.data[cursor:cursor+2]))
        elif texture.compression_format is GloverTexbank.TextureCompressionFormat.uncompressed_32b:
            mode = "RGBA"
            # TODO: test
            for cursor in range(0, size[0]*size[1]*4, 4):
                raw = struct.unpack(">BBBB", texture.data[cursor:cursor+4])
                decoded_pixels.append(raw)

    if len(decoded_pixels) == 0:
        raise TextureDecodeException("Unsupported image format ({:}/{:}) for texture {:}".format(str(texture.compression_format), str(texture.color_format), texture.id))
    im = PIL.Image.new(mode, size)
    if len(palette) > 0:
        im.putpalette(palette, rawmode="RGBA")
    im.putdata(decoded_pixels)
    return im
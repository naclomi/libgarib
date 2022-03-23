import struct
import sys

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

def texToPillow(texture: GloverTexbank):
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
        sys.stderr.write("WARNING: Unsupported image format ({:}/{:}) for texture {:}".format(str(texture.compression_format), str(texture.color_format), texture.id))
    im = PIL.Image.new(mode, size)
    if len(palette) > 0:
        im.putpalette(palette, rawmode="RGBA")
    im.putdata(decoded_pixels)
    return im
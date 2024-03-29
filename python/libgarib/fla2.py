import collections
import io
import os
import struct
import sys

MAGIC_NUMBER_FLA = b"FLA2"

try:
    from .cppcore.fla2 import compress as cpp_compress
except:
    cpp_compress = None

def py_compress(src, dst, src_length=None, progress_callback=None):
    # pypy/cpython cross-compatability hack:
    # cpython treats single-byte slices of a bytestring
    # as integers, while pypy treats them as characters,
    # and we need to change our behavior accordingly
    byte_slice_coerce = type(b"\x00"[0]) is int

    if type(src) is not bytes:
        src = src.read()
    src_length = len(src)

    dst.write(b"FLA2")
    dst.write(struct.pack("<I", src_length))

    window = [None] * 0x1000
    window_wr_cursor = 0

    progress_delta = src_length / 100
    progress_counter = progress_delta
    progress_ticks = 0

    read_cursor = 0
    done = False
    while not done:
        cmd_byte_location = dst.tell()
        dst.write(b"\x00")
        cmd = 0
        for cmd_bit in range(8):
            next_byte = src[read_cursor]
            read_cursor += 1
            progress_counter -= 1

            window[window_wr_cursor] = next_byte
            window_wr_cursor = (window_wr_cursor + 1) & 0xfff

            best_token = (None,0)
            search_cursor = (window_wr_cursor - 2) & 0xfff
            while ((search_cursor - window_wr_cursor) & 0xfff) >= 1:
                if window[search_cursor] == next_byte:
                    # Build token
                    local_window_wr_cursor = window_wr_cursor
                    src_cursor = read_cursor
                    window_rd_cursor = (search_cursor + 1) & 0xfff
                    for _ in range(16):
                        if src_cursor >= src_length:
                            break
                        next_src_byte = src[src_cursor]
                        next_window_byte = window[window_rd_cursor]
                        if next_window_byte != next_src_byte:
                            break

                        window[local_window_wr_cursor] = next_src_byte
                        local_window_wr_cursor = (local_window_wr_cursor + 1) & 0xfff

                        window_rd_cursor = (window_rd_cursor + 1) & 0xfff
                        src_cursor += 1
                    token = (search_cursor, (window_rd_cursor - search_cursor) & 0xfff)
                    if token[1] > best_token[1]:
                        best_token = token
                    if ((window_wr_cursor - search_cursor) & 0xFFF) <= token[1]:
                        break
                search_cursor = (search_cursor - 1) & 0xfff

            if best_token[0] is None or best_token[1] <= 2:
                if byte_slice_coerce: 
                    dst.write(struct.pack("B", next_byte))
                else:
                    dst.write(next_byte)
            else:
                cmd |= 1 << (7-cmd_bit)

                backref_start = (window_wr_cursor - 1 - best_token[0]) & 0xfff
                backref_len = (best_token[1] - 2) & 0xF
                backref = ((backref_start & 0xFF) << 8) | ((backref_start & 0xF00) >> 4) | backref_len
                dst.write(struct.pack("<H", backref))                
                # Debug: write tokens out in ASCII:
                # dst.write(("{:}".format(str((backref_start, backref_len+2)))).encode())

                read_cursor += backref_len + 1
                progress_counter -= backref_len + 1

                window_wr_cursor = (window_wr_cursor + backref_len + 1) & 0xfff

            if progress_counter <= 0:
                progress_counter += progress_delta
                progress_ticks += 1
                if progress_callback is not None:
                    progress_callback(progress_ticks)

            if read_cursor >= src_length:
                done = True
                # write mid-block terminator sequence, if necessary
                if cmd_bit < 7:
                    cmd |= 1 << (7-(cmd_bit+1))
                    dst.write(b"\x00\x00")
                break
        dst_head = dst.tell()
        dst.seek(cmd_byte_location)
        dst.write(struct.pack("B", cmd))
        dst.seek(dst_head)

        # write end-block terminator sequence, if necessary
        if done and cmd_bit == 7:
            dst.write(b"\x80\x00\x00")

def compress(src, dst, src_length=None, progress_callback=None, force_pure_python=False):
    if cpp_compress is None or force_pure_python:
        py_compress(src, dst, src_length, progress_callback)
    else:
        src_bytes = src.read(src_length)
        dst_bytes = cpp_compress(src_bytes)
        dst.write(dst_bytes)

def decompress(src, dst):
    if type(src) is bytes:
        src = io.BytesIO(src)

    magic = src.read(4)
    if magic != MAGIC_NUMBER_FLA:
        raise ValueError("Not an FLA2 stream")

    window = [b"\x00"] * 0x1000
    cursor = 0
    bytes_written = 0

    uncompressed_length = struct.unpack("<I", src.read(4))[0]

    while True:
        cmd = struct.unpack("B", src.read(1))[0]
        for bit in "{:08b}".format(cmd):
            if bit == "0":
                next_byte = src.read(1)
                dst.write(next_byte)

                window[cursor] = next_byte
                cursor = (cursor + 1) & 0xFFF

                bytes_written += 1
            else:
                backref = struct.unpack("BB", src.read(2))
                if backref[0] == 0 and backref[1] == 0:
                    if bytes_written != uncompressed_length:
                        raise ValueError("Premature EOF")
                    return bytes_written
                backref_len = (backref[0] & 0x0F) + 2
                backref_dist = ((backref[0] & 0xF0) << 4) + backref[1]

                backref_start = cursor - backref_dist
                backref_end = backref_start + backref_len

                backref_data = b""

                for read_cursor in range(backref_start, backref_end):
                    read_cursor &= 0xFFF
                    next_byte = window[read_cursor]

                    window[cursor] = next_byte
                    cursor = (cursor + 1) & 0xFFF

                    backref_data += next_byte

                dst.write(backref_data)

                bytes_written += backref_len

def data_from_stream(file, length=None):
    file_offset = file.tell()
    magic_numbers = file.read(4)
    file.seek(file_offset)
    if magic_numbers == MAGIC_NUMBER_FLA:
        raw_data_stream = io.BytesIO()
        decompress(file, raw_data_stream)
        raw_data = raw_data_stream.getvalue()
    else:
        if length is None:
            file.seek(0, os.SEEK_END)
            length = file.tell()
            file.seek(file_offset)
        raw_data = file.read(length)
    return raw_data

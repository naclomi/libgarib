import dataclasses
import struct
import typing

class LinkException(Exception):
    pass

def padSize(size, boundary=8):
    return -size % boundary

def padBytes(data, boundary=8):
    if padSize(len(data)) == 0:
        return data
    else:
        pad = b"\0" * padSize(len(data))
        return data + pad

class Linkable(object):
    def __init__(self):
        self.parent_offset: int = 0
        self.parent: typing.Union[None, 'Linkable'] = None

    def finalize(self):
        pass

    def absolute_offset(self) -> int:
        if self.parent is None:
            return 0
        return self.parent.absolute_offset() + self.parent.field_offset(self)

    def __len__(self) -> int:
        return 0

    def link(self) -> bytes:
        return b""

@dataclasses.dataclass
class LinkablePointer(object):
    offset: int
    dtype: str # struct format specifier
    target: Linkable
    target_offset: int = 0

    def rewrite(self, data: bytearray):
        size = struct.calcsize(self.dtype)
        if isinstance(self.target_offset, int):
            target_offset = self.target_offset
        elif isinstance(self.target, LinkableStruct):
            target_offset = self.target.field_offset(self.target_offset)
        else:
            raise Exception("Pointer target offset is a field, but target isn't a struct")
        absolute_dst = self.target.absolute_offset() + target_offset
        # print(type(self.target),hex(self.offset), hex(self.target.absolute_offset()), hex(target_offset), hex(absolute_dst))
        data[self.offset: self.offset+size] = struct.pack(self.dtype, absolute_dst)

class LinkableBytes(Linkable):
    def __init__(self, data: bytearray, pointers: typing.List[LinkablePointer]=None):
        super().__init__()
        self.data = data
        if type(self.data) is not bytearray:
            self.data = bytearray(self.data)
        self.pointers = pointers or list()

    def __len__(self):
        data_len = len(self.data)
        return data_len + padSize(data_len)

    def finalize(self):
        for pointer in self.pointers:
            if pointer.target is None:
                # Relative pointer
                pointer.target = self

    def link(self):
        for pointer in self.pointers:
            pointer.rewrite(self.data)
        return padBytes(self.data)

class LinkableStruct(Linkable):
    def __init__(self, data: typing.List[Linkable] = None):
        super().__init__()
        self.data = []
        if data is not None:
            for new_child in data:
                self.append(new_child)

    def __len__(self):
        data_len = sum(len(d) for d in self.data)
        return data_len + padSize(data_len)

    def append(self, child: Linkable):
        self.data.append(child)
        child.parent = self

    def finalize(self):
        for linkable in self.data:
            linkable.finalize()

    def field_offset(self, child):
        cursor = 0
        for linkable in self.data:
            if linkable is child:
                return cursor
            cursor += len(linkable)
        else:
            raise LinkException("Not a child of struct")

    def link(self):
        raw = []
        for linkable in self.data:
            raw.append(linkable.link())
        return padBytes(b"".join(raw))


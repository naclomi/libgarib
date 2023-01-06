import dataclasses
import struct
import typing

class LinkException(Exception):
    pass

def padLen(size):
    return size + (4 - size & 3)

def padBytes(data):
    pad_len = 4 - len(data) & 3
    if pad_len == 0:
        return data
    else:
        pad = b"\0" * pad_len
        return data + pad

class Linkable(object):
    def __init__(self):
        self.parent_offset: int = 0
        self._absolute_offset: typing.Union[None, int] = None
        self.parent: typing.Union[None, 'Linkable'] = None

    def finalize(self):
        pass

    def absolute_offset(self) -> int:
        if self.parent is None:
            return 0
        elif self._absolute_offset is None:
            return self.parent.field_offset(self) + self.parent.absolute_offset()
        else:
            return self._absolute_offset

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
        absolute_dst = self.target.absolute_offset() + self.target_offset
        data[self.offset: self.offset+size] = struct.pack(self.dtype, absolute_dst)

class LinkableBytes(Linkable):
    def __init__(self, data: bytearray, pointers: typing.List[LinkablePointer]=None):
        super().__init__()
        self.data = data
        if type(self.data) is not bytearray:
            self.data = bytearray(self.data)
        self.pointers = pointers or list()

    def __len__(self):
        return padLen(len(self.data))

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
        self.data = data or []

    def __len__(self):
        return padLen(sum(len(d) for d in self.data))

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


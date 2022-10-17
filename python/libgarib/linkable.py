import dataclasses
import struct
import typing

class LinkException(Exception):
    pass

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

@dataclasses.dataclass
class LinkableBytes(Linkable):
    data: bytes
    pointers: typing.List[LinkablePointer]

    def __len__(self):
        return len(self.data)

    def link(self):
        for pointer in self.pointers:
            pointer.rewrite(self.data)
        return self.data

@dataclasses.dataclass
class LinkableStruct(Linkable):
    data: typing.List[Linkable] = dataclasses.field(default_factory=list)
    absolute_offset: int = None

    def __len__(self):
        return sum(len(d) for d in self.data)

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
        return b"".join(raw)


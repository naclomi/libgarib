from collections.abc import Sequence, Mapping, Set

class GenericProxy(object):
    CACHE = {}

    @classmethod
    def of(cls, obj):
        if id(obj) not in cls.CACHE:
            if isinstance(obj, Sequence) and not isinstance(obj, str):
                cls.CACHE[id(obj)] = ListProxy(obj)
            elif isinstance(obj, Mapping):
                cls.CACHE[id(obj)] = DictProxy(obj)
            elif hasattr(obj, "__dict__"):
                cls.CACHE[id(obj)] = ObjProxy(obj)
            else:
                cls.CACHE[id(obj)] = obj
        return cls.CACHE[id(obj)]

    def __init__(self, obj):
        self.obj = obj

    def __len__(self):
        return self.obj.__len__()

    def __iter__(self):
        it = self.obj.__iter__()
        try:
            while True:
                yield GenericProxy.of(next(it))
        except StopIteration:
            return

    def __repr__(self):
        return self.obj.__repr__()

    def __str__(self):
        return self.obj.__repr__()

    def __contains__(self, key):
        return self.obj.__contains__(key)

    def __getitem__(self, key):
        return GenericProxy.of(self.obj.__getitem__(key))

    def __setitem__(self, key, value):
        self.obj.__setitem__(key, value)

class PseudoList(list):
    ...

class PseudoDict(dict):
    ...

class ListProxy(GenericProxy, list):
    def __new__(cls, obj=None):
        # For dpath segment creation; if someone tries
        # to create an empty collection of the same "type"
        # as a proxy class, actually give them a proper
        # empty collection rather than a proxy class pointing
        # to None
        if obj is None:
            s = PseudoList.__new__(cls)
            s.__class__ = PseudoList
            return s
        return super().__new__(cls, obj)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(list(i for i in self))

class DictProxy(GenericProxy, dict):
    def __new__(cls, obj=None):
        # For dpath segment creation; if someone tries
        # to create an empty collection of the same "type"
        # as a proxy class, actually give them a proper
        # empty collection rather than a proxy class pointing
        # to None
        if obj is None:
            s = PseudoDict.__new__(cls)
            s.__class__ = PseudoDict
            return s
        return super().__new__(cls, obj)

    def __init__(self, obj):
        GenericProxy.__init__(self, obj)
        # CPYTHON HACK: add a dummy object to the
        # dict contents, which forces the internal
        # 'ma_used' flag to true. this allows C
        # modules like the json encoder to iterate
        # over it
        dict.__setitem__(self, ..., ...)

    def __iter__(self):
        it = self.obj.__iter__()
        try:
            while True:
                yield next(it)
        except StopIteration:
            return

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(dict(self.items()))

    def keys(self):
        return self.obj.keys()

    def values(self):
        return (GenericProxy.of(v) for v in self.obj.values())

    def items(self):
        return ((k, self[k]) for k in self.keys())

    def get(self, *args, **kwargs):
        return self.obj.get(*args, **kwargs)

class ObjProxy(GenericProxy, dict):
    def __new__(cls, obj=None):
        # For dpath segment creation; if someone tries
        # to create an empty collection of the same "type"
        # as a proxy class, actually give them a proper
        # empty collection rather than a proxy class pointing
        # to None
        if obj is None:
            s = PseudoDict.__new__(cls)
            s.__class__ = PseudoDict
            return s
        return super().__new__(cls, obj)

    def __init__(self, obj):
        GenericProxy.__init__(self, obj)
        # CPYTHON HACK: add a dummy object to the
        # dict contents, which forces the internal
        # 'ma_used' flag to true. this allows C
        # modules like the json encoder to iterate
        # over it
        dict.__setitem__(self, ..., ...)

    def keys(self):
        all_attr = set()
        all_attr.update(k for k in self.obj.__dict__.keys() if not k.startswith("_"))
        for k,v in vars(type(self.obj)).items():
            if k.startswith("_"):
                continue
            if type(v) is property:
                all_attr.add(k)
        return all_attr

    def values(self):
        return (GenericProxy.of(self[k]) for k in self.keys())

    def items(self):
        return ((k, self[k]) for k in self.keys())

    def __contains__(self, key):
        return self.keys().__contains__(key)
    
    def __len__(self):
        return self.keys().__len__()

    def __iter__(self):
        it = self.keys().__iter__()
        try:
            while True:
                yield next(it)
        except StopIteration:
            return

    def __getitem__(self, key):
        return GenericProxy.of(getattr(self.obj, key))

    def __setitem__(self, key, value):
        setattr(self.obj, key, value)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(dict(self.items()))

    def get(self, key, default=None):
        if key in self.keys():
            return self[key]
        return default


class CircularLink(object):
    def __init__(self, obj):
        self.obj = obj

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "CircularLink<0x{:X},{:}>".format(id(self.obj), str(self.obj))

def kaitaiToJson(obj, visited = None):
    if visited is None:
        visited = set()
    if issubclass(type(obj), list):
        if id(obj) in visited:
            return CircularLink(obj)
        visited.add(id(obj))
        return [kaitaiToJson(v, visited) for v in obj]
    elif hasattr(obj, "__dict__"):
        if id(obj) in visited:
            return CircularLink(obj)
        visited.add(id(obj))
        d = {}
        all_attr = {}
        all_attr.update(obj.__dict__)
        for k,v in vars(type(obj)).items():
            if type(v) is property:
                all_attr[k] = getattr(obj, k)
        for k, v in all_attr.items():
            if k.startswith("_"):
                continue
            d[k] = kaitaiToJson(v, visited)
        return d
    else:
        return obj
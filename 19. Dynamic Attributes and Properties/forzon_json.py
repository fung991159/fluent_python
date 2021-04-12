from collections import Mapping, MutableSequence


class FrozenJSON:
    """A read-only facade for navigating a JSON-like object
    using attribute notation"""

    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, Mapping):
            return cls(obj)
        elif isinstance(obj, MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj  # this is the base case for build tranversal


if __name__ == "__main__":
    d = FrozenJSON({"a": [1, 2, 3], "b": {"inner": "inner_value"}})
    # print(d.b["a"])
    print(d.__mro__)



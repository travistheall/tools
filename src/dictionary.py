"""
Simple dictionary that allows insertion of new keys,
but prohibits updates on the inserted keys.

The idea behind this is throw an error when someone
tries to set an existing item in the dictionary.
Mutable data structures are cast to immutable equivalents.
"""
import collections
import types
from typing import Any, Optional


class ImmutableKeyError(KeyError):
    """
    Error for trying to set an existing
    key in an ImmutableKeyDefaultOrderedDict.
    """

    msg = "Immutable Key Dictionary. Cannot modify the key '%s'."

    def __init__(self, key: str) -> None:
        super().__init__(self.msg % key)


class TypeConversionMap(dict):
    """
    Singleton dictionary where the lookup is the
    type of the key passed in rather than its actual value.

    TypeConversionMap is used to provide immutable
    alternatives to mutable datastructures.
    """

    inst = None
    conv_map = {dict: types.MappingProxyType, list: tuple, set: frozenset}

    def __new__(cls):
        """Each instance of this class is conv_map with type key lookups."""
        if not cls.inst:
            cls.inst = super().__new__(cls)
            cls.inst |= cls.conv_map
            del cls.conv_map

        return cls.inst

    def __getitem__(self, key: Any) -> Optional[type]:
        """Implements type based key lookups."""
        if key_inst := [i_type for i_type in self if isinstance(key, i_type)]:
            key = key_inst[0]

        return super().get(key, None)


class ImmutableKeyDefaultOrderedDict(collections.OrderedDict):
    """
    Dictionary that allows insertion of new keys,
    but prohibits updates on the inserted keys.
    It converts mutable value types into immutable equivalents.
    """

    conv_map = TypeConversionMap()

    def __getitem__(self, key: Any) -> Any:
        """Mimic collections' default dict behavior."""
        return super().get(key, None)

    def __setitem__(self, key: Any, value: Any) -> None:
        """Implements dictionary key insertion and error raised."""
        if self[key]:
            raise ImmutableKeyError(key)

        if conv_type := self.conv_map[value]:
            value = conv_type(value)

        super().__setitem__(key, value)

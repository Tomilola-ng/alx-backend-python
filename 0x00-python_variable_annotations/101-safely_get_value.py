#!/usr/bin/env python3
"""
    FIRST ELEMENT
    ANY | NONE
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """ I DON'T KNOW YET """

    if key in dct:
        return dct[key]
    else:
        return default

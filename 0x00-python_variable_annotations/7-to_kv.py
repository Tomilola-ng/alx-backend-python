#!/usr/bin/env python3
"""
    TUPLE OF STR, AND FLOAT
"""

from typing import Union, Tuple

def to_kv(k: str, v : Union[int, float]) -> Tuple[str, float]:
    """
        SUM UP A LIST
    """

    return (k, float(v ** 2))

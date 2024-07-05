#!/usr/bin/env python3
"""
    RETURN ELEMENT LENGTH
"""

from typing import Sequence, Iterable, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        ITERABLE RESPONSE
    """

    return [(i, len(i)) for i in lst]

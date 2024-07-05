#!/usr/bin/env python3
"""
    FIRST ELEMENT
    ANY | NONE
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        ITERABLE RESPONSE
    """

    if lst:
        return lst[0]
    else:
        return None

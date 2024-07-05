#!/usr/bin/env python3
"""
    SUM OF MIXED ARRAY OF FLOATS
    AND INTS WITH TYPE ANNOTATIONS
"""

from typing import List, Union

def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """
        SUM UP A LIST
    """

    return float(sum(input_list))

#!/usr/bin/env python3
"""
    SUM OF ARRAY OF FLOATS WITH TYPE ANNOTATIONS
"""

def sum_list(input_list: list[float]) -> float:
    """
        SUM UP A LIST
    """

    total: float = 0

    for item in input_list:
        total += item

    return total

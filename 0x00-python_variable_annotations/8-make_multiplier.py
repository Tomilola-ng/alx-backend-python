#!/usr/bin/env python3
"""
    RETURN MULTIPLIER FUNC
"""

from typing import Callable, Union

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        ARRANGE MULTIPLYING FUNCTION.
    """

    def multiply(num: float) -> Union[float, int]:
        """ SUB MULTIPLIER FUNC """
        return num * multiplier

    return multiply

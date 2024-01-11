#!/usr/bin/env python3
"""
Module Documentation
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function Documentation
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function

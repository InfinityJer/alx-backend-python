#!/usr/bin/env python3
"""
Module Documentation
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Corrected the factor to an integer

# The script in 102-main.py prints the annotations
print(zoom_array.__annotations__)

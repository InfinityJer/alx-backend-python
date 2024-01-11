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

zoom_2x = zoom_array(tuple(array))  # Convert the list to a tuple

zoom_3x = zoom_array(tuple(array), 3)  # Convert the list to a tuple, and use integer factor

# The script in 102-main.py prints the annotations
print(zoom_array.__annotations__)

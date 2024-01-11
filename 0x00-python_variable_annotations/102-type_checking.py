#!/usr/bin/env python3
"""
Module Documentation
"""

from typing import Tuple, List

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms into the given tuple by repeating each element a specified number of times.

    Args:
    - lst (Tuple): The input tuple to be zoomed in.
    - factor (int): The factor by which each element in the tuple is repeated.

    Returns:
    - List: The zoomed-in list.

    Example:
    >>> zoom_array((1, 2, 3), 3)
    [1, 1, 1, 2, 2, 2, 3, 3, 3]
    """
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
#!/usr/bin/env python3
"""
Module Documentation
"""

from typing import Tuple, List

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms into the given tuple by repeating each element a specified number of times.

    Args:
    - lst (Tuple): The input tuple to be zoomed in.
    - factor (int): The factor by which each element in the tuple is repeated.

    Returns:
    - List: The zoomed-in list.

    Example:
    >>> zoom_array((1, 2, 3), 3)
    [1, 1, 1, 2, 2, 2, 3, 3, 3]
    """
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

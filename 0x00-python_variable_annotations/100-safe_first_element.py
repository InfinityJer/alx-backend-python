#!/usr/bin/env python3
"""
Module Documentation
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Function Documentation
    """
    if lst:
        return lst[0]
    else:
        return None

#!/usr/bin/env python3
from typing import Iterable, List, Tuple, Sequence
"""
Module 9-element_length
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples

    Args:
        lst: list of values
    Returns:
        list of tuples
    """
    return [(i, len(i)) for i in lst]

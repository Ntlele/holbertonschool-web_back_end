#!/usr/bin/env python3
from typing import Iterable, List, Tuple, Sequence
"""
Module 9-element_length
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function that gets the leghth of a list

    Args:
        lst (list): list of values
    Returns:
        list of tuples
    """
    return [(i, len(i)) for i in lst]

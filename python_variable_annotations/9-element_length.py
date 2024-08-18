#!/usr/bin/env python3
"""
    Contains the element_length function
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Returns a list of tuples, where each
        tuple contains an element from the
        input sequence and the length of that element.
        Args:
            lst (Sequence[Any]): A sequence of elements
            that can be passed to the
            `len()` function (e.g., strings, lists, tuples).
        Returns:
            List[Tuple[Any, int]]: A list of tuples.
            Each tuple contains an element
            from the input sequence and the length of that
            element.
    """
    return [(i, len(i)) for i in lst]

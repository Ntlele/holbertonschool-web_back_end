#!/usr/bin/env python3
from typing import List
"""
Module 5-sum_list
"""


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floating-point numbers.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of all the numbers in the input list.
        
    Example:
        >>> sum_list([1.2, 2.3, 3.4])
        6.9
        
    Note:
        This function uses Python's built-in `sum` function, which returns the sum of the elements in the list.
    """
    return sum(input_list)

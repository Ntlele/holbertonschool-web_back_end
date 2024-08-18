#!/usr/bin/env python3
from typing import Tuple, Union, Callable
"""
Module 5-sum_list
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns the product of multiplier and float value """
    def product(value: float):
        return multiplier * value
    return product
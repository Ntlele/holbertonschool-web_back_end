#!/usr/bin/env python3
"""
Module 5-sum_list
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns the product of multiplier and float value """
    def product(value: float):
        return multiplier * value
    return product

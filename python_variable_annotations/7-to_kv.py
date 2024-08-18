#!/usr/bin/env python3
"""
Module 5-sum_list
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns the tuple of the arguments """
    return (k, float(v**2))

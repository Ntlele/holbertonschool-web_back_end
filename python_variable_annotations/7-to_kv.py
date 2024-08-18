#!/usr/bin/env python3
from typing import Tuple, Union
"""
Module 5-sum_list
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns the tuple of the arguments """
    return k, v

print(to_kv("eggs", 3))
print(to_kv("school", 0.02))
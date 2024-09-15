#!/usr/bin/env python3
"""
Async Comprehensions
"""


from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Async Comprehensions

    Returns:
        List[float]: _description_
    """
    numbers = [num async for num in async_generator()]
    return numbers

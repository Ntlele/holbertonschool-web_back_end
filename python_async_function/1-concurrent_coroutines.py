#!/usr/bin/env python3

"""
    contains an async routine function that calls wait_random n times
    Imports:
        asyncio
        typing
        wait_random
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        returns a list of all the delays (float values).
    """
    delays = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    return delays

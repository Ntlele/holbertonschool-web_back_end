#!/usr/bin/env python3

"""
    module that contains an async routine that returns a random value
    Imports:
        asyncio
        random
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        returns the random delay as a float
        Args:
            max_delay (int): delay value during execution
        Returns:
            a float number
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

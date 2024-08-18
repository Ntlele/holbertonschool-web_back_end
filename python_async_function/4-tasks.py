#!/usr/bin/env python3

"""
    similar function to wait_n but calls task_wait random instead
    Imports:
        asyncio
        typing
        task_wait_random
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        Returns a list of all the delays (float values)
        by calling task_wait_random n times.
        Args:
            n (int): Number of times to call task_wait_random.
            max_delay (int): Maximum delay value for each call.
        Returns:
            List[float]: A list of delays obtained from task_wait_random.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays

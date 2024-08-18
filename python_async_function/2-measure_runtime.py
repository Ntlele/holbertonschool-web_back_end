#!/usr/bin/env python3

"""
    contains a function that measures the runtime when using wait_n
    Imports:
        asyncio
        time
        wait_n
"""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
        measures the runtime of using wait_n
        Args:
            n (int): first arg for wait_n
            max_delay (int): sec arg for wait_n
        Returns:
            a float number approximate to runtime
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time

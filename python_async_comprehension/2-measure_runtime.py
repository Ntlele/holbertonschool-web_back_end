#!/usr/bin/env python3
"""Run time for four parallel comprehension"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measuring runtime
    """
    start_time = time.time()
    await asyncio.gather(async_comprehension())
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    async def main():
        print(await measure_runtime())

    asyncio.run(main())

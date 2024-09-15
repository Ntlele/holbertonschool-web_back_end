#!/usr/bin/env python3

"""
    Module that contains a coroutine to measure the runtime of async_comprehension.
    Imports:
        asyncio
        async_comprehension (from 1-async_comprehension)
"""

import asyncio
import time

# Import async_comprehension from 1-async_comprehension using __import__
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension four times in parallel.

    This coroutine uses asyncio.gather to run async_comprehension four times concurrently,
    measures the total time taken for all executions, and returns the runtime.

    Returns:
        float: The total runtime of the concurrent executions in seconds.
    """
    start_time = time.time()  # Record the start time

    # Run async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()  # Record the end time
    return end_time - start_time  # Calculate and return the total runtime

# Example usage:
if __name__ == "__main__":
    async def main():
        print(await measure_runtime())

    asyncio.run(main())

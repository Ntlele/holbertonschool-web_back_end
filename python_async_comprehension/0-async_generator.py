#!/usr/bin/env python3

"""
    Module that contains an asynchronous generator that yields random values.
    Imports:
        asyncio
        random
"""

import asyncio
import random

async def async_generator():
    """
    Asynchronously generates random numbers between 0 and 10.

    This coroutine waits for 1 second asynchronously, then yields a random
    integer between 0 and 10. It repeats this process 10 times.

    Yields:
        int: A random integer between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.randint(0, 10)  # Yield a random number between 0 and 10

# Example usage:
async def main():
    async for number in async_generator():
        print(number)

# Run the example usage
if __name__ == "__main__":
    asyncio.run(main())

#!/usr/bin/env python3

"""
    Module that contains an asynchronous comprehension function.
    Imports:
        asyncio
        async_generator (from 0-async_generator)
"""

import asyncio
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> list:
    """
    Collects 10 random numbers from async_generator using async comprehension.

    This coroutine uses asynchronous list comprehension to collect 10 random
    numbers yielded by async_generator and returns them as a list.

    Returns:
        list: A list of 10 random numbers.
    """
    return [number async for number in async_generator()]

# The main function to test async_comprehension
async def main():
    print(await async_comprehension())

if __name__ == "__main__":
    asyncio.run(main())

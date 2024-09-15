#!/usr/bin/env python3
"""Async Generator"""


import asyncio
from random import uniform
from typing import AsyncGenerator, Generator


async def async_generator() -> Generator[float, None, None]:
    """coroutine that will loop 10 times and yield random
    between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
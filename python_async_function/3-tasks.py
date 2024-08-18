#!/usr/bin/env python3

"""
    contains function that utilizes async.Task
    Imports:
        asyncio
        wait_random
"""

import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
        calls wait_random and returns it as an asyncio.Task
        Args:
            max_delay (int) arg for wait_random
        Returns:
            an asyncio.Task object
    """
    background_task = asyncio.create_task(wait_random(max_delay))
    return background_task

#!/usr/bin/env python3

"""
Asynchronous Tasks Management

This module demonstrates spawning multiple asynchronous tasks and managing their
execution and results.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(task_count: int, max_delay: int) -> List[float]:
    """
    Spawn 'wait_random' task_count times with the specified max_delay.

    Args:
    task_count (int): The number of tasks to spawn.
    max_delay (int): The maximum delay for each task.

    Returns:
    List[float]: A list of delays for each completed task.
    """

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(task_count)]
    return [await task for task in asyncio.as_completed(tasks)]
    

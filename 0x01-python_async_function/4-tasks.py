#!/usr/bin/env python3
"""The basics of async"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(task_count: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random task_count times with the specified max_delay.

    Args:
    task_count (int): The number of tasks to spawn.
    max_delay (int): The maximum delay for each task.

    Returns:
    List[float]: A list of delays for each completed task.
    """
    tasks = [task_wait_random(max_delay) for _ in range(task_count)]
    completed_tasks = [await task for task in asyncio.as_completed(tasks)]
    return completed_tasks

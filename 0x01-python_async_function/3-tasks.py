#!/usr/bin/env python3
"""Async basics"""

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Creates an asyncio Task for the wait_random function with a specified max_delay.

    Args:
    max_delay (int): The maximum delay for the wait_random function.

    Returns:
    Task: An asyncio Task object for the wait_random function.
    """
    task = create_task(wait_random(max_delay))
    return task
    

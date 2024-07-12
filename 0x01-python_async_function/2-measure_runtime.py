#!/usr/bin/env python3
"""The basics of async"""

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(task_count: int, max_delay: int) -> float:
    """
    Measure the average runtime of executing 'wait_n' tasks.

    Args:
    task_count (int): The number of tasks to spawn.
    max_delay (int): The maximum delay for each task.

    Returns:
    float: The average runtime per task.
    """
    start_time = time()

    run(wait_n(task_count, max_delay))

    end_time = time()

    total_time = end_time - start_time
    average_time = total_time / task_count

    return average_time
    

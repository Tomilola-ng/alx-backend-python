#!/usr/bin/env python3

"""
ASYNC
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (included as a float value)
    seconds and eventually returns the delay.

    Args:
    max_delay (int): Maximum delay time in seconds (default is 10).

    Returns:
    float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
    

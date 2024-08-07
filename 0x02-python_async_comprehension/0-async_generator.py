#!/usr/bin/env python3

"""
    ASYNCHRONOUS TASKS
    USING ASYNCIO, AND RANDOM
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
        A coroutine that yields 10 random numbers between 0 and 10.
        Each yield is preceded by an asynchronous wait of 1 second.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

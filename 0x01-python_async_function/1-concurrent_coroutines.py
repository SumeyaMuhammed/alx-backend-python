#!/usr/bin/env python3
"""
This module contains a coroutine that spawns multiple instances of another coroutine
and returns a list of delays in ascending order.
"""

import asyncio
import importlib
from typing import List

# Dynamically import the module with a name that starts with a number
basic_async_syntax = importlib.import_module('0-basic_async_syntax')

# Access the wait_random function from the imported module
wait_random = basic_async_syntax.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay for each call.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays

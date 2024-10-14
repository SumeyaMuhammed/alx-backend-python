#!/usr/bin/env python3
"""
This module contains a function that spawns multiple tasks and returns a list of delays.
"""

import asyncio
import importlib
from typing import List

tasks_module = importlib.import_module('3-tasks')

task_wait_random = tasks_module.task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay and returns a list of delays.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays

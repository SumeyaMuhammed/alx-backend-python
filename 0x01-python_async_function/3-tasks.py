#!/usr/bin/env python3
"""
This module contains a function that creates an asyncio.Task using a coroutine.
"""

import asyncio
import importlib

basic_async_syntax = importlib.import_module('0-basic_async_syntax')

wait_random = basic_async_syntax.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task using the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: The created task.
    """
    return asyncio.create_task(wait_random(max_delay))

#!/usr/bin/env python3
"""
This module contains a function that measures the runtime of an asynchronous coroutine.
"""

import time
import asyncio
import importlib

concurrent_coroutines = importlib.import_module('1-concurrent_coroutines')

wait_n = concurrent_coroutines.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns the average time per task.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay for each call.

    Returns:
        float: The average time per task.
    """
    start_time = time.time()  
    asyncio.run(wait_n(n, max_delay)) 
    end_time = time.time()  
    total_time = end_time - start_time 
    return total_time / n 

#!/usr/bin/env python3
'''
This module contains a solution for task 1
'''
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """_summary_

    Returns:
        List[float]: _description_
    """
    return [i async for i in async_generator()]

#!/usr/bin/env python3
'''
This module contains a solution for task 0
'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """_summary_

    Returns:
        AsyncGenerator[float, None]: _description_

    Yields:
        Iterator[AsyncGenerator[float, None]]: _description_
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10

#!/usr/bin/env python3
'''This module provides a type-annotated function that takes a float as argument and returns a function that multiplies a float by it.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function.
    '''
    return lambda x: x * multiplier

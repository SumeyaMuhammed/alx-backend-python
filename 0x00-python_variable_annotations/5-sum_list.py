#!/usr/bin/env python3
'''This module provides a type-annotated function which takes a list of floats as argument and returns their sum as a float.
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Computes the sum of a list of floating-point numbers.
    '''
    return float(sum(input_list))

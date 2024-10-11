#!/usr/bin/env python3
'''This module uses mypy to validate a given piece of code and apply any necessary changes.
'''
from typing import List, Tuple, Union, Sequence

def zoom_array(lst: Sequence[Union[int, float]], factor: int = 2) -> List[Union[int, float]]:
    """
    Zooms in on the elements of the array by repeating each element a specified number of times.

    Returns:
    List[Union[int, float]]: A list with the elements repeated according to the specified factor.
    """
    zoomed_in: List[Union[int, float]] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3) 

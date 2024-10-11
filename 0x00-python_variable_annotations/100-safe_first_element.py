#!/usr/bin/env python3
'''This module augments a given code with the correct duck-typed annotations:
'''
from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it exists, otherwise returns None.
    """
    if lst:
        return lst[0]
    return None

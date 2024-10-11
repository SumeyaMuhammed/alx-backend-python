#!/usr/bin/env python3
'''This module adds type annotations to the function.
'''
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely gets the value from a dictionary-like mapping for the specified key.

    Returns:
    Union[Any, T]: The value associated with the key if found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

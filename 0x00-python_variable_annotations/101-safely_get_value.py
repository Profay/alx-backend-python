#!/usr/bin/env python3
""" More involved type annotations module
"""

from typing import Sequence, Union, Any, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Return a value in a dictionary
    or default value
    """
    if key in dct:
        return dct[key]
    else:
        return default

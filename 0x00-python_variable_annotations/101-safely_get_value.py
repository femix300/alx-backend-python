#!/usr/bin/env python3
'''More involved type annotations'''
from typing import Union, Any, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    '''type annotations practice'''
    if key in dct:
        return dct[key]
    else:
        return default

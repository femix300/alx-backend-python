#!/usr/bin/env python3
'''Duck typing - first element of a sequence'''
from typing import Iterable, Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''duck type annotations praactice'''
    if lst:
        return lst[0]
    else:
        return None

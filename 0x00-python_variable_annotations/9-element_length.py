#!/usr/bin/env python3
''' Let's duck type an iterable object'''
from typing import Tuple, List, Sequence, Iterable, Any


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns appropriate type'''

    return [(i, len(i)) for i in lst]

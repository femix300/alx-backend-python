#!/usr/bin/env python3
'''Complex types - mixed list'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Returns the sum of a mixed list contating ints and floats'''

    return sum(mxd_lst)

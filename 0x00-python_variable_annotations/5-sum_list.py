#!/usr/bin/env python3
from typing import List
from functools import reduce

'''Complex types - list of floats'''


def sum_list(input_list: List[float]) -> float:
    '''Returns the sum of a list of floats'''

    return reduce(lambda x, y: x + y, input_list)

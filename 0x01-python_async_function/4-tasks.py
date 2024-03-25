#!/usr/bin/env python3
'''Asynchronus tasks'''
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Calls the task_wait_random function for n times
    and returns a list containing its return value
    '''

    list_of_delays = []
    for i in range(n):
        delay = await task_wait_random(max_delay)
        list_of_delays.append(delay)
    return list_of_delays

#!/usr/bin/env python3
'''Asynchronus tasks'''
from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Calls the task_wait_random function for n times
    and returns a list containing its return value
    '''

    tasks = []
    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)
    return [await task for task in asyncio.as_completed(tasks)]

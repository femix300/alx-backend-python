#!/usr/bin/env python3
'''Execute multiple coroutines using async'''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    '''
    Calls the wait random function for n times
    and returns a list containing its return value
    '''

    list_of_delays = []
    for i in range(n):
        delay = await wait_random(max_delay)
        list_of_delays.append(delay)
    return list_of_delays

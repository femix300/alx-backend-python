#!/usr/bin/env python3
'''
A program that demonstrates basic asynchronus
programming in JavaScript
'''
import random
import asyncio


async def wait_random(max_delay=10):
    '''Sleeps for a random number of seconds'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

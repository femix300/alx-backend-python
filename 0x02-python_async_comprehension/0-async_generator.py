#!/usr/bin/env python3
'''Async Generators'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Yields a random number every 10 seconds'''
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)

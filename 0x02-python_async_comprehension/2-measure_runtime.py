#!/usr/bin/env python3
'''Run time for four parallel comprehensions'''
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measure the running time'''
    start_time = time.time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time

#!/usr/bin/env python3
'''Task 2: Run time for four parallel comprehensions
'''
import asyncio
from time import time
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Execute async_comprehension four times in parallel using asyncio.gather.
    Measure the total runtime and return it.
    '''
    start_time = time()

    # Run async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time()

    return end_time - start_time

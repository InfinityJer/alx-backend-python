#!/usr/bin/env python3
"""
1-concurrent_coroutines.py - Module containing an asynchronous routine
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay value.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    delays = []

    # Create a list to store the tasks
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Execute the tasks concurrently
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays


if __name__ == "__main__":
    # Example usage
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))

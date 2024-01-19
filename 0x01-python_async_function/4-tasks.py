#!/usr/bin/env python3
"""
4-tasks.py - Module containing a function to create asyncio.Tasks
"""

import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns task_wait_random n
    times with the specified max_delay.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay value.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    delays = []

    # Create a list to store the tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Execute the tasks concurrently
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays


if __name__ == "__main__":
    # Example usage
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))

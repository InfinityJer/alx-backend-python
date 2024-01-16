#!/usr/bin/env python3
"""
3-tasks.py - Module containing a regular function to create an asyncio.Task
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function that takes an integer max_delay returns an asyncio task

    Args:
        max_delay (int): Maximum delay value.

    Returns:
        asyncio.Task: Task representing the execution of wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))


if __name__ == "__main__":
    # Example usage in an async function
    async def test(max_delay: int) -> None:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))

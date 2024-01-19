#!/usr/bin/env python3
"""
0-basic_async_syntax.py - Module containing an asynchronous coroutine
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Async coroutine that awaits a random delay (0 to max_delay seconds) and eventually returns the result

    Args:
        max_delay (int): Maximum delay value (default is 10).

    Returns:
        float: Random delay between 0 and max_delay seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


if __name__ == "__main__":
    # Example usage
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))

#!/usr/bin/env python3
"""
Async Generator Module
"""

import asyncio
import random
import typing


async def async_generator() -> typing.AsyncGenerator[float, None]:
    """
    Coroutine that yields a random number between 0 and 10 after
    asynchronously waiting 1 second, repeated 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

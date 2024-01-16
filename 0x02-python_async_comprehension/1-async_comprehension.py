#!/usr/bin/env python3
'''Task 1: Async Comprehension
'''
import typing


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    '''Collect 10 random numbers using async comprehension over async_gen.
    Returns:
        List of 10 random numbers.
    '''
    return [i async for i in async_generator()]

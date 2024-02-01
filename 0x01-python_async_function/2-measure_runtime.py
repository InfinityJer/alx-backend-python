#!/usr/bin/env python3
"""
2-measure_runtime.py - Module containing a function to measure runtime
"""

import time
import asyncio  # Add this line to import the asyncio module
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay value.

    Returns:
        float: Average execution time per call.
    """
    start_time = time.time()

    # Measure the total execution time for wait_n
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    # Calculate average execution time per call
    avg_time_per_call = total_time / n

    return avg_time_per_call


if __name__ == "__main__":
    # Example usage
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))

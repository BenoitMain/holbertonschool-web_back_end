#!/usr/bin/env python3
"""
Module for executing multiple asynchronous waits and returning sorted delays.

Functions:
    wait_n(n: int, max_delay: int) -> list[float]:
    Spawns n wait_random coroutines & returns their delays in ascending order.
"""

import asyncio
import importlib

wait_random = importlib.import_module("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """

    Args:
        n (int): Number of coroutines to spawn.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        list[float]: List of delays (float values) in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    result = []
    for delay in delays:
        i = 0
        while i < len(result) and result[i] < delay:
            i += 1
        result.insert(i, delay)
    return result

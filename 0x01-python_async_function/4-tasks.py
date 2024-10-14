#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async
mandatory
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random function n times

    Args:
        n (int): number of time wait _random should be callled.
        max_delay (int): delay period

    Returns:
        List[float]: List of all the delays in sorted order
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)

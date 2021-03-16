#!/usr/bin/env python3
'''
The basics of async
'''
import asyncio
from random import uniform


async def wait_random(max_delay: float = 10.0) -> float:
    d = uniform(max_delay, 0)
    return d

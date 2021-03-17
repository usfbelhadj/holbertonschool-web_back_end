#!/usr/bin/env python3
'''
Let's execute multiple coroutines at the same time with async
'''

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Take the code from wait_n and alter it into a new function task_wait_n./
    The code is nearly identical to wait_n except task_wait_random is /
    being called.
    '''

    n_wait = []
    comp_wait = []

    for i in range(n):
        n_wait.append(wait_random(max_delay))
    for i in asyncio.as_completed(n_wait):
        comp_wait.append(await i)
    return comp_wait

#!/usr/bin/env python3
'''
Async Comprehensions
'''


import asyncio

from random import uniform

from typing import List

a_g = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Import async_generator from the previous task and then write/
    a coroutine called async_comprehension that takes no arguments.
    The coroutine will collect 10 random numbers using an async/
    comprehensing over async_generator, then return the 10 random numbers.
    '''
    Numbers = []
    async for i in a_g():
        Numbers.append(i)
    return Numbers

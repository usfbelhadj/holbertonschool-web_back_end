#!/usr/bin/env python3
'''
Async Generator
'''


import asyncio

from random import uniform


async def async_generator():
    '''
    Write a coroutine called async_generator that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously wait 1 second,/
    then yield a random number between 0 and 10. Use the random module.
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)

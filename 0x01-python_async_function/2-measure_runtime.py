#!/usr/bin/env python3
'''
Measure the runtime
'''
import asyncio
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Create a measure_time function with integers n and max_delay as arguments/
    that measures the total execution time for wait_n(n, max_delay),/
    and returns total_time / n. Your function should return a float.
    '''
    start_loop = time()
    asyncio.run(wait_n(n, max_delay))
    end_loop = time() - start_loop
    return end_loop / n

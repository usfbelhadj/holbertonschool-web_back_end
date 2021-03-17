#!/usr/bin/env python3

import asyncio


async def test():
    for i in range(9):
        await asyncio.sleep(1)
        print('Hello {}'.format(i))

print(asyncio.run(test()))

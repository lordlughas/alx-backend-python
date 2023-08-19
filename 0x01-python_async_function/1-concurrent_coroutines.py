#!/usr/bin/env python3
'''Task 1's module
'''
from typing import List
import asyncio

async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    function that returns a sorted list of float numbers gotten randomly
    '''
    wait_random = __import__('0-basic_async_syntax').wait_random

    delay_list = []
    i = 0

    while i < n:
        delay_list.append(await wait_random(max_delay))
        i += 1

    return sorted(delay_list)


if __name__ == '__main__':
    print(asyncio.run(wait_n(5, 2)))
    print(asyncio.run(wait_n(7, 4)))
    print(asyncio.run(wait_n(10, 0)))

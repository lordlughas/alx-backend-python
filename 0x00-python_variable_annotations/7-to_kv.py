#!/usr/bin/env python3

'''module that takes two argument and return a tuple'''


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''function that returns a tuple'''
    return(k, v**2)


if __name__ == '__main__':
    print(to_kv.__annotations__)
    print(to_kv('eggs', 3))
    print(to_kv('school', 0.02))

#!/usr/bin/env python3

""" Module to return a string representation """


def to_str(n: float) -> float:
    return str(n)


if __name__ == "__main__":
    print(f'to_str(3.142)')
    print(to_str(0.00))

    print(to_str.__annotations__)

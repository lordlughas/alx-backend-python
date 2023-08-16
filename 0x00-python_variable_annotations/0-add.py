#!/usr/bin/env python3

""" A python module that returns the summation of two float numbers """


def add(a: float, b:float) -> float:
    """ A function that takes two float numbers and returns their sum"""
    return a + b


if __name__ == '__main__':

    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)

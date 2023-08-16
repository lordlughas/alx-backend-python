#!/usr/bin/env python3

""" module that concatenates two string"""


def concat(str1: str, str2: str) -> str:
    ''' function to concatenates two strings'''
    return str1 + str2


if __name__ == '__main__':
    
    str1 = "egg"
    str2 = "shell"
    print(concat(str1, str2) == "{}{}".format(str1, str2))
    print(concat.__annotations__)

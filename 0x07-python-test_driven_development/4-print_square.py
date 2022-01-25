#!/usr/bin/python3
"""
4-print_square
a function that prints a square with the character #
"""


def print_square(size):
    """size is the size of the square
    size must be an integer, more than of 0,
    and no float"""

    if type(size) is not (int):
        if type(size) is float and size < 0:
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()

#!/usr/bin/python3
"""

0-add_integer.py
Function that adds 2 integers.
"""


def add_integer(a, b=98):
    """Comprobar que el numbero no es un float,
    si no es un float ni un int devolver: a/b must be an integer
    Return a + b"""
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    return a + b

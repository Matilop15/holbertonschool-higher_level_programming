#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
        if a < b:
            c = a + b
            return(c)
        else:
            return(sub(a, b))

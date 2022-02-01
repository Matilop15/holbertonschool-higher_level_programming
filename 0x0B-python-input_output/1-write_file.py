#!/usr/bin/python3
# Matias López <3959@holbertonschool.com>
"""
1-write_file.py
a function that writes a string to a text file
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """write a string and return number of characters"""
    with open(filename, encoding='UTF-8') as f:
        for line in f:
            return len(f.readline())

#!/usr/bin/python3
# Matias López <3959@holbertonschool.com>
"""
2-append_write.py
a function that appends a string at the end of a text file
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """if the file doesn’t exist, it should be created
    'a' open file for add
    """
    with open(filename, 'a') as f:
        characters = f.write(text)

    return characters

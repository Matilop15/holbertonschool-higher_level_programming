#!/usr/bin/python3
# Matias López <3959@holbertonschool.com>
"""
4-from_json_string.py
a function that returns an object (Python data structure)
represented by a JSON string
"""


import json


def from_json_string(my_str):
    """(Python data structure) represented by a JSON"""
    return json.loads(my_str)

#!/usr/bin/python3
# Matias López <3959@holbertonschool.com>
"""
6-load_from_json_file.py
a function that creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """using JSON create an object"""
    with open(filename, 'r') as f:
        return json.load(f)

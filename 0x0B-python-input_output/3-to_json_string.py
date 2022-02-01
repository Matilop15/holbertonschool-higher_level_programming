#!/usr/bin/python3
# Matias López <3959@holbertonschool.com>
"""
3-to_json_string.py
a function that returns the JSON representation of an object (string)
"""


import json

def to_json_string(my_obj):
    """change representacion of an object with JSON"""
    return json.dumps(my_obj)

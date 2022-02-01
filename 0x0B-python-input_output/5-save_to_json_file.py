#!/usr/bin/python3
# Matias López <3959@holbertonschool.com>
"""
5-save_to_json_file.py
a function that writes an Object to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """write an object using JSON"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))

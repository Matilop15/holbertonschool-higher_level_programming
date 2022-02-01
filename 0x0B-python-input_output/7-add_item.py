#!/usr/bin/python3
# Matias López <3959@holbertonschool.com>
"""
7-add_item.py
a script that adds all arguments to a Python list
"""


import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    arch = load_from_json_file("add_item.json")
    save_to_json_file(arch + sys.argv[1:], "add_item.json")
except Exception:
    save_to_json_file(sys.argv[1:], "add_item.json")

#!/usr/bin/python3
"""
 sends a request to the URL and displays the value of the variable
"""

import requests
import sys

if __name__ = "__main__":
	try:
		with requests.head('X-Request-Id') as resp:
			if resp is not None:
				print(resp)
	except Exception:
	pass

#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    resp = request.get('https://intranet.hbtn.io/status')
    if resp is not None:
        print('Body response:$')
        print('\t- type: {}'.format(type(resp.txt)))
        print('\t- content: {}'.format(respt.txt))

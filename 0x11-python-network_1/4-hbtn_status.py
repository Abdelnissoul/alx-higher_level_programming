#!/usr/bin/python3
"""
Scripy in py to fetch https://alx-intranet.hbtn.io/status
"""

import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    respond = requests.get(url)
    print("Body response:")
    print("\t- type:", type(respond.text))
    print("\t- content:", respond.text)

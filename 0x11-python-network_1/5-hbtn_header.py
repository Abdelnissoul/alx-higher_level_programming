#!/bin/bash/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id"""


import sys
import requests


if __name__ == "__main__":
    resp = get(argv[1])
    print(resp.headers.get('X-Request-Id'))

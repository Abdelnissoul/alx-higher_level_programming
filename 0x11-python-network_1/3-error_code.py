#!/usr/bin/python3
"""
Python script that sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.error
import sys


if __name__ == '__main__':
    argv = sys.argv
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as er:
        print("Error code: {}".format(er.status))

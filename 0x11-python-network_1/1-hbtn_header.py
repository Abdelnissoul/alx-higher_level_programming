#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
nd displays the value of the X-Request-Id
"""


if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        id_req = response.headers["X-Request-Id"]
        print(id_req)

#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        subject = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(subject)))
        print("\t- content: {}".format(subject))
        print("\t- utf8 content: {}".format(subject.decode("utf-8")))


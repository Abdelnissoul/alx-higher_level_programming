#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display id
"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    user_name = argv[1]
    password = argv[2]

    url = "https://api.github.com/user"
    resp = get(url, auth=(user_name, password))

    if resp.status_code == 200:
        user_data = resp.json()
        print(user_data.get('id'))
    else:
        print("Authentication failed or unable to fetch user data.")

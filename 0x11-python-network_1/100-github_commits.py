#!/usr/bin/python3
"""
listing 10 commits (from the most recent to oldest) of the repository
"""


if __name__ == '__main__':
    from requests import get
    from sys import argv

    repo = argv[1]
    owner = argv[2]
    i = 0

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    response = get(url)

    if response.status_code == 200:
        response_json = response.json()
        for element in response_json:
            if i > 9:
                break
            sha = element.get('sha')
            author = element.get('commit').get('author').get('name')
            print("{}: {}".format(sha, author))
            i += 1
    else:
        print("Error:", response.status_code)

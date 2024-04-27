#!/usr/bin/python3
"""
Py script that sends a request to the URL
and displays the body of the response.
"""


if __name__ == '__main__':
    from requests import post
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': argv[1] if len(argv) >= 2 else ""}
    resp = post(url, data)

    content_type = resp.headers.get('content-type')

    if content_type == 'application/json':
        result = resp.json()
        if result:
            user_id = result.get('id')
            user_name = result.get('name')
            if user_id is not None and user_name:
                print("[{}] {}".format(user_id, user_name))
            else:
                print('No result')
        else:
            print('No result')
    else:
        print('Not a valid JSON')

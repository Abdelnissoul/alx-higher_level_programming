#!/bin/bash
# Takes in a URL and gives all the HTTP methods that the server will accept

curl -s -I "${1}" | grep "Allow:" | cut -d " " -f 2-

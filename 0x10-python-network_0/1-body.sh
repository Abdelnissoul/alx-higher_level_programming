#!/bin/bash
# sends a GET request, after taking in a URL and displays the body if the status code is 200

response=$(curl -s -o /dev/null -w "%{http_code}" "$1")

if [[ $response -eq 200 ]]; then
    curl -s "$1"
fi

#!/bin/bash
# sends a GET request, after taking in a URL and displays the body if the status code is 200
curl -s -L "${1}"

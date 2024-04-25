#!/bin/bash
# Sends a request and takes a URl and displays the size of the response body
curl -s "${1}" | wc -c

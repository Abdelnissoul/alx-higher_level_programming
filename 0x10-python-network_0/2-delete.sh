#!/bin/bash
# DELETE request to the URL as the first argument and displays the body of the response
curl -s -X DELETE "${1}"

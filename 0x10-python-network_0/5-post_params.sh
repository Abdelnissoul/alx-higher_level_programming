#!/bin/bash
# Takes in a URL, sends a POST request with specified parameters, and gives the response

curl -s -X POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"

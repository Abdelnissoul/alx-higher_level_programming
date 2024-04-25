#!/bin/bash
# This is a Script that makes a request for having a specific answer
curl -s -X PUT -L -d "user_id=98" 0.0.0.0:5000/catch_me

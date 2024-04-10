#!/bin/bash

# Make a request to the server and follow redirects
curl -L -X PUT -s -d "user_id=98" -H "Referer: You got me!" http://0.0.0.0:5000/catch_me

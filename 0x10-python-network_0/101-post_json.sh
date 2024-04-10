#!/bin/bash
# Send post request using json file
myjson="$2"
curl -X POST -H "Content-Type: application/json" -d @"$myjson" "$1"

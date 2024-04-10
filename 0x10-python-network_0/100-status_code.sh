#!/bin/bash
# Get the response code only
curl -o /dev/null -s -w "%{http_code}" $1

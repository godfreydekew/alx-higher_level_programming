#!/bin/bash
# Display request methods available
curl -v -X OPTIONS -i "$1" 2>/dev/null | grep -i "^Allow:" | cut -d ' ' -f 2-

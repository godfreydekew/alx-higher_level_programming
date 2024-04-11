#!/usr/bin/python3
""" Sends a post request with data"""
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    params = {
        "email": sys.argv[2]
    }
    query_string = urllib.parse.urlencode(params)
    data = query_string.encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        """Prints the response after the post request"""
        data = response.read()
        print(data.decode('utf-8'))

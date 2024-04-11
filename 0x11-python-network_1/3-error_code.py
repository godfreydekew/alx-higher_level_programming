#!/usr/bin/python3
""" Displays errcode information"""
import urllib.request
from urllib.error import HTTPError, URLError
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            """Prints the response after the post request"""
            print(response.read().decode('utf-8'))
    except HTTPError as err:
        print(f"Error code: {err.code}")

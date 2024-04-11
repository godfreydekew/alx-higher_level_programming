#!/usr/bin/python3
""" fetches json data"""
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        """Displays a specific item value in th headers"""
        print(response.headers['X-Request-Id'])

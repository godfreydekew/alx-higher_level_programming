#!/usr/bin/python3
"""Post request with paramaters"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    response = requests.post(url, json=data)
    print(response.text)

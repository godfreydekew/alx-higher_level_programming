#!/usr/bin/python3
"""Accesing a variable in response headers"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers["X-Request-Id"])

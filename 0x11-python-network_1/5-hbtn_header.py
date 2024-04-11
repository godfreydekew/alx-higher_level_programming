#!/usr/bin/python3
"""Accesing a variable in response headers"""
import requests
import sys


url = sys.argv[1]
response = requests.get(url)
print(response.headers["X-Request-Id"])

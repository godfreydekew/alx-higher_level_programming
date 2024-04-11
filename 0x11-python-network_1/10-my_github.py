#!/usr/bin/python3
"""Connects to the Github APT server"""
import requests
import sys


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    auth = requests.auth.HTTPBasicAuth(username, password)
    response = requests.get(url, auth=auth)
    print(response.json().get("id"))

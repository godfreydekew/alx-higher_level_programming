#!/usr/bin/python3
"""Prints the latest 10 commits"""
import requests
import sys

if __name__ == '__main__':
    owner = sys.argv[2]
    repo = sys.argv[1]
    url = 'https://api.github.com/repos/{owner}/{repo}/commits'
    params = {
        'per_page': '10',
    }
    for commit in requests.get(url.format(
            owner=owner, repo=repo), params=params).json():
        print("{}: {}".format(commit.get("sha"), commit.get(
            "commit", {}).get("author", {}).get("name")))

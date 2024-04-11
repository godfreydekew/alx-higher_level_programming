#!/usr/bin/python3
"""Post request and cathing errors"""
import requests
import sys
import json

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    chr = sys.argv[1] if len(sys.argv) == 2 else ""
    params = {
        'q': chr
    }
    response = requests.post(url, data=params)
    try:
        data = response.json()
        if len(data):
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except json.decoder.JSONDecodeError:
        print("Not a valid JSON")

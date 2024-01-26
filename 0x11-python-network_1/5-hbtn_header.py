#!/usr/bin/python3
"""Python script takes in a URL,requests to the URL,displays value"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))

#!/usr/bin/python3
"""info http request"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":

    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.info().get('X-Request-Id'))

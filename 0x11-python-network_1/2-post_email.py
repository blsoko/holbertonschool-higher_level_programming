#!/usr/bin/python3
"""post request"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":

    url = argv[1]
    values = {'email': argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode('UTF-8')
        print(the_page)

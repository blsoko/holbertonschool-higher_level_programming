#!/usr/bin/python3
"""Fetching URL"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        print("Body response:\n\t- type: <class 'bytes'>\n\t" +
              "- content: {}\n\t- utf8 content: OK"
              .format(response.read().decode('UTF-8')))

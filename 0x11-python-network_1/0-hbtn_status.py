#!/usr/bin/python3
"""Fetching URL"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        rpe = response.read()
        print("Body response:\n\t- type: {}\n\t"
              "- content: {}\n\t- utf8 content: {}"
              .format(type(rpe), rpe, rpe.decode('utf-8')))

#!/usr/bin/python3
"""status using handler"""
import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: <class 'str'>\n\t- content: {}"
          .format(r.text))

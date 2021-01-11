#!/usr/bin/python3
"""post email"""
import requests
from sys import argv


if __name__ == "__main__":

    url = argv[1]
    myobj = {'email': argv[2]}

    x = requests.post(url, data=myobj)

    print(x.text)

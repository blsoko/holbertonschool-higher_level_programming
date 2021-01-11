#!/usr/bin/python3
"""github api"""
import requests
from sys import argv
import json


if __name__ == "__main__":

    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[1], argv[2])
    r = requests.get(url)
    cont = 0
    for i in r.json()[:10]:
        cont += 1
        print("{} {}".format(i.get('sha'), i.get('commit')
              .get('author').get('name')))
        if cont == 10:
            break

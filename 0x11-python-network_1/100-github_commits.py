#!/usr/bin/python3
"""github api"""
import requests
from sys import argv


if __name__ == "__main__":

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[1], argv[2])
    r = requests.get(url)
    cont = 0
    for i in r.json():
        cont += 1
        print("{}: {}".format(i.get('sha'), i.get('commit')
              .get('author').get('name')))
        if cont == 10:
            break

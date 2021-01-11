#!/usr/bin/python3
"""github api"""
import requests
from sys import argv


if __name__ == "__main__":

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[1], argv[2])
    r = requests.get(url)
    r = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(r[i].get('sha'), r[i].get('commit')
                  .get('author').get('name')))
    except:
        pass

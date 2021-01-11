#!/usr/bin/python3
"""json api"""
import requests
from sys import argv


if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'
    letter = ""
    if len(argv) == 2:
        letter = "" + argv[1]
    myobj = {'q': letter}
    x = requests.post(url, data=myobj)
    try:
        parse = eval(x.text)
        if parse:
            print("[{}] {}".format(parse.get('id'), parse.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

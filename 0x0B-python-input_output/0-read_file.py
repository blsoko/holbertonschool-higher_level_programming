#!/usr/bin/python3
""" Read file """


def read_file(filename=""):
    """ Read file

    Args:
        filename (str, optional): [doc]. Defaults to "read mode".
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())

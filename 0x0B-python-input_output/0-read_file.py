#!/usr/bin/python3
""" Read file """


def read_file(filename=""):
    """ Read file

    Args:
        filename (str, optional): [doc]. Defaults to "read mode".
    """
    with open(filename) as file:
        print(file.read())

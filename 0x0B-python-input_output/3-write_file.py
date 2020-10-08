#!/usr/bin/python3
""" Write a file, create if it doesn't exist and overwrites
"""


def write_file(filename="", text=""):
    """ Write a file, create if it doesn't exist and overwrites
    Args:
        filename (str): file read in mode utf-8. Defaults to "".
        text (str): text to be written. Defaults to "".
    """
    with open(filename, "w+", encoding="utf-8") as f:
        return(f.write(text))

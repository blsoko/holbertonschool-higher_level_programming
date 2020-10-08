#!/usr/bin/python3
""" Append a file, create a file if it doesn't exist
"""


def append_write(filename="", text=""):
    """ Append a file, create a file if it doesn't exist

    Args:
        filename (str): file read in mode utf-8. Defaults to "".
        text (str): text to be written. Defaults to "".
    """
    with open(filename, "a+", encoding="utf-8") as f:
        return(f.write(text))

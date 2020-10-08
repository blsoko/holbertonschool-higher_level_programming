#!/usr/bin/python3
""" Write a function that inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """ Write a function that inserts a line of text to a file

    Args:
        filename (str): [description]. Defaults to "".
        search_string (str): [description]. Defaults to "".
        new_string (str): [description]. Defaults to "".
    """
    with open(filename, "r+", encoding='utf-8') as f:
        emptystr = ""
        while True:
            line = f.readline()
            emptystr = emptystr + line
            if not line:
                break
            if search_string in line:
                emptystr = emptystr + new_string
        f.seek(0)
        f.write(emptystr)

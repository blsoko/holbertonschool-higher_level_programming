#!/usr/bin/python3
""" Count number of lines
Returns: [int]: [number of lines]
"""


def number_of_lines(filename=""):
    """ return number of lines

    Args:
        filename (str): file read in mode utf-8. Defaults to "".

    Returns:
        [int]: [number of lines]
    """
    with open(filename, "r", encoding="utf-8") as file:
        line_n = 0
        while True:
            line = file.readline()
            if not line:
                break
            line_n += 1
        return line_n

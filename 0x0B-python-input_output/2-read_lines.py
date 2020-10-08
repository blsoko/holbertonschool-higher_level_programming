#!/usr/bin/python3
""" Read file and print number of lines:
"""


def read_lines(filename="", nb_lines=0):
    """ Read file and print number of lines:

    Args:
        filename (str): file read in mode utf-8. Defaults to "".
        nb_lines (int): Number of lines. Defaults to 0.
    """
    with open(filename, "r", encoding="utf-8") as file:
        line_n = 1
        if nb_lines <= 0:
            print(file.read(), end='')
        else:
            line = file.readline()
            while line and line_n <= nb_lines:
                print(line, end='')
                if not line:
                    break
                line = file.readline()
                line_n += 1

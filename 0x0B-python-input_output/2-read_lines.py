#!usr/bin/python3
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
            for i in range(nb_lines):
                print(file.readline(), end='')

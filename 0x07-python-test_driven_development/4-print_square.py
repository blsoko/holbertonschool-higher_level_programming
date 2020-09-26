#!/usr/bin/python3
"""print_square"""


def print_square(size):
    """print_square

    Args:
        size ([type]): [description]

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for k in range(size):
        for j in range(size):
            print("#", end='')
        print()
    if size == 0:
        print("")

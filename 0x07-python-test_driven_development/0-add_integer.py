#!/usr/bin/python3
"""add_integer: sum of two integers
"""
def add_integer(a, b=98):
    """sum of two integers

    Args:
        a (int): n
        b (int, 98): n. Defaults to 98.

    Returns:
        int: sum
    """
    if type(a) == float:
        a = int(a)
    elif type(b) == float:
        b = int(a)
    elif type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    return a + b
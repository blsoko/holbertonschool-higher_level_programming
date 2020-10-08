#!/usr/bin/python3
""" Write a function that returns the dictionary description

    Returns:
        [dict]: [description]
"""


def class_to_json(obj):
    """ Write a function that returns the dictionary description

    Args:
        obj ([type]): object to being converted into a dict

    Returns:
        [dict]: [description]
    """
    return obj.__dict__

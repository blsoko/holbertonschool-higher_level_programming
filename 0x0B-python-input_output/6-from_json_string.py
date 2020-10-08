#!/usr/bin/python3
""" Converts into a python object
"""
import json


def from_json_string(my_str):
    """ Converts into a python object

    Args:
        my_str ([type]): json object
    """
    return(json.loads(my_str))

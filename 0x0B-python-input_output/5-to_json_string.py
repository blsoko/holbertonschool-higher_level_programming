#!/usr/bin/python3
""" convert to json string format
"""
import json


def to_json_string(my_obj):
    """ convert to json string format

    Args:
        my_obj ([type]): object to be changed
    """
    return(json.dumps(my_obj))

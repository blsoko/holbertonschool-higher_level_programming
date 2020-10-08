#!/usr/bin/python3
""" Encoding json file
"""
import json


def save_to_json_file(my_obj, filename):
    """ Encoding json file

    Args:
        my_obj ([type]): object in python to json encoding
        filename (str): file write in mode utf-8. Defaults to "".
    """
    with open(filename, "w+", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))

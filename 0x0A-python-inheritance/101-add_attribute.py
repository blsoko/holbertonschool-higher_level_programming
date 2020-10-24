#!/usr/bin/python3
"""Write a function that adds a new attribute to an object if it’s possible"""


def add_attribute(mc, name, name2):
    """Write a function that adds a new attribute to an object if it’s
    possible"""
    if '__dict__' not in dir(mc):
        raise TypeError("can't add new attribute")
    else:
        setattr(mc, name, name2)

#!/usr/bin/python3
"""if the object is an instance of a class"""


def inherits_from(obj, a_class):
    """ if the object is an instance of a class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class

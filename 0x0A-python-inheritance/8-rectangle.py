#!/usr/bin/python3
"""Write a class BaseGeometry"""


class BaseGeometry:
    """Write a class BaseGeometry"""
    def area(self):
        """ Area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates if int > 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Write a class Rectangle"""
    def __init__(self, width, height):
        """ initialization """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

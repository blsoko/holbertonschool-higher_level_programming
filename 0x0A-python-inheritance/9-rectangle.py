#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseGeometry"""


class BaseGeometry:
    """Write a class Rectangle that inherits from BaseGeometry"""
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
    """Write a class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """ initialization """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Area of rectangle"""
        return (self.__height * self.__width)

    def __str__(self):
        """ str method """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

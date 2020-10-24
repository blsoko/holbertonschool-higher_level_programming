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
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """ Area of rectangle"""
        return (self.__height * self.__width)

    def __str__(self):
        """ str method """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """Write a class Square that inherits from Rectangle"""
    def __init__(self, size):
        """ initialization """
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """area of square"""
        return (self.__size * self.__size)

    def __str__(self):
        """str method"""
        return str("[Square] {}/{}".format(self.__size, self.__size))

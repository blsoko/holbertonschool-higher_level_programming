#!/usr/bin/python3
"""[class Rectangle that defines a rectangle]"""


class Rectangle:
    """[class Rectangle that defines a rectangle]"""
    def __init__(self, width=0, height=0):
        """[class Rectangle that defines a rectangle]"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """[rectangle's width]"""
        return self.__width

    @width.setter
    def width(self, width):
        """[rectangle's width]"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """[rectangle's height]"""
        return self.__height

    @height.setter
    def height(self, height):
        """[rectangle's height]"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """[rectangle's area]"""
        return (self.__height * self.__width)

    def perimeter(self):
        """[rectangle's perimeter]"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

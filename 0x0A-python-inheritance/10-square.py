#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseGeometry"""
Recta = __import__("9-rectangle").Rectangle


class Square(Recta):
    """Write a class Square that inherits from Rectangle"""
    def __init__(self, size):
        """ initialization """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of square"""
        return (self.__size * self.__size)

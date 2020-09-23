#!/usr/bin/python3
'''4-square.py: class square'''


class Square:
    """
        Prototype of a square
    """
    def __init__(self, size=0):
        """[summary]

        Args:
            size (int, optional): [size of square]. Defaults to 0.

        """        '''Define Square instance in size'''
        self.size = size

    @property
    def aSquare(self):
        """[return area of square]

        Returns:
            [type]: [int]
        """
        return self.__size

    @aSquare.setter
    def aSquare(self, value):
        """[summary]

        Args:
            value (int, optional): [size of square]. Defaults to 0.

        Raises:
            TypeError: [size must be >= 0]
            TypeError: [size must be an integer]
        """        '''Define Square instance in size'''
        if (type(value) is int):
            if (value < 0):
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """[return area of square]

        Returns:
            [type]: [int]
        """
        if type(self.size) is int:
            return (self.size * self.size)
        else:
            raise TypeError("size must be an integer")

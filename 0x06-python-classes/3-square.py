#!/usr/bin/python3
'''3-square.py: class square'''


class Square:
    """
        Prototype of a square
    """
    def __init__(self, size=0):
        """[summary]

        Args:
            size (int, optional): [size of square]. Defaults to 0.

        Raises:
            TypeError: [size must be >= 0]
            TypeError: [size must be an integer]
        """        '''Define Square instance in size'''
        if (type(size) is int):
            if (size < 0):
                raise TypeError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """[return area of square]

        Returns:
            [type]: [int]
        """
        return (self.__size * self.__size)

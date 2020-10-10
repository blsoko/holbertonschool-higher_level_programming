#!/usr/bin/python3
'''5-square.py: class square'''


class Square:
    """
        Prototype of a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """[summary]

        Args:
            size (int, optional): [size of square]. Defaults to 0.

        """        '''Define Square instance in size'''
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if (type(position) != tuple or len(position) != 2 or
            type(position[0]) != int or position[0] < 0 or
                type(position[1]) != int or position[1] < 0):
            raise TypeError("position must be a tuple of" +
                            " 2 positive integers")
        self.__position = position

    def area(self):
        """[return area of square]

        Returns:
            [type]: [int]
        """
        return (self.__size * self.__size)

    def my_print(self):
        """ print a square """
        if self.__size == 0:
            print()
        if self.__size != 0:
            for p in range(self.__position[1]):
                print()
        for j in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end='')
            for k in range(self.__size):
                print("#", end='')
            print()

    @property
    def position(self):
        """ Position setter """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter for position"""
        if (type(value) != tuple or len(value) != 2 or type(value[0]) != int or
            value[0] < 0 or type(value[1]) != int or
                value[1] < 0):
            raise TypeError("position must be a tuple of" +
                            " 2 positive integers")
        else:
            self.__position = value

    @property
    def size(self):
        """[return area of square]

        Returns:
            [type]: [int]
        """
        return self.__size

    @size.setter
    def size(self, value):
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
        self.__size = value

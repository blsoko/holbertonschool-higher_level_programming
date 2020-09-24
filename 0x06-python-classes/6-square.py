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
        self.__size = size
        self.__position = position

    def area(self):
        """[return area of square]

        Returns:
            [type]: [int]
        """
        return (self.__size * self.__size)

    def my_print(self):
        """ print a square """
        if self.__size == 0 or self.__position[1] != 0:
            print()
        for j in range(self.__size):
            for x in range(self.__position[0]):
                if self.__position[1] > 0:
                    print("_", end='')
                elif self.__position[1] == 0:
                    print(" ", end='')
            for k in range(self.__size):
                print("#", end='')
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if value:
            if value[0] > 0 and value[1] > 0:
                self.__position = value
            else:
                raise TypeError("position must be a tuple of" +
                                " 2 positive integers")

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

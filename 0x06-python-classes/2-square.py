#!/usr/bin/python3
'''2-square.py: class square'''


class Square:
    '''Create a class named Square with their propery size'''
    def __init__(self, size=0):
        '''Define Square instance in size'''
        if (type(size) is int):
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

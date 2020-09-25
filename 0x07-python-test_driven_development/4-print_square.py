#!/usr/bin/python3

def print_square(size):
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for k in range(size):
        for j in range(size):
            print("#", end='')
        print()
    if size == 0:
        print("")
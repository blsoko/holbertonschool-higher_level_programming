#!/usr/bin/python3
def islower(c):
    num = ord(c)
    for i in range(97, 123):
        if (num == i):
            return True
    return False

#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        num = ord(str[i])
        if (num > 96 and num < 123):
            num = num - 32
        print(chr(num), end='')
    print()

#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    argsCount = len(argv)
    if argsCount != 4:
        print("Usage: {} <a> <operator> <b>" .format(argv[0]))
        exit(1)
    flag = 0
    lista = ['-', '+', '*', '/']
    a = int(argv[1])
    b = int(argv[3])
    for i in range(0, 4):
        if argv[2] == lista[i]:
            flag = 1
    if flag != 1:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if argv[2] == '+':
        print("{} {} {} = {}" .format(argv[1], argv[2], argv[3], add(a, b)))
    elif argv[2] == '-':
        print("{} {} {} = {}" .format(argv[1], argv[2], argv[3], sub(a, b)))
    elif argv[2] == '/':
        print("{} {} {} = {}" .format(argv[1], argv[2], argv[3], div(a, b)))
    else:
        print("{} {} {} = {}" .format(argv[1], argv[2], argv[3], mul(a, b)))

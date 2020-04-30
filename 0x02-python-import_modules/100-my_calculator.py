#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    argsCount = len(argv)
    flag = 0
    lista = ['-', '+', '*', '/']
    if argsCount != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    for i in range(0, 4):
        if argv[2] == lista[i]:
            flag = 1
    if flag != 1:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    result = 0
    result = int(argv[1]) + int(argv[3])
    print("{} {} {} = {}" .format(argv[1], argv[2], argv[3], result))

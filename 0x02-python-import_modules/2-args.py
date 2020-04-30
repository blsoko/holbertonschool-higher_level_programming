#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argsCount = len(sys.argv)
    str = (sys.argv)
    if argsCount == 1:
            print("0 arguments.")
    elif argsCount == 2:
            print("1 argument:\n1: {}" .format(str[1]))
    else:
            print("{:d} arguments:" .format(argsCount - 1))
            for i in range(1, argsCount):
                    print("{:d}: {}" .format(i, str[i]))

#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as er:
        print(er)
        return False
    else:
        return True

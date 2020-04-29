#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        var = number * -1
        saved = (var % 10)
    else:
        saved = number % 10
    print(saved, end='')
    return(saved)

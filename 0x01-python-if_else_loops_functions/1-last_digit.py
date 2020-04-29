#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    var = number * -1
    saved = (var % 10) * -1
else:
    saved = number % 10
if saved < 6:
    print(
        "Last digit of {} is {} and is less than 6 and not 0"
        .format(number, saved))
elif saved > 5:
    print(
        "Last digit of {} is {} and is greater than 5" .format(number, saved))
else:
    print("Last digit of {} is {} and is 0" .format(number, saved))

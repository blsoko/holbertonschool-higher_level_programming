#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = set(my_list)
    a = list(a)
    sum = 0
    for i in range(0, len(a)):
        sum = sum + a[i]
    return(sum)

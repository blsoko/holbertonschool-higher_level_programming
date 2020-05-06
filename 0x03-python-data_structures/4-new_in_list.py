#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        b = [] + my_list
        if (idx >= 0 and idx < len(b)):
            b[idx] = element
        return(b)
    return(my_list)

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lista_c = [0, 0]
    for i in range(0, 2):
        if 0 <= i < len(tuple_a) and 0 <= i < len(tuple_b):
            lista_c[i] = tuple_a[i] + tuple_b[i]
        elif 0 <= i < len(tuple_a) and not (0 <= i < len(tuple_b)):
            lista_c[i] = tuple_a[i] + 0
        elif 0 <= i < len(tuple_b) and not (0 <= i < len(tuple_a)):
            lista_c[i] = 0 + tuple_b[i]
    tuple_c = (lista_c[0], lista_c[1])
    return(tuple_c)

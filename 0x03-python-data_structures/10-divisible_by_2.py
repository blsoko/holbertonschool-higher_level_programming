#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) != 0:
        lista = [[0] for i in range(0, len(my_list))]
        for i in range(0, len(my_list)):
            if (my_list[i] % 2 == 0):
                lista[i] = True
            else:
                lista[i] = False
        return(lista)
    else:
        lista = []
        return(lista)

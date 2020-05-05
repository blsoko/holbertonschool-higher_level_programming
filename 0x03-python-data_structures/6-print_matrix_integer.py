#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print()
    for i in range(0, len(matrix[0])):
        print("{}".format(matrix[i]))

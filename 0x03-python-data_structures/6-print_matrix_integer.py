#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print()
        exit()
    print(matrix[0][0])
    for i in range(0, len(matrix[0])):
        for j in range(0, len(matrix[0])):
            if j != len(matrix[0]) - 1:
                print(matrix[i][j], end=" ")
            else:
                print(matrix[i][j], end="")
        print()

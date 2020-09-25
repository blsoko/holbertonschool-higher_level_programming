#!/usr/bin/python3

def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif all(isinstance(x, list) for x in matrix):
        for i in range(len(matrix)):
            if len(matrix[0]) != len(matrix[i]):
                raise TypeError("Each row of the matrix must have the same size")
        new_matrix = list(map(list, matrix))
        for j in range(len(new_matrix)):
            for i in range(len(new_matrix[0])):
                if type(new_matrix[j][i]) != int:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                new_matrix[j][i] = (float("{:.2f}".format(new_matrix[j][i] / div)))
        return(new_matrix)
    else:
        raise TypeError("Each row of the matrix must have the same size")

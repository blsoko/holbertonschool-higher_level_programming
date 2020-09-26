#!/usr/bin/python3
"""matrix_divided
"""


def matrix_divided(matrix, div):
    """divide matrix

    Args:
        matrix ([type]): [description]
        div ([type]): [description]

    Raises:
        ZeroDivisionError: division by zero
        TypeError: div must be a number
        TypeError: Each row of the matrix must have the same size
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: [description]
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    elif len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    elif type(matrix[0]) == list and len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    elif type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif all(isinstance(x, list) for x in matrix):
        for i in range(len(matrix)):
            if len(matrix[0]) != len(matrix[i]):
                raise TypeError("Each row of the matrix must have" +
                                " the same size")
        new_matrix = list(map(list, matrix))
        for j in range(len(new_matrix)):
            for i in range(len(new_matrix[0])):
                if type(new_matrix[j][i]) != int:
                    raise TypeError("matrix must be a matrix " +
                                    "(list of lists) of integers/floats")
                new_matrix[j][i] = (float("{:.2f}"
                                    .format(new_matrix[j][i] / div)))
        return(new_matrix)
    else:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")

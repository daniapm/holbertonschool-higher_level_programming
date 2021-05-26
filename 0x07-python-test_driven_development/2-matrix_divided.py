#!/usr/bin/python3
"""
module  that adds 2 integers.
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix.
    argc:
        matrix: list of lists of integers or floats
        div: number (integer or float
    """
    if type(div) is None or type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix(list of lists)"
                        " of integers/floats")
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        for j in range(len(matrix)):
            if (type(matrix[i][j])) is not int and (matrix[i][j]) is not float:
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
    return [[round(count/div, 2) for count in i] for i in matrix]

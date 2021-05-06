#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in matrix:
        new = (list(map(lambda x: x ** 2, i)))
        return new

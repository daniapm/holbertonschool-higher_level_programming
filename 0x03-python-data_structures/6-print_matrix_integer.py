#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for fila in matrix:
        count_fila = 1
        for valor in fila:
            if count_fila == len(fila):
                print("{:d}".format(valor), end="")
            else:
                print("{:d}".format(valor), end=" ")
            count_fila = count_fila + 1
        print()

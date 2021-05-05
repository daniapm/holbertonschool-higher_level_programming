#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for fila in matrix:
            count_fila = 1
            for valor in fila:
                if count_fila == 3:
                    print("{}".format(valor))
                else:
                    print("{}".format(valor), end=" ")
                count_fila = count_fila + 1

    else:
        print()

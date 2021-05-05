#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for fila in matrix:
            count_fila = 1
            for valor in fila:
                if count_fila == 3:
                    print(valor)
                else:
                    print(valor, end=" ")
                count_fila = count_fila + 1

    else:
        print()

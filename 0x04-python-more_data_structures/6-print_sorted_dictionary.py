#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for ident, clave in (sorted(a_dictionary.items())):
        print(ident + ':', clave)

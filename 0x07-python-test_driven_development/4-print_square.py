#!/usr/bin/python3
"""
module prints My name is <first name> <last name>
"""


def print_square(size):
    """
    prints square with the character #.
    argc:
        size:  length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(0, size):
            for j in range(0, size):
                print("#", end="")
            print()

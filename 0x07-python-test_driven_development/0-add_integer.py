#!/usr/bin/python3
"""
module  that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    that adds 2 integers.
    argc:
        a: first value
        b: last value
    """
    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")
    elif type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        suma = int(a) + int(b)
        return suma

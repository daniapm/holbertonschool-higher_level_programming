#!/usr/bin/python3
"""
Documentation for a class instance that return true or false
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class
    """
    if type(obj) == a_class:
        return True
    else:
        return False

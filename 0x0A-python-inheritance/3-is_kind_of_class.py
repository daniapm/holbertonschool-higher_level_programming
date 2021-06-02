#!/usr/bin/python3
"""
Documentation for a class instance that return true or false
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an
    instance of a class that inherited from
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False

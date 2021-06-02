#!/usr/bin/python3
"""
Documentation for inherits_from
"""


def inherits_from(obj, a_class):
    """
    inherits_from
    argc:
    obj: the object is an instance of a class that inherited
    a_class: class
    Return: True or False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False

#!/usr/bin/python3
"""
Documentation for MyList class that inherits from the list class
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object
    argc:
    obj: the object is an instance of a class that inherited
    Return: dir of the obj
    """
    return (dir(obj))

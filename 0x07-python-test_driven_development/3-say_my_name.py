#!/usr/bin/python3
"""
module prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    prints My name is <first name> <last name>
    argc:
        first_name: first name of the string
        last_name: last_name of the string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))

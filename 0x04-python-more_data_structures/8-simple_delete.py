#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary and a_dictionary:
        remove = a_dictionary
        del remove[key]
        return remove
    return a_dictionary

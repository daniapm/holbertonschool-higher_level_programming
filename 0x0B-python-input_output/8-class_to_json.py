#!/usr/bin/python3
"""Documentation for a class_to_json function"""


def class_to_json(obj):
    """ function that returns the dictionary description with simple data structure
    Args:
        my_obj: object
    """
    return (obj.__dict__)

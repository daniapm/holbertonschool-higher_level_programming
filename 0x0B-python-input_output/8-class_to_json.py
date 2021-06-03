#!/usr/bin/python3
"""Documentation for a class_to_json function"""


import json


def class_to_json(obj):
    """ function that writes an Object to a text file, using a JSON representation
    Args:
        my_obj: object
        filename: text file
    """
    m = json.dumps(obj.__dict__)
    return m

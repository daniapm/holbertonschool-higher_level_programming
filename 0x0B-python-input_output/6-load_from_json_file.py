#!/usr/bin/python3
"""Documentation for a load_from_json function"""


import json


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file
    Args:
        filename: text file
    """
    with open(filename) as file:
        j_son = json.load(file)
    return j_son

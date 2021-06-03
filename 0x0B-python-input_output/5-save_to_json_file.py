#!/usr/bin/python3
"""Documentation for a save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file, using a JSON representation
    Args:
        my_obj: object
        filename: text file
    """
    with open(filename, "w", encoding='utf-8') as file:
        j_son = json.dumps(my_obj)
        file.write(j_son)

#!/usr/bin/python3
"""Documentation for to_json_string function"""


import json


def to_json_string(my_obj):
    """  function that returns the JSON representation of an object
    Args:
        my_obj: string
    """
    return json.dumps(my_obj)

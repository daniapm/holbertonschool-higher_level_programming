#!/usr/bin/python3
"""Documentation for a from_json_string function"""


import json


def from_json_string(my_str):
    """  function that returns an object
    Args:
        my_str: string
    """
    return json.loads(my_str)

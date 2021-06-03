#!/usr/bin/python3
"""Documentation for read_file function"""


def append_write(filename="", text=""):
    """ function that appends a string at the end of a text file
    Args:
        filename: file to write
        text: text to write
    """
    with open(filename, "a", encoding='utf-8') as file:
        wt = file.write(text)
    return wt

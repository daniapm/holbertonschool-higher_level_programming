#!/usr/bin/python3
"""Documentation for read_file function"""


def write_file(filename="", text=""):
    """function that writes a string to a text file
    Args:
        filename: file to open
        text: text to write
    """
    with open(filename, 'w', encoding='utf-8') as file:
        wt = file.write(text)
    return wt

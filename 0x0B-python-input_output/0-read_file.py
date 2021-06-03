#!/usr/bin/python3
def read_file(filename=""):
    """Read a plain text file and return the contents as a string."""
    with open(filename, encoding='utf-8') as file:
        read_data = file.read()
        print(read_data, end="")
    file.closed

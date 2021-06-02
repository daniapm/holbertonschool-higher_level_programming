#!/usr/bin/python3
"""
Documentation for MyList class that inherits from the list class
"""


class MyList(list):
    """
    MyList class that inherits from the list class
    """
    def print_sorted(self):
        """
        Print the list witch Function sorted
        """
        print(sorted(self))

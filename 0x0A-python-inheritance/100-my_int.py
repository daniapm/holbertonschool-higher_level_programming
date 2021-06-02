#!/usr/bin/python3
"""
Documentation for BaseGeometty class
"""


class MyInt(int):
    """
    MyInt class
    """
    def __ne__(self, other):
        """
        operator to compare ne
        """
        return True

    def __eq__(self, other):
        """
        operator to compare eq
        """
        return False

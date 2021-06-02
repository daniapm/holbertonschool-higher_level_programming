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
        MyInt class
        """
        return int(self) != other

    def __eq__(self, other):
        """
        MyInt class
        """
        return int(self) == other

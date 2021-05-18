#!/usr/bin/python3


"""
definition square class

"""


class Square:

    """
    class Private instance attribute: size

    """
    def __init__(self, size=0):
        """
        argc:
        size: Square size

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

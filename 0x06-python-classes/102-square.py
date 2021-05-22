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
        if type(size) is not int or type(size) is not float:
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """
        I'm the 'size' property.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        argc:
        size: Square size

        """
        if type(size) is not int or type(size) is not float:
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        argc:
        self: parametro
        Returns:
        area: square area

        """
        area = self.__size * self.__size
        return area

    def __eq__(self, other):
        return self.__size == other.__size

    def __lt__(self, other):
        return self.__size == other.__size

    def __gt__(self, other):
        return self.__size > other.__size

    def __ge__(self, other):
        return self.__size >= other.__size

    def __le__(self, other):
        return self.__size <= other.__size

    def __ne__(self, other):
        return not self.__eq__(other)

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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
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
        return self.__size < other.__size

    def __gt__(self, other):
        return self.__size > other.__size

    def __ge__(self, other):
        return self.__size >= other.__size

    def __le__(self, other):
        return self.__size <= other.__size

    def __ne__(self, other):
        return self.__size != other.__size

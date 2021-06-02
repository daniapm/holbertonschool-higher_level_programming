#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

"""
Documentation for Square class
"""


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size):
        """
        Instantiation with size
        argc:
        size: size of the Square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Public instance method area
        Return: Regtangule area
        """
        return self.__size * self.__size

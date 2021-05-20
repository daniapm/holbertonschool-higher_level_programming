#!/usr/bin/python3


"""
definition Rectangle class

"""


class Rectangle:

        """
    empty class Rectangle

        """
        def __init__(self, width=0, height=0):
            """
            argc:
            width: Rectangle width
            height: Rectangle height
            """
            if type(height) is not int:
                raise TypeError("height must be an integer")
            elif height < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = height
            if type(width) is not int:
                raise TypeError("width must be an integer")
            elif width < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = width

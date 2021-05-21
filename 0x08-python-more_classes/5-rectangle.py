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

        @property
        def height(self):
            """
            I'm the 'height' property.

            """
            return self.__height

        @height.setter
        def height(self, value):
            """
            argc:
            height: Rectangle height

            """
            if type(value) is not int:
                    raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

        @property
        def width(self):
            """
            I'm the 'width' property.

            """
            return self.__width

        @width.setter
        def width(self, value):
            """
            argc:
            width: Rectangle width

            """
            if type(value) is not int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        def area(self):
            """
            argc:
            self: parametro
            Returns:
            area: rectangule area

            """
            area = self.__width * self.__height
            return area

        def perimeter(self):
            """
            argc:
            self: parametro
            Returns:
            perimeter: rectangule perimeter

            """
            if self.__width is 0 or self.__height is 0:
                return 0
            else:
                perimeter = ((self.__width) * 2) + ((self.__height) * 2)
                return perimeter

        def __str__(self):
            """
            argc:
            self: parametro
            Returns: string

            """

            if self.__width == 0 or self.height == 0:
                return("")
            new_print = ""
            for altura in range(0, self.__height):
                for base in range(0, self.__width):
                    new_print += "#"
                if altura != self.__height - 1:
                    new_print += "\n"
            return (new_print)

        def __repr__(self):
            """
            argc:
            self: parametro
            Returns: string

            """
            r = f'{self.__class__.__name__}({repr(self.__width)}, {repr(self.__height)})'
            return r

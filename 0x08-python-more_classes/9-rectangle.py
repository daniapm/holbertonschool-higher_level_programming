#!/usr/bin/python3


"""
definition Rectangle class

"""


class Rectangle:

        """
    empty class Rectangle

        """

        number_of_instances = 0
        print_symbol = "#"

        def __init__(self, width=0, height=0):
            """
            argc:
            width: Rectangle width
            height: Rectangle height
            """
            Rectangle.number_of_instances += 1
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
                    new_print += str(self.print_symbol)
                if altura != self.__height - 1:
                    new_print += "\n"
            return (new_print)

        def __repr__(self):
            """
            argc:
            self: parametro
            Returns: string

            """
            r = 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)
            return r

        def __del__(self):
                print("Bye rectangle...")
                Rectangle.number_of_instances -= 1

        @staticmethod
        def bigger_or_equal(rect_1, rect_2):

            """
        static metodo of class
        argc:
        rect_1: Rectangle width
        rect_2: Rectangle height
        Return: comparation of area of the rectangules

            """
            if not isinstance(rect_1, Rectangle):
                raise TypeError("rect_1 must be an instance of Rectangle")
            if not isinstance(rect_2, Rectangle):
                raise TypeError("rect_2 must be an instance of Rectangle")
            if rect_1.area() > rect_2.area():
                return rect_1
            elif rect_2.area() > rect_1.area():
                return rect_2
            else:
                return rect_1

        @classmethod
        def square(cls, size=0):
            """
        metodo of class
        argc:
        size: Rectangle width
        Return: size

            """
            new_class = cls
            widt_h = size
            heigh_t = size
            return new_class(widt_h, heigh_t)

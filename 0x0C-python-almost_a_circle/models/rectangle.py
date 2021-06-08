#!/usr/bin/python3
"""
Documentation for Rectangle class empy
"""


from models.base import Base
from sys import argv


class Rectangle(Base):
    """
    Rectangule class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor
        args:
            id: atribute id of the base
            width: width rectangle
            height: height rectangle
            x: x of the rectangle
            y: y of the rectangle
            id: id rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        value: Rectangle width

        """
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        I'm the 'heigth' property.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        argc:
        value: Rectangle heigth

        """
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        I'm the 'x' property.

        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        argc:
        value: Rectangle x

        """
        if not (isinstance(value, int)):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        I'm the 'y' property.

        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        argc:
        value: Rectangle y

        """
        if not (isinstance(value, int)):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        area rectangle
        """
        return self.__width * self.height

    def display(self):
        """
        display rectangle with #
        """
        for x in range(self.__y):
            print("")
        for lado2 in range(self.__height):
            print(self.__x * " ", end="")
            for lado1 in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """
        Rpresentacion string of the object
        Return: string
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Rpresentacion string of the object
        args:
            *args: arguments
            **kwargs: key and value
        """
        len_arg = (len(args))
        len_kwargs = (len(kwargs))
        if (len_kwargs != 0):
            for key, value in kwargs.items():
                setattr(self, key, value)
        elif (len_arg != 0):
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """
        Rpresentacion dictionary of the object
        """
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}

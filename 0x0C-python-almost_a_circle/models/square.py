#!/usr/bin/python3
from models.rectangle import Rectangle
"""
Documentation for Base class empy
"""


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        class constructor
        args:
            id: atribute id of the base
            size: size rectangle
            x: x of the rectangle
            y: y of the rectangle
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """
        I'm the 'size' property.

        """
        return self.width

    @size.setter
    def size(self, value):
        """
        argc:
        value: Rectangle size

        """
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """
        Rpresentacion string of the object
        Return: string
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

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
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

    def to_dictionary(self):
        """
        Rpresentacion dictionary of the object
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

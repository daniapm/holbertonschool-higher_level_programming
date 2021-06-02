#!/usr/bin/python3
"""
Documentation for BaseGeometty class
"""


class BaseGeometry:
    """
    BaseGeometty class
    """
    def area(self):
        """
        Public instance method area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method integer_validator
        argc:
        name: always a string
        value: validates value
        Return: Exception with message
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

"""
Documentation for BaseGeometty class empy
"""


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        """
        Instantiation with width and heigth
        argc:
            width: width of the Rectangule
            height: heigth of the Rectangule
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

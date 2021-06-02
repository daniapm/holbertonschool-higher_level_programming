#!/usr/bin/python3
"""
Documentation for BaseGeometty class
"""


class BaseGeometry():
    """
    BaseGeometty class
    """
    def area(self):
        """
        Public instance method area
        Return: Exception with message
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
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            self.name = name
            self.value = value

#!/usr/bin/python3
"""
Documentation for BaseGeometty class empy
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
"""
Documentation for Rectangle class
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
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Public instance method area
        Return: Regtangule area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Public instance method str
        Return: str area
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


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

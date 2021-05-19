#!/usr/bin/python3


"""
definition Square class

"""


class Square:

    """
    class Private instance attribute: size
    class Private instance attribute: position

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        argc:
        size: Square size
        position: Square position

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) is not int or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[1]) is not int or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        """
        I'm the 'size' property.

        args: None

        Return: size of square

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        I'm the 'size' property.

        args: value

        Return: size of square

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        I'm the 'position' property.

        args: None

        Return: position of square

        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        I'm the 'position' property.

        args: value

        Return: position of square

        """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[0]) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or type(value[1]) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        argc:
        self: parametro
        Returns:
        area: square area

        """
        area = self.__size * self.__size
        return area

    def my_print(self):
        """
        argc:
        self: parametro
        Returns: nothing

        """

        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__position[1]):
                print("")
            for i in range(0, self.__size):
                for b in range(0, self.__position[0]):
                    print(" ", end="")
                for a in range(0, self.__size):
                    print("#", end="")
                print("")

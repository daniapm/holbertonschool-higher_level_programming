#!/usr/bin/python3
class Square:
    """definition square class"""
    def __init__(self, size=0):
        """arguments: size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """Private instance attribute: size"""

#!/usr/bin/python3
"""Documentation for class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """ initializer class Student whit atributes
        Args:
            first_name: first name of the studen
            last_name: last name of the studen
            age: age of the studen
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ method that retrieves a dictionary representation of a Student instance
        Args:
            attrs: atribute
        """
        if not isinstance(attrs, list):
            return self.__dict__
        list_string = {}
        for count in attrs:
            try:
                list_string[count] = self.__dict__[count]
            except:
                continue
        return list_string

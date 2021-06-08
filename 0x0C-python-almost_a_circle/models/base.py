#!/usr/bin/python3
"""
Documentation for Base class empy
"""


import json
import os
import csv


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor
        args:
            id: atribute id of the base
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method to_json_string
        args:
            list_dictionaries: list of dictionaries
        return: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method save_to_file
        args:
            list_objs: list of instances who inherits of Base
        """
        dictionaries = []
        filename = cls.__name__ + '.json'
        if list_objs is not None:
            for list in list_objs:
                dictionaries.append(list.to_dictionary())
            with open(filename, "w") as file:
                file.write(Base.to_json_string(dictionaries))
        else:
            with open(filename, "w") as file:
                file.write(Base.to_json_string(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """
        Static method from_json_string
        args:
            json_string:  string representing a list of dictionaries
        return: list represented by json_string
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Static method create
        args:
            dictionary: double pointer to a dictionary
        return: new dictionary
        """
        if dictionary is not None:
            filename = cls.__name__
            if filename == "Square":
                dum = cls(1, 1)
            elif filename == "Rectangle":
                dum = cls(1, 0)
            dum.update(**dictionary)
            return dum
        else:
            return None

    @classmethod
    def load_from_file(cls):
        """
        Class method load_from_file
        args:
            cls: clase
        return: new dictionary
        """
        dictionaries = []
        if os.path.exists(cls.__name__ + ".json") is True:
            with open(cls.__name__ + ".json", "r") as file:
                dics = cls.from_json_string(file.read())
                for index in dics:
                    dictionaries.append(cls.create(**index))
                return dictionaries
        else:
            return []

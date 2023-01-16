#!/usr/bin/python3
""" This module contains the Base class"""

import json



class Base:
    """Base class with private class attributes and constructors"""


    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string representation of list_objs to a file
        args:
            cls: Which ever class you need to save
            lst_objs; list of class instances you want to save
        """
        new_list = []
        if list_objs:
            for inst in list_objs:
                new_list.append(cls.to_dictionary(inst))
            with open("{}.json".format(cls.__name__), 'w') as f:
                f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string
        args:
            json_string: is a string representing a list of dictionaries
        return:
            Empty list if Json_string is None or empty
            returns the list represented by json_string
        """
        new_list = []
        if json_string is None or len(json_string) == 0:
            return new_list
        return json.loads(json_string)

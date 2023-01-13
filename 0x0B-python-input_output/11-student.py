#!/usr/bin/python3
"""
The module contains a class that defines student
"""


class Student:
    """ Class that defines a student by attributes
    """

    def __init__(self, first_name, last_name, age):
        """ initialize student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns the dict representation of the instance"""
        if attrs is None or not isinstance(attrs, list):
            return(self.__dict__)
        d = {}
        for k in attrs:
            if not isinstance(k, str):
                return (self.__dict__)
            if k in self.__dict__.keys():
                d[k] = self.__dict__[k]
        return (d)

    def reload_from_json(self, json):
        """ Retrives a dictionary representation of a student instance
        args:
            self: instance of class
            json: JSON file to extract data
        """
        for val in json.keys():
            self.__dict__[k] = json[k]

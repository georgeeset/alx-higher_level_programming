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

    def to_json(self):
        """ returns the dict representation of the instance"""
        return(self.__dict__)

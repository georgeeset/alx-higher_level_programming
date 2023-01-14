#!/usr/bin/python3
""" This module contains the Base class"""


class Base:
    """Base class with private class attributes and constructors"""


    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

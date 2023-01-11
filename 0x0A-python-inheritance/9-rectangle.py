#!/usr/bin/python3
"""This module contains a Rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class that defines a rectangle from BaseGeometry Class """

    def __init__(self, width, height):
        """ Initializes instance
        args:
            self: instance of class
            width: integer width of ractangle
            height: integer height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates area and returns the value"""
        return self.__width * self.__height

    def __str__(self):
        """Return class in formatted string"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)

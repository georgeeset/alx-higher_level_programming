#!/usr/bin/python3
"""
Module contains rectang class
"""


class Rectangle:
    """
    Rectangle class defines a rectangle by:
    Private instance attribute: width
    Private instance attribute: height
    Instatation with optional width and height of 0
    """

    def _validate_size(self, length, id):
        """
        Validate the value of length:
        args:
            @self: instanve of the class
            @length: size to be validated
            @id: name with with we can identify the exception
        Return:
            returns nothing
        Raise:
            TypeError: if length is not integer
            ValueError: if length is less than 0
        """
        if not isinstance(length, int):
            raise TypeError(f"{id} must be an integer")
        if length < 0:
            raise ValueError(f"{id} must be >= 0")

    def __init__(self, width=0, height=0):
        """
        Method that initializes the instance
        """
        self._validate_size(width, "width")
        self._width = width

        self._validate_size(height, "height")
        self._height = height


    @property
    def width(self):
        """
        Getter for width
        Args:
            self: instance of the class
        Return:
            returns width of rectangel
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        setter for width
        Args:
            self: instance of the class
            value: new vlaue of width
        Return:
            returns nothing
        """
        self._validate_size(value, "width")
        self._width = value


    @property
    def height(self):
        """
        Getter for height
        Args:
            self: instance of the class
        Return:
            returns height of rectangel
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        setter for height
        Args:
            self: instance of the class
            value: new vlaue of height
        Return:
            returns nothing
        """
        self._validate_size(value, "height")
        self._height = value

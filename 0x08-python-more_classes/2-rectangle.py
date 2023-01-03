#!/usr/bin/python3
"""
This module is composed by a class that defines a Rectangle
"""


class Rectangle:
    """ Class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ Method that initializes the instance
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self._width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._height = height

    @property
    def width(self):
        """ method that returns the value of the width
        Returns:
            width of the rectangle
        """

        return self._width

    @width.setter
    def width(self, value):
        """ method that defines the width
        Args:
            value: width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """ method that returns the value of the height
        Returns:
            height of the rectangle
        """

        return self._height

    @height.setter
    def height(self, value):
        """ method that defines the height
        Args:
            value: height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        public instanve method
        args:
            self: instance of class
        Returns:
            Area of rectangle
        """
        return self._height * self._width

    def perimeter(self):
        """
        Public instanve method:
        Args:
            self: instance of the class
        Return:
            Returns perimeter of rectangle
        """
        return 2 * (self._height + self._width)

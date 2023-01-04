#!/usr/bin/python3
"""
This module is composed by a class that defines a Rectangle
"""


class Rectangle:
    """ Class that defines a rectangle """

    number_of_instances = 0
    print_symbol = "#"

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

        Rectangle.number_of_instances += 1

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
        if self._height == 0 or self._width == 0:
            return (0)
        return 2 * (self._height + self._width)

    def __str__(self):
        """ Method that returns the Rectangle #
        Returns:
            str of the rectangle
        """

        rectangle = ""
        if self._width == 0 or self._height == 0:
            return rectangle

        for i in range(0, self._height):
            rectangle += (str(self.print_symbol) * self._width) + '\n'
        return rectangle[:-1]

    def __repr__(self):
        """ Method that returns the string represantion of the instance
        Returns:
            string represenation of the object
        """

        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """ Method that prints a message when the instance is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Indicate the biggest rectangle based on the area
        args:
            rect_1: first rectangle
            rect_2: second rectangle
        Return:
            returns the biggest rectangle
        Raises:
            TypeError: if rect_1 or rect_2 is not an instance of ractangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """ Method that returns a new instance of Rectangle class
        Args:
            cls: rectangle class
            size: rectangle width and rectangle height
        Returns:
            a new instance of Rectangle class
        """

        return cls(size, size)

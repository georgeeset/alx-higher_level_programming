#!/usr/bin/python3
"""This module contains the Rectangle Class"""

from models.base import Base

class Rectangle(Base):
    """Rectangle class Inherits form Base class"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the instance of Rectangle
        args:
            width: width of rectangle
            height; HEIGHT OF THE RECTANGLE
            x: x axis property
            y: y axis property
            id: Id of rectangle
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """read the value of width"""

        return (self.__width)

    @width.setter
    def width(self, width):
        """update the value of width"""

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """get value of height"""

        return (self.__height)

    @height.setter
    def height(self, height):
        """Update the value of height"""

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def x(self):
        """getter for the value of x"""

        return (self.__x)

    @x.setter
    def x(self, x):
        """update the value of x"""

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getter for y"""

        return (self.__y)

    @y.setter
    def y(self, y):
        """ Update Y data"""

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Area return Area of Rectangle"""

        return (self.__height * self.__width)

    def display(self):
        """ Display recrtangle with # pattern"""

        for h in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """ string representation rectangle"""

        dt = f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"
        return (dt)

    def display(self):
        """print in stdout the rectangle instance with the character
        # by taking care of x and y
        """

        print('\n' * self.y, end="")
        for h in range(self.height):
            print(' ' * self.x, end="")
            print('#' * self.width)

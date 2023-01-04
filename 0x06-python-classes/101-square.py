#!/usr/bin/python3
"""
this module contains a square class
"""


class Square:
    """
    This class defines a square by:
        private instance attribute: size
        Private instanve attribute: Position
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        initialize the class:
        args:
           size: optional integer
           self: instance of the class
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """ Get value of size"""
        return self._size

    @size.setter
    def size(self, value):
        """Set value of size
        args:
            value: new value of size
        Returns:
            returns nothing
        Raise:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self._size = value

    @property
    def position(self):
        """ Get the value of position"""
        return self._position

    @position.setter
    def position(self, value):
        """ store new position value
        args:
            self: instance of class
            value: new tuple value for position
        Raises:
           TypeError: if value is not tuple or not possitive number

        """

        if isinstance(value, tuple):
            if len(value) == 2:
                if isinstance(value[0], int) and isinstance(value[1], int):
                    if value[0] >= 0 and value[1] >= 0:
                        self._position = value
                        return

        raise TypeError("position must be a tuple of 2 positive integer")

    def area(self):
        """ finds the area
        args:
            self: instance of class
        return:
            the current square area
        """
        return self._size ** 2

    def __str__(self):
        """prints in stdout the square with che character #"""

        text = ""
        if self._position[1] > 0:
            text += "\n" * self._position[1]
        if self._size == 0:
            text = "\n"
        else:
            for i in range(self._size):
                text += " " * self._position[0]
                text += "#" * self._size
                if i < self._size - 1:
                    text += "\n"
        return (text)

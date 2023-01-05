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

    def my_print(self):
        """prints in stdout the square with che character #"""

        if self._position[1] > 0:
            print("\n" * self._position[1], end="")
        if self._size == 0:
            print()
        else:
            for i in range(self._size):
                print(" " * self._position[0], end="")
                print("#" * self._size)

    def __str__(self):
        rtn = ""

        if self.size == 0:
            return rtn

        for i in range(self.position[1]):
            rtn += "\n"

        for i in range(0, self.size):
            for k in range(self.position[0]):
                rtn += " "
            for j in range(self.size):
                rtn += "#"
            if i is not (self.size - 1):
                rtn += "\n"

        return rtn

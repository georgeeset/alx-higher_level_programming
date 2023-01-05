#!/usr/bin/python3
"""The module contains Square class
"""


class Square:
    """ A class that defines a square by its size
    """
    def __eq__(self, other):
        return self._size == other._size

    def __lt__(self, other):
        return self._size < other._size

    def __le__(self, other):
        return self._size <= other._size

    def __ne__(self, other):
        return self._size != other._size

    def __gt__(self, other):
        return self._size > other._size

    def __ge__(self, other):
        return self._size >= other._size

    def __init__(self, size=0):
        """ Method to initialize the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size

    def area(self):
        """ Method that returns the square are of the object
        """
        return (self._size ** 2)

    @property
    def size(self):
        """ Method to returns the size value
        """
        return self._size

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

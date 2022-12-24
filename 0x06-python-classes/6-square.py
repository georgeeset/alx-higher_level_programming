#!/usr/bin/python3
""" Write a class Square that defines a square by: private attribute size"""


class Square:

    """ A class that defines a square by its size
    """

    def _validate_position(self, val):
        """ verify data before updating position """
        if (not isinstance(val, tuple)) or (len(val) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not isinstance(val[0], int)) or (not isinstance(val[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (val[0] < 0) or (val[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            return (True)

    def __init__(self, size=0, position=(0, 0)):
        """ Method to initialize the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if self._validate_position(position):
            self.__position = position

    def area(self):
        """
        Method that returns the square are of the object
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ Getter for square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for square size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size Must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Print in stdout the square with the character #
        at the position given by the position attribute.
        """
        if self.__size == 0:
            print()
            return
        for j in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            print(" " * self.__position[0], end='')
            print("#" * self.__size)

    @property
    def position(self):
        """get position data"""
        return self.__position

    @position.setter
    def position(self, value):
        """updata the value of position"""
        if self._validate_position(value):
            self.__position = value

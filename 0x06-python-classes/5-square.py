#!/usr/bin/python3
""" Write a class Square that defines a square by: private attribute size"""


class Square:

    """ A class that defines a square by its size
    """
    def __init__(self, size=0):
        """ Method to initialize the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

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
        """Print in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return ()
        for i in range(0, self.__size):
            print("#" * self.__size)

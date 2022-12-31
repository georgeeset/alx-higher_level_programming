#!/usr/bin/python3

"""
Module to print square
"""


def print_square(size):
    """ Print a square with the character #
    Args:
        @size: the size length of the square

    Return:
        Returns nothing

    Exceptions:
        TypeError: if value is not an integer
        TypeErro: if value of size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        for j in range(0, size):
            print('#', end='')
        print()

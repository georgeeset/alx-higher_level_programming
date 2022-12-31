#!/usr/bin/python3
"""
This module adds two numbers and return the result
"""


def add_integer(a, b=98):
    """ Function adds to integers a and b
    Args:
        a: first number
        b: second number 98 by default

    Returns:
       addition of a and b

    Raises:
        TypeError: if a or b is neither integer nor float
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)

#!/usr/bin/python3
"""Module contains Geometry class"""


class BaseGeometry:
    """Geometry class definition"""

    def area(self):
        """ Area not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value"""

        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')

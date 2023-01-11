#!/usr/bin/python3
"""Module contains class Square"""


class Square(__import__('9-rectangle').Rectangle):
    """Square Class"""

    def __init__(self, size):
        """Initializes the square"""

        super().integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates and returns area"""
        return super().area()

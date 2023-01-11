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
        return self.__size * self.__size

    def __str__(self):
        """Returns String format of the class"""
        return f"[Square] {self.__size}/{self.__size}"

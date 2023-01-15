#!/usr/bin/python3
""" Contains Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class that extends form Rectangle class"""


    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)


    def __str__(self):
        """print string representation of square"""

        data = f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
        return (data)

    @property
    def size(self):
        """ getter ror size"""
        return self.height

    @size.setter
    def size(self, size):
        """ update size"""
        self.width = size
        self.height = size

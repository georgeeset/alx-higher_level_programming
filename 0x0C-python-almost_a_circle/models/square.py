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

    def update(self, *args, **kwargs):
        """update dquare with the following dataf format for *args:
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """
        attributes = ["id", "size", "x", "y"]
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for attr, val in kwargs.items():
                setattr(self, attr, val)

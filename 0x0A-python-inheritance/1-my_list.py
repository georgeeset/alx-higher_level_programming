#!/usr/bin/python3
"""
module contains method A class MyList
"""


class MyList(list):
    """
    This class that inherites for list
    """

    def print_sorted(self):
        """
        Class method that print sorted list
        args:
           self: instance of the class
        """
        print(sorted(self))

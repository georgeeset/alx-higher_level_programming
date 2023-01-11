#!/usr/bin/python3
"""
module contains a class MyList which is ment to work as a
mustom list
"""


class MyList(list):
    """
    This is a custum class that inherites from list class
    """

    def __init__(self, *argc, **argv):
        """
        initialize the instance of myList class
        """
        list.__init__(self, *argc, **argv)

    def print_sorted(self):
        """
        Class method that print sorted list
        args:
           self: instance of the class
        """
        sorted_lst = self.copy()
        sorted_lst.sort()
        print(sorted_lst)

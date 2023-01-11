#!/usr/bin/python3
""" This module contains a custom integer class MyInt"""


class MyInt(int):
    """ custom int class MyInt inherits from class int"""

    def __eq__(self, other):
        """Method that returns inverted comparizon check """
        return not super().__eq__(other)

    def __ne__(self, other):
        """ Method that returns == check """
        return not super().__ne__(other)

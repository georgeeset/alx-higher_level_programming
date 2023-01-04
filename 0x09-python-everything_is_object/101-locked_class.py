#!/usr/bin/python3
"""
This is a module that containts a clas that avoids
dynmaically created attributes
"""


class LockedClass:
    """Empty class with no class or object attribute"""

    __slots__ = ['first_name']

    def __init__(self):
        """made empty for now"""
        pass

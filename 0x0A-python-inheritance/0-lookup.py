#!/usr/bin/python3
"""
this file contains a function called lookup(obj)

"""

def lookup(obj):
    """
    Retuns the list of available attributes and methods of an object:
    args:
       obj: the class or object
    Returns:
       List of information extracted form the ohject
    """
    return dir(obj)

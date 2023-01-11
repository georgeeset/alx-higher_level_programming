#!/usr/bin/python3
"""the object is an instance of a class that
inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """Checks if an object inherits from a_class
    Args:
        obj - object to be checked
        a_class - class to compare
    Return:
        bool - True if obj is an instance of a_class, False otherwise
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)

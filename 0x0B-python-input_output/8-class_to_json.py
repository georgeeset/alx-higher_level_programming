#!/usr/bin/python3
"""this module contains a function that returns a dictionary
descriptionwith simple data structure

"""


def class_to_json(obj):
    """ converts an object to a JSON drepresentation
    args:
        obj: is an instance of a clas
    return:
        returns dictionary description of object
    """
    return (obj.__dict__)

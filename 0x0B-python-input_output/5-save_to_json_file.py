#!/usr/bin/python3
"""this module writes an object to a text file"""


from json import dump


def save_to_json_file(my_obj, filename):
    """Writes an object to text file using JSON repr
    Args:
        my_object: JSON string
        filename: storage location
    """

    with open(filename, "w", encoding="UTF-8") as f:
        dump(my_obj, f)

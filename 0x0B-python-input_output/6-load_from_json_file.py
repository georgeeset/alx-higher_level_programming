#!/usr/bin/python3
"""this module contains a function that creates an object form JSON file"""


from json import load


def load_from_json_file(filename):
    """creates an object from a JSON file"""

    with open(filename, "r", encoding="UTF-8") as f:
        return load(f)

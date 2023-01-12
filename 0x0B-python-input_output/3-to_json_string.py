#!/usr/bin/python3
"""
    This Module contains a function that returns
the JSON representation of an object
"""

import json


def to_json_string(my_obj):
    """Returns the json format"""
    return json.dumps(my_obj)

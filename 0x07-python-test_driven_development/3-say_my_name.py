#!/usr/bin/python3
"""
Function that prints MY name is first last name
"""


def say_my_name(first_name, last_name=""):
    """
    Print My name is <first_name> <last name>

    Args:
        @first_name:
        @last_name:

    Return:
        no returns

    Exceptions:
       TypeError: if either first_name or last_name is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

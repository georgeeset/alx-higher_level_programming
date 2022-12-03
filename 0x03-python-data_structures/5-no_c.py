#!/usr/bin/python3

def no_c(my_string):
    """ Removes all occurence of C or c from a string
    and return the nre string
    """
    newString = ""
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        newString += char

    return (newString)

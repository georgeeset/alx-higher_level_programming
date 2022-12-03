#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """ replace an element of a lis tat a specific position
    and return the modified list
    returns original list if idx is negative or outof range
    """
    length = len(my_list)
    if idx < 0 or idx >= length:
        return (my_list)
    my_list[idx] = element
    return (my_list)

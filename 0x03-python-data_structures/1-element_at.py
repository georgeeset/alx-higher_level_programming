#!/usr/bin/python3

def element_at(my_list, idx):
    """ retrieves an element from a list
    return None if idx is negative and if
    idx is outof range of the list
    """
    length = len(my_list);
    if idx < 0 or idx >= length:
        return (None)
    return my_list[idx]

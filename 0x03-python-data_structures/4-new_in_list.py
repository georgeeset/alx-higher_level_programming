#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """replace an element in a list at a idx position
    and return a nre list without changing original list
    return original lis if idx is negative or outsid list range
    """
    if not my_list:
        return
    length = len(my_list)
    if idx >= length or idx < 0:
        return (my_list)
    new_list = my_list.copy()
    new_list[idx] = element
    return (new_list)

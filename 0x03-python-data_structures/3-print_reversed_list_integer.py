#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    print all integer of a list in reverse order
    format: one integer per line.
    """
    length = len(my_list)
    for i in range(1, length + 1):
        print("{:d}".format(my_list[length - i]))

#!/usr/bin/python3

def max_integer(my_list=[]):
    highest = 0
    if len(my_list) == 0:
        return None
    for i in range(0, len(my_list)):
        if (i == 0):
            highest = my_list[0]
        else:
            if my_list[i] > highest:
                highest = my_list[i]
    return (highest)

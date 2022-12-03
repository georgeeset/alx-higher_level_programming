#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """ find all multiple of 2 in list
    RETURN A BOOLIAN list that indicate
    if it is multiple of 2
    """
    isDivisible = []
    for item in my_list:
        if item % 2 == 0:
            isDivisible.append(True)
        else:
            isDivisible.append(False)
    return (isDivisible)

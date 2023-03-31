#!/usr/bin/env python3

"""a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """ function using recursion """
    lst = list_of_integers

    if len(lst) == 0 or lst is None:
        return None

    if (len(lst) == 1):
        return (lst[0])

    if lst[0] > lst[1]:
        return lst[0]
    if lst[-1] > lst[-2]:
        return lst[-1]

    center = len(lst) // 2

    if (lst[center - 1] > lst[center]):
        return(find_peak(lst[:center]))
    elif (lst[center + 1] > lst[center]):
        return(find_peak(lst[center + 1:]))
    else:
        return(lst[center])

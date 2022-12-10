#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return (0)
    multiplier = list(map(lambda x: x[0] * x[1], my_list))
    adder = list(map(lambda x: x[1], my_list))
    return (addList(multiplier)/addList(adder))


def addList(the_list=[]):
    if not the_list:
        return (0)
    val = 0
    for i in the_list:
        val += i
    return (val)

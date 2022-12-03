#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """ add to tupls
    if tuple is smaller than 2, use the value 0
    to replce.
    if tuple is bigger than 2, use the first 2
    """
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a == 0:
        a1 = 0
        a2 = 0
    elif len_a == 1:
        a1 = tuple_a[0]
        a2 = 0
    else:
        a1 = tuple_a[0]
        a2 = tuple_a[1]

        if len_b == 0:
            b1 = 0
            b2 = 0
        elif len_b == 1:
            b1 = tuple_b[0]
            b2 = 0
        else:
            b1 = tuple_b[0]
            b2 = tuple_b[1]

    new_tuple = (a1 + b1, a2 + b2)
    return (new_tuple)

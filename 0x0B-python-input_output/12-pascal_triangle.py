#!/usr/bin/python3
""" this module contains pasacal traingle function"""


def pascal_triangle(n):
    """ Function that returns the pascal triangle
    Args:
        n: size of trangle
    Returns:
        matrix: a matrix with the pascal triangle
    """

    last = []
    pascal = []

    for i in range(n):
        row_list = []
        ki = -1
        kj = 0
        for j in range(0, len(last) + 1):
            if ki == -1 or kj == len(last):
                row_list += [1]
            else:
                row_list += [last[ki] + last[kj]]
            ki += 1
            kj += 1
        pascal.append(row_list)
        last = row_list

    return (pascal)

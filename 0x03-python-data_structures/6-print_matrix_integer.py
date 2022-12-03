#!/usr/bin/python3

def print_matrix_integer(matrix = [[]]):
    """ function that prints a matrix of integer"""
    if not matrix:
        return
    for item in matrix:
        if not item:
            pass
        for i in range(0, len(item)):
            if i > 0:
                print(" {:d}".format(item[i]), end = '')
            else:
                print("{:d}".format(item[i]), end = '')
        print('\n', end = '')

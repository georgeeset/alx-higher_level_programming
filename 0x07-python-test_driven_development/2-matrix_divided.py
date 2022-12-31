#!/usr/bin/python3
"""
multiply all members of a matrix by a given number
"""


def matrix_divided(matrix, div):
    """ Divides all element of a matrix by div
    Args:
        @matrix: List of Lists
        @div: integer or float

    Rerutns:
        Returns a new matrix rounded to 2 decimal places

    Exceptions:
        TypeError: if matrix is not a list of lists of integers/float
                   if div is not an integer or float
        ZeroDivistionError: if div is given as 0
    """

    new_matrix = matrix.copy()
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"
    msg3 = "division by zero"
    msg4 = "div must be a number"

    if not isinstance(matrix, list):
        raise TypeError(msg1)

    elementLen = 0
    for item in matrix:
        if not isinstance(item, list):
            raise TypeError(msg1)
        if len(item) != elementLen:
            if elementLen == 0:
                elementLen = len(item)
            else:
                raise TypeError(msg2)
        for element in item:
            if not isinstance(element, int) and not isinstance(element, float):
                raise TypeError(msg1)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError(msg4)

    if div == 0:
        raise ZeroDivisionError(msg3)

    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: round(x/div, 2), matrix[i]))

    return (new_matrix)

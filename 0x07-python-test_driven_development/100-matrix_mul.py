#!/usr/bin/python3

"""
This module writes a function that multiplies 2 matrices
"""


def matrix_check(matrix, id):
    """
    check if a matrix data given is real matrix
    Args:
        @matrix: list to lists
        @id: string containing the id of matrix sent
               this will be used to indicate
               the matrix causing error
    Returns:
        Return nothing
    Raises:
        TypeError: if m_a or m_b aren't a list
        TypeError: if m_a or m_b aren't a list of a lists
        ValueError: if m_a or m_b are empty
        TypeError: if the lists of m_a or m_b don't have integers or floats
        TypeError: if the rows of m_a or m_b don't have the same size
    """

    ma_len = 0
    msg1 = f"each row of {id} must be of the same size"
    msg2 = f"{id} should contain only integers or floats"

    if not isinstance(matrix, list):
        raise TypeError(f"{id} must be a list")
    else:
        if matrix == [] or matrix == [[]]:
            raise ValueError(f"{id} can't be empty")
        for item in matrix:
            if not isinstance(item, list):
                raise TypeError(f"{id} must be a list of lists")
            else:
                if len(item) != ma_len:
                    if ma_len == 0:
                        ma_len = len(item)
                    else:
                        raise TypeError(msg1)
                for it in item:
                    if not isinstance(it, float) and not isinstance(it, int):
                        raise TypeError(msg2)
    return


def matrix_mul(m_a, m_b):
    """
    multiply two matrices
    Args:
        @m_a: matrix a
        @m_b: matrix b

    Return:
        Returns new matrix

    Raises:
        ValueError: if m_a and m_b can't be multiplied
    """
    x = 0
    newMatrix = []

    matrix_check(m_a, "m_a")
    matrix_check(m_b, "m_b")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    for a in m_a:
        smallMatrix = []
        y = 0
        num = 0
        while y < len(m_b[0]):
            num += a[x] * m_b[x][y]
            if x == len(m_b) - 1:
                x = 0
                y += 1
                smallMatrix.append(num)
                num = 0
            else:
                x += 1
        newMatrix.append(smallMatrix)
    return (newMatrix)

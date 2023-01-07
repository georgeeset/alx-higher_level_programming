#!/usr/bin/python3
import numpy as np
"""Task 7 - Lazy Matrix Multiplication
This is our function to be tested
"""


def lazy_matrix_mul(m_a, m_b):
    """Multiples two matrices
    Args:
        m_a (list): first matrix
        m_b (list): second matrix
    Returns:
        Returns the product matrix
    """
    try:
        result = np.matmul(m_a, m_b)
    except:
        raise
    return result

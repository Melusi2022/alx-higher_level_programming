#!/usr/bin/python3
"""

Module divides an element by a number indicated

"""


def matrix_divided(matrix, div):
    """
    Matrix divider method
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    new_matrix = []
    row_size = None
    for row in matrix:
        temp = []
        if not all(isinstance(val, (int, float)) for val in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if row_size is None:
            row_size = len(row)
        elif row_size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        temp = []
        for element in row:
            temp.append(round((element / div), 2))
        new_matrix.append(temp)

    return new_matrix

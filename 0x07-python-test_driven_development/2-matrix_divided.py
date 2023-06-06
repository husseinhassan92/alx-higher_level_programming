#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains method that divides all elements of a matrix and returns new matrix
Requires same size lists of ints or floats, and max two decimal places
"""


def matrix_divided(matrix, div):
    """ Return divided matrix by the div number """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    massage = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(massage)
    divided_matrix = []
    length = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(massage)
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []

        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError(massage)
            new_row.append(round((ele / div), 2))
        divided_matrix.append(new_row)
    return divided_matrix

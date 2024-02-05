#!/usr/bin/python3
"""Defining a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
        Divide all elements of a matrix by a given divisor.

        Parameters:
        - matrix (list of lists): The matrix to be divided.
         Each row must have the same size.
        - div (int or float): The divisor to divide each
        element of the matrix.

        Raises:
        - TypeError: If 'div' is not an integer or float.
          If the matrix is not a list of lists containing
           only integers or floats.
          If the rows of the matrix have different sizes.

        - ZeroDivisionError: If 'div' is equal to zero.

        Returns:
        - list of lists: A new matrix with each element
        rounded to two decimal places
          after being divided by 'div'.
        """

    mat = []
    msg = " matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for sub in matrix:
        if len(matrix[0]) != len(sub):
            raise TypeError("Each row of the matrix must have the same size")
        for i in sub:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError(msg)
        mat.append([round(i / div, 2) for i in sub])
    return mat

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = []
    for row in matrix:
        new_rows = [index**2 for index in row]
        my_matrix.append(new_rows)
    return my_matrix

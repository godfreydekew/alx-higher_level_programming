#!/usr/bin/python3
"""Defines pascal_triangle function"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n."""
    if n <= 0:
        return []

    res = [[1]]

    for i in range(n - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res

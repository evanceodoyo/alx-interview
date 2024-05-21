#!/usr/bin/python3
"""Implements Pascal's Triangle"""


def pascal_triangle(n):
    """
    Calculates and returns list of lists of integers representing
    Pascal's triangle of `n`.
    """
    triangle = [[1], [1, 1]]
    if n <= 0:
        return []

    if n == 1:
        return triangle[:1]

    for i in range(1, n - 1):
        row = [1]
        for k in range(i):
            row.append(triangle[i][k] + triangle[i][k+1])
            if k == i - 1:
                row.append(1)
        triangle.append(row)

    return triangle

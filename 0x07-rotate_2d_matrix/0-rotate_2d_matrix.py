#!/usr/bin/python3
"""Module for rotating a 2D matrix
"""


def rotate_2d_matrix(matrix):
    """Rotates nxn matrix by 90 degrees clockwise in-place.
    Parameters:
      matrix (list[list]): 2D matrix.
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(len(matrix)):
        matrix[i].reverse()

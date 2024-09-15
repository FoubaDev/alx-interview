#!/usr/bin/python3
"""
Do not return anything. The matrix must be edited in-place.
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate matrix in 90° clockwise
    """
    matrix[:] = list(map(list, zip(*matrix)))
    for row in matrix:
        row.reverse()

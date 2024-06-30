#!/usr/bin/python3
"""
Create a function that implement pascal_triangle
"""


def pascal_triangle(n):
    """
    Args:
        n (int) number of list integer in pascal triangle.
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    triangle = []
    for i in range(n):
        # Initialize a row with all 1s
        row = [1] * (i + 1)
        # Each element(not first and last) is sum of the 2 elements above it
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        # Add the completed row to the triangle
        triangle.append(row)
    return triangle

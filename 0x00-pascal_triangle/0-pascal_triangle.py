#!/usr/bin/python3

"""
pascals triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of ints representing pascals triangle
    """

    if n <= 0:
        return []

    triangle = []

    for x in range(n):
        row = [1] * (x + 1)
        if x > 1:
            for y in range(1, len(row) - 1):
                row[y] = triangle[x - 1][y - 1] + triangle[x - 1][y]
        triangle.append(row)
    return triangle

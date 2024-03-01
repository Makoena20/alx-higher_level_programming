#!/usr/bin/python3
"""
Module for generating Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    print("Correct output: n = 5")
    print(pascal_triangle(5))
    print("Correct output: n = 1")
    print(pascal_triangle(1))
    print("Correct output: n = 0")
    print(pascal_triangle(0))
    print("Correct output: n = 100")
    print(pascal_triangle(100))

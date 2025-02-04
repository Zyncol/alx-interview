#!/usr/bin/python3
"""
Task Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """rotating two dimension matrix 90 degrees clockwise
    Args:
        matrix (list[[list]]): a matrix
    """
    num = len(matrix)
    for z in range(int(num / 2)):
        y = (num - z - 1)
        for k in range(z, y):
            x = (num - 1 - k)
            # current number
            tmp = matrix[z][k]
            # change top for left
            matrix[z][k] = matrix[x][z]
            # change left for bottom
            matrix[x][z] = matrix[y][x]
            # change bottom for right
            matrix[y][x] = matrix[k][y]
            # change right for top
            matrix[k][y] = tmp

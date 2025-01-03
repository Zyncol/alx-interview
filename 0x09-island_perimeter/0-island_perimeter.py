#!/usr/bin/python3
"""
Island Perimeter task handling
"""


def island_perimeter(grid):
    """
    Calculating perimeter of the island described in grid
    Args:
        grid:list of integers containing 0(water) or 1(land)
    Return:
        perimeter of the island
    """

    t = 0
    for c in range(len(grid)):
        for j in range(len(grid[c])):
            if (grid[c][j] == 1):
                if (c <= 0 or grid[c - 1][j] == 0):
                    t += 1
                if (c >= len(grid) - 1 or grid[c + 1][j] == 0):
                    t += 1
                if (j <= 0 or grid[c][j - 1] == 0):
                    t += 1
                if (j >= len(grid[c]) - 1 or grid[c][j + 1] == 0):
                    t += 1
    return t

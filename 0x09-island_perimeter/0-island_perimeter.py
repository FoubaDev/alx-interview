#!/usr/bin/python3
"""
Do not return anything. The matrix must be edited in-place.
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
You can assume the matrix will have 2 dimensions and will not be empty.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.
    Args:
        grid (list of list of int): A grid where 1 represents land and
        0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    counter = 0
    grid_max = len(grid) - 1  # index of the last list in the grid
    lst_max = len(grid[0]) - 1  # index of the last square in list

    for lst_idx, lst in enumerate(grid):
        for land_idx, land in enumerate(lst):
            if land == 1:
                # left and right
                if land_idx == 0:
                    # left side
                    counter += 1

                    # right side
                    if lst[land_idx + 1] == 0:
                        counter += 1
                elif land_idx == lst_max:
                    # left side
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # right side
                    counter += 1
                else:
                    # left side
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # right side
                    if lst[land_idx + 1] == 0:
                        counter += 1

                # top and down
                if lst_idx == 0:
                    # top side
                    counter += 1

                    # bottom side
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1
                elif lst_idx == grid_max:
                    # top side
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    # bottom side
                    counter += 1
                else:
                    # top side
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    # bottom side
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1

    return counter

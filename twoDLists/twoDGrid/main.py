"""
2D Grid
-------
It's common to represent a 2D grid as a list of lists in Python. For example, a 2x3 grid can be represented as:

    grid = [
    [0, 0, 0],
    [0, 0, 0]
    ]

    rows = len(grid)    # 2
    cols = len(grid[0]) # 3

In this example, the variable grid is a list of lists. The variable rows is the number of rows in the grid, and the variable cols is the number of columns in the grid.
We assume that each sub-list in the grid has the same length, which is usually the case for a 2D grid in algorithm problems.

Challenge
---------
Implement the following function using the grid operations described above:

    1. in_bounds(grid: List[int], r: int, c: int) -> bool that takes a 2D grid grid and two integers r and c, where r is the index of a row and c is the index of a column.
    It should return True if the cell at row r and column c is within the bounds of the grid, and False otherwise.
        Example: in_bounds([[1, 2], [3, 4]], 2, 1) should return False, there is no row at index 2.

"""


from typing import List


def in_bounds(grid: List[List[int]], r: int, c: int) -> bool:
    grid_row: int = len(grid)
    grid_column: int = len(grid[0])

    if(r < grid_row and c < grid_column):
        return True
    else:
        return False


# do not modify below this line
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 2))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, 3))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 4))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, -1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1, 3))

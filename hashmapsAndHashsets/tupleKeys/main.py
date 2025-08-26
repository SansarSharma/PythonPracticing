"""
Tuple Keys
----------
It's common to store pairs of values in a dictionary or set. For example, we might store the row, column pair of a cell in a grid. While we cannot store a list as a key in a dictionary, we can use a tuple instead.


    dict_of_pairs = {}

    dict_of_pairs[(0, 0)] = 1
    dict_of_pairs[(0, 1)] = 2

    print(dict_of_pairs)  # {(0, 0): 1, (0, 1): 2}

    set_of_pairs = set()

    set_of_pairs.add((0, 0))
    set_of_pairs.add((0, 1))

    print(set_of_pairs)  # {(0, 0), (0, 1)}


In the above code, we created a dictionary and a set where the keys and elements are tuples.
We can use tuples to store pairs of values in a single object. This is useful when we want to store multiple values together, but we don't want to create a new class or structure.

Challenge
---------
Implement the following function:

    1. grid_to_set(grid: List[List[int]]) -> Set[Tuple[int, int]] that takes a 2D grid of integers and returns a set of tuples where each tuple is a pair of the row and column. The set should only contain the coordinates of cells that have a value of 1.
        Example: Given a grid [[1, 0, 0], [0, 0, 0]] we should return a set with (0, 0). This is because the cell at row 0, column 0 has a value of 1, and it is the only cell with a value of 1.


"""


from typing import List, Set, Tuple


def grid_to_set(grid: List[List[int]]) -> Set[Tuple[int, int]]:
    result = set()
    length_row: int = len(grid)
    length_collumn: int = 0

    for row in range(0, length_row, 1):
        length_collumn = len(grid[row])

        for collumn in range(0, length_collumn, 1):
            if (grid[row][collumn] == 1):
                result.add((row, collumn))

    return result


# do not modify below this line

output1 = grid_to_set([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
print(type(output1))
print(sorted(list(output1)))

output2 = grid_to_set([[1, 0, 0], [0, 0, 0]])
print(type(output2))
print(sorted(list(output2)))

output3 = grid_to_set([[1, 1, 1], [1, 1, 1]])
print(type(output3))
print(sorted(list(output3)))

output4 = grid_to_set([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print(type(output4))
print(sorted(list(output4)))

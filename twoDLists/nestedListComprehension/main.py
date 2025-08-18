"""
Nested List Comprehension
-------------------------
It's common to need to initialize a 2-D list of a given size, especially a 2-D grid. Suppose we wanted to declare a 2x3 grid of zeros. You might be tempted to try this:

    grid = [[0] * 3] * 2
    print(grid) # [[0, 0, 0], [0, 0, 0]]

At first it seems correct. We create a list of size 3 with [0] * 3. We add it to a list, and multiply the result by 2.
However, this code will not work as expected. The issue is that the inner list is a reference to the same list object.
This means that if we change one of the inner lists, all the inner lists will change as shown below.

    grid = [[0] * 3] * 2
    grid[0][0] = 1
    print(grid) # [[1, 0, 0], [1, 0, 0]]

A better way to initialize a 2-D list is to use a nested list comprehension:

    grid = [[0 for i in range(3)] for j in range(2)]
    grid[0][0] = 1
    print(grid) # [[1, 0, 0], [0, 0, 0]]

We create the inner list of zeroes with list comprehension. Then we use that list for the outer list with list comprehension again. This works as expected because each inner list is a separate object.

But there's a more concise solution you may prefer:

    grid = [[0] * 3 for _ in range(2)]

This code is equivalent to the previous code but uses less characters. We create a list of zeroes with [0] * 3 and use it for the outer list with list comprehension.
Since the variable in the for loop is not used, we use an underscore _ to indicate that it is a throwaway variable.
This is a common convention in Python.


Challenge
---------

    1. create_grid(rows: int, cols: int, value: int) -> List[List[int]] that takes three integers rows, cols, and value. It returns a 2-D list of size rows x cols where each element is equal to value.

Time Complexity
To initialze a 2-D grid of size n x m with a given value, the time complexity is O(n∗m).
"""


from typing import List


def create_grid(rows: int, cols: int, value: int) -> List[List[int]]:
    grid = [[value] * cols] * rows
    return grid

# do not modify below this line
print(create_grid(2, 3, 0))
print(create_grid(3, 2, 1))
print(create_grid(4, 4, 4))
print(create_grid(1, 1, 5))
print(create_grid(1, 5, 5))



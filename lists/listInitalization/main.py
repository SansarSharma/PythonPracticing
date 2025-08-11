"""
List Initialization
-------------------
If we want to create an empty list of a specific size, this is the easiest way to do it in Python

my_list = [0] * 5

The above code will create a list of 5 zeros. It might seem strange to multiply a list by a number, but this is the standard way to create a list of a specific size in Python. We could have replaced the 0 with any other value.

my_list = [1] * 3

The above code will create a list of 3 ones.


Challenge
---------
Implement the following functions:

    1. create_list_with_value(size: int, index: int, value: int) -> List[int] which should create and return a list of length size.
    All values in the list should be 0, except for the value at index "index", which should be the parameter value.
        You may assume the index is within the bounds of the list

Time complexity: O(n) where n is the size of the resulting list.
"""

from typing import List


def create_list_with_value(size: int, index: int, value: int) -> List[int]:
    result: list[int] = [0] * size
    result[index] = value

    return result


# do not modify below this line
print(create_list_with_value(5, 3, 7))
print(create_list_with_value(1, 0, 5))
print(create_list_with_value(10, 9, 9))
print(create_list_with_value(10, 9, 0))

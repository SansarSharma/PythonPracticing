"""
List Concat
-----------
Instead of using the extend() method there's an even easier way to concatenate two lists in Python. We can use the + operator:

The only difference between this and the extend() method is that the + operator creates a new list, while the extend() method modifies the original list.


Challenge
---------
Implement the following functions:

    1. combine_elements(arr1: List[int], arr2: List[int]) -> List[int] which takes two lists of integers and returns a new list that contains all the elements of the first list followed by all the elements of the second list.
    Do not modify the original lists.

Time complexity: O(n+m) where n is the length of one list and m is the length of the other list.
"""

from typing import List


def combine_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    result: List[int] = arr1 + arr2
    return result


# do not modify below this line
arr1 = [1, 3, 5]
arr2 = [4, 6, 8]

print(combine_elements(arr1, arr2))
print(arr1)
print(arr2)

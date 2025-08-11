"""
List Clone
----------
It's common to need to make a copy of a list in many algorithms. Python provides multiple ways to clone a list. Here are a few ways to do it:
    1. Using the copy() method:

        original_list = [1, 2, 3]
        cloned_list = original_list.copy()

    2. Using the slicing syntax:

        original_list = [1, 2, 3]
        cloned_list = original_list[:]

    3. Using the list() constructor:

        original_list = [1, 2, 3]
        cloned_list = list(original_list)

Keep in mind, that if you have a list of objects, the above methods will not create deep copies of the elements within the list. In this case we have a list of integers, which are primitive types, so we don't need to worry about that.
But if you had a list of lists, for example, you would need to use the copy.deepcopy() method to create a deep copy.

    4. Using copy.deepcopy() for deep copies:

        import copy
        original_list = [[1, 2], [3, 4]]
        cloned_list = copy.deepcopy(original_list)


Challenge
---------
Implement the following functions:

    1. remove_element(arr: List[int], element: int) -> List[int] that takes a list of integers and returns a new list with the specified element removed. You should not modify the original list.
        You may assume the element is always in the list.

Tip: It's okay if you don't remember how to remove an element from a list. You can look back at a previous lesson or do a quick search to refresh your memory.

Time complexity: O(n) where n is the length of the list being copied.
"""

import copy
from typing import List


def remove_element(arr: List[int], element: int) -> List[int]:
    new_list = copy.deepcopy(arr)
    new_list.remove(element)

    return (new_list)


# do not modify below this line
arr = [1, 3, 5, 7, 9]

print(remove_element(arr, 3))
print(arr)
print(remove_element(arr, 9))
print(arr)
print(remove_element(arr, 1))
print(arr)

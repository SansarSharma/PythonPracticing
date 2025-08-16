"""
Multi-Dimensional List
----------------------
We briefly mentioned nested lists earlier when we covered list cloning. A nested list is a list that contains other lists. This allows us to create multi-dimensional lists, which are lists of lists.

    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

This is a 2D list, where each element is a list of integers. Thus, nested_list[0] and nested_list[1] are lists themselves, and not integers. Perhaps it's better visualized like this:

    nested_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(nested_list[0])  # [1, 2, 3]
    print(nested_list[1])  # [4, 5, 6]
    print(nested_list[2])  # [7, 8, 9]

If we want to access elements in a list, we can do so by chaining the indices:

    print(nested_list[0][0])  # 1
    print(nested_list[2][2])  # 9
    print(nested_list[1][2])  # 6

The lists don't all have to be the same length:

    nested_list = [[1], [2, 3], [4, 5, 6]]

    for sublist in nested_list:
        for element in sublist:
            print(element)

The above code declares a 2D list with varying lengths for each sublist. We can iterate over the elements in each list using nested loops. The code will output the numbers 1 through 6.

Challenge
---------

    1. find_max_in_each_list(nested_arr: List[List[int]]) -> List[int] which takes a 2D list of integers and returns a list of the maximum element in each sublist.
    The returned list should contain the maximum element from each sublist in the order they appear in the input list.
        Example: find_max_in_each_list([[1, 2], [3, 4, 2]]) should return [2, 4].

You may assume that each sublist will contain at least one element.

"""

from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    max_list: List[int] = []
    max_num: int = 0
    temp_num: int = 0

    for sub_arr in nested_arr:

        for x in sub_arr:

            temp_num = x
            if (temp_num > max_num):
                max_num = temp_num

        max_list.append(max_num)
        max_num = 0
        temp_num = 0

    return max_list


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
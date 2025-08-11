"""
Resizable List Part 2
---------------------
These list operations are less common, but they are absolutely worth knowing:
    1. index(): Returns the index of the first occurrence of a specified element in the list.
        If the element is not in the list, we will get an ValueError.
    2. remove(): Removes the first occurrence of a specified element from the list.
    3. extend(): Adds the elements of another list to the end of the list.

Here are examples of each:

my_list = [1, 3, 2, 3]
my_list.index(3) # 1
my_list.remove(3) # [1, 2, 3]
my_list.extend([4, 5]) # [1, 2, 3, 4, 5]

If we want to check if an element is in a list, we can use the in operator:

my_list = [1, 2, 3]
if 3 in my_list:
    print("3 is in the list")

This is preferable to using index() unless we actually need the index of the element.


Challenge
---------
Implement the following functions:

    1. append_elements(arr1: List[int], arr2: List[int]) -> List[int]. It should append the elements of arr2 to the end of arr1 and return the resulting list.
    Yes, this is the same function from the previous lesson.
    2. remove_elements(arr1: List[int], arr2: List[int]) -> List[int]. It should remove all elements of arr2 from arr1 and return the resulting list.
        If any of the elements in arr2 are not in arr1, then skip them.
        You don't have to worry about implementing an efficient solution. Try to use the built-in functions.

Time Complexity

index()
Time complexity: O(n), where n is the length of the list.

pop().
Time complexity: O(n), where n is the length of the list.

insert().
Time complexity: O(m), where m is the length of the list passed to extend().

in operator on a list.
Time complexity: O(n), where n is the length of the list.
"""

from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    newlist: List[int] = arr1[:]

    newlist.extend(arr2)

    return newlist


def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    newlist: List[int] = arr1[:]

    for x in arr2:
        if x in newlist:
            newlist.remove(x)

    return newlist


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))
print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))


"""
Resizable List Part 1
---------------------
Some languages have both fixed-size arrays and resizable arrays. In Python, we only have resizable arrays, which are referred to as lists in Python. This means that we can add or remove elements from a list at any time.

The common operations on a list include:

    1 append(): Adds an element to the end of the list.
    2 pop(): Removes and returns the last element of the list.
        -If the list is already empty, we will get an IndexError.
        - We can also pass an integer to pop() to remove an element at a specific index.
        - If we pop(index) an index that is out of bounds, we will get an IndexError.
    3 insert(): Inserts an element at a specified index in the list.
        -If the index is out of bounds, we will get an IndexError.

Here are examples of each:
my_list = [1, 2, 3]

my_list.append(4) # [1, 2, 3, 4]
my_list.append(5) # [1, 2, 3, 4, 5]

my_list.pop() # [1, 2, 3, 4]

my_list.insert(1, 3) # [1, 3, 2, 3, 4]


Challenge
---------
Implement the following functions:

    1. append_elements(arr1: List[int], arr2: List[int]) -> List[int]. It should append the elements of arr2 to the end of arr1 and return the resulting list.
    2. pop_n(arr: List[int], n: int) -> List[int]. It should remove the last n elements from the list and return the resulting list. If n is greater than the length of the list, it should return an empty list.
    3. insert_at(arr: List[int], index: int, element: int) -> List[int]. It should insert the element at the specified index in the list and return the resulting list. If the index is out of bounds, you should insert it at the end of the list.

Time Complexity

append()
Time complexity: O(1)

pop().
Time complexity: O(1)

insert().
Time complexity: O(n),

where n is the number of elements in the list.
"""

from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    newlist: List[int] = arr1[:]
    length:int = len(arr2)

    for x in range(0,length,1):
        newlist.append(arr2[x])

    return newlist


def pop_n(arr: List[int], n: int) -> List[int]:
    newlist: List[int] = arr[:]
    arrLength: int = len(newlist)

    if(n >= arrLength):
        return []

    for x in range(0,n,1):
        newlist.pop()

    return newlist


def insert_at(arr: List[int], index: int, element: int) -> List[int]:
    newlist: List[int] = arr[:]

    newlist.insert(index,element)
    return newlist


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(pop_n([1, 2, 3, 4, 5], 2))
print(pop_n([1, 2, 3, 4, 5], 6))
print(pop_n([1, 2, 3, 4, 5], 5))

print(insert_at([1, 2, 3, 4, 5], 2, 6))
print(insert_at([1, 2, 3, 4], 6, 5))

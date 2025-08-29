"""
Heapify
-------
If we are given a list of elements up front, we can convert them into a heap using the heapq.heapify() function. This function rearranges the elements in the list so that they form a valid heap.
The heap is a min heap by default, meaning that the element with the smallest priority is at index 0.

    import heapq

    heap = [4, 2, 5, 3, 1]

    heapq.heapify(heap)

    while heap:
        print(heapq.heappop(heap))

The output of this code will be:

    1
    2
    3
    4
    5

We transformed the original list [4, 2, 5, 3, 1] into a heap using heapq.heapify(). We then popped all the elements from the heap in order of their priority.

Challenge
---------
Implement the following functions:

    1. heapify_strings(strings: List[str]) -> List[str] that takes a list of strings and returns a list of strings that have been transformed into a min heap.
    2. heapify_integers(integers: List[int]) -> List[int] that takes a list of integers and returns a list of integers that have been transformed into a min heap.
    3. heap_sort(nums: List[int]) -> List[int] that takes a list of integers and returns a list of integers that have been sorted in ascending order.
    You should use the heapify function to transform the list into a heap before sorting it.

Time and Space Complexity
    The time complexity of heapq.heapify() is O(n) where n is the number of elements in the heap.
    This means it's more efficient than pushing elements onto the heap one by one, which would take O(nlog(n)) time.

"""


import heapq
from typing import List


def heapify_strings(strings: List[str]) -> List[str]:
    heap_copied: List[str] = strings[:]

    heapq.heapify(heap_copied)
    return heap_copied


def heapify_integers(integers: List[int]) -> List[int]:
    heap_copied: List[int] = integers[:]

    heapq.heapify(heap_copied)
    return heap_copied


def heap_sort(nums: List[int]) -> List[int]:
    heap_copied: List[int] = nums[:]
    sorted_list: List[int] = []

    heapq.heapify(heap_copied)

    while heap_copied:
        sorted_list.append(heapq.heappop(heap_copied))

    return sorted_list


# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))

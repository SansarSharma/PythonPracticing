"""
Heap N Smallest
---------------
Heaps provide a very convenient way to find the smallest elements in a collection. For this we can use heapq.nsmallest():

    import heapq

    my_array = [1, 6, 3, 5, 7, 9, 8, 10, 2, 12]

    heapq.nsmallest(3, my_array)  # returns [1, 2, 3]
    heapq.nsmallest(5, my_array)  # returns [1, 2, 3, 5, 6]
    heapq.nsmallest(1, my_array)  # returns [1]

1. We initialized an unsorted array my_array with some integers.
2. We called heapq.nsmallest(3, my_array). This returns the 3 smallest elements in my_array. The elements are returned in sorted order.
3. We also called heapq.nsmallest(5, my_array) which returns the 5 smallest elements in my_array.
4. We also called heapq.nsmallest(1, my_array) which returns the smallest element in my_array.


Challenge
---------
Implement the following functions using heapq.nsmallest():

    1. get_min_element(arr: List[int]) -> int that returns the smallest element in the list arr.
    2. get_min_4_elements(arr: List[int]) -> List[int] that returns the 4 smallest elements in the list arr in increasing order.
    3. get_min_2_elements(arr: List[int]) -> List[int] that returns the 2 smallest elements in the list arr in decreasing order.

Note: Assume all input arrays are unsorted and contain enough elements to return the required number of elements.

Time and Space Complexity:

    The time complexity of heapq.nsmallest() is O(mlog(n)) where n is the number of elements to return and m is the size of the input.

    One way to implement nsmallest() is to iterate over the input and push each element onto a heap. We ensure the size of the heap is at most n by popping the largest element if the heap size exceeds n. Thus, we will use a max heap.


"""


import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    num_list: List[int] = heapq.nsmallest(1, arr)
    num: int = num_list[0]

    return num


def get_min_4_elements(arr: List[int]) -> List[int]:
    store: List[int] = []

    store = (heapq.nsmallest(4, arr))
    return store


def get_min_2_elements(arr: List[int]) -> List[int]:
    store: List[int] = []
    reverse: List[int] = []
    length: int = None
    selected: int = None

    store = (heapq.nsmallest(2, arr))
    length = len(store) - 1

    while (length >= 0):
        selected = store[length]
        reverse.append(selected)
        length -= 1

    return reverse


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

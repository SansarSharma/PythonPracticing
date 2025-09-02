"""
Heap N Largest
--------------
We also have heapq.nlargest() to get the n largest elements in a collection.

    import heapq

    my_array = [1, 6, 3, 5, 7, 9, 8, 10, 2, 12]

    heapq.nlargest(3, my_array)  # returns [12, 10, 9]
    heapq.nlargest(5, my_array)  # returns [12, 10, 9, 8, 7]
    heapq.nlargest(1, my_array)  # returns [12]

1. We initialized an unsorted array my_array with some integers.
2. We called heapq.nlargest(3, my_array). This returns the 3 largest elements in my_array. The elements are returned in decreasing order.
3. We also called heapq.nlargest(5, my_array) which returns the 5 largest elements in my_array in decreasing order.
4. We also called heapq.nlargest(1, my_array) which returns the largest element in my_array.

Challenge
---------
Implement the following functions using heapq.nlargest():

    1. get_max_element(arr: List[int]) -> int that returns the largest element in the list arr.
    2. get_max_4_elements(arr: List[int]) -> List[int] that returns the 4 largest elements in the list arr in decreasing order.
    3. get_max_2_elements(arr: List[int]) -> List[int] that returns the 2 largest elements in the list arr in increasing order.

Note: Assume all input arrays are unsorted and contain enough elements to return the required number of elements.

Time and Space Complexity:

    The time complexity of heapq.nlargest() is O(mlog(n)) where n is the number of elements to return and m is the size of the input.

    One way to implement nlargest()  is to iterate over the input and push each element onto a heap.
    We ensure the size of the heap is at most n by popping the smallest element if the heap size exceeds n. Thus, we will use a min heap.


"""


import heapq
from typing import List


def get_max_element(arr: List[int]) -> int:
    num_list: List[int] = heapq.nlargest(1, arr)
    num: int = num_list[0]

    return num

def get_max_4_elements(arr: List[int]) -> List[int]:
    store: List[int] = []

    store = (heapq.nlargest(4, arr))
    return store


def get_max_2_elements(arr: List[int]) -> List[int]:
    store: List[int] = []
    reverse: List[int] = []
    length: int = None
    selected: int = None

    store = (heapq.nlargest(2, arr))
    length = len(store) - 1

    while (length >= 0):
        selected = store[length]
        reverse.append(selected)
        length -= 1

    return reverse


# do not modify below this line
print(get_max_element([1, 2, 3]))
print(get_max_element([3, 2, 1, 4, 6, 2]))
print(get_max_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_max_4_elements([4, 9, 7, 3, 2, 7, 4, 6, 2]))
print(get_max_4_elements([4, 9, 7, 2, 1, 3, 2, 3, 4, 6, 2, 3]))
print(get_max_4_elements([4, 7, 2, 3, 2, 4, 6, 2]))

print(get_max_2_elements([4, 5, 3, 7]))
print(get_max_2_elements([8, 8, 7, 9]))
print(get_max_2_elements([1, 2, 3, 9, 8, 7, 6]))

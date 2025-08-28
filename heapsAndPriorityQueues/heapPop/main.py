"""
Heap Pop
---------
We can also remove elements from a heap using the heapq.heappop() function. This function removes the element with the smallest priority from the heap and returns it.

    import heapq

    heap = []

    heapq.heappush(heap, "banana")
    heapq.heappush(heap, "apple")
    heapq.heappush(heap, "kiwi")

    print(heapq.heappop(heap))  # apple
    print(heapq.heappop(heap))  # banana
    print(heapq.heappop(heap))  # kiwi

1. We pushed the strings "banana", "apple", and "kiwi" onto the heap.
2. We popped the element with the smallest priority, which is "apple". By default, the priority of strings is determined by their lexicographical order, with smaller lexicographical strings having higher priority.
3. We popped the next element with the smallest priority, which is now "banana".
4. We popped the last element with the smallest priority, which is now "kiwi".
5. The heap is now empty. If we try to pop an element from an empty heap, we will get an IndexError.

Challenge
---------
Implement the following function:

    1. heap_pop(heap: List[int]) -> List[int] that pops all elements from the heap heap and returns them in a list in the order that they were popped.
    The heap should be a min heap, meaning that the elements with the smallest priority should be popped first.

Time and Space Complexity
    The time complexity of heapq.heappop() is O(log(n)) where n is the number of elements in the heap.

"""


import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    storage: List[int] = []
    length: int = len(heap)

    for index in range(0, length, 1):
        storage.append(heapq.heappop(heap))

    return storage


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))


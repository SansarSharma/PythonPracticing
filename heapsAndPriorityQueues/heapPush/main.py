"""
Heap Push
---------
Heaps (or priority queues) are a data structure that allow you to insert (push) and remove (pop) elements based on some priority associated with each element.
In Python, a heap is a minimum heap by default, meaning that the element with the smallest priority is always at the top of the heap.


    import heapq

    heap = [] # min heap

    heapq.heappush(heap, 3)
    heapq.heappush(heap, 1)

    print(heap[0])  # 1

    heapq.heappush(heap, 0)

    print(heap[0])  # 0


1. We first imported the heapq module, which contains functions for working with heaps.
2. We created an empty list called heap. Heaps are implemented as lists in Python.
3. We pushed the elements 3 and 1 onto the heap.
4. We accessed the element with the smallest priority, which is 1. The element with the smallest priority is always at index 0. This is the same as calling .top() in other languages.
5. We pushed the element 0 onto the heap.
6. We accessed the element with the smallest priority, which is now 0.


Challenge
---------
Implement the function:

    1. heap_push(heap: List[int], value: int) -> int that pushes the integer value onto the heap.
    The heap should be a min heap, meaning that the element with the smallest priority should be at index 0. After pushing the element, return the element with the smallest priority.

Time and Space Complexity
    The time complexity of heapq.heappush() is O(log(n)) where n is the number of elements in the heap.
    The time complexity of accessing the element with the smallest priority is O(1), since indexing into a list is O(1).
    The space complexity of a heap is O(n), where n is the number of elements in the heap.

"""

import heapq
from typing import List


def heap_push(heap: List[int], value: int) -> int:
    heap_copied: List[int] = heap[:]
    small_num: int = None

    heapq.heappush(heap_copied, value)
    small_num = heap_copied[0]

    return small_num


# do not modify below this line
print(heap_push([1, 2, 3], 4))
print(heap_push([1, 2, 3], 0))
print(heap_push([1, 2, 3], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 5))

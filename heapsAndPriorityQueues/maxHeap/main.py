"""
Heapify
-------
Unfortunately, Python does not have a built-in max heap implementation.
However, we can simulate a max heap by negating the values we insert into the heap. This way, the element with the largest priority (the smallest value) will be at the top of the heap.

Suppose we had a set of numbers [4, 2, 3, 5]. We can insert these numbers into a max heap by negating them and inserting them into a min heap.
The negated numbers would be [-4, -2, -3, -5]. When we pop elements from the min heap, we would negate them again to get the original numbers.

    import heapq

    nums = [4, 2, 3, 5]
    max_heap = []

    for num in nums:
        heapq.heappush(max_heap, -num) # Negate the number

    while max_heap:
        top = -heapq.heappop(max_heap) # Negate the number back
        print(top)

The output of this code will be:

    5
    4
    3
    2

1. We negated the numbers and pushed them onto the heap, which is technically implemented as a min heap.
2. This way the largest original number, 5, will be at the top of the heap after negation.
3. We popped the elements from the heap and negated them back to get the original numbers.
4. The popped values were -5, -4, -3, -2 before we negated them back to 5, 4, 3, 2.


Challenge
---------
Implement the function:

    1. get_reverse_sorted(nums: List[int]) -> List[int] which takes a list of integers and returns the integers in reverse sorted order.
    You should use the max heap technique described above to achieve this. The list of integers given is not necessarily a heap.


"""


import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap_copied: List[int] = []
    store: List[int] = []

    for index in nums:
        heapq.heappush(heap_copied, -index)

    while heap_copied:
        store.append(-heapq.heappop(heap_copied))

    return store


# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
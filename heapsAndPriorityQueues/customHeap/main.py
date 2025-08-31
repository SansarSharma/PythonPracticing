"""
Custom Heap
-----------
Unfortunately, Python does not have a custom key parameter for the heapq module. This means that we cannot directly create a heap with custom priorities. However, we can simulate a custom heap by using a tuple as the element in the heap.

With tuples, Python will use the first element of the tuple as the priority. If two tuples have the same first element, Python will compare the second element of the tuples, and so on.

If we wanted to create a heap of integers by using the absolute value of each integer as the priority, we could use the following code:

    import heapq

    nums = [4, -2, 3, -5]
    heap = []

    for num in nums:
        pair = (abs(num), num)
        heapq.heappush(heap, pair)

    while heap:
        pair = heapq.heappop(heap)
        original_num = pair[1]
        print(original_num)

The output of this code will be:

    -2
    3
    4
    -5

1. We pushed tuples onto the heap where the first element was the absolute value of the number and the second element was the original number. [(4, 4), (2, -2), (3, 3), (5, -5)].
2. The heap was a min heap based on the first element of each tuple.
3. We popped the tuples and printed the second element from each, which was the original number.


Challenge
---------
This technique can also be used to implement a max heap:

    1. Implement the function get_reverse_sorted(nums: List[int]) -> List[int] which takes a list of integers and returns the integers in reverse sorted order.
    You should use the tuple technique described above to achieve this.


"""


import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap: List[int] = []
    store: List[int] = []
    pair: int = None
    value: int = None

    for index in nums:
        heapq.heappush(heap, (-index, index))

    while heap:
        pair = heapq.heappop(heap)
        value = pair[1]
        store.append(value)

    return store


# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))

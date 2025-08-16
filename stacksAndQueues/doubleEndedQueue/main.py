"""
Double Ended Queue
------------------
The deque provided in Python is actually a double-ended queue. It allows you to push or pop from either end of the queue efficiently. Here are two more common operations supported by a deque:

    1. appendleft() is used to enqueue an element to the left side of the queue.

    from collections import deque

    queue = deque()
    queue.appendleft(1) # [1]
    queue.appendleft(2) # [2, 1]


    2. pop() is used to remove and return the rightmost element from the queue.

    queue = deque([1, 2]) # pass a list to initialize the queue
    queue.pop() # [1]
    queue.pop() # []


Challenge
---------
Implement the following function using the queue operations described above:

    1. rotate_list(arr: List[int], k: int) -> Deque[int] that takes a list of integers arr and an integer k. It should convert the list into a deque. And next, rotate the values in the list to the right by k steps and return the resulting deque.
        Example: rotate_list([1, 2, 3, 4, 5], 2) should return deque([4, 5, 1, 2, 3]).

Time Complexity:
    1 appendleft(): O(1)
    2 pop(): O(1)

"""


from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    queue: Deque[int] = deque(arr)
    length: int = len(queue)

    if length == 0:
        return queue

    k = k % length

    for x in range(0, k, 1):
        queue.appendleft(queue.pop())

    return queue

# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))



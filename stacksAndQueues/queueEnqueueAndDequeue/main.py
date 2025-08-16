"""
Queue Enqueue and Dequeue
-------------------------
Python provides a deque class from the collections module that can be used to implement a queue.

    1. append() is used to enqueue an element to the right side of the queue.

    from collections import deque

    queue = deque()
    queue.append(1) # [1]
    queue.append(2) # [1, 2]

    2. popleft() is used to remove and return the leftmost element from the queue.

    queue = deque([1, 2]) # pass a list to initialize the queue

    queue.popleft() # Returns 1, queue is now [2]
    queue.popleft() # Returns 2, queue is now []

    3. [0] and [-1] can be used to access the leftmost and rightmost elements of the queue respectively. This assumes that the queue is not empty.

    queue = deque([1, 2, 3, 4])

    leftmost_element = queue[0] # 1
    rightmost_element = queue[-1] # 4

    Tip: In Python, we can also index any element in the queue using the square brackets [] similar to a list. This is technically not a queue operation but can be useful in some cases.

    4. len() can be used to check if the queue is empty.

    queue = deque([1, 2])

    while len(queue) > 0:
        print(queue.popleft())

Challenge
---------
Implement the following function using the queue operations described above:

    1. rotate_list(arr: List[int], k: int) -> Deque[int] that takes a list of integers arr and an integer k. It should convert the list into a deque, then rotate the values in the list to the left by k steps and return the resulting deque.
        Example: rotate_list([1, 2, 3, 4, 5], 2) should return deque([3, 4, 5, 1, 2]).

Hint: Any element you remove from the left side of the queue can be appended to the right side.

Time Complexity:
    1 append(): O(1)
    2 popleft(): O(1)
    3 Getting the first or last element with [0], [-1]: O(1)
    4 Getting an arbitrary element with [i]: O(n)
    3 len():O(1)

"""

from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    queue: List[int] = deque(arr)
    length: int = len(queue)
    k = k % len(queue)

    if (length == 0):
        return queue

    for x in range(0, k, 1):
        queue.append(queue.popleft())
    return queue


# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))


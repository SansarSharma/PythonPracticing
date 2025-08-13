"""
Stack Push and Pop
------------------
Python does not have a built-in stack data structure, but we can use a list for the same purposes.

    1. append() is used to push an element onto the stack.

    stack = []
    stack.append(1)
    stack.append(2)

    2. pop() is used to remove and return the top element from the stack.

    stack = [1, 2]
    top_element = stack.pop() # 2

    3. [-1] can be used to access the top element of the stack without removing it. This assumes that the stack is not empty.

    stack = [1, 2]
    top_element = stack[-1] # 2

    4. len() can be used to check if the stack is empty.

    stack = [1, 2]
    while len(stack) > 0:
        print(stack.pop())

Challenge
---------
Implement the following function using the stack operations described above:

    1. reverse_list(arr: List[int]) -> List[int] that takes a list of integers and returns a new list of the integers in reverse order.

Hint: Recall that elements from a stack are removed in reverse order.

Time Complexity:
    1 append(): O(1)
    2 pop():O(1)
    3 [-1]:O(1)
    4 len(): O(1)

-------------
You don't have to focus too much on the more complicated examples we presented. You will never be forced to use list comprehension, but it's worth knowing how to read it and implement the first example we've shown.
"""

from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    stack: List[int] = []
    reversed_stack: List[int] = []
    length:int = len(arr)

    for x in range(0,length,1):
        stack.append(arr[x])

    while len(stack) > 0:
        reversed_stack.append(stack.pop())

    return reversed_stack


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))

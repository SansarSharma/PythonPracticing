"""
Min Max Shortcut
----------------
You may recall Python has built-in functions to find the minimum and maximum values. We can use these functions to condense the following code:

transactions = -2
if transactions < 0:
    transactions = 0

into:

transactions = -2
transactions = max(0, transactions)

In the above code, we check if the value of transactions is less than 0. If so, we set transactions to 0, since it doesn't make sense to have a negative number of transactions.

This is a common pattern that comes up in algorithm problems. So we condense the code slightly by taking the max() of transactions and 0. We are essentially saying transactions should never be allowed to be negative.

We can also use the min() function to ensure a value doesn't exceed a certain limit:

transactions = 101

# This will ensure transactions is never greater than 100
if transactions > 100:
    transactions = 100

# This is equivalent to the above code
transactions = min(100, transactions)

Sometimes we can use these functions to make our code more readable and concise, especially if we already have a bunch of nested loops or conditional statements. In other cases you may prefer to keep the original if-statement.
In the above examples, we used constant values 0 and 100, but we could've also used variables.

Challenge
---------
Implement the following function:

    1. disallow_negatives(num: int) -> int that takes an integer and returns the integer if it is greater than or equal to 0. Otherwise, it should return 0.
    2. max_difference(nums: List[int]) -> int that takes a list of integers and returns the maximum difference between any two adjacent elements in the list, by subtracting the element on the left from the element on the right.
    In other words, it should return the maximum value of nums[i] - nums[i - 1] for all valid indices i.

You may assume the output will always be a positive integer.
Example: Given the list [10, 1, 3, 7], the maximum adjacent difference is 7 - 3 = 4.
You may assume all input lists will have at least two elements.
"""

from typing import List


def disallow_negatives(num: int) -> int:
    return (max(0, num))


def max_difference(nums: List[int]) -> int:
    diff: int = nums[1] - nums[0]
    length: int = len(nums)
    temp_diff: int = 0

    for x in range(1, length, 1):
        temp_diff = nums[x] - nums[x - 1]

        if (temp_diff > diff):
            diff = temp_diff

    return diff


# do not modify below this line
print(disallow_negatives(-2))
print(disallow_negatives(-1))
print(disallow_negatives(0))
print(disallow_negatives(1))
print(disallow_negatives(2))

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_difference([1, 2, 3, 4, 5, 6, 8, 9]))
print(max_difference([10, 1, 3, 7]))
print(max_difference([2, 4, 7, 5, 7, 8, 4, 2]))

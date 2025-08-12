"""
List Comprehension
------------------
A very powerful feature in Python is comprehension. It applies to lists and other data types in Python that we will cover later. It allows us to create lists in a concise way. Here's an example:

my_list = [i for i in range(5)]
print(my_list) # [0, 1, 2, 3, 4]

This is called list comprehension. In the above example, we have a for loop inside the square brackets. The loop iterates over the range of numbers from 0 to 4. Before the loop we place the expression i which is the value we want to add to the list.
This is a very concise way to create a list.

And it's very flexible:

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
result = [i + j for i, j in zip(arr1, arr2)]

Above we have two lists arr1 and arr2. We use the zip() function to iterate over both lists at the same time. We then add the elements of both lists together and create a new list. The expression i + j is the value we want to add to the list.

We can also add a condition to the comprehension:

arr = [1, 2, 3, 4, 5]
result = [i for i in arr if i % 2 == 0]

In the above example, we have a list arr. We iterate over the list and add the element to the new list only if it's even.
This might seem like overkill since we can accomplish the same thing with a simple loop, but it demonstrates the flexibility of list comprehension.

Challenge
---------
Implement the following function using list comprehension:

    1. create_list_of_odds(n: int) -> List[int] which takes an integer n and returns a list of all odd numbers from 1 to n (inclusive).

Hint: You can use the range() function and pass three arguments to it: the start (inclusive), the end (non-inclusive), and the step.

Time complexity: O(n) where n is the number of times the loop within the list comprehension runs.

-------------
You don't have to focus too much on the more complicated examples we presented. You will never be forced to use list comprehension, but it's worth knowing how to read it and implement the first example we've shown.
"""

from typing import List


def create_list_of_odds(n: int) -> List[int]:
    nums : List[int] = []

    for x in range(1,n+1,1):

        if x % 2 != 0:
            nums.append(x)

    return nums

# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))


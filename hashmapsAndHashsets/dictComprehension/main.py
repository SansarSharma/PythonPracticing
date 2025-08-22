"""
Dict Comprehension
------------------
Similar to list comprehension, Python also supports dictionary comprehension. We can use dictionary comprehensions to initialize dictionaries in a more concise way.

    nums = [1, 2, 3, 4, 5]
    squared = {num: num * num for num in nums}
    print(squared)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

In the above code, we created a dictionary where the keys are the numbers from the list nums and the values are the square of each number.
Notice that the syntax is similar to list comprehension, but we use curly braces instead of square brackets. Inside the curly braces, we have a key-value pair separated by a colon before the loop.

Challenge
---------
Implement the following function using dictionary comprehension:

    1. num_to_index(nums: List[int]) -> Dict[int, int] that takes a list of integers and returns a dictionary where the keys are the elements of the list and the values are the indices of those elements in the list.
    You can assume that all elements in the list are unique.


"""


from typing import List, Dict


def num_to_index(nums: List[int]) -> Dict[int, int]:
    store: Dict[int,int] = {}
    length:int = len(nums)

    for index in range(0,length,1):
        store[nums[index]] = index

    return store


# do not modify below this line
print(num_to_index([1, 2, 3, 4, 5, 6, 7, 8]))
print(num_to_index([8, 7, 6, 5, 4, 3, 2, 1]))
print(num_to_index([0, 3, 2, 4, 5, 1]))


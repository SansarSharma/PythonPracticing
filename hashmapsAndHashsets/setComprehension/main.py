"""
Hash Set Basics
---------------
Just like with lists and dictionaries, Python also supports set comprehension. We can use set comprehension to initialize sets in a more concise way.

    nums = [1, 3, 5]
    squared = {num * num for num in nums}
    print(squared)  # {1, 9, 25}

In the above code, we created a set where the elements are the square of each number in the list nums. Notice that the syntax is similar to list comprehension, but we use curly braces instead of square brackets. Inside the curly braces, we have the expression we want to add to the set.

Both dictionaries and sets use curly braces. The difference between them is that dictionaries have key-value pairs separated by a colon, while sets only have the elements themselves.


Challenge
---------
Implement the following function using set comprehension:

    1. double_nums(nums: List[int]) -> Set[int] that takes a list of integers and returns a set with the double of each number in the list.
        Example: double_nums([1, 2, 3]) should return a set with the elements 2, 4, and 6.


"""


from typing import List, Set


def double_nums(nums: List[int]) -> Set[int]:
    double: Set[int] = {num*2 for num in nums}
    return double


# do not modify below this line

output1 = double_nums([1, 2, 3])
print(type(output1))
print(sorted(list(output1)))

output2 = double_nums([4, -2, 0, 7])
print(type(output2))
print(sorted(list(output2)))

output3 = double_nums([10, 20, 30, 40, 50])
print(type(output3))
print(sorted(list(output3)))


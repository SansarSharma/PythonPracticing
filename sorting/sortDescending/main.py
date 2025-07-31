"""
Sort Descending
--------------
The .sort() method also accepts some optional parameters. This is the .sort() function signature:

def sort(key=None, reverse=False) -> None:

    1. The key parameter allows us to customize the sorting order. We will learn more about this soon.
    2. The reverse parameter is a boolean value that determines whether the list should be sorted in descending order. By default, it is set to False.

If we want to sort a list in descending order, we can set the reverse parameter to True.

elements = [5, 3, 6, 2, 1]
elements.sort(key=None, reverse=True)
print(elements) # [6, 5, 3, 2, 1]

We can actually omit the key parameter and only pass the reverse parameter, by using a feature of Python called keyword arguments.

elements.sort(reverse=True)

It's also possible for us to sort the list in ascending order and then manually reverse the result.

elements = [5, 3, 6, 2, 1]
elements.sort()
elements.reverse()

Challenge
---------
Implement the following functions:

1. sort_words(words: List[str]) -> List[str] - This function accepts a list of words and returns the list of words sorted in descending order.
2. sort_numbers(numbers: List[int]) -> List[int] - This function accepts a list of numbers and returns the list of numbers sorted in descending order.
3. sort_decimals(numbers: List[float]) -> List[float] - This function accepts a list of decimal numbers and returns the list of decimal numbers sorted in descending order.
"""

from typing import List


def sort_words(words: List[str]) -> List[str]:
    words.sort()
    words.reverse()
    return words

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort()
    numbers.reverse()
    return numbers

def sort_decimals(numbers: List[float]) -> List[float]:
    numbers.sort()
    numbers.reverse()
    return numbers



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))

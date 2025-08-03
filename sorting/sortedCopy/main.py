"""
Sort Lambda
-----------
There is another way to sort a list in Python, using the sorted() function.
The sorted() function returns a new list with the elements sorted in the specified order.
The original list remains unchanged.

words = ["kiwi", "pear", "apple", "banana", "cherry", "blueberry"]
sorted_words = sorted(words)
print(sorted_words) # ['apple', 'banana', 'blueberry', 'cherry', 'kiwi', 'pear']

The sorted() function takes the list as the first argument and returns a new list with the elements sorted in ascending order by default.

You can also specify the order using the reverse parameter:
numbers = [5, -3, 2, -4, 6, -2, 4]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers) # [6, 5, 4, 2, -2, -3, -4]

You can also pass a custom function to the key parameter to specify the sorting criteria.
numbers = [5, -3, 2, -4, 6, -2, 4]
sorted_numbers = sorted(numbers, key=abs)
print(sorted_numbers) # [2, -2, -3, 4, -4, 5, 6]

For the most part, it's similar to the sort() method, but it returns a new list instead of modifying the original list.

Challenge
---------
Implement the following functions:

    1. sort_words(words: List[str]) -> List[str] - This function accepts a list of words and returns a new list of words sorted in ascending order.
    Do not modify the original list.
    2. sort_numbers(numbers: List[int]) -> List[int] - This function accepts a list of numbers and returns a new list of numbers sorted in descending order based on their absolute value.
    Do not modify the original list.
"""

from typing import List


def sort_words(words: List[str]) -> List[str]:
    wordList: List[str] = sorted(words)
    return wordList

def sort_numbers(numbers: List[int]) -> List[int]:
    numList: List[int] = sorted(numbers,key=abs,reverse=True)
    return numList

# do not modify below this line
original_words = ["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]

print(original_words)
print(sort_words(original_words))

original_numbers = [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]

print(original_numbers)
print(sort_numbers(original_numbers))


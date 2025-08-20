"""
Default Dict
------------
In algorithms, it's very common to count the frequency of elements in a list or a string. The straight forward way to do this is with the following code:

    nums = [1, 2, 4, 3, 2, 1]
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    print(freq)  # {1: 2, 2: 2, 4: 1, 3: 1}

The above code iterates through nums, if a number is not in the dictionary, it adds it with a value of 1. If the number is already in the dictionary, it increments the value by 1.
This is perfectly fine, but Python provides a more elegant way to do this using the collections module.

The collections module provides a class called defaultdict that is a subclass of the built-in dict class.
It allows you to set a default value for a key that doesn't exist in the dictionary. This can be very useful when counting the frequency of elements in a list. Consider the following code:

    from collections import defaultdict

    nums = [1, 2, 4, 3, 2, 1]
    freq = defaultdict(int)

    for num in nums:
        freq[num] += 1

    print(freq)  # {1: 2, 2: 2, 4: 1, 3: 1}

We removed the need for conditional statements within the loop, but how? Well we created a defaultdict, and passed in int as the default value.
This means that if a key doesn't exist in the dictionary, it will be created with a default value of the integer 0. This allows us to increment the value without checking if the key exists.

This pattern is also used with other data types, such as lists and sets. For example, if you wanted to create a dictionary where the default value is an empty list, you would use:

    nums = [1, 2, 4, 3, 2, 1]
    d = defaultdict(list)

    for num in nums:
        d[num].append(num)

    print(d)  # {1: [1, 1], 2: [2, 2], 4: [4], 3: [3]}

This will create a dictionary where each key is a number in the list, and the value is a list of all the occurrences of that number.
Even if the number doesn't exist in the dictionary, it will first create an empty list as the default value, and then append the given value num to the list.


Challenge
---------
Implement the following function using a defaultdict:

    1. count_chars(s: str) -> Dict[str, int] that takes a string and returns a dictionary where the keys are the characters in the string and the values are the number of times each character appears in the string.
        Example: count_chars("hello") should return {'h': 1, 'e': 1, 'l': 2, 'o': 1}

    2. nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]] that takes a list of lists of integers and returns a dictionary where the keys are the first element of each list and the values are the rest of the elements in the list.
        Example: The input [[1, 2, 3], [4, 5, 6], [1, 4]] should return {1: [2, 3, 4], 4: [5, 6]}
        You may assume each sublist will have at least two elements.

"""


from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    storage: Dict[str, int] = defaultdict(int)

    for index in s:
        storage[index] += 1

    return storage


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    storage: Dict[int, List[int]] = defaultdict(list)

    for sublist in nums:
        key = sublist[0]
        values = sublist[1:]
        storage[key].extend(values)

    return storage


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
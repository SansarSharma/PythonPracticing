"""
Sorted Dict Basics
------------------
Python does not have a built-in sorted dictionary data structure. However, we can use the sorted containers library to create a sorted dictionary in Python.
It supports the same operations as a regular dictionary, but the keys are always sorted. A sorted dictionary may not contain duplicate keys.


Insertion: Insert a key-value pair into the sorted dict.

    from sortedcontainers import SortedDict

    sorted_dict = SortedDict()

    sorted_dict['C'] = 90

    sorted_dict['B'] = 80

    sorted_dict['A'] = 70

    print(sorted_dict)  # SortedDict({'A': 70, 'B': 80, 'C': 90})


Access: Access the value associated with a key.

    sorted_dict = SortedDict({'a': 1})

    print(sorted_dict['a']) # 1


Deletion: Delete a key-value pair from the sorted dict.

    sorted_dict = SortedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

    # removes & return the last key-value pair in sorted order
    sorted_dict.popitem() # ('d', 4)

    # removes & return the first key-value pair in sorted order
    sorted_dict.popitem(0) # ('a', 1)

    # remove & return the value associated with the key
    sorted_dict.pop('b') # 2

    del sorted_dict['c'] # {}

        As shown above, there are several ways to delete a key-value pair from a sorted dictionary.
        You can use the popitem() method to remove and return the first or last key-value pair in sorted order.
        You can also use the pop() method to remove and return the value associated with a specific key, or the del keyword to delete a key-value pair.

        The popitem() method will raise a KeyError if the dictionary is empty.

        The pop() method will raise a KeyError if the key does not exist.

        The del keyword will also raise a KeyError if the key does not exist.


Lookup: Check if a key exists in the sorted dict.

    sorted_dict = SortedDict({'a': 1})

    does_a_exist = 'a' in sorted_dict # True
    does_b_exist = 'b' in sorted_dict # False

        For lookup operations, you can also use the in operator, similar to how you would check if an element is in a list.


Iterating: Loop through the sorted dict.

    sorted_dict = SortedDict({'a': 1, 'b': 2, 'c': 3})

    for key, value in sorted_dict.items():
        print(key, value)

        Notice that we loop through the sorted dictionary using the items() method, which returns a list of key-value pairs. We will iterate over the key-value pairs in sorted order based on the keys.
        If we only iterated over the keys, but we needed the values as well, we would have to do a lookup for each key, which would be less efficient. (See the time complexity section below.)


Challenge
---------
Implement the following functions:

    1. remove_keys(sorted_dict: SortedDict[str, int], keys: List[str]) -> SortedDict[str, int]. It should take a sorted dictionary and a list of keys and remove the key-value pairs associated with those keys from the dictionary.
    Return the modified sorted dictionary.
        You may assume that all keys in the list exist in the sorted dictionary.
    2. get_values_before_target(sorted_dict: SortedDict[str, int], target: str) -> List[int]. It should take a sorted dictionary and a target key and return a list of values associated with keys that come before the target key in sorted order.
        You may assume that the target key exists in the sorted dictionary.
        The order of the values in the output list should match the order of the keys in the sorted dictionary.
        Example: get_values_before_target(SortedDict({'Alice': 90, 'Bob': 80, 'Charlie': 70}), 'Charlie') should return [90, 80].


Time and Space Complexity:

    Insertion: O(logn)
    Access: O(logn)
    Deletion: O(logn)
    Lookup: O(logn)


"""


from typing import List
from sortedcontainers import SortedDict


def remove_keys(sorted_dict: SortedDict[str, int], keys: List[str]) -> SortedDict[str, int]:
    pass


def get_values_before_target(sorted_dict: SortedDict[str, int], target: str) -> List[int]:
    pass


# do not modify below this line
print(remove_keys(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35}), ['Bob']))
print(remove_keys(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), ['Bob', 'David']))
print(remove_keys(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40, 'Eve': 45}), ['Alice', 'Eve']))

print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35}), 'Bob'))
print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), 'David'))
print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), 'Charlie'))
print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), 'Bob'))
print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), 'Alice'))


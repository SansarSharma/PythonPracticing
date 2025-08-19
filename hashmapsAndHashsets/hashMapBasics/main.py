"""
Hash Map Basics
---------------
Behind lists, hash maps are the most commonly used data structure in Python. A hash map is a collection of key-value pairs.
Each key is unique, and it maps to a specific value. Keys may be of any immutable type, such as integers, strings, or as we will see later, tuples.

In Python, hash maps are implemented using the dict class. The common operations on a hash map include:

Insertion: Insert a key-value pair into the hash map.

    my_dict = {}
    my_dict['a'] = 1 # {'a': 1}

Access: Access the value associated with a key.

    my_dict = {'a': 1}
    print(my_dict['a']) # 1

Deletion: Delete a key-value pair from the hash map.

    my_dict = {'a': 1, 'b': 2}
    del my_dict['a'] # {}
    my_dict.pop('b') # {}
    my_dict.pop('c') # KeyError: 'c'
    my_dict.pop('c', 'default') # No error, returns 'default'

        As shown above, there are two ways to delete a key-value pair from a hash map: using the del keyword or the pop() method. The only difference is that the pop() method returns the value associated with the key.

If the key does not exist, both pop() and del will raise a KeyError. To avoid this, you can pass a default value to the pop() method, which will be returned if the key does not exist.

Lookup: Check if a key exists in the hash map.

    my_dict = {'a': 1}
    does_a_exist = 'a' in my_dict # True
    does_b_exist = 'b' in my_dict # False

For lookup operations, you can also use the in operator, similar to how you would check if an element is in a list.

Challenge
---------
Implement the following functions:

    1. build_hash_map(keys: List[str], values: List[int]) -> Dict[str, int]. It takes two lists, keys and values, and returns a hash map where the keys are the elements of the keys list and the values are the elements of the values list.
        This may be a good opportunity to use the zip() function in Python.

    2. get_values(hash_map: Dict[str, int], keys: List[str]) -> List[int]. It takes a hash map and a list of keys and returns a list of the values associated with those keys.
        You may assume that all keys in the list exist in the hashmap
        The order of the values in the output list should match the order of the keys in the input list.

Tip: If you don't recall how to loop through a dictionary, check out the Dict Looping lesson from the Python for Beginners course.

Time Complexity
    Insertion: O(1)
    Access: O(1)
    Deletion: O(1)
    Lookup: O(1)

The above time complexities are technically for the average case, but in most cases it's safe to assume that these hash map operations are O(1).
"""

from typing import List, Dict


def build_hash_map(keys: List[str], values: List[int]) -> Dict[str, int]:
    build: Dict[str, int] = {}
    key_length: int = len(keys)
    value_length: int = len(values)

    if (key_length == value_length):

        for x in range(0, key_length, 1):
            build[keys[x]] = values[x]

        return build

    else:
        return build


def get_values(hash_map: Dict[str, int], keys: List[str]) -> List[int]:
    key_length: int = len(keys)
    valuearr: List[int] = []

    for x in range(0, key_length, 1):
        valuearr.append(hash_map[keys[x]])

    return valuearr


# do not modify below this line
print(build_hash_map(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(build_hash_map(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(build_hash_map(["Doug", "Bob", "Tommy"], [80, 90, 100]))

print(get_values({"Alice": 90, "Bob": 80, "Charlie": 70}, ["Alice", "Bob", "Charlie"]))
print(get_values({"Jane": 25, "Charlie": 60, "Carol": 100, }, ["Jane", "Carol"]))
print(get_values({"X": 205, "Y": 78, "Z": 100}, ["Y"]))


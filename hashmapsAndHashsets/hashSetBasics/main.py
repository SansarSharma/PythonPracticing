"""
Hash Set Basics
---------------
Hash sets are very similar to hash maps, but they only store keys without any associated values. Hash sets also cannot contain duplicates, just like hash maps.
In Python, hash sets are implemented using the set class. The common operations on a hash set include:

Insertion: Insert a key into the hash set.

    my_set = set()
    my_set.add('a') # {'a'}

Deletion: Delete a key from the hash set.

    my_set = {'a'}

    my_set.remove('a') # {}
    my_set.remove('a') # KeyError

    my_set.add('b') # {'b'}
    my_set.discard('b') # {}
    my_set.discard('b') # {} (no error)

        As shown above, you can use the remove() method to delete an element from a hash set. If the element does not exist, the method will raise a KeyError.
        Alternatively, you can use the discard() method, which will not raise an error if the element does not exist.

Lookup: Check if a key exists in the hash set.

    my_set = {'a'}

    'a' in my_set # True
    'b' in my_set # False

        For lookup operations, you can also use the in operator, similar to how you would check if an element is in a list.

Challenge
---------
Implement the following function using a Counter:

    1. build_hash_set(keys: List[str]) -> Set[str]. It takes a list of strings and returns a hash set containing those strings.

    2. check_keys(hash_set: Set[str], keys: List[str]) -> List[bool].
    It takes a hash set and a list of keys and returns a list of booleans indicating whether each key exists in the hash set. The order of the booleans in the output list should match the order of the keys in the input list.
        Example: check_keys({'a', 'b', 'c'}, ['a', 'd', 'c']) should return [True, False, True].


Time Complexity


    1.  Insertion: O(1)
    2.  Deletion: O(1)
    3.  Lookup: O(1)


The above time complexities are technically for the average case, but in most cases it's safe to assume that these hash set operations are O(1).
"""


from typing import List, Set


def build_hash_set(keys: List[str]) -> Set[str]:
    my_set: Set[str] = set()
    length: int = len(keys)

    for index in range(0,length,1):
        my_set.add(keys[index])

    return my_set


def check_keys(hash_set: Set[str], keys: List[str]) -> List[bool]:
    result: List[bool] = []
    length: int = len(keys)

    for index in range(0,length,1):
        result.append(keys[index] in hash_set)

    return result


# do not modify below this line

output1 = build_hash_set(["Alice", "Bob", "Charlie"])
print(type(output1))         # check the type of the output
print(sorted(list(output1))) # set order is not guaranteed so we need to sort the list

output2 = build_hash_set(["XY", "XX", "YY", "XY", "YX"])
print(type(output2))         # check the type of the output
print(sorted(list(output2))) # set order is not guaranteed so we need to sort the list

print(check_keys({"Alice", "Bob", "Charlie"}, ["Alice", "Bob", "Charlie", "David"]))
print(check_keys({'a', 'b', 'c'}, ['a', 'd', 'c']))
print(check_keys({'a', 'c'}, ['d', 'c']))
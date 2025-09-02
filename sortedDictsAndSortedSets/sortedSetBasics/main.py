"""
Sorted Set Basics
-----------------
Sorted sets are very similar to hash sets, but they store keys in sorted order. Sorted sets may not contain duplicate elements. The common operations on a sorted set include:


Insertion: Insert a key into the sorted set.

    from sortedcontainers import SortedSet

    my_set = SortedSet()

    my_set.add(90)
    my_set.add(80)
    my_set.add(85)

    print(my_set) # SortedSet([80, 85, 90])


Deletion: Delete a key from the sorted set.

    my_set = SortedSet([90, 80, 85, 95])

    my_set.remove(90) # SortedSet([80, 85, 95])

    my_set.discard(100) # SortedSet([80, 85, 95])

    my_set.pop() # 95

    my_set.pop(0) # 80

    print(my_set) # SortedSet([85])

    my_set.clear() # SortedSet([])

        The remove() method will raise a KeyError if the element does not exist, while the discard() method will not.
        The pop() method will remove and return the largest element in the sorted set.
        The pop(0) method will remove and return the smallest element in the sorted set.
        The clear() method will remove all elements from the sorted set.


Lookup: Check if a key exists in the sorted set.

    sorted_set = SortedSet([4, 3, 5, 2, 1])

    for num in sorted_set:
        print(num)  # 1, 2, 3, 4, 5

        For lookup operations, you can also use the in operator, similar to how you would check if an element is in a list.


Iterating: Loop through the sorted set.

    sorted_set = SortedSet([4, 3, 5, 2, 1])

    for num in sorted_set:
        print(num)  # 1, 2, 3, 4, 5

        The elements in a sorted set are always sorted in ascending order.


Challenge
---------
Implement the following functions:

    1. get_first_three(sorted_set: SortedSet[int], nums1: List[int], nums2: List[int]) -> List[int]. It takes a sorted set of integers and two lists of integers, nums1 and nums2.
    The elements from nums1 should be added to the sorted set, and then the elements from nums2 should be removed from the sorted set.
    Finally, return the first three elements of the sorted set.
        It's possible some elements in nums2 may not exist in the sorted set, so ensure your code does not raise an error in this case.
        You may assume there will always be at least three elements in the sorted set after adding and removing elements.


Time and Space Complexity:

    Insertion: O(logn)
    Deletion: O(logn)
        Note: clear() is O(n)
    Lookup: O(logn)


"""


from typing import List
from sortedcontainers import SortedSet


def get_first_three(sorted_set: SortedSet[int], nums1: List[int], nums2: List[int]) -> List[int]:
    pass


# do not modify below this line
print(get_first_three(SortedSet(), [1, 2, 3], [4]))
print(get_first_three(SortedSet([1, 4, 7, 2, 8, 9]), [10], [1, 7, 2]))
print(get_first_three(SortedSet([1, 2, 3, 7]), [], [4, 5, 6]))
print(get_first_three(SortedSet([1, 2, 3, 4, 5, 6, 7, 8, 9]), [10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9]))



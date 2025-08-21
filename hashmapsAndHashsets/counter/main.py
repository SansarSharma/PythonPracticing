"""
Counter
-------
If all we want to do is count the occurrences of elements in a list, an even better solution exists than the defaultdict. We can use the collections.Counter class:


    from collections import Counter

    nums = [1, 2, 4, 3, 2, 1]

    counter = Counter(nums)

    print(counter)  # Counter({1: 2, 2: 2, 4: 1, 3: 1})

    counter[100] += 1 # No error, even though 100 is not a key

    print(counter)  # Counter({1: 2, 2: 2, 4: 1, 3: 1, 100: 1})


The Counter class is a subclass of the dict class, and it provides a more concise way to count the occurrences of elements in a list.
It returns a dictionary where the keys are the elements in the list and the values are the number of times each element appears.
It behaves similarly to a defaultdict with an integer default value, meaning if a key doesn't exist, it will return 0.


Tip - Sometimes using the Counter class can feel like cheating, so in a real interview it might be worth checking with you're interviewer if they're fine with you using it.
      Usually if the problem you are given is a challenging one, they should be fine with it. Worst case, you can use a defaultdict or implement the counting logic yourself with a regular dictionary.

If we want to count the occurences of multiple lists or strings, we can use the update() method:

    nums1 = [1, 2, 4, 3, 2, 1]
    nums2 = [1, 2, 3, 4, 5]

    counter = Counter(nums1)
    counter.update(nums2)

    print(counter)  # Counter({1: 3, 2: 3, 4: 2, 3: 2, 5: 1})


Challenge
---------
Implement the following function using a Counter:

    1. count_chars(s1: str, s2: str) -> CounterType that takes two strings and returns a Counter object that counts the occurences of each character in the two strings combined.
        Example: count_chars("hello", "world") should return Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1})


"""


from collections import Counter
from typing import Counter as CounterType


def count_chars(s1: str, s2: str) -> CounterType:
    counter: dict[str, int] = []

    counter = Counter(s1)
    counter.update(s2)

    return counter


# do not modify below this line
print(count_chars("hello", "world"))
print(count_chars("hello", "worldhello"))
print(count_chars("areallylongstring", "heyhowisitgoing"))
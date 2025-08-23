"""
Dict Items
----------
If we wanted all the keys from a dictionary, we could loop over the dictionary and append the keys to a list. But Python provides a more concise way to get all the keys from a dictionary using the keys() method.

    my_dict = {"a": 1, "b": 2, "c": 3}
    keys = my_dict.keys()
    print(keys)  # dict_keys(['a', 'b', 'c'])
    keys_list = list(keys)
    print(keys_list)  # ['a', 'b', 'c']


The keys() method returns a view object that displays a list of all the keys in the dictionary. We can convert this view object to a list using the list() method.

Similarly, we can get all the values from a dictionary using the values() method.


    my_dict = {"a": 1, "b": 2, "c": 3}
    values = my_dict.values()
    print(values)  # dict_values([1, 2, 3])
    values_list = list(values)
    print(values_list)  # [1, 2, 3]


Lastly, we can get all the key-value pairs from a dictionary using the items() method. This is most commonly used when we want to loop over both the keys and values in a dictionary.


    my_dict = {"a": 1, "b": 2, "c": 3}
    for key, value in my_dict.items():
        print(key, value)


Challenge
---------
Implement the following function using a Counter:

    1. get_dict_items(age_dict: Dict[str, int]) -> List[Tuple[str, int]] that takes a dictionary of names and ages and returns a list of tuples where each tuple contains a name and an age.


"""


from typing import Dict, List, Tuple


def get_dict_items(age_dict: Dict[str, int]) -> List[Tuple[str, int]]:
    return list(age_dict.items())


# do not modify below this line
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35}))
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}))
print(get_dict_items({'Bob': 30, 'David': 40, 'Charlie': 35, 'Alice': 25, 'Eve': 45}))
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40, 'Eve': 45, 'Frank': 50}))

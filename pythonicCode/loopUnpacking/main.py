"""
Loop Unpacking
--------------
We can also use unpacking in loops to iterate over a list of lists. This is useful when we know the size of the inner lists and want to unpack them into variables.

points = [[0, 0], [2, 4], [3, 6], [5, 10]]
for x, y in points:
    print(f"x: {x}, y: {y}")

We could accomplish this without packing with slightly more code:
for point in points:
    x, y = point[0], point[1]
    print(f"x: {x}, y: {y}")

You can see we saved a line of code by using unpacking.

Challenge
---------
Implement the following functions:

    1. best_student(scores: List[Tuple[str, int]]) -> str: that takes a list of tuples. Each tuple represents the (name, score) of a student. Find the student with the highest score and return their name.

You may assume that a score will never be less than 0 and that only one student will have the highest score.
"""
from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    arrLength: int = len(scores)
    name: str = ""
    score: int = -1
    tempName: str = None
    tempScore: int = None

    for index in range(0, arrLength, 1):
        tempName = scores[index][0]
        tempScore = scores[index][1]

        if (tempScore >= score):
            name = tempName
            score = tempScore

    return (f"{name}")


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))




"""
Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two
different items in the array that, when added together, give the target value. The indices of these items should
 then be returned in a tuple / list (depending on your language) like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers;
 target will always be the sum of two different items from that array).

Based on: http://oj.leetcode.com/problems/two-sum/

two_sum([1, 2, 3], 4) # returns [0, 2] or [2, 0]

"""


def two_sum(numbers: list, target: int) -> list:  # type: ignore[return]
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]


print(two_sum([1, 2, 3], 4))


# Best practice and clever solution using enumerate() and list comprehension:


def two_sums(numbers: list, target: int) -> tuple:  # type: ignore[return]
    for i, val1 in enumerate(numbers[:-1]):
        for j, val2 in enumerate(numbers[i + 1 :]):
            if val1 + val2 == target:
                return i, j + i + 1


"""
given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5."""


def solution(A: list) -> int:
    A.sort()
    smallest = 1
    for i in A:
        if i == smallest:
            smallest += 1
    return smallest

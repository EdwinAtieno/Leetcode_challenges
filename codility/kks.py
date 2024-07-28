"""
there is an array number made of N integers. each number has at least two digits and its first and last digits are
different. you can selsect a pair of numbers if the last digit of the first selected number is the same as the first
digit  of the second number. calculate the number of ways in which such a pair of numbers can be selected. example
numbers = [30,12,29,91] the function should return 3. the pairs are: (12,29), (29,91),(91,12)
"""

from typing import Any


def solution(n: list) -> Any:
    count = 0
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if str(n[i])[-1] == str(n[j])[0]:
                count += 1
    return count


numbers = [30, 12, 29, 91]
print(solution(numbers))

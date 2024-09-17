"""
given two sets of cards, a and b, and card number x, return the difference between the card set and that the difference
is | a[i] - b[i] > or = x | for all i in a and b
"""


def twoSetCards(a: list, b: list, x: int) -> int:
    return sum(1 for i in range(len(a)) if abs(a[i] - b[i]) >= x)


a = [1, 2, 3]
b = [4, 5, 6]
x = 1
print(twoSetCards(a, b, x))

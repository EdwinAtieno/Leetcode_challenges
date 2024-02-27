x = 7

print(x**3)
print(x & 3)
print(x | 3)
print(x ^ 3)
print(x >> 3)
print(x << 3)

"""
Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
"""
print((6 + 3) - (6 + 3))

"""
Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:
"""

print(100 + 5 * 3)

# Python Operators Overview

This document provides an overview of various categories of operators in Python, including examples for each.

## Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:

| Operator | Name            | Example  ||
|----------|-----------------|----------|-------------------------|
| +        | Addition        | x + y    |
| -        | Subtraction     | x - y    |
| *        | Multiplication  | x * y    |
| /        | Division        | x / y    |
| %        | Modulus         | x % y    |
| **       | Exponentiation  | x ** y   |
| //       | Floor division  | x // y   |

## Assignment Operators
Assignment operators are used to assign values to variables:

| Operator | Example | Same As ||
|----------|---------|---------|-------------------------|
| =        | x = 5   | x = 5   |
| +=       | x += 3  | x = x + 3 |
| -=       | x -= 3  | x = x - 3 |
| *=       | x *= 3  | x = x * 3 |
| /=       | x /= 3  | x = x / 3 |
| %=       | x %= 3  | x = x % 3 |
| //=      | x //= 3 | x = x // 3 |
| **=      | x **= 3 | x = x ** 3 |
| &=       | x &= 3  | x = x & 3  |
| \|=      | x \|= 3 | x = x \| 3 |
| ^=       | x ^= 3  | x = x ^ 3  |
| >>=      | x >>= 3 | x = x >> 3 |
| <<=      | x <<= 3 | x = x << 3 |

## Comparison Operators
Comparison operators are used to compare two values:

| Operator | Name                   | Example ||
|----------|------------------------|---------|-------------------------|
| ==       | Equal                  | x == y  |
| !=       | Not equal              | x != y  |
| >        | Greater than           | x > y   |
| <        | Less than              | x < y   |
| >=       | Greater than or equal  | x >= y  |
| <=       | Less than or equal     | x <= y  |

## Logical Operators
Logical operators are used to combine conditional statements:

| Operator | Description                                       | Example              ||
|----------|---------------------------------------------------|----------------------|-------------------------|
| and      | Returns True if both statements are true          | x < 5 and x < 10    |
| or       | Returns True if one of the statements is true      | x < 5 or x < 4      |
| not      | Reverse the result, returns False if the result is true | not(x < 5 and x < 10) |

## Identity Operators
Identity operators are used to compare objects, checking if they are the same object with the same memory location:

| Operator | Description | Example ||
|----------|-------------|---------|-------------------------|
| is       | Returns True if both variables are the same object | x is y               |
| is not   | Returns True if both variables are not the same object | x is not y           |

## Membership Operators
Membership operators are used to test if a sequence is presented in an object:

| Operator | Description                                       | Example              ||
|----------|---------------------------------------------------|----------------------|-------------------------|
| in       | Returns True if a sequence with the specified value is present in the object | x in y |
| not in   | Returns True if a sequence with the specified value is not present in the object | x not in y |

## Bitwise Operators
Bitwise operators are used to compare (binary) numbers:

| Operator | Name | Description                                       | Example              ||
|----------|------|---------------------------------------------------|----------------------|-------------------------|
| &        | AND  | Sets each bit to 1 if both bits are 1             | x & y               |
| \|       | OR   | Sets each bit to 1 if one of two bits is 1        | x \| y              |
| ^        | XOR  | Sets each bit to 1 if only one of two bits is 1   | x ^ y               |
| ~        | NOT  | Inverts all the bits                              | ~x                 |
| <<       | Zero fill left shift | Shift left by pushing zeros in from the right and let the leftmost bits fall off | x << 2 |




# Python Operators Precedence

This document provides an overview of the precedence order of Python operators, listed in descending order from the highest precedence to the lowest.

| Operator | Description                           |           |
|----------|---------------------------------------|-----------|
| ()       | Parentheses                           |           |
| **       | Exponentiation                        |           |
| +x, -x, ~x | Unary plus, unary minus, and bitwise NOT |        |
| *, /, //, % | Multiplication, division, floor division, and modulus |    |
| +, -     | Addition and subtraction              |           |
| <<, >>   | Bitwise left and right shifts         |           |
| &        | Bitwise AND                           |           |
| ^        | Bitwise XOR                           |           |
| \|       | Bitwise OR                            |           |
| ==, !=, >, >=, <, <=, is, is not, in, not in | Comparisons, identity, and membership operators |
| not      | Logical NOT                           |           |
| and      | Logical AND                           |           |
| or       | Logical OR                            |           |

Note: Parentheses have the highest precedence, and operators with the same precedence are evaluated from left to right. Use parentheses to clarify the order of evaluation when needed.

Feel free to click on "Try it" links to experiment with the operators in a Python environment.
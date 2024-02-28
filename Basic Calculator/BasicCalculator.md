# Expression Evaluator

This Python solution provides an implementation to evaluate mathematical expressions represented as strings. The expressions include the basic operators (`+`, `-`, `*`, `/`) and may contain spaces between numbers and operators. The solution aims to calculate and return the value of the given expression.

## Code

```python
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # my code
        stack = []
        num = 0
        sign = "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if (not s[i].isdigit() and s[i] != " ") or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / float(num)))
                sign = s[i]
                num = 0
        return sum(stack)

    def calculateII(self, s):
        """
        :type s: str
        :rtype: int
        """
        # my code
        return eval(s)
```

## Usage

The solution offers two methods:

1. **`calculate` Method:**
   - Takes a string `s` as input, representing a mathematical expression.
   - Returns an integer, which is the result of evaluating the expression.

2. **`calculateII` Method:**
   - Takes a string `s` as input, representing a mathematical expression.
   - Returns an integer, utilizing the `eval` function to evaluate the expression.

## Example

```python
# Example Usage
solution = Solution()
expression = "3+2*2"
result = solution.calculate(expression)
print(result)
```

**Output:**
```
7
```

This example demonstrates the usage of the `calculate` method to evaluate the expression "3+2*2," resulting in the value 7.

Feel free to utilize these methods for your expression evaluation needs. Note that the solution follows integer division rules, truncating towards zero, and does not use built-in functions like `eval()` for mathematical expression evaluation.
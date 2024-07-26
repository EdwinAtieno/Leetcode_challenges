# Readme: Lambda Functions in Python

Lambda functions, also known as anonymous functions, are concise and small functions that can take any number of arguments but have only one expression.

## Syntax

```python
lambda arguments : expression
```

### Example 1: Adding 10 to a Number

```python
# Add 10 to argument a, and return the result
x = lambda a: a + 10
print(x(5))  # Output: 15
```

### Example 2: Multiplying Two Numbers

```python
# Multiply argument a with argument b and return the result
x = lambda a, b: a * b
print(x(5, 6))  # Output: 30
```

## Why Use Lambda Functions?

Lambda functions are particularly powerful when used as anonymous functions inside other functions. They are handy for short, temporary operations.

### Example: Creating a Doubler Function

```python
def myfunc(n):
    return lambda a: a * n

# Create a function that always doubles the number you send in
mydoubler = myfunc(2)
print(mydoubler(11))  # Output: 22
```

In this example, `myfunc` is a function that returns a lambda function. `mydoubler` is a function created by calling `myfunc(2)`, and it effectively doubles any number passed to it.

Use lambda functions when an anonymous function is needed for a short period, and their concise syntax makes them suitable for such scenarios.
def create_phone_number(n: list) -> str:
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


"""
    .format(): This is a string method that is used to perform string formatting. It allows you to insert values into a string in a specified format.

    *n: The asterisk (*) before n is used to unpack the elements from the n iterable (e.g., a tuple, list, etc.). It allows you to pass multiple arguments to the .format() method.

    Here's a step-by-step explanation of how .format(*n) works:
"""


def create_phone_numbers(n: list) -> str:
    # your code here
    f = "".join(map(str, n[0:3]))
    s = "".join(map(str, n[3:6]))
    t = "".join(map(str, n[6:10]))
    return "(" + f + ") " + s + "-" + t

"""Complete the solution so that the function will break up camel casing, using a space between words.
Example

"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

"""
import re


def solution(s: str) -> str:
    camel_case_words = re.sub(r"([a-z])([A-Z])", r"\1 \2", s)
    # Join the words with a space and return the result
    return camel_case_words


# or you can use the following code
def solution1(s: str) -> str:
    newStr = ""
    for letter in s:
        if letter.isupper():
            newStr += " "
        newStr += letter
    return newStr

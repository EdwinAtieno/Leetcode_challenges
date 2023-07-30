"""Complete the solution so that the function will break up camel casing, using a space between words.
Example

"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

"""
import re
def solution(s):
    camel_case_words = re.sub(r'([a-z])([A-Z])', r'\1 \2', s)
    # Join the words with a space and return the result
    return camel_case_words
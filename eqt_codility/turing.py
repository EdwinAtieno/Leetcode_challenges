"""
given twos string set1 and set2 find all odd words
a word is called odd when it appears only once in one of the sets, and not in the other set
example input: set1 = "this is a test", set2 = "this is a test too"
output: "too"
example input: set1 = "this is a test", set2 = "google"
output: ["google"]
example input: set1 = "this is a best test", set2 = "this is a google test"
output: ["best", "google"]
"""


def find_odd_words(set1: str, set2: str) -> list:
    words_set1 = set(set1.split())
    words_set2 = set(set2.split())

    # Find words that appear only once in one of the sets
    odd_words_set1 = words_set1 - words_set2
    odd_words_set2 = words_set2 - words_set1

    # Combine the odd words from both sets into a single list
    odd_words = list(odd_words_set1 | odd_words_set2)

    return odd_words


print(find_odd_words("this is a  best test", "this is a test too"))

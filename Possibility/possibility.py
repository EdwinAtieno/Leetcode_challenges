from typing import Tuple


def check_key(key: str, hint: str) -> Tuple[int, int]:
    correct_count = 0
    wrong_count = 0
    # check for correct digit and placement
    if key[0] == hint[0]:
        correct_count += 1
    # check for correct digit but wrong placement
    elif key[0] in hint:
        wrong_count += 1
    if key[1] == hint[1]:
        correct_count += 1
    elif key[1] in hint:
        wrong_count += 1
    if key[2] == hint[2]:
        correct_count += 1
    elif key[2] in hint:
        wrong_count += 1
    # return a tuple with the number of correct and wrong digits
    return correct_count, wrong_count


# list of hints and their corresponding keys
hints = [
    ("682", (1, 0)),
    ("614", (0, 1)),
    ("206", (0, 2)),
    ("738", (0, 0)),
    ("780", (0, 1)),
]

# generate all possible 3-digit keys
keys = [
    str(i) + str(j) + str(k)
    for i in range(0, 10)
    for j in range(0, 10)
    for k in range(0, 10)
]

# iterate over each key and check if it matches all the hints
for key in keys:
    match = True
    for hint in hints:
        if check_key(key, hint[0]) != hint[1]:
            match = False
            break
    if match:
        print("The correct key is:", key)
        break

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        output = {}


        for word in strs:
            word_list = list(word)
            word_list.sort()
            word_key = "".join(word_list)

            if output.get(word_key):
                output.get(word_key).append(word)
            else:
                output[word_key] =[word]


        return [val for val in output.values()]

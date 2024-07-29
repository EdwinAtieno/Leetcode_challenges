"""
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help
 him to find out, how many cakes he could bake considering his recipes?
Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the
maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour
or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.
"""
from typing import (
    Any,
    List,
)


def cakes(recipe: dict, available: dict) -> Any:
    for key in recipe:
        if key not in available:
            return 0
    return min([available[key] // recipe[key] for key in recipe])


def cake(recipe: dict, available: dict) -> Any:
    min_cake = []
    for i in recipe:
        if i not in available:
            return 0  # Return "0" as a string to indicate unavailability of an ingredient
        biggie = available[i] // recipe[i]
        min_cake.append(biggie)
    min_cakez = "".join(map(str, min_cake))
    return min(min_cakez)


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))
print(cake(recipe, available))


def solution(a: List) -> Any:
    a.sort()
    count = 1
    for i in range(1, len(a)):
        if a[i] != a[i - 1]:
            count += 1
    return count


def valid_brace(string: List) -> Any:
    stack = []
    for c in string:
        if c in ["(", "[", "{"]:
            stack.append(c)
        elif c == ")":
            if not stack or stack.pop() != "(":
                return False
        elif c == "]":
            if not stack or stack.pop() != "[":
                return False
        elif c == "}":
            if not stack or stack.pop() != "{":
                return False
    return not stack


"""there are N guests (numbered from 0 to N-1) IN A SANATORIUM WAITING TO BE ASSIGNED A ROOM. IN EACH ROAM, ANY NUMBER OF GUEST
CAN BE ACCOMMODATED. HOWEVER, NOT ALL GIEST LIKE TO HAVE A LOT OF ROOMMATES. YOU ARE GIVEN AN ARRAY A OF N INTEGERS: THE K-TH GUEST WANTS TO BE IN A
ROOM THAT CONTAINS AT MOST a[k] guests including themself. write a function given that given the array A, returns the minimum number of rooms needed to accommodate all guests.
for example given A = [1,1,1,1,1] your function should return 5. each guest wants to be in a separate room.
for example given A = [2,1,4] your function should return 2. the second guest should be accommodated alone, and the other two guests can share the other room.
"""

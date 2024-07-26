thistuple = ("apple", "banana", "cherry")
print(thistuple)

"""Print the number of items in the tuple:"""
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

"""One item tuple, remember the comma:
"""
thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = "apple"
print(type(thistuple))

"""Using the tuple() method to make a tuple:"""
thistuple = tuple(
    ("apple", "banana", "cherry")
)  # note the double round-brackets
print(thistuple)

"""Print the last item of the tuple:"""
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

"""Return the third, fourth, and fifth item:"""
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

"""This example returns the items from the beginning to, but NOT included, "kiwi":"""
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

"""This example returns the items from index -4 (included) to index -1 (excluded)"""
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

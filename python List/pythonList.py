thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

thislist = list(
    ("apple", "banana", "cherry")
)  # note the double round-brackets
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist[1])


"""
Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
"""
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

"""
By leaving out the start value, the range will start at the first item:
This example returns the items from the beginning to, but NOT including, "kiwi":
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

"""This example returns the items from "cherry" to the end:"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

"""This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

"""Check if "apple" is present in the list:"""
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

"""Change the second item:"""
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

"""Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


"""
Change the second value by replacing it with two new values:
"""
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


"""Change the second and third value by replacing it with one value:"""
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

"""Insert "watermelon" as the third item:"""
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

"""Using the append() method to append an item:"""
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

"""Add the elements of tropical to thislist:"""
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

"""Remove "banana":"""
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

"""Remove the second item:"""
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

"""Remove the first item:"""
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

"""Clear the list content:"""
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

"""Print all items in the list, one by one:"""
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)


"""Print all items by referring to their index number:"""
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

"""A short hand for loop that will print all items in a list:"""
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

"""Print all items, using a while loop to go through all the index numbers"""
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

"""With list comprehension you can do all that with only one line of code:"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

"""Only accept items that are not "apple":"""
newlists = [x for x in fruits if x != "apple"]

"""You can use the range() function to create an iterable:"""
newlist1 = [x for x in range(10)]

"""Set the values in the new list to upper case:"""
newlist3 = [x.upper() for x in fruits]
print(newlist, newlist1, newlist3, newlists)

"""
The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
"""
thislist = ["apple", "banana", "cherry"]
newlist = [x if x != "banana" else "orange" for x in thislist]
print(thislist, newlist)

"""Sort the list alphabetically:"""
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

"""Sort the list descending:"""
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

"""Sort the list based on how close the number is to 50:"""


class listFunc(object):
    def myfunc(self, n: int) -> int:
        return abs(n - 50)

    thislist = [100, 50, 65, 82, 23]
    thislist.sort(key=myfunc)
    print(thislist)


"""Case sensitive sorting can give an unexpected result:"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

"""Perform a case-insensitive sort of the list:"""
thislist2 = ["banana", "Orange", "Kiwi", "cherry"]
thislist2.sort(key=str.lower)
print(thislist2)

"""Reverse the order of the list items:"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

"""Make a copy of a list with the copy() method:"""
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

"""Join two list:"""
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

"""
Another way to join two lists is by appending all the items from list2 into list1, one by one:
"""
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)

"""Use the extend() method to add list2 at the end of list1:"""
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

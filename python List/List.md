# Python Lists

Lists in Python are versatile data structures used to store multiple items in a single variable. They are ordered, changeable, and allow duplicate values. Here's an overview of Python lists and their operations:

## Creating Lists

Lists are created using square brackets:

```python
thislist = ["apple", "banana", "cherry"]
print(thislist)
```

## List Items

- List items are ordered and indexed.
- They are changeable and allow duplicate values.
- Items can be of any data type.

## Using `list()` Constructor

It is possible to use the `list()` constructor:

```python
thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)
```

## Accessing Items

List items are accessed by referring to the index number:

```python
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
```

## Negative Indexing

Negative indexing starts from the end:

```python
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])  # Refers to the last item
```

## Range of Indexes

Specify a range of indexes to get a sublist:

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
```

## Check if Item Exists

Use the `in` keyword to check if an item is present:

```python
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
```

## Changing Item Values

Change the value of a specific item by referring to the index:

```python
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
```

## Changing a Range of Item Values

Change values within a specific range:

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
```

## Inserting Items

Insert a new list item at a specific index:

```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "watermelon")
print(thislist)
```

# Python List Operations

Lists in Python are versatile data structures used to store and manipulate collections of items. Here's an overview of various list operations in Python:

## Append Items

To add an item to the end of the list, use the `append()` method:

```python
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
```

## Extend List

To append elements from another list to the current list, use the `extend()` method. It can also add items from any iterable object:

```python
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
```

## Remove Specified Item

The `remove()` method removes the specified item. If there are multiple occurrences, it removes the first one:

```python
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
```

## Remove Specified Index

The `pop()` method removes the specified index. If no index is specified, it removes the last item. The `del` keyword can also be used:

```python
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
```

## Clear the List

The `clear()` method empties the list:

```python
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
```

## Loop Through a List

You can loop through the list items using a `for` loop:

```python
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
```

## Loop Through the Index Numbers

Loop through the list items by referring to their index number:

```python
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
```

## Using a While Loop

Loop through the list items using a `while` loop:

```python
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i += 1
```

## Looping Using List Comprehension

List Comprehension offers a concise syntax for looping through lists:

```python
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
```

## List Comprehension

Create a new list based on existing values:

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
```

## Sort List Alphanumerically

The `sort()` method sorts the list alphanumerically:

```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
```

## Sort Descending

To sort descending, use the `reverse=True` keyword argument:

```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)
```

## Customize Sort Function

Customize your sort function using the `key` argument:

```python
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)
```

## Case Insensitive Sort

For case-insensitive sorting, use `key=str.lower`:

```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)
```

## Reverse Order

The `reverse()` method reverses the current sorting order of the elements:

```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
```

## Copy a List

Make a copy of a list using the `copy()` method:

```python
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
```

## Join Two Lists

Use the `extend()` method or the `+` operator to join two lists:

```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
```

## List Methods

Python provides various built-in methods for list manipulation:

- `append()`: Adds an element at the end of the list.
- `clear()`: Removes all elements from the list.
- `copy()`: Returns a copy of the list.
- `count()`: Returns the number of elements with the specified value.
- `extend()`: Adds elements of a list (or any iterable) to the end of the current list.
- `index()`: Returns the index of the first element with the specified value.
- `insert()`: Adds an element at the specified position.
- `pop()`: Removes the element at the specified position.
- `remove()`: Removes the item with the specified value.
- `reverse()`: Reverses the order of the list.
- `sort()`: Sorts the list.

Feel free to explore these operations to enhance your list manipulation skills in Python!
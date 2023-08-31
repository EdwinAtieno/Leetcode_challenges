"""
There are N guests (numbered from 0 to N-1) in a sanatorium waiting to be assigned a room.
In each room, any number of guests can be accommodated. However, not all guests like to have a lot of roommates.
You are given an array A of N integers: the K-th guest wants to be in a room that contains at most A[K] guests,
including themselves. Write a function: int solution (vector<int> &A); that, given the array A, returns the minimum
number of rooms needed to accommodate all guests. Examples: 1. Given A = [1, 1, 1, 1, 1], your function should return 5.
Each guest should be accommodated in their own separate room. 2. Given A = [2, 1, 4], your function should return 2.
The second guest should be accommodated in one room and the other two guests in another room. 3.
Given A = [2, 7, 2, 9, 8], your function should return 2. The first and the third guests should be accommodated in one
room and the other three guests in another room. 4. Given A = [7, 3, 1, 1, 4, 5, 4, 9], your function should return 4.
The guests can be accommodated as follows: the first two guests in one room, the third and the fourth guests in t
wo single rooms, and the other guests in another room. Write an efficient algorithm for the following assumptions:
 • N is an integer within the range [1..100,000]; • each element of array A is an integer within the range [1..100,000].

"""


def room(A: list) -> int:
    # Sort the array A in descending order based on the maximum number of guests allowed
    A.sort(key=lambda x: -x)

    # Initialize variables to keep track of the minimum number of rooms needed
    min_rooms = 1
    curr_guests = 0

    # Loop through the sorted array and assign guests to rooms
    for k in range(len(A)):
        # Get the maximum number of guests allowed for the current guest
        max_guests = A[k]

        # If there are already enough guests in the current room, start a new room
        if curr_guests >= max_guests:
            min_rooms += 1
            curr_guests = 0

        # Add the current guest to the current room
        curr_guests += 1

    # Return the minimum number of rooms needed
    return min_rooms


print(room([7, 3, 1, 1, 4, 5, 4, 9]))

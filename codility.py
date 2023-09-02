# """
# There are N guests (numbered from 0 to N-1) in a sanatorium waiting to be assigned a room.
# In each room, any number of guests can be accommodated. However, not all guests like to have a lot of roommates.
# You are given an array A of N integers: the K-th guest wants to be in a room that contains at most A[K] guests,
# including themselves. Write a function: int solution (vector<int> &A); that, given the array A, returns the minimum
# number of rooms needed to accommodate all guests. Examples: 1. Given A = [1, 1, 1, 1, 1], your function should return 5.
# Each guest should be accommodated in their own separate room. 2. Given A = [2, 1, 4], your function should return 2.
# The second guest should be accommodated in one room and the other two guests in another room. 3.
# Given A = [2, 7, 2, 9, 8], your function should return 2. The first and the third guests should be accommodated in one
# room and the other three guests in another room. 4. Given A = [7, 3, 1, 1, 4, 5, 4, 9], your function should return 4.
# The guests can be accommodated as follows: the first two guests in one room, the third and the fourth guests in t
# wo single rooms, and the other guests in another room. Write an efficient algorithm for the following assumptions:
#  • N is an integer within the range [1..100,000]; • each element of array A is an integer within the range [1..100,000].
#
# """
# from typing import Any
#
#
# def room(A: list) -> int:
#     # Sort the array A in descending order based on the maximum number of guests allowed
#     A.sort(key=lambda x: -x)
#
#     # Initialize variables to keep track of the minimum number of rooms needed
#     min_rooms = 1
#     curr_guests = 0
#
#     # Loop through the sorted array and assign guests to rooms
#     for k in range(len(A)):
#         # Get the maximum number of guests allowed for the current guest
#         max_guests = A[k]
#
#         # If there are already enough guests in the current room, start a new room
#         if curr_guests >= max_guests:
#             min_rooms += 1
#             curr_guests = 0
#
#         # Add the current guest to the current room
#         curr_guests += 1
#
#     # Return the minimum number of rooms needed
#     return min_rooms
#
#
# print(room([7, 3, 1, 1, 4, 5, 4, 9]))
#
#
# """
# Please help solve this python question A DOMINO is a rectangular title divide into two separate squares.
# Each square is decorated with a number of spots (also called pips) denoted with a value from 0 to 6.
# other is an array a of length 2n representing n dominoes. DOMINOES ARE ARRANGED IN A LINE IN THE ORDER in which
# they appear in array. the number of dots on the left and right parts of the k-th domino are A[2K] AND A[2*K+1]
# respectively. FOR EXAMPLE, AN ARRAY A=[2,4,1,3,4,6,2,4,1,6] REPRESENTS A SEQUENCE OF FIVE DOMINO TILES: (2,4) (1,3)
# (4,6) (2,4) (1,6). IN A CORRECT DOMINO sequence, each pair neighboring tiles should have the same number of dots on t
# heir adjacent parts. for example tiles (2,4) and (4,6) form a correct domino sequence and tiles (2,4) and (1,3) do not.
#  what is the minimum number of domino tiles that must be removed from the sequence so that the remaining tiles form a
#  correct domino sequence? example A=[2, 4, 1, 3, 4, 6, 2, 4, 1, 6] function returns 3
# """
#
#
# def find_pairs(numbers):
#     """
#     Finds all pairs of numbers in the array `numbers` where the last digit of the first selected number is the same as the first digit of the second number.
#
#     Args:
#       numbers: The array of numbers.
#
#     Returns:
#       The number of pairs of numbers found.
#     """
#     pairs = set()
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             if numbers[i][-1] == numbers[j][0]:
#                 pairs.add((numbers[i], numbers[j]))
#     return len(pairs)
#
#
# numbers = [30, 12, 29, 91]
# print(find_pairs(numbers))
#
#
# def soliton(A: list) -> Any:
#     """# Initialize variables to keep track of the minimum number of domino tiles that must be removed
#     min_tiles = 0
#     k = 0
#
#     # Loop through the array A and check if the current pair of tiles form a correct domino sequence
#     while k < len(A) - 1:
#         # Get the number of dots on the left and right parts of the current pair of tiles
#         left = A[k]
#         right = A[k + 1]
#
#         # If the current pair of tiles do not form a correct domino sequence, remove one of the tiles
#         if left != right:
#             min_tiles += 1
#             k += 1
#
#         # Move on to the next pair of tiles
#         k += 1
#
#     # Return the minimum number of domino tiles that must be removed
#     return min_tiles"""
#
#     n = len(A) // 2
#     T = [[float("inf") for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         T[i][i] = 0
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             for k in range(i, j):
#                 T[i][j] = min(T[i][j], T[i][k] + T[k + 1][j])
#     return T[1][n - 1]
#
#
# print(soliton([2, 4, 1, 3, 4, 6, 2, 4, 1, 6]))
def find_pairs(numbers: list) -> int:
    """
    Finds all pairs of numbers in the array `numbers` where the last digit of the first selected number is the same as the first digit of the second number.

    Args:
      numbers: The array of numbers.

    Returns:
      The number of pairs of numbers found.
    """
    pairs = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if str(numbers[i])[-1] == str(numbers[j])[0]:
                pairs.add((numbers[i], numbers[j]))
    return len(pairs)


numbers = [30, 12, 29, 91]
print(find_pairs(numbers))

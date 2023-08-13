"""
A DOMINO is a rectanngula title divide into two separate squares. Each square is decorated with a number of spots (also called pips) denoted with a value from 0 to 6.
ther is an array a of length 2*n representing n dominoes. DOMINOES ARE ARRANGEDE IN A LINE IN THE ORDER in which they appear in array. the number of dots
on the left and right parts of the k-th domino are A[2*K] AND A[2*K+1] respectively. FOR EXAMPLE, AN ARRAY A=[2,4,1,3,4,6,2,4,1,6] REPRESENTS A SEQUENCE OF FIVE DOMINO
TILES: (2,4) (1,3) (4,6) (2,4) (1,6). IN A CORRECT DOMINO sequence, each pair neighboring tiles should have the same number of dots on their adjacent parts. for example tiles (2,4) and (4,6) form a correct domino sequence and tiles (2,4) and (1,3) do not. what is the minimum number of domino tiles that must be removed from the sequence so that the remaining tiles form a correct domino sequence? example A=[2, 4, 1, 3, 4, 6, 2, 4, 1, 6] function returns 3
"""
from typing import List


def minmum_domino(A: List) -> int:
    count = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if (
                A[i][0] == A[j][0]
                or A[i][0] == A[j][1]
                or A[i][1] == A[j][0]
                or A[i][1] == A[j][1]
            ):
                count += 1
    return count

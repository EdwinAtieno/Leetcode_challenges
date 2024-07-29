"""
 A DOMINO is a rectanngula title divide into two separate squares. Each square is decorated with a number of spots
(also called pips) denoted with a value from 0 to 6.
ther is an array a of length 2*n representing n dominoes. the i-th domino has a[2*i] and a[2*i+1] representing the
values of the two squares. write a function that returns the maximum number of pips that can be obtained by rearranging
the dominoes. you can rotate each domino to swap the values.
"""
from typing import List


def dominio(A: List) -> int:
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

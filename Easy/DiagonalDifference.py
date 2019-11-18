"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
"""


def diagonalDifference(arr):
    leftToRight = 0
    rightToLeft = 0
    for i in range(len(arr)):
        leftToRight += arr[i][i];
        rightToLeft += arr[(len(arr) - 1) - i][i];
    return abs(rightToLeft - leftToRight)


arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

print(diagonalDifference(arr))

"""
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros.
    Print the decimal value of each fraction on a new line.
"""


def plusMinus(arr):
    """
    arr: list of integer
    returns ratio of positive negative and zeros
    """
    countPositive = 0
    countNegative = 0
    countZeros = 0
    for i in arr:
        if i > 0:
            countPositive += 1
        if i < 0:
            countNegative += 1
        if i == 0:
            countZeros += 1
    poRatio = round(float(countPositive / len(arr)), 6)
    neRatio = round(float(countNegative / len(arr)), 6)
    zeRatio = round(float(countZeros / len(arr)), 6)
    print(format(poRatio, '.6f'))
    print(format(neRatio, '.6f'))
    print(format(zeRatio, '.6f'))


arr = [55, 48, 48, 45, 91, 97, 45, 1, 39, 54, 36, 6, 19, 35, 66, 36, 72, 93, 38, 21, 65, 70, 36, 63, 39, 76, 82, 26, 67,
       29, 24, 82, 62, 53, 1, 50, 47, 65, 67, 19, 66, 90, 77]
plusMinus(arr)

"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four
    of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated
    long integers.
"""


def miniMaxSum(arr):
    """
    arr: string of integer
    returns : min and max
    """
    s = 0
    a = sorted(arr)
    for i in a:
        s += i
    print(s - a[0], s - a[-1])


a = [1, 2, 3, 4, 5]
miniMaxSum(a)

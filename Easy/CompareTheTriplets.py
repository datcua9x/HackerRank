"""
find their comparison points by comparing a[0] with b[0 ,a[1] with b[1] , and a[2]  with  b[2]
if a[i] > b[i] Alice get 1 point
if a[i] < b[i] Bob get 1 point
if a[i] = b[i] nobody receives a point.
"""


def compareTriplets(a, b):
    """
    :param a: list of 3 numbers
    :param b: list of 3 numbers
    :return: score of Alice and Bob
    """
    countAlice = 0
    countBob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            countAlice += 1
        elif a[i] < b[i]:
            countBob += 1
    return countAlice, countBob


a = [17, 28, 30]
b = [99, 16, 8]
print(compareTriplets(a, b))

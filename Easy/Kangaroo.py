"""
The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show.
If it is possible, return YES, otherwise return NO
"""


def kangaroo(x1, v1, x2, v2):
    """
    :param x1: integers, starting position for kangaroo 1
    :param v1: integers, starting jump distance for kangaroo 1
    :param x2: integers, starting position for kangaroo 2
    :param v2: integers, starting jump distance for kangaroo 2
    :return: YES or NO
    """
    check = False
    for i in range(10000):
        x1 += v1
        x2 += v2
        if x2 == x1:
            check = True
            break
        else:
            check = False
    if check:
        return "YES"
    else:
        return "NO"


print(kangaroo(2081, 8403, 9107, 8400))

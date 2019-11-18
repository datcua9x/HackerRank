"""
Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. The last
    line is not preceded by any spaces.
Write a program that prints a staircase of size .
"""


def staircase(n):
    """
    n: integer
    returns: a staircase of size  using # symbols and spaces.
    """

    for i in range(1, n + 1):
        print(str('#' * i).rjust(n))


staircase(5)

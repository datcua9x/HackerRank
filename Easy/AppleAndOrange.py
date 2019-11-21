"""Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges
that land on Sam's house, each on a separate line.

countApplesAndOranges has the following parameter(s):

s: integer, starting point of Sam's house location.
t: integer, ending location of Sam's house location.
a: integer, location of the Apple tree.
b: integer, location of the Orange tree.
apples: integer array, distances at which each apple falls from the tree.
oranges: integer array, distances at which each orange falls from the tree.
"""


def countApplesAndOranges(s, t, a, b, apples, oranges):
    """
    :param s: integer, starting point of Sam's house location.
    :param t: integer, ending location of Sam's house location.
    :param a: integer, location of the Apple tree.
    :param b: integer, location of the Orange tree.
    :param apples: integer array, distances at which each apple falls from the tree.
    :param oranges: integer array, distances at which each orange falls from the tree.
    :return:
    """
    countA = 0
    countO = 0
    for i in apples:
        range = i + a
        if s <= range <= t:
            countA += 1
    for i in oranges:
        range = i + b
        if s <= range <= t:
            countO += 1
    print(countA, countO)


apples = [-2, 2, 1]
oranges = [5, -6]

print(countApplesAndOranges(7, 11, 5, 15, apples, oranges))

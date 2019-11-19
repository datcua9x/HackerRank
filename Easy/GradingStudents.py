"""
Every student receives a grade  in the inclusive range from 0 to 100
Any grade less than 40 is a failing grade.
If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5
If the value of grade is less than 38 , no rounding occurs as the result will still be a failing grade.
"""
from pip._vendor.msgpack.fallback import xrange
import random


def gradingStudents(grades):
    """
    :param grades:an array of integers representing grades before rounding
    :return: an array of integers
    """
    s = []
    for j in grades:
        for i in range(0, 105, 5):
            if j >= 38:
                abstract = i - j
                if 3 > abstract >= 0:
                    s.append(i)
                if 5 > abstract >= 3:
                    s.append(j)
        if j < 38:
            s.append(j)
    return s


my_randoms = random.sample(xrange(0, 101), 10)
print("Original Grades     ", my_randoms)
print("Grades after rounded", gradingStudents(my_randoms))

"""
You are in charge of the cake for your niece's birthday and have decided the cake will have one candle for each
year of her total age. When she blows out the candles, she’ll only be able to blow out the tallest ones. Your task is
to find out how many candles she can successfully blow out.
"""


def birthdayCakeCandles(ar):
    max = ar[1]
    count = 0
    for i in ar:
        if i > max:
            max = i
    for i in ar:
        if i == max:
            count += 1
    return count


ar = [3, 2, 1, 3]
print(birthdayCakeCandles(ar))

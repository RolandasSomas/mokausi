"""
Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
"""

import math


def verciam_skaicius(skaicius=int):
    data = []
    for i in str(skaicius)[::-1]:
        data.append(i)
    return " ".join(data)


print(verciam_skaicius(5649874456))

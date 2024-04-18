"""
Exercise 5: Get all values from the dictionary and add them to a list but don’t add duplicates
Given:

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
Expected Outcome:

[47, 52, 44, 53, 54]
"""

speed = {
    "jan": 47,
    "feb": 52,
    "march": 47,
    "April": 44,
    "May": 52,
    "June": 53,
    "july": 54,
    "Aug": 44,
    "Sept": 54,
}


def no_duplicates(speeds):
    for value in speed.values():
        a = []
        a.append(value)
        b = set(a)
        print(b)


no_duplicates(speed)

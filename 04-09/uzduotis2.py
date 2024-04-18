"""
Parašykite funkciją, kuri perkeltų visus vieno tipo elementus į list galą:
move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.
Registruokite įvestis ir rezultatus į failą.
"""


def move_ones_to_end(arr):
    not_ones = []
    ones = []
    for num in arr:
        if num == 1:
            ones.append(num)
        else:
            not_ones.append(num)
    return not_ones + ones


arr = (1, 3, 2, 4, 4, 1, 1)
result = move_ones_to_end(arr)
print(result)

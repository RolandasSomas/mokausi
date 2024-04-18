"""
Exercise 3: Create a Python set such that it shows the element from both lists in a pair
Given:
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
Expected Output:
Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)
"""

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]


def return_zipped_data(listas_1, listas_2):
    result = []
    for i in range(len(listas_1)):
        result.append((listas_1[i], listas_2[i]))
    return result


print(return_zipped_data(first_list, second_list))

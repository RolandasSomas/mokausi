"""
8. Parasyti funckija, kuri priimtu du variabe – lista kartotini.
Grazinti turi lista, kuriame buvo listai su kartotiniu nariu skaiciumis. Pvz.
Data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Kartotinis = 3
Grazina [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""

import math

Data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
kartotinis = 3


def return_sliced_list(numbers: list, number: int):
    value = math.ceil(len(numbers) / number)
    result = []
    for i in range(value):
        first_index, second_index = i * number, i * number + number
        result.append(numbers[first_index:second_index])
    return result


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
kartotinis = 1

print(return_sliced_list(numbers=data, number=kartotinis))

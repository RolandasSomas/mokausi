'''
Pvz. jei duota:
Data = {
1: ‘vienas’,
2: ‘du’,
3: ‘trys’,
4: ‘keturi’
}
Reikaling = [1, 2]

Trinti = [3]

Grazina du dictus:

{
1: ‘vienas’,
2: ‘du’,
4: ‘keturi’
}
Ir:
{
1: ‘vienas’,
2: ‘du’,
}
# '''
# data = {
# 1: 'vienas',
# 2: 'du',
# 3: 'trys',
# 4: 'keturi'
# }
#
# pirmas_sarasas = data.pop(3)
# print(data)
#
# antras_sarasas = data.pop(3 and 4)
# print(data)

import copy
data=[]
def calculate_dict(data: dict, kintamasis:list, deleting_key):
    result_n = {}
    new_data = copy.deepcopy(data)
    for key in data:
        if key in kintamasis:
            result_n[key] = data[key]
        if key in deleted_keys:
            del new_data[key]
    return result_n, new_data


numbers  = {
1: 'vienas',
2: 'du',
3: 'trys',
4: 'keturi'
}

needed_keys= [1, 2]
deleted_keys = [1]

print(calculate_dict(data=numbers, kintamasis=needed_keys, deleting_key= deleted_keys))

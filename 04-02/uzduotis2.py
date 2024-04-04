'''
Sukurkite funkciją, kuri prie kiekvieno list nario prideda string galūnę
'''

# def add_string(values:list,end_string= 'string') -> list:
#     return [f'{d}_{end_string}' for d in data]
#
# data = [1, 3, 'namas', 'kepure']
# end_string = 'string'
# print(add_string(values=data, end_string=end_string))

my_list = [10, 20, 30, 40, 50]

for index, element in enumerate(my_list):
    print("Index:", index, "Element:", element)
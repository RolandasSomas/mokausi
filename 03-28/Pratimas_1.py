'''
Raskite visus skaičius nuo 1 iki 1000, kurie dalijasi iš 6.
'''


# result=int()
#
# for i in range(1, 1010):
#     if i % 6 == 0:
#         print(i, 'dalijasi is 6')

# destytojo versija

def find_numbers_devide_number_six():
    rezultatas= []
    for number in range(1, 1001):
        if number % 6 == 0:
            rezultatas.append(number)
    return rezultatas

print(find_numbers_devide_number_six())


'''
Raskite visus skaičius iš 1-1000, kuriuose yra 9.
'''

listas = []
for number in range(1, 1000):
    if str('9') in number:
    listas.append(number)
    print(number.find('9'))



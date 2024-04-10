'''
Sukurkite 3 funkcijas, kurios yra susijusios viena su kita
(viena iškviečiama kitoje), ir išbandykite visus logging
sunkumo lygius pagal savo projektą
'''

def first_function():
    print('Hello this is function is called from another')

def second_function():
    print('This is second function and its running well')
    first_function()

def main():
    print('This is main function, working properly, now calling other two:')
    second_function()

main()

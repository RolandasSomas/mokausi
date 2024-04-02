'''
Sukurkite kintamuosius, kuriuose reprezentuotų vartotojo vardą ir slaptažodį.
 Pradėkite begalinį ciklą, leidžiantį įvesti vartotojo vardą ir slaptažodį.
  Jei duomenys teisingi, sustabdykite begalinį ciklą ir išspausdinkite pasisveikinimo pranešimą.
'''



correct_name, correct_last_name = 'Rolandas', 'Somas'
while True:
    input_name = input('prasau ivesti varda:')
    input_last_name = input('prasau ivesti pavarde:')

    if (input_name, input_last_name) == (correct_name, correct_last_name):
        print(f'Hello{correct_name}, {correct_last_name}')
        break
    print('prasau ivesti dar karta')

# while True:
#     vardas = input('iveskite vartotojo varda:')
#     if len(vardas) != 0:
#          break
# print(f'jusu vartotojo vardas: {vardas}')
#
# while True:
#     psw = input('iveskite slaptazodi:')
#     if len(psw) != 0:
#          break
# if vardas and psw !=0:
#     print('Sveiki prisijunge')









'''
Sukurkite string iš daugybės žodžių: Apskaičiuokite, kiek žodžių turi raidę e.
'''

tekstas = ('Pamėginkite suprasti kas čia vyksta. Patarimas: judėti nuo '
           'smulkiausiu detalių kaip pvz suprasti ką daro enumerate,'
           ' sujungti detalę po detalės kol bus viskas aišku')

lauzytas_tekstas= tekstas.split()


for i in lauzytas_tekstas:
    if i.count('e') != 0:
        print('turi raide e : ',i)



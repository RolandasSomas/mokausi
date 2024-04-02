'''
Patys sukurkite bent 5 skirtingas funkcijas ir jas išbandykite
'''

def sudedam_skaiciu(a:int, b:int):
    return a+b

ats = sudedam_skaiciu(8, 9)
print('sudeti du skaiciai: ', ats)

def vardas_pavarde_amzius(vardas: str, pavarde: str, amzius:int):
    print(f'Mane vadina: {vardas} {pavarde}, ir man yra {amzius} metai')

vardas_pavarde_amzius(vardas= 'Rolandas' , pavarde= 'Somas' , amzius= 37)


def dezes_matmenys(ilgis:int, plotis:int, aukstis:int):
    print(f'dezes ilgis: {ilgis} , plotis: {plotis}, aukstis: {aukstis}')

dezes_matmenys(ilgis=10, plotis = 15, aukstis= 20)

def kmi_skaiciuokle(mase:int, ugis: int):
    print(f'tavo kuno mases indeksas yra: {mase/ugis}')

kmi_skaiciuokle(95,184)
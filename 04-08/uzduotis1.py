'''
Reikia parašyti funckiją, kuri turėtų du variable – vienas yra listas,
kitas – iš kokio skaičiaus reikia kad dalintusi.
 Reikia grazinti visus skaicius kurie dalinasi is duoto skaiciaus.
'''

skaiciai = [2, 4, 6, 8, 10, 12]
daliklis = 3


def skaiciavimas(skaiciai=list, daliklis=int):
    result = []
    for s in skaiciai:
        if s % daliklis == 0:
            result.append(s)
    return result


print(skaiciavimas(skaiciai, daliklis))





'''
Tarp lyginių ir nelyginių skaičių vyksta didelis karas. Šiame kare jau žuvo daug skaičių,
todėl tavo užduotis - jį nutraukti. Jūs turite nustatyti, kurios grupės
sumos didesnės: lyginių ar nelyginių. Laimi didesnė grupė.

Sukurkite funkciją, kuri paimtų sveikųjų skaičių sąrašą,
 atskirai suskaičiuotų lyginių ir nelyginių skaičių sumas,
 tada grąžintų lyginių ir nelyginių skaičių sumų skirtumą skaičių.

Pavyzdys:

war_of_numbers([2, 8, 7, 5]) ➞ 2
# 2 + 8 = 10
# 7 + 5 = 12
# 12 yra didesnis už 10
# Taigi grąžiname 12 - 10 = 2
war_of_numbers([12, 90, 75]) ➞ 27
war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]) ➞ 168
'''


def skaiciu_karas(a:list):
    sum_even = sum(num for num in skaiciu_sarasas if num % 2 == 0)
    sum_odd = sum(num for num in skaiciu_sarasas if num % 2 != 0)

    difference = abs(sum_even - sum_odd)

    return difference

skaiciu_sarasas = [5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]
result = skaiciu_karas(skaiciu_sarasas)

print(result)


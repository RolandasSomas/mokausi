'''
1. Lentynoje sudeti batai:
[8.90, 4,90, 13,20, 8,80, 14,00, 12,00]
a) Paskaičiuokite kiek eurų liks žmogui, jei jis šiuo metu pirks dvejus pigiausius batus;
b) kokius dvejus batus jam nupirkti, jei jis turi 20 eurų ir nori, kad jam liktų kuo mažiau eurų;
'''
from operator import index
# a uzduoties dalis
pinigai = 20
kainos = [8.90, 4.90, 13.20, 8.80, 14.00, 12.00]
is_eiles= sorted(kainos)
pigiausia_batu_suma = sum(is_eiles[:2])

print('like pinigai: ', round(pinigai - sum(is_eiles[:2]), 2))





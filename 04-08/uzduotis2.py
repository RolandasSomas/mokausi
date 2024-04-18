"""
Parašyti funkciją, į kurią padavus skaičių atspausdintų
tokia tvarka kaip parodyta žemiau. Funkcija turi
priimti 2 variable – nuo kurio iki kurio skaiciaus.:
"""

# 1
# 22
# 333
# 4444
# 55555
# Pvz jei nuo 3 iki 5, spausdina:
# 333
# 4444
# 55555


# def numbers(nuo:int, iki:int):
#     for i in range(nuo, iki):
#        for s in range(i):
#            print(i)
#
#
# numbers(nuo,iki)
nuo = 2
iki = 6


def numbers(nuo: int, iki: int):
    for i in range(nuo, iki + 1):
        print(str(i) * int(i))


numbers(nuo, iki)

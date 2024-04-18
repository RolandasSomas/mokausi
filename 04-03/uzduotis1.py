"""
Parašykite funkciją, kuri paima du list'us ir prie pirmojo list pirmojo elemento prideda antrojo
listpirmąjį elementą, antrojo sąrašo antrąjį elementą, antrojo sąrašo antrąjį elementą ir antrojo sąrašo
 antrąjį elementą. pirmąjį sąrašą su antruoju antrojo sąrašo elementu ir t. t., ir t. t. Grąžinkite True,
 jei visi elementų deriniai sudaro tą patį skaičių. Priešingu atveju grąžinama False. Pavyzdys:

# """

# puzzle_pieces= ([1, 2, 3, 4], [4, 3, 2, 1])
# # 1 + 4 = 5; 2 + 3 = 5; 3 + 2 = 5; 4 + 1 = 5
# # Abiejų sąrašų suma yra [5, 5, 5, 5, 5]
# puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]) ➞ True
# puzzle_pieces([1, 2], [-1, -1]) ➞ False
# puzzle_pieces([9, 8, 7], [7, 8, 9, 10]) ➞ False
listas1 = [1, 2, 3, 4]
listas2 = [4, 3, 2, 1]


def numbers_same(a: list, b: list) -> bool:
    if len(a) != len(b):
        return False
    else:
        for i in range(len(a) - 1):
            if listas1[i] + listas2[i] != listas1[i + 1] + listas2[i + 1]:
                return False
        return True
    return False


print(type(listas1))
print(len(listas1))

print(numbers_same(listas1, listas2))

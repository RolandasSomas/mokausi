"""
1. Yra sugeneruojami random pagalba 4 skaiciai (nuo 0000 iki 9999).
2. Tada paprasoma konsoleje suvesti kiek bandymų spėti turime. (Tarkim vartotojas suves 3 kartus)
3. Vartotojo prasoma meginsti atspeti skaiciu (pvz vartotojas speja 0123).
4. Sistema skaiciuoja kiek skaiciu yra karvių, ir kiek yra bulių. Karve yra toks skaicius,
kuris yra teisingas, bet stovi ne savo vietoje, bulius – ir teisingas, ir teisingoje vietoje.
Jei visi buliai – zaidimo pabaiga.
5. Jei skaicius neatspetas per nustatyta bandymu skaiciu – zaidimas pralostas.
"""

from random import randint

#
# # def random_skaiciai():
# a1 = str(randint(0, 9999))
# a2 = str(randint(0, 9999))
# a3 = str(randint(0, 9999))
# a4 = str(randint(0, 9999))
# # return a1, a2, a3, a4
#
#
# skaicius1 = a1.zfill(4)
# skaicius2 = a2.zfill(4)
# skaicius3 = a3.zfill(4)
# skaicius4 = a4.zfill(4)
#
# print(skaicius1)
# print(skaicius2)
# print(skaicius3)
# print(skaicius4)
# def pataikei():
#     print('Sveikiname pataikei')
#
# bandymai = int(input('Iveskite bandymu skaiciu: '))
# spejamas_skaicius = int(input('Iveskite 4 skaitmenu skaiciu: '))
# def spejimas():
#     for i in range(bandymai):
#         if spejamas_skaicius == skaicius1:
#            pataikei()
#         elif spejamas_skaicius == skaicius2:
#          pataikei()
#         elif spejamas_skaicius == skaicius3:
#             pataikei()
#         elif spejamas_skaicius == skaicius4:
#             pataikei()
#         else:
#             print('Nepataikete!')
#
# spejimas()


def generate_numbers():
    return "".join([str(randint(0, 9)) for _ in range(4)])


def check_cows_bulls(generated_number, player_prediction):
    cows, bulls = 0, 0
    for index, value in enumerate(player_prediction):
        if value == generated_number[index]:
            bulls += 1
        elif value in generated_number:
            cows += 1
    return cows, bulls
    pass


def main():
    generate_number = generate_numbers()
    try_number = int(input("Kiek kartu spesi: "))

    for i in range(try_number):
        players_prediction = input("pamegink atspeti")
        print(players_prediction)
        cows, bulls = check_cows_bulls(generate_number, players_prediction)
        if bulls == 4:
            return " You are the winner"
        else:
            print(f"you have {bulls} bulls and {cows} cows")
    print(generated_number, try_number)
    return "Game over"


# generated_number = '1234'
# player_prediction = '1432'
# check_cows_bulls(generated_number, player_prediction)
print(main())

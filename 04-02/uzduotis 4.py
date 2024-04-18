"""
Sukurkite funkciją, kuri grąžintų tik unikalius simbolius turinčias string reikšmes
"""

#
# def unikalus(sakinys: str) -> list:
#     words = sakinys.split()
#     geras_zodis= []
#     for word in words:
#         for letter in word:
#             if word.count(letter) > 1:
#                 break
#         else:
#             geras_zodis.append(word)
#         return geras_zodis
#
# sakinys= 'dsa dasd asdsa ewqgs gfdhte '
# a = unikalus(sakinys)
# print(a)


def return_unique(row):
    return " ".join(set(symbols))


def return_words_unique_symbols(text):
    words = text.split()
    result_words_with_unique_symbols = []
    for word in words:
        if len(word) == len(set(word)):
            result_words_with_unique_symbols.append(word)
    print(words)
    return result_words_with_unique_symbols


symbols = (
    "dasdaslkjdsalkdjsalkjdhsa;jdh sa;jdhj;lskajd;lksajd;klsajd;kj ;kljkl fhj lajfha"
)
print(return_unique(symbols))

text = (
    "Šis pavyzdys rodo, kad the_func() priima tris argumentus, x, y ir z, kad x gali būti int arba float, y turi "
    "būti tuple, kuriame saugomi string, o z gali būti none arba float. Grąžinimo tipas yra str, "
    "kurį nurodote naudodami -> po baigiamųjų skliaustų, bet prieš dvitaškį"
)

print(return_words_unique_symbols(text=text))

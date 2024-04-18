"""
Jums duotas bigramų masyvas ir žodžių masyvas. Parašykite funkciją,
 kuri grąžintų True, jei iš šio masyvo galima rasti kiekvieną
bigramą bent vieną kartą žodžių masyve.

Pavyzdys:

can_find([["at", "be", "th", "au"], ["beautiful", "the", "hat"]) ➞ True
can_find([["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]) ➞ False
# "cu" nėra nė viename iš žodžių.
can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]) ➞ True
can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks", "cooks"]) ➞ False
"""


def can_find(bigrams: list, words: list):
    for bigram in bigrams:
        for word in words:
            if bigram in word:
                break
        else:
            return False
    return True


print(can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks", "cooks"]))

#
# kitas sprendimo budas
# # def can_find(bigrams: list, words: list):
# #     words_sentence = " ".join(words)
# #     for bigram in bigrams:
# #         if bigram not in words_sentence:
# #             return print(False)
#     return print(True)

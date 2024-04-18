# text = '''
# Sukurkite funkciją, kuri priima eilučių sąrašą ir grąžina naują sąrašą,
# kuriame yra tik tos eilutės, kurios prasideda balsiu. Naudokite lambda
# funkcijas, kad įgyvendintumėte logiką, tikrinančią, ar eilutė prasideda balsiu.
# '''
text = ["namas", "aruodas", "ezeras"]


def check_row_starts(text: list):

    is_vowel = lambda word: word[0] in "aeiouAEIOU"
    return [t for t in text if is_vowel(t)]


print(check_row_starts((text)))

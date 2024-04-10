'''
Exercise 1:	Write a Python program to find the most common elements and their counts in a specified text.
Original string: lkseropewdssafsdfafkpwe
Most common three characters of the said string:
[('s', 4), ('e', 3), ('f', 3)]
'''
# from collections import Counter
# text = 'lkseropewdssafsdfafkpwe'
#
# def rasti_dazniausias_raides():
#     skaiciuoti_raides = Counter(text)
#     dazniausia = skaiciuoti_raides.most_common()
#     return dazniausia
#
#
# print(rasti_dazniausias_raides()[0:3])

def return_most_common(text, number=3):
    result = []
    for l in set(text):
        result.append((l, text.count(l)))
    result.sort(key=lambda x: x[1])
    result.sort(key=lambda x: x[1], reverse=True)
    return result[:3]
string = 'lkseropewdssafsdfafkpwe'

print(return_most_common(string))

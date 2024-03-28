'''
Parašykite programą, kuri patikrintų,
ar duotas skaičius yra kvadratas.
'''

import math
import random



skaicius = random.randint(1 ,100)
print(skaicius)
a = math.sqrt(skaicius)
print(a)

if type(a) == int():
    print('kvadrato skaicius traukiasi:',skaicius)
else:
    print('nesitraukia')

print(type(a))

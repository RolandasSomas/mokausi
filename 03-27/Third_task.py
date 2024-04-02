'''
Sugeneruokite dict iš 10 skaitmenų (keys): 1,2,3...10.
Kiekvienam key turėtų būti priskirta atsitiktinio sveikojo skaičiaus vertė nuo 1 iki 100
'''
import random

import math


# atsitiktiniai = {}
#
# for i in range(10):
#     atsitiktiniai.update((i), (randint[1:100]))
#     atsitiktiniai.values()
#
# print(atsitiktiniai)

result= {}
for i in range(1, 11):
    result[i] = random.randint(1 ,100)

print(result)


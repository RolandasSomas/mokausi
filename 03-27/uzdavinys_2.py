
skaiciai= [1, 2, 3, 4, 5, 6, 18, 90, 118, 991, 196151]

lyginiu_skaiciu_suma = 0
nelyginiu_skaiciu_suma = 0

import math

for x in range(len(skaiciai)):
    if x % 2 == 0:
        lyginiu_skaiciu_suma += 1
    else:
        nelyginiu_skaiciu_suma +=1

print(lyginiu_skaiciu_suma)
print(nelyginiu_skaiciu_suma)



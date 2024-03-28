'''
Sukurkite PIN kodo nulaužimo programą. Tarkime, PIN kodą sudaro 4 atsitiktiniai skaitmenys.
 Reikšmę galite saugoti kintamajame. Tada sukurkite ciklą, einantį per visas galimas kombinacijas,
 kol rasite tą, kurią įvedėte
'''

import random
import time
# print('' .join([str(randint.random(0,10)) for _ in range(4)]))

pin = str(random.randint(1, 9999)).zfill(4)
checking = int()
print('gautas kodas:', pin)
time.sleep(3)

while True:
    checking = str(random.randint(1, 9999)).zfill(4)
    if checking == pin:
        print('radau teisinga koda!', checking)
        break
    else:
        print(checking)



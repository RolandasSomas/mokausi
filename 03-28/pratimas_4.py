"""
Naudodami tą patį string, kaip ir ankstesniame pratime:
apskaičiuokite zodziu, kurios turi daugiau nei 5 simbolius, skaičių
"""

tekstas = (
    "Pamėginkite suprasti kas čia vyksta. Patarimas: judėti nuo "
    "smulkiausiu detalių kaip pvz suprasti ką daro enumerate,"
    " sujungti detalę po detalės kol bus viskas aišku"
)

lauzytas_tekstas = tekstas.split()
suma = 0
for i in lauzytas_tekstas:
    if len(i) > 5:
        suma += 1
        print("zodis turi daugiau nei 5 simbolius: ", i)
print("suma", suma)

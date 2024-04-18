"""
Apie šalį galima sakyti, kad ji yra didelė, jei ji yra:
Didelė gyventojų skaičiumi.
Didelė pagal plotą.
Šalies klasę papildykite taip, kad joje būtų atributas is_big. Nustatykite jį į True, jei tenkinamas kuris nors iš šių kriterijų:
Gyventojų skaičius yra didesnis nei 20 mln.
Plotas didesnis nei 3 mln. km².
Taip pat sukurkite metodą, kuris palygintų šalies gyventojų tankį su kitos šalies objektu. Grąžinkite tokio formato eilutę:
{country} has a {smaller / larger} population density than {other_country}
Pavyzdys:
australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)
australia.is_big ➞ True
andorra.is_big ➞ False
andorra.compare_pd(australia) ➞ "Andorra has a larger population density than Australia"
"""


class Country:
    def __init__(self, name: str, population: int, area: int):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = population > 20000000 or area > 3000000


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)
print(australia.is_big)
print(andorra.is_big)

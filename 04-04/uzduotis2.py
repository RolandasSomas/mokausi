try:
    reiksme = int(input("Pirma: "))
    reiksme_2 = int(input("Antra: "))
    reiksme
    print(reiksme_2 / reiksme)
except ValueError:
    print("Gavome Value error")
try:
    print(reiksme_2 / reiksme)
except TypeError:
    print("Gavome type Error")

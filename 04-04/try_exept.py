data = {1: "vienas", 2: "du", 3: "trys"}


def enter_numbers():
    while True:
        try:
            value = int(input("ivesk skaiciu:"))
        except ValueError:
            raise ValueError("suvestas ne skaicius")
        if value > 10:
            print("daugiau nei 10")
        else:
            print("maziau nei 10")
        if value == 15:
            break


enter_numbers()
ERRORS = (ValueError, KeyError)


def ivedu_numerius():
    while True:
        try:
            value = int(input("iveskite skaiciu:"))
            print(data[value])
        except (KeyError, ValueError):
            raise ValueError("suvestas ne skaicius")


ivedu_numerius()

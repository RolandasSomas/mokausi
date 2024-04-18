"""
Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)

* * * * *

* * * *

* * *

* *

*
"""

# def printing_stars(kiek:int):
#     is_galo = kiek+1
#     for i in range(kiek+1):
#         is_galo-= 1
#         print(str('*') * int(is_galo))
#
# printing_stars(8)


def printing_stars(kiek: int):
    for i in range(kiek, 0, -1):
        print("*" * i)


printing_stars(8)

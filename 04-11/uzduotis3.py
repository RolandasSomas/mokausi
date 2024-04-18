'''
Sukurkite knygos klasę Book, kuri turi du atributus:
name
author
ir du metodus:
Metodas, pavadintas .get_title(), kuris grąžina: "Pavadinimas: " + egzemplioriaus pavadinimas.
Metodas .get_autor(), kuris grąžina: "Autorius: " + egzempliorius autorius.
'''

class Book:

    def __init__(self):
        self.name = 'Hamletas'
        self.author = 'Viljamas Šekspyras'

    def get_title(self):
        print(f'Pavadinimas: {self.name}')

    def get_author(self):
        print(f'Autorius: {self.author}' )

a = Book()
a.get_title(self.name='tutt')
a.get_author()




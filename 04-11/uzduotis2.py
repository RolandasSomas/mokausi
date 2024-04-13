'''
Darbuotojo klasėje sukurkite egzempliorių atributus fullname (vardas, pavardė) ir email (el. paštas).
 Turint asmens vardą ir pavardę:
Vardą ir pavardę suformuokite paprasčiausiai sujungdami vardą ir pavardę,
atskiriamus tarpeliu.
Elektroninį paštą suformuokite sujungdami vardą ir pavardę, tarp jų įterpdami simbolį .
Pabaigoje įrašydami @company.com. Įsitikinkite, kad visas el. laiškas būtų** rašomas mažosiomis raidėmis**.
'''

class Details:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.full_name = f'{name} {surname}'
        self.email= f'{name}.{surname}@company.com'.lower()

  

a = Details('Rolandas','Somas')

print(a.full_name, a.email)
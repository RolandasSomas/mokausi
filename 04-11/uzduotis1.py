'''
Sukurkite Calculator klasę su pagrindinėmis funkcijomis:
sudėti, dalyti, dauginti, atimti ir t. t.. Inicijuokite klasę ir
parodykite keletą skaičiavimų.
'''

class Calculator:
    def __init__(self,x=10, y = 15):
        self.x = 10
        self.y = 15
    def divide(self):
        print(self.x/self.y)
    def multiply(self):
        print(self.x * self.y)
    def add_numbers(self):
        print(self.x + self.y)
    def minus_numbers(self):
        print(self.x - self.y)

action = Calculator()

action.divide()
action.multiply()
action.add_numbers()
action.minus_numbers()

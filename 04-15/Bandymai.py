class Animal:

    def __init__(self, age: int = 10, colour: str = "Yellow"):
        self.age = age
        self.colour = colour

    def eat(self):
        print("Animal Eats")

    def make_sounds(self):
        print("Garsiai rekia")


class Bird(Animal):
    def __init__(self, age, colour, type: str = "Water bird"):
        super().__init__()
        self.colour = "Brown"
        self.type = type

    def fly(self):
        print("Bird flies")

    def make_sounds(self):
        print("Garsiai gieda")


bird = Bird(10, "yellow")
print(bird.colour)
bird.make_sounds()


class Zinduolis(Animal):
    pass


class Mammoth(Zinduolis):
    def __init__(self):
        pass

    def walk(self):
        self.__new_method()
        print("Walk very fast!!")

    def __new_method(self):
        print("new method")


class Hybrid_Animal(Zinduolis, Animal):
    pass


hybrid = Hybrid_Animal(10, "black")
mamutas = Mammoth()
mamutas.walk()

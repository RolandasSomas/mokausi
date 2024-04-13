

class Color:
   def __init__(self):
        self.keiciam = 'Green'

class animal:
    def __init__(self, age = 10, name = 'Pearch', *args, **kwargs):
        self.full_name = 'Persikute'
        self.age = 10
        self.age_after_ten_years = self.age +10
        self.color= Color()

    def run (self, speed: str = 'greitai'):
      value = f'{speed} bega {self.full_name}, color {self.color.keiciam}'
      print(value)

    def lipti_i_medi(self):
        print(f'{self.full_name} karstosi i medi')

    def begti_lipti_i_medi(self, speed: str = 'Greitai'):
        self.run(speed=speed)
        self.lipti_i_medi()


Animal = animal()
# print(Animal.run())
# Animal.lipti_i_medi()
Animal.begti_lipti_i_medi(speed = 'Atsiputusi')

Animal_2 = animal()

animal_2_color = 'red'
print(id(Animal), id(Animal_2))


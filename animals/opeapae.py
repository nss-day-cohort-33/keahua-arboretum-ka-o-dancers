from animals import Animal
from interfaces import IFlying
from interfaces import Identifiable

class Opeapea(Animal, IFlying, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Ope'ape'a")
        IFlying.__init__(self)
        Identifiable.__init__(self)
        self.prey = [ "Fruit", "Flowers", "Grasshopper", "Fruit Fly" ]
        self.min_release_age = 5


    def list_prey(self):
        for index, prey in enumerate(self.prey):
            print(f'{index + 1}. {prey} ')

    def feed(self, prey):
        if prey in self.prey:
            print(f'The opeapea ate {prey} for a meal')
        else:
            print(f'The opeapea rejects the {prey}')


    def __str__(self):
        return f'Opeapea {self.id}. I vant to drink your blood!'

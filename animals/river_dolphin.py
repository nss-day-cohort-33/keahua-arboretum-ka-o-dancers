from animals import Animal
from interfaces import IFreshwater
from interfaces import ISwimming
from interfaces import Identifiable

class RiverDolphin(Animal, IFreshwater, Identifiable):

    def __init__(self):
        Animal.__init__(self, "River dolphin")
        IFreshwater.__init__(self)
        ISwimming.__init__(self)
        Identifiable.__init__(self)
        self.prey = [ "Trout", "Mackarel", "Salmon", "Sardine" ]
        self.min_release_age = 13


    def list_prey(self):
        for index, prey in enumerate(self.prey):
            print(f'{index + 1}. {prey} ')

    def feed(self, prey):
        if prey in self.prey:
            print(f'The dolphin ate {prey} for a meal')
        else:
            print(f'The dolphin rejects the {prey}')


    def __str__(self):
        return f'Dolphin {self.id}. Eeee EeeEEeeeeEE!'

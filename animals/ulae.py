from animals import Animal
from interfaces.animal import ISaltwater
from interfaces import ISwimming
from interfaces import Identifiable

class Ulae(Animal, ISaltwater, ISwimming, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Ulae")
        ISaltwater.__init__(self)
        ISwimming.__init__(self)
        Identifiable.__init__(self)
        self.prey = [ "Shrimp", "Crabs", "Squid", "Octopus" ]
        self.min_release_age = 1


    def list_prey(self):
        for index, prey in enumerate(self.prey):
            print(f'{index + 1}. {prey} ')


    def feed(self, prey):
        if prey in self.prey:
            print(f'The ulae ate {prey} for a meal')
        else:
            print(f'The ulae rejects the {prey}')


    def __str__(self):
        return f'Ulae {self.id}. Eeee EeeEEeeeeEE!'

from animals import Animal
from interfaces import IFreshwater
from interfaces import IStagnant
from interfaces import ISwimming
from interfaces import Identifiable

class Kikakapu(Animal, IFreshwater, IStagnant, ISwimming, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Kikakapu")
        IFreshwater.__init__(self)
        IStagnant.__init__(self)
        ISwimming.__init__(self)
        Identifiable.__init__(self)
        self.prey = [ "Coral", "Algae", "Shrimp", "Mollusk" ]
        self.min_release_age = 1


    def list_prey(self):
        for index, prey in enumerate(self.prey):
            print(f'{index + 1}. {prey} ')


    def feed(self, prey):
        if prey in self.prey:
            print(f'The Kikakapu ate {prey} for a meal')
        else:
            print(f'The Kikakapu rejects the {prey}')


    def __str__(self):
        return f'Kikakapu {self.id}. Have you seen my friend dory?'

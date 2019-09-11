from animals import Animal
from interfaces import IFlying
from interfaces import Identifiable

class Pueo(Animal, IFlying, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Pueo")
        IFlying.__init__(self)
        Identifiable.__init__(self)
        self.prey = [ "Mice", "Rats", "Hamster", "Crickets" ]
        self.min_release_age = 8


    def list_prey(self):
        for index, prey in enumerate(self.prey):
            print(f'{index + 1}. {prey} ')

    def feed(self, prey):
        if prey in self.prey:
            print(f'The pueo ate {prey} for a meal')
        else:
            print(f'The pueo rejects the {prey}')


    def __str__(self):
        return f'Pueo {self.id}. How many licks does it take to get to the center of a tootsie pop!'

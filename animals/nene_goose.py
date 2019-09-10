from animals import Animal
from interfaces import IFlying
from interfaces import Identifiable

class NeneGoose(Animal, IFlying, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        IFlying.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Grass", "Flowers", "Fruit", "Seeds" }
        self.min_release_age = 7


    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The goose ate {prey} for a meal')
        else:
            print(f'The goose rejects the {prey}')


    def __str__(self):
        return f'Goose {self.id}. Honk Honk!'

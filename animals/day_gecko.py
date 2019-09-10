from animals import Animal
from interfaces import IWalking
from interfaces import ITerrestrial
from interfaces import Identifiable

class DayGecko(Animal, IWalking, ITerrestrial, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Gold Dust Day Gecko")
        IWalking.__init__(self)
        Identifiable.__init__(self)
        ITerrestrial.__init__(self)
        self.__prey = { "Crickets", "Roaches", "Mealworms", "Waxworms" }
        self.min_release_age = 2


    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The gecko ate {prey} for a meal')
        else:
            print(f'The gecko rejects the {prey}')


    def __str__(self):
        return f'Gecko {self.id}. You can save 15% on car insurance!'

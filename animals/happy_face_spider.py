from animals import Animal
from interfaces import IStagnant
from interfaces import Identifiable

class HappyFaceSpider(Animal, IStagnant, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Happy Face Spider")
        IStagnant.__init__(self)
        Identifiable.__init__(self)
        self.prey = [ "Fruit Flies", "Grasshopper"]
        self.min_release_age = 0.5

    def list_prey(self):
        for index, prey in enumerate(self.prey):
            print(f'{index + 1}. {prey} ')

    def feed(self, prey):
        if prey in self.prey:
            print(f'The spider ate {prey} for a meal')
        else:
            print(f'The spider rejects the {prey}')


    def __str__(self):
        return f'Spider {self.id}. Wilbur didnt know what to do or which way to run!'

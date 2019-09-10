from interfaces import IAquatic
from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants


class River(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)
      self.plant_max = 12
      self.animal_max = 8

    def add_animal(self, animal):
            if len(self.animals) < self.animal_max:
                self.animals.append(animal)
            elif len(self.animals) >= self.animal_max:
                print("Too many animals, FOOL")
                input("press any key to continue")


    def add_plant(self, plant):
        try:
            if plant.freshwater and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants that require brackish water or stagnant water to a river biome")

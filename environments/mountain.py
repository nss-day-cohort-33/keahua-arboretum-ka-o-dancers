from interfaces import IAquatic
from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants


class Mountain(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)
      self.plant_max = 4
      self.animal_max = 6

    def add_animal(self, animal):
            if len(self.animals) < self.animal_max:
                self.animals.append(animal)
            elif len(self.animals) >= self.animal_max:
                print("Too many animals, FOOL")
                input("press any key to continue")


    def add_plant(self, plant):
            if len(self.plants) < self.plant_max:
                self.plants.append(plant)
            elif len(self.plants) >= self.plant_max:
                print("Too many plants, FOOL")
                input("press any key to continue")

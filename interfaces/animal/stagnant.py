from interfaces.habitat.aquatic import IAquatic

class IStagnant(IAquatic):

   def __init__(self):
        super().__init__()
        self.water_type = "stagnant"

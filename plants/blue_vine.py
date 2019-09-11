from plants.plant import Plant
from interfaces import Identifiable

class BlueVine(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Blue Jade Vine")
        Identifiable.__init__(self)



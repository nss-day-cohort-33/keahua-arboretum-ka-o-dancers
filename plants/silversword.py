from plants.plant import Plant
from interfaces import Identifiable

class Silversword(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Silversword")
        Identifiable.__init__(self)


from plants.plant import Plant
from interfaces import Identifiable

class RainbowTree(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree")
        Identifiable.__init__(self)


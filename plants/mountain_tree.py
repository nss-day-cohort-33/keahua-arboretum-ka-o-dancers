from plants.plant import Plant
from interfaces import Identifiable

class MountainTree(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Mountain Apple Tree")
        Identifiable.__init__(self)


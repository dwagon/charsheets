from charsheets.armour.base_armour import BaseArmour
from charsheets.constants import Armour


#############################################################################
class Leather(BaseArmour):
    tag = Armour.LEATHER

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stealth_disadvantage = False
        self.ac = 11
        self.dex_mod = True
        self.dex_max = 9


# EOF

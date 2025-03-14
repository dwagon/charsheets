from charsheets.armour.base_armour import BaseArmour
from charsheets.constants import Armour, ArmourCategory


#############################################################################
class Studded(BaseArmour):
    tag = Armour.STUDDED
    category = ArmourCategory.LIGHT

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stealth_disadvantage = False
        self.ac = 12
        self.dex_mod = True
        self.dex_max = 9


# EOF

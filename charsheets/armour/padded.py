from charsheets.armour.base_armour import BaseArmour
from charsheets.constants import Armour, ArmourCategory


#############################################################################
class Padded(BaseArmour):
    tag = Armour.PADDED
    category = ArmourCategory.LIGHT

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stealth_disadvantage = True
        self.ac = 11
        self.dex_mod = True
        self.dex_max = 9


# EOF

from charsheets.armour.base_armour import BaseArmour
from charsheets.constants import Armour, ArmourCategory


#############################################################################
class Unarmoured(BaseArmour):
    tag = Armour.NONE
    category = ArmourCategory.NONE

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stealth_disadvantage = False
        self.ac = 10
        self.dex_mod = True
        self.dex_max = 9


# EOF

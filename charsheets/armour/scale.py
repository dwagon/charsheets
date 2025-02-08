from charsheets.armour.base_armour import BaseArmour
from charsheets.constants import Armour, ArmourCategory


#############################################################################
class Scale(BaseArmour):
    tag = Armour.SCALE
    category = ArmourCategory.MEDIUM

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stealth_disadvantage = True
        self.ac = 14
        self.dex_mod = True
        self.dex_max = 2


# EOF

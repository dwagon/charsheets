from charsheets.armour.base_armour import BaseArmour
from charsheets.constants import Armour, ArmourCategory


#############################################################################
class HalfPlate(BaseArmour):
    tag = Armour.HALFPLATE
    category = ArmourCategory.MEDIUM

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stealth_disadvantage = True
        self.ac = 15
        self.dex_mod = True
        self.dex_max = 2


# EOF

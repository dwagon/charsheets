from charsheets.armour.base_armour import BaseArmour
from charsheets.constants import Armour, ArmourCategory


#############################################################################
class Hide(BaseArmour):
    tag = Armour.HIDE
    category = ArmourCategory.MEDIUM

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stealth_disadvantage = False
        self.ac = 12
        self.dex_mod = True
        self.dex_max = 2


# EOF

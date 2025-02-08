from charsheets.armour.base_armour import BaseArmour
from charsheets.constants import Armour, ArmourCategory


#############################################################################
class Shield(BaseArmour):
    tag = Armour.SHIELD
    category = ArmourCategory.SHIELD

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stealth_disadvantage = False
        self.ac_mod = 2
        self.dex_mod = False


# EOF

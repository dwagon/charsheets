from charsheets.armour.base_armour import BaseArmour
from charsheets.constants import Armour, ArmourCategory


#############################################################################
class Ring(BaseArmour):
    tag = Armour.RING_MAIL
    category = ArmourCategory.HEAVY

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stealth_disadvantage = True
        self.ac = 14
        self.dex_mod = False
        self.dex_max = 0


# EOF

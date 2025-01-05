from charsheets.armour.base_armour import BaseArmour
from charsheets.constants import Armour


#############################################################################
class ChainMail(BaseArmour):
    tag = Armour.CHAIN_MAIL

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stealth_disadvantage = True
        self.ac = 16
        self.dex_mod = False
        self.dex_max = 0


# EOF

from charsheets.armour.base_armour import BaseArmour
from charsheets.constants import Armour
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class HalfPlate(BaseArmour):
    tag = Armour.HALFPLATE

    def __init__(self, wearer: "Character"):
        super().__init__(wearer=wearer)
        self.stealth_disadvantage = True
        self.ac = 15
        self.dex_mod = True
        self.dex_max = 2


# EOF

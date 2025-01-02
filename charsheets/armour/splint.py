from charsheets.armour.base_armour import BaseArmour
from charsheets.constants import Armour
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Splint(BaseArmour):
    tag = Armour.SPLINT

    def __init__(self, wearer: "Character"):
        super().__init__(wearer=wearer)
        self.stealth_disadvantage = True
        self.ac = 17
        self.dex_mod = False
        self.dex_max = 0


# EOF

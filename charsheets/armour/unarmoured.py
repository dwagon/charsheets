from charsheets.armour.base_armour import BaseArmour
from charsheets.constants import Armour
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Unarmoured(BaseArmour):
    tag = Armour.NONE

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stealth_disadvantage = False
        self.ac = 10
        self.dex_mod = True
        self.dex_max = 9


# EOF

from typing import TYPE_CHECKING
from charsheets.constants import Armour
from charsheets.reason import Reason
from charsheets.util import safe

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class BaseArmour:
    tag: Armour

    def __init__(self, wearer: "Character"):
        self.wearer: "Character" = wearer
        self.ac: int = 0
        self.stealth_disadvantage: bool = False
        self.dex_mod: bool = False
        self.dex_max = 2
        self.ac_mod = 0

    ########################################################################
    def __str__(self):
        return safe(self.tag.title())

    ########################################################################
    def armour_class(self) -> Reason[int]:
        arm = Reason(self.tag, max(self.ac, self.ac_mod))
        if self.dex_mod:
            arm.add("dex_modifier", min(self.dex_max, self.wearer.dexterity.modifier))

        return arm


# EOF

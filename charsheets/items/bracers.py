"""Wrist Wear"""

from typing import TYPE_CHECKING

from charsheets.items.base_item import BaseItem
from charsheets.reason import Reason
from charsheets.weapons.base_weapon import BaseWeapon

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter


#############################################################################
class BracersOfArchery(BaseItem):
    """https://www.dndbeyond.com/magic-items/4593-bracers-of-archery"""

    name = "Bracers of Archery"

    def mod_ranged_atk_bonus(self, weapon: BaseWeapon, character: "BaseCharacter") -> Reason[int]:
        return Reason("Bracers of Archery", 2)


# EOF

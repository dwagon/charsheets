"""Magic Belts"""

from typing import TYPE_CHECKING

from charsheets.items.base_item import BaseItem
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter


#############################################################################
class BeltOfGiantStrength(BaseItem):
    """https://www.dndbeyond.com/sources/dnd/basic-rules-2014/magic-items#BeltofGiantStrength"""

    pass


#############################################################################
class BeltOfHillGiantStrength(BeltOfGiantStrength):
    name = "Belt of Hill Giant Strength"

    def mod_stat_str_set(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Belt of Hill Giant Strength", 21)


#############################################################################
class BeltOfStoneGiantStrength(BeltOfGiantStrength):
    name = "Belt of Stone Giant Strength"

    def mod_stat_str_set(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Belt of Stone Giant Strength", 23)


#############################################################################
class BeltOfFireGiantStrength(BeltOfGiantStrength):
    name = "Belt of Fire Giant Strength"

    def mod_stat_str_set(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Belt of Fire Giant Strength", 25)


#############################################################################
class BeltOfCloudGiantStrength(BeltOfGiantStrength):
    name = "Belt of Cloud Giant Strength"

    def mod_stat_str_set(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Belt of Cloud Giant Strength", 27)


#############################################################################
class BeltOfStormGiantStrength(BeltOfGiantStrength):
    name = "Belt of Storm Giant Strength"

    def mod_stat_str_set(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Belt of Storm Giant Strength", 29)


# EOF

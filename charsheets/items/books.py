"""Magic Books"""

from typing import TYPE_CHECKING

from charsheets.items.base_item import BaseItem
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter


#############################################################################
class ManualOfBodilyHealth(BaseItem):
    name = "Manual of Bodily Health"
    hide = True

    def mod_stat_con(self, character: "BaseCharacter") -> Reason[int]:
        return Reason(self.name, 2)


#############################################################################
class ManualOfGainfulExercise(BaseItem):
    name = "Manual of Gainful Exercise"
    hide = True

    def mod_stat_str(self, character: "BaseCharacter") -> Reason[int]:
        return Reason(self.name, 2)


#############################################################################
class ManualOfQuicknessOfAction(BaseItem):
    name = "Manual of Quickness of Action"
    hide = True

    def mod_stat_dex(self, character: "BaseCharacter") -> Reason[int]:
        return Reason(self.name, 2)


#############################################################################
class TomeOfClearThough(BaseItem):
    name = "Tome of Clear Thought"
    hide = True

    def mod_stat_int(self, character: "BaseCharacter") -> Reason[int]:
        return Reason(self.name, 2)


#############################################################################
class TomeOfLeadershipAndInfluence(BaseItem):
    name = "Tome of Leadership and Influence"
    hide = True

    def mod_stat_cha(self, character: "BaseCharacter") -> Reason[int]:
        return Reason(self.name, 2)


#############################################################################
class TomeOfUnderstanding(BaseItem):
    name = "Tome of Understanding"
    hide = True

    def mod_stat_wis(self, character: "BaseCharacter") -> Reason[int]:
        return Reason(self.name, 2)


# EOF

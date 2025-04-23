from typing import TYPE_CHECKING

from aenum import extend_enum

from charsheets.constants import Feature
from charsheets.features import Darkvision60
from charsheets.features.base_feature import BaseFeature
from charsheets.race2014.base_race import BaseRace
from charsheets.reason import Reason

if TYPE_CHECKING:
    from charsheets.character import Character

extend_enum(Feature, "DWARVEN_RESILIENCE14", "Dwarven Resilience")
extend_enum(Feature, "DWARVEN_TOUGHNESS14", "Dwarven Toughness")


#############################################################################
class Dwarf(BaseRace):
    #########################################################################
    def __init__(self):
        super().__init__()
        self.speed = 25

    #########################################################################
    def race_feature(self) -> set[BaseFeature]:
        return {Darkvision60()}

    #########################################################################
    def mod_stat_con(self, character: "Character") -> Reason[int]:
        return Reason("Dwarf", 2)


#############################################################################
class HillDwarf(Dwarf):
    #########################################################################
    def mod_stat_wis(self, character: "Character") -> Reason[int]:
        return Reason("Hill Dwarf", 1)


#############################################################################
class MountainDwarf(Dwarf):
    #########################################################################
    def mod_stat_str(self, character: "Character") -> Reason[int]:
        return Reason("Mountain Dwarf", 1)


# EOF

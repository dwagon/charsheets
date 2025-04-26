from typing import TYPE_CHECKING

from charsheets.constants import Language
from charsheets.features.base_feature import BaseFeature
from charsheets.race2014.base_race import BaseRace
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter


#############################################################################
class Human(BaseRace):
    #########################################################################
    def __init__(self, language: Language):
        super().__init__()
        self.speed = 30
        self._language = language

    #########################################################################
    def race_feature(self) -> set[BaseFeature]:
        return set()

    #########################################################################
    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        return Reason("Human", self._language)

    #########################################################################
    def mod_stat_str(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Human", 1)

    #########################################################################
    def mod_stat_dex(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Human", 1)

    #########################################################################
    def mod_stat_con(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Human", 1)

    #########################################################################
    def mod_stat_int(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Human", 1)

    #########################################################################
    def mod_stat_wis(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Human", 1)

    #########################################################################
    def mod_stat_cha(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Human", 1)


# EOF

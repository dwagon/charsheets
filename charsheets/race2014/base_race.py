from typing import TYPE_CHECKING

from charsheets.constants import Weapon, Proficiency, Language
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character, BaseCharacter


#############################################################################
class BaseRace:
    def __init__(self) -> None:
        self.character: Character | None = None
        self.speed = 30

    #########################################################################
    def race_feature(self) -> set[BaseFeature]:
        raise NotImplementedError

    #########################################################################
    def mod_add_prepared_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason()

    #########################################################################
    def mod_specific_weapon_proficiency(self, character: "BaseCharacter") -> Reason[Weapon]:
        return Reason()

    #########################################################################
    def mod_hp_bonus(self, character: "BaseCharacter") -> Reason[int]:
        return Reason()

    #########################################################################
    def mod_armour_proficiency(self, character: "BaseCharacter") -> Reason[Proficiency]:
        return Reason()

    #########################################################################
    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        return Reason()

    #########################################################################
    def mod_stat_str(self, character: "BaseCharacter") -> Reason[int]:
        return Reason()

    #########################################################################
    def mod_stat_dex(self, character: "BaseCharacter") -> Reason[int]:
        return Reason()

    #########################################################################
    def mod_stat_con(self, character: "BaseCharacter") -> Reason[int]:
        return Reason()

    #########################################################################
    def mod_stat_int(self, character: "BaseCharacter") -> Reason[int]:
        return Reason()

    #########################################################################
    def mod_stat_wis(self, character: "BaseCharacter") -> Reason[int]:
        return Reason()

    #########################################################################
    def mod_stat_cha(self, character: "BaseCharacter") -> Reason[int]:
        return Reason()

    #########################################################################
    @property
    def name(self) -> str:
        return self.__class__.__name__.title()


# EOF

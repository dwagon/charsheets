from typing import TYPE_CHECKING

from charsheets.constants import Weapon
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
    @property
    def name(self) -> str:
        return self.__class__.__name__.title()


# EOF

from typing import TYPE_CHECKING

from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class BaseSpecies:
    def __init__(self) -> None:
        self.character: Character | None = None

    #########################################################################
    def species_feature(self) -> set[BaseFeature]:
        raise NotImplementedError

    #########################################################################
    @property
    def name(self) -> str:
        return self.__class__.__name__.title()

    #########################################################################
    @property
    def speed(self) -> int:
        return 30

    #############################################################################
    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason()

    #############################################################################
    def mod_add_movement_speed(self, character: "Character") -> Reason[int]:
        return Reason()

    #############################################################################
    def mod_set_movement_speed(self, character: "Character") -> Reason[int]:
        return Reason()


# EOF

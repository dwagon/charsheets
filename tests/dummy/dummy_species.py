from typing import TYPE_CHECKING

from charsheets.features import Darkvision60
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.species.base_species import BaseSpecies

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class DummySpecies(BaseSpecies):

    def species_feature(self) -> set[BaseFeature]:
        return {Darkvision60()}

    @classmethod
    def mod_initiative_bonus(cls, character: "Character") -> Reason:
        return Reason("species_bonus", 1)


# EOF

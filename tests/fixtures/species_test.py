from typing import TYPE_CHECKING
from charsheets.reason import Reason
from charsheets.species import Species
from charsheets.constants import Ability

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class TestSpecies(Species):
    def species_abilities(self) -> set[Ability]:
        return {Ability.DARKVISION60}

    @classmethod
    def initiative_bonus(cls, character: "Character") -> Reason:
        return Reason("species_bonus", 1)


# EOF

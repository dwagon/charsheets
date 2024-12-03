from typing import TYPE_CHECKING
from charsheets.reason import Reason
from charsheets.species import Species
from charsheets.constants import Ability

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class DummySpecies(Species):

    def species_abilities(self) -> set[Ability]:
        return {Ability.DARKVISION60}

    @classmethod
    def mod_initiative_bonus(cls, character: "Character") -> Reason:
        return Reason("species_bonus", 1)


# EOF

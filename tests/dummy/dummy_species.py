from typing import TYPE_CHECKING

from charsheets.abilities import Darkvision60
from charsheets.abilities.base_ability import BaseAbility
from charsheets.reason import Reason
from charsheets.species.base_species import BaseSpecies

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class DummySpecies(BaseSpecies):

    def species_abilities(self) -> set[BaseAbility]:
        return {Darkvision60()}

    @classmethod
    def mod_initiative_bonus(cls, character: "Character") -> Reason:
        return Reason("species_bonus", 1)


# EOF

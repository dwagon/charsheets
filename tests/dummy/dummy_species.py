from typing import TYPE_CHECKING

from charsheets.abilities import Darkvision60
from charsheets.abilities.base_ability import BaseAbility
from charsheets.reason import Reason
from charsheets.species import Species

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class DummySpecies(Species):

    def species_abilities(self) -> set[BaseAbility]:
        return {Darkvision60()}

    @classmethod
    def mod_initiative_bonus(cls, character: "Character") -> Reason:
        return Reason("species_bonus", 1)


# EOF

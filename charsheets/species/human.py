from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Skill, Ability
from charsheets.reason import Reason
from charsheets.species.base_species import BaseSpecies
from charsheets.exception import NotDefined

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Human(BaseSpecies):
    #########################################################################
    def __init__(self, skill: Skill):
        super().__init__()
        self.skillful_skill = skill

    #########################################################################
    def species_abilities(self) -> set[BaseAbility]:
        return {Resourceful(), Skillful(self.skillful_skill)}


#############################################################################
class Resourceful(BaseAbility):
    tag = Ability.RESOURCEFUL
    _desc = """You gain Heroic Inspiration whenever you finish a Long Rest."""


#############################################################################
class Skillful(BaseAbility):
    tag = Ability.SKILLFUL
    _desc = """You gain proficiency in one skill of your choice."""

    #########################################################################
    def __init__(self, skill: Skill):
        super().__init__()
        self.skillful_skill = skill

    #########################################################################
    @property
    def desc(self) -> str:
        return f"You gained proficiency in {self.skillful_skill}"

    #########################################################################
    def mod_add_skill_proficiency(self, character: "Character") -> Reason[Skill]:
        return Reason("Skillful", self.skillful_skill)


# EOF

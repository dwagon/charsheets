from typing import TYPE_CHECKING
from charsheets.species import Species
from charsheets.ability import BaseAbility
from charsheets.constants import Ability, Skill

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Human(Species):
    #########################################################################
    def __init__(self, skill: Skill):
        super().__init__()
        self.skillful_skill = skill

    #########################################################################
    def mod_add_skill_proficiency(self, character: "Character") -> set[Skill]:
        return {self.skillful_skill}

    #########################################################################
    def species_abilities(self) -> set[Ability]:
        return {Ability.RESOURCEFUL, Ability.SKILLFUL}


#############################################################################
class AbilityResourceful(BaseAbility):
    tag = Ability.RESOURCEFUL
    desc = """You gain Heroic Inspiration whenever you finish a Long Rest."""


#############################################################################
class AbilitySkillful(BaseAbility):
    tag = Ability.SKILLFUL
    desc = """You gain proficiency in one skill of your choice."""


# EOF

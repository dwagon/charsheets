""" Skills"""

from typing import TYPE_CHECKING
from charsheets.ability_score import AbilityScore
from charsheets.reason import Reason
from charsheets.constants import Skill

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class CharacterSkill:
    def __init__(self, skill: Skill, character: "Character", proficient: int, origin: str = ""):
        self.skill = skill
        self.stat: AbilityScore = SKILL_STAT_MAP[self.skill]
        self.prof_bonus = character.proficiency_bonus if proficient else 0
        self.proficient: int = proficient
        self.origin = origin
        self.character = character

    #########################################################################
    @property
    def modifier(self) -> Reason:
        bonus = Reason("stat", self.stat.modifier)
        if self.proficient:
            bonus.add("proficiency", self.prof_bonus)
        bonus.extend(self.character.check_modifiers(f"mod_skill_{self.name}"))
        return bonus

    #########################################################################
    def __str__(self):
        return f"{self.modifier}: {self.proficient}"


# EOF

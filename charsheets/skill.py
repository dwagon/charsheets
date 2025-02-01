""" Skills"""

from typing import TYPE_CHECKING

from charsheets.ability_score import AbilityScore
from charsheets.constants import Skill, SKILL_STAT_MAP
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class CharacterSkill:
    def __init__(self, skill: Skill, character: "Character", proficient: int, origin: str = ""):
        self.skill = skill
        self.stat: AbilityScore = SKILL_STAT_MAP[self.skill]
        self.prof_bonus = character.proficiency_bonus if proficient else 0
        self.proficient: int = proficient
        self.expert: bool = False
        self.origin = origin
        self.character = character

    #########################################################################
    @property
    def modifier(self) -> Reason:
        char_stat = self.character.stats[self.stat]
        bonus = Reason("stat", char_stat.modifier)
        if self.proficient:
            bonus.add("proficiency", self.prof_bonus)
        if self.expert:
            bonus.add("expert", self.prof_bonus)
        mod = f"mod_skill_{self.skill.name.lower()}"
        bonus.extend(self.character.check_modifiers(mod))
        return bonus

    #########################################################################
    def __str__(self):
        return f"{self.modifier}: {self.proficient}"


# EOF

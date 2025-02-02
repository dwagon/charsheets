""" Skills"""

from typing import TYPE_CHECKING

from charsheets.ability_score import AbilityScore
from charsheets.constants import Skill, SKILL_STAT_MAP
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class CharacterSkill:
    def __init__(self, skill: Skill, character: "Character", proficient: bool = False, origin: str = ""):
        self.skill = skill
        self.stat: AbilityScore = SKILL_STAT_MAP[self.skill]
        self.proficient: bool = proficient
        self.expert: bool = False
        self.origin = origin
        self.character = character

    #########################################################################
    @property
    def prof(self) -> str:
        """For display"""
        if self.expert:
            return "1"
        elif self.proficient:
            return "0.5"
        else:
            return "0"

    #########################################################################
    @property
    def modifier(self) -> Reason:
        char_stat = self.character.stats[self.stat]
        bonus = Reason("stat", char_stat.modifier)
        if self.expert:
            bonus.add("expert", self.character.proficiency_bonus * 2)
        elif self.proficient:
            bonus.add("proficiency", self.character.proficiency_bonus)
        mod = f"mod_skill_{self.skill.name.lower()}"
        bonus.extend(self.character.check_modifiers(mod))
        return bonus

    #########################################################################
    def __repr__(self):
        if self.expert:
            prof_str = "Expert"
        elif self.proficient:
            prof_str = "Proficient"
        else:
            prof_str = ""

        return f"{self.skill.name.title()} ({self.origin}): {prof_str}"


# EOF

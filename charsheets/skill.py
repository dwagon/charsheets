""" Skills"""

from ability_score import Ability


#############################################################################
class CharacterSkill:
    def __init__(self, stat: Ability, prof_bonus: int, proficient: bool):
        self.stat: Ability = stat
        self.prof_bonus = prof_bonus
        self.proficient: bool = proficient

    #########################################################################
    @property
    def modifier(self) -> int:
        bonus = self.stat.modifier
        if self.proficient:
            bonus += self.prof_bonus
        return bonus

    #########################################################################
    def __str__(self):
        return f"{self.modifier}: {self.proficient}"

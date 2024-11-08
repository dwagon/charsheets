""" Skills"""

from charsheets.ability_score import AbilityScore


#############################################################################
class CharacterSkill:
    def __init__(self, stat: AbilityScore, prof_bonus: int, proficient: int):
        self.stat: AbilityScore = stat
        self.prof_bonus = prof_bonus
        self.proficient: int = int(proficient)

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


# EOF

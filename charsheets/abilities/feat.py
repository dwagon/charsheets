from charsheets.ability import BaseAbility
from charsheets.constants import Ability, Stat


#############################################################################
class AbilityScoreImprovement(BaseAbility):
    tag = Ability.ABILITY_SCORE_IMPROVEMENT
    desc = """Increase a stat twice"""

    def __init__(self, stat1: Stat, stat2: Stat):
        self.stat1 = stat1
        self.stat2 = stat2


# EOF

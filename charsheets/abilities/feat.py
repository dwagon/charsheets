from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability, Stat

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class AbilityScoreImprovement(BaseAbility):
    tag = Ability.ABILITY_SCORE_IMPROVEMENT
    _desc = """Increase a stat twice"""

    def __init__(self, stat1: Stat, stat2: Stat):
        self.stats = [stat1, stat2]

    #############################################################################
    @property
    def desc(self) -> str:
        if self.stats[0] == self.stats[1]:
            return f"Increased {self.stats[0].title()} twice"
        return f"Increased {self.stats[0].title()} and {self.stats[1].title()}"

    #############################################################################
    def mod_stat_str(self, character: "Character") -> int:
        return self.stats.count(Stat.STRENGTH)

    #############################################################################
    def mod_stat_dex(self, character: "Character") -> int:
        return self.stats.count(Stat.DEXTERITY)

    #############################################################################
    def mod_stat_con(self, character: "Character") -> int:
        return self.stats.count(Stat.CONSTITUTION)

    #############################################################################
    def mod_stat_int(self, character: "Character") -> int:
        return self.stats.count(Stat.INTELLIGENCE)

    #############################################################################
    def mod_stat_wis(self, character: "Character") -> int:
        return self.stats.count(Stat.WISDOM)

    #############################################################################
    def mod_stat_cha(self, character: "Character") -> int:
        return self.stats.count(Stat.CHARISMA)


# EOF

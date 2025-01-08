from typing import TYPE_CHECKING
from charsheets.constants import Feat, Stat
from charsheets.feats.base_feat import BaseFeat

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class AbilityScoreImprovement(BaseFeat):
    tag = Feat.ABILITY_SCORE_IMPROVEMENT
    _desc = """Increase a stat twice"""

    def __init__(self, stat1: Stat, stat2: Stat, character: "Character"):
        super().__init__(character)
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


#############################################################################
class Actor(BaseFeat):
    tag = Feat.ACTOR

    #############################################################################
    @property
    def desc(self) -> str:
        bonus = self.character.charisma.modifier + 8 + self.character.proficiency_bonus
        return f"""You gain the following benefits.

Impersonation. While you're disguised as a real or fictional person,you have Advantage on Charisma (Deception or 
Performance) checks to convince others that you are that person.

Mimicry. You can mimic the sounds of other creatures, including speech. A creature that hears the mimicry must 
succeed on a Wisdom (Insight) check to determine the effect is faked (DC {bonus})."""

    #############################################################################
    def mod_stat_cha(self, character: "Character") -> int:
        return 1


# EOF

from charsheets.constants import Origin, Feat, Skill, Stat
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from charsheets.character import Character


#################################################################################
class BaseOrigin:
    tag = Origin.NONE
    proficiencies: set[Skill] = set()
    origin_feat = Feat.NONE
    tool_proficiency = "None"
    origin_stats: tuple[Stat, Stat, Stat]

    #############################################################################
    def __init__(self, *args: Stat):
        self.stats = tuple(args)

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
    def __repr__(self):
        return f"{self.tag.name.title()}"


# EOF

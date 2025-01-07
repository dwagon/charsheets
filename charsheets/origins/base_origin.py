from charsheets.constants import Origin, Feat, Skill, Stat, Tool
from typing import TYPE_CHECKING

from charsheets.exception import InvalidOption

from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class BaseOrigin:
    tag = Origin.NONE
    proficiencies: set[Skill]
    origin_feat = Feat.NONE
    tool_proficiency: Tool = Tool.NONE
    origin_stats: tuple[Stat, Stat, Stat]

    #############################################################################
    def __init__(self, *args: Stat):
        self.stats = tuple(args)
        self._validation()

    #############################################################################
    def _validation(self):
        for stat in self.stats:
            if stat not in self.origin_stats:
                raise InvalidOption(f"{self.tag} doesn't support {stat}")

    #############################################################################
    def mod_add_tool_proficiency(self, character: "Character") -> Reason[Tool]:
        return Reason[Tool](self.tag.title(), self.tool_proficiency)

    #############################################################################
    def mod_add_skill_proficiency(self, character: "Character") -> Reason[Skill]:
        return Reason(self.tag.title(), *list(self.proficiencies))

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

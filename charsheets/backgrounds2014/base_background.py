from typing import TYPE_CHECKING

from charsheets.constants import Background, Skill, Tool, Language
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class BaseBackground:
    tag = Background.NONE
    proficiencies: set[Skill]
    tool_proficiencies: set[Tool] = set()

    #############################################################################
    def __init__(self):
        pass

    #############################################################################
    def mod_add_tool_proficiency(self, character: "Character") -> Reason[Tool]:
        return Reason[Tool](self.tag.title(), *self.tool_proficiencies)

    #############################################################################
    def mod_add_skill_proficiency(self, character: "Character") -> Reason[Skill]:
        return Reason(self.tag.title(), *list(self.proficiencies))

    #############################################################################
    def mod_add_language(self, character: "Character") -> Reason[Language]:
        return Reason()

    #############################################################################
    def __repr__(self):
        return f"{self.tag.name.title()}"


# EOF

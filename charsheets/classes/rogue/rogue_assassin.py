from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.rogue import Rogue
from charsheets.constants import Ability, Tool
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class RogueAssassin(Rogue):
    #############################################################################
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Rogue (Assassin)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {Assassinate(), AssassinsTools()}
        abilities |= super().class_abilities()
        return abilities


#############################################################################
class Assassinate(BaseAbility):
    tag = Ability.ASSASSINATE
    _desc = """You're adept at ambushing a target, granting you the following benefits. 

    Initiative. You have Advantage on Initiative rolls. 

    Surprising Strikes. During the first round of each combat, you have Advantage on 
    attack rolls against any creature that hasn't taken a turn. If your Sneak Attack hits any target during that 
    round, the target takes extra damage of the weapon's type equal to your Rogue level."""


#############################################################################
class AssassinsTools(BaseAbility):
    tag = Ability.ASSASSINS_TOOLS
    _desc = """You gain a Disguise Kit and a Poisoner’s Kit, and you have proficiency with them."""

    def mod_add_tool_proficiency(self, character: "Character") -> Reason[Tool]:
        return Reason("Assassins Tools", Tool.DISGUISE_KIT, Tool.POISONERS_KIT)


# EOF

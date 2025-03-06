from typing import TYPE_CHECKING

from aenum import extend_enum

from charsheets.classes.rogue import Rogue
from charsheets.constants import Feature, Tool
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class RogueAssassin(Rogue):
    #############################################################################
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Assassin"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {Assassinate(), AssassinsTools()}
        abilities |= super().class_features()
        if self.level >= 9:
            abilities |= {InfiltrationExpertise()}
        return abilities


extend_enum(Feature, "ASSASSINATE", "Assassinate")
extend_enum(Feature, "ASSASSINS_TOOLS", "Assassins Tools")
extend_enum(Feature, "INFILTRATION_EXPERTISE", "Infiltration Expertise")


#############################################################################
class Assassinate(BaseFeature):
    tag = Feature.ASSASSINATE
    _desc = """Initiative. You have Advantage on Initiative rolls. 

    Surprising Strikes. During the first round of each combat, you have Advantage on 
    attack rolls against any creature that hasn't taken a turn. If your Sneak Attack hits any target during that 
    round, the target takes {self.owner.level} extra damage of the weapon's type"""


#############################################################################
class AssassinsTools(BaseFeature):
    tag = Feature.ASSASSINS_TOOLS
    _desc = """You gain a Disguise Kit and a Poisoner’s Kit, and you have proficiency with them."""
    hide = True

    def mod_add_tool_proficiency(self, character: "Character") -> Reason[Tool]:
        return Reason("Assassins Tools", Tool.DISGUISE_KIT, Tool.POISONERS_KIT)


#############################################################################
class InfiltrationExpertise(BaseFeature):
    tag = Feature.INFILTRATION_EXPERTISE
    _desc = """Masterful Mimicry. You can unerringly mimic another person's speech, handwriting, or both if you have
            spent at least 1 hour studying them.
            
            Roving Aim. Your speed isn't reduced to 0 by using Steady Aim."""


# EOF

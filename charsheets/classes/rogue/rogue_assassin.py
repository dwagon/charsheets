from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.rogue import Rogue
from charsheets.constants import Feature, Tool, Stat
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "ASSASSINATE", "Assassinate")
extend_enum(Feature, "ASSASSINS_TOOLS", "Assassins Tools")
extend_enum(Feature, "DEATH_STRIKE", "Death Strike")
extend_enum(Feature, "ENVENOM_WEAPONS", "Envenom Weapons")
extend_enum(Feature, "INFILTRATION_EXPERTISE", "Infiltration Expertise")


#################################################################################
class RogueAssassin(Rogue):
    _class_name = "Assassin"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(Assassinate())
        self.add_feature(AssassinsTools())
        super().level3(**kwargs)

    #############################################################################
    def level9(self, **kwargs: Any):
        self.add_feature(InfiltrationExpertise())

    #############################################################################
    def level13(self, **kwargs: Any):
        self.add_feature(EnvenomWeapons())

    #############################################################################
    def level17(self, **kwargs: Any):
        self.add_feature(DeathStrike())


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


#############################################################################
class EnvenomWeapons(BaseFeature):
    tag = Feature.ENVENOM_WEAPONS
    _desc = """When you use the Poison option of your Cunning Strike, the target also takes 2d6 Poison damage 
    whenever it fails the saving throw. This damage ignores Resistance to Poison damage."""


#############################################################################
class DeathStrike(BaseFeature):
    tag = Feature.DEATH_STRIKE

    @property
    def desc(self) -> str:
        dc = 8 + self.owner.stats[Stat.DEXTERITY].modifier + self.owner.proficiency_bonus
        return f"""When you hit with your Sneak Attack on the first round of a combat, the target must succeed on a 
            Constitution saving throw (DC 8 {dc}), or the attack's damage is doubled against the target."""


# EOF

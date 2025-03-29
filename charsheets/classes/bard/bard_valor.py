from typing import TYPE_CHECKING, cast, Any

from aenum import extend_enum

from charsheets.classes.bard import Bard
from charsheets.constants import Feature, Proficiency
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


extend_enum(Feature, "COMBAT_INSPIRATION", "Combat Inspiration")
extend_enum(Feature, "MARTIAL_TRAINING", "Martial Training")
extend_enum(Feature, "EXTRA_ATTACK_BARD", "Extra Attack")


#################################################################################
class BardValorCollege(Bard):

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(CombatInspiration())
        self.add_feature(MartialTraining())

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(ExtraAttack())


#################################################################################
class CombatInspiration(BaseFeature):
    tag = Feature.COMBAT_INSPIRATION
    _desc = """A creature that has a Bardic Inspiration die from you can use it for one of the following effects.

    Defense. When the creature is hit by an attack roll, that creature can use its Reaction to roll the Bardic 
    Inspiration die and add the number rolled to its AC against that attack, potentially causing the attack to miss.

    Offense. Immediately after the creature hits a target with an attack roll, the creature can roll the Bardic 
    Inspiration die and add the number rolled to the attack's damage against the target."""


#################################################################################
class MartialTraining(BaseFeature):
    tag = Feature.MARTIAL_TRAINING
    hide = True
    _desc = """You can use a Simple or Martial weapon as a Spellcasting Focus to cast spells from your Bard spell 
    list."""

    def mod_armour_proficiency(self, character: "Character") -> Reason[Proficiency]:
        return Reason("Martial Training", cast(Proficiency, Proficiency.MEDIUM_ARMOUR), cast(Proficiency, Proficiency.SHIELDS))

    def mod_weapon_proficiency(self, character: "Character") -> Reason[Proficiency]:
        return Reason("Martial Training", cast(Proficiency, Proficiency.MARTIAL_WEAPONS))


#################################################################################
class ExtraAttack(BaseFeature):
    tag = Feature.EXTRA_ATTACK_BARD
    _desc = """You can cast one of your cantrips that has a casting time of an action in place of one of those 
    attacks."""

    def mod_extra_attack(self, character: "Character") -> Reason[str]:
        return Reason("Extra Attack", "Attack twice per Attack action")


# EOF

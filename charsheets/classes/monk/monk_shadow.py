from typing import TYPE_CHECKING

from charsheets.classes.monk import Monk
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class MonkWarriorOfShadow(Monk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Monk (Warrior of Shadow)"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {ShadowArts()}
        abilities |= super().class_features()
        if self.level >= 6:
            abilities |= {ShadowStep()}
        if self.level >= 11:
            abilities |= {ImprovedShadowStep()}
        return abilities


#############################################################################
class ShadowArts(BaseFeature):
    tag = Feature.SHADOW_ARTS
    _desc = """You have learned to draw on the power of the Shadowfell, gaining the following benefits. 

    Darkness. You can expend 1 Focus Point to cast the Darkness spell without spell components. You can see within 
    the spell’s area when you cast it with this feature. While the spell persists, you can move its area of Darkness 
    to a space within 60 feet of yourself at the start of each of your turns.

    Darkvision. You gain Darkvision with a range of 60 feet. If you already have Darkvision, its range increases by 
    60 feet.

    Shadowy Figments. You know the Minor Illusion spell. Wisdom is your spellcasting ability for it."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Shadow Arts", Spell.MINOR_ILLUSION)


#############################################################################
class ShadowStep(BaseFeature):
    tag = Feature.SHADOW_STEP
    _desc = """While entirely within Dim Light or Darkness, you can use a Bonus Action to teleport up to 60 feet to 
    an unoccupied space you can see that is also in Dim Light or Darkness. You then have Advantage on the next melee 
    attack you make before the end of the current turn."""


#############################################################################
class ImprovedShadowStep(BaseFeature):
    tag = Feature.IMPROVED_SHADOW_STEP
    _desc = """You can draw on your Shadowfell connection to empower your teleportation. When you use your Shadow 
    Step, you can expend 1 Focus Point to remove the requirement that you must start and end in Dim Light or Darkness 
    for that use of the feature. As part of this Bonus Action, you can make an Unarmed Strike immediately after you 
    teleport."""


# EOF

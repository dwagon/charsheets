from typing import TYPE_CHECKING

from charsheets.features.base_feature import BaseFeature
from charsheets.classes.ranger import Ranger
from charsheets.constants import Feature
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    pass


#################################################################################
class RangerGloomStalker(Ranger):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Gloom Stalker"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {DreadAmbusher(), UmbralSight()}
        abilities |= super().class_features()

        self.prepare_spells(Spell.DISGUISE_SELF)
        if self.level >= 5:
            self.prepare_spells(Spell.ROPE_TRICK)
        if self.level >= 7:
            abilities |= {IronMind()}
        if self.level >= 9:
            self.prepare_spells(Spell.FEAR)

        return abilities


#############################################################################
class DreadAmbusher(BaseFeature):
    tag = Feature.DREAD_AMBUSHER
    _desc = """You have mastered the art of creating fearsome ambushes, granting you the following benefits.

    Ambusher's Leap.  At the start of your first turn of each combat, your Speed increases by 10 feet until the end 
    of that turn.

    Dreadful Strike. When you attack a creature and hit it with a weapon, you can deal an extra 2d6 Psychic damage. 
    You can use this benefit only once per turn, you can use it a number of times equal to your Wisdom modifier (
    minimum of once), and you regain all expended uses when you finish a Long Rest.

    Initiative Bonus. When you roll Initiative, you can add your Wisdom modifier to the roll."""


#############################################################################
class UmbralSight(BaseFeature):
    tag = Feature.UMBRAL_SIGHT
    _desc = """You gain Darkvision with a range of 60 feet. If you already have Darkvision, its range increases by 60
    feet.

    You are also adept at evading creatures that rely on Darkvision. While entirely in Darkness, you have the
    Invisible condition to any creature that relies on Darkvision to see you in that Darkness."""

    # TODO - darkvision


#############################################################################
class IronMind(BaseFeature):
    tag = Feature.IRON_MIND
    _desc = """You have honed your ability to resist mind-altering powers. You gain proficiency in Wisdom saving 
    throws. If you already have this proficiency, you instead gain proficiency in Intelligence or Charisma saving 
    throws (your choice)."""


# EOF

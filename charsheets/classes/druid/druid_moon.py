from typing import Any, TYPE_CHECKING

from aenum import extend_enum

from charsheets.classes.druid import Druid
from charsheets.constants import Feature, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:
    from charsheets.character import Character

extend_enum(Feature, "CIRCLE_FORMS", "Circle Forms")
extend_enum(Feature, "CIRCLE_OF_THE_MOON_SPELLS", "Circle of the Moon Spells")
extend_enum(Feature, "IMPROVED_CIRCLE_FORMS", "Improved Circle Forms")
extend_enum(Feature, "MOONLIGHT_STEP", "Moonlight Step")


#################################################################################
class DruidCircleOfTheMoon(Druid):

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(CircleForms())
        self.add_feature(CircleOfTheMoonSpells())

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(ImprovedCircleForms())

    #############################################################################
    def level10(self, **kwargs: Any):
        self.add_feature(MoonlightStep())


#############################################################################
class CircleOfTheMoonSpells(BaseFeature):
    tag = Feature.CIRCLE_OF_THE_MOON_SPELLS
    _desc = """Circle of the Sea Spells"""
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        assert character.druid is not None
        spells = Reason("Circle of the Moon Spells", Spell.CURE_WOUNDS, Spell.MOONBEAM, Spell.STARRY_WISP)
        if character.druid.level >= 5:
            spells |= Reason("Circle of the Moon Spells", Spell.CONJURE_ANIMALS)
        if character.druid.level >= 7:
            spells |= Reason("Circle of the Moon Spells", Spell.FOUNT_OF_MOONLIGHT)
        if character.druid.level >= 9:
            spells |= Reason("Circle of the Moon Spells", Spell.MASS_CURE_WOUNDS)
        return spells


#############################################################################
class CircleForms(BaseFeature):
    tag = Feature.CIRCLE_FORMS

    @property
    def desc(self) -> str:
        return f"""You can channel lunar magic when you assume a Wild Shape form, granting you the benefits below.

    Challenge Rating. The maximum Challenge Rating for the form is {self.owner.level // 3}.

    Armor Class. Until you leave the form, your AC equals {13+self.owner.wisdom.modifier} if that total is higher than
    the Beast's AC.

    Temporary Hit Points. You gain {3*self.owner.level} Temporary Hit Points."""


#############################################################################
class ImprovedCircleForms(BaseFeature):
    tag = Feature.IMPROVED_CIRCLE_FORMS
    _desc = """While in Wild Shape form, you gain the following benefits.

    Lunar Radiance. Each of your attacks in a Wild Shape form can deal its normal damage type of Radiant damage. You
    make this choice each time you hit with those attacks.

    Increased Toughness. You can add your Wisdom modifier to your Constitution saving throws.
    """


#############################################################################
class MoonlightStep(BaseFeature):
    tag = Feature.MOONLIGHT_STEP
    recovery = Recovery.LONG_REST

    @property
    def goes(self) -> int:
        return max(1, self.owner.wisdom.modifier)

    _desc = """As a Bonus Action, you teleport up to 30 feet to an unoccupied space you can see, and you have
    Advantage on the next attack roll you make before the end of this turn. 
    
    You can also regain uses by expending a level 2+ spell slot for each use you want to restore (no action required)."""


# EOF

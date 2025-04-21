from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.druid import Druid
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "AQUATIC_AFFINITY", "Aquatic Affinity")
extend_enum(Feature, "CIRCLE_OF_THE_SEA_SPELLS", "Circle of the Sea Spells")
extend_enum(Feature, "OCEANIC_GIFT", "Oceanic Gift")
extend_enum(Feature, "STORMBORN", "Stormborn")
extend_enum(Feature, "WRATH_OF_THE_SEA", "Wrath of the Sea")


#################################################################################
class DruidCircleOfTheSea(Druid):
    _class_name = "Circle of the Sea Druid"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(WrathOfTheSea())
        self.add_feature(CircleOfTheSeaSpells())

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(AquaticAffinity())

    #############################################################################
    def level10(self, **kwargs: Any):
        self.add_feature(Stormborn())

    #############################################################################
    def level14(self, **kwargs: Any):
        self.add_feature(OceanicGift())


#############################################################################
class CircleOfTheSeaSpells(BaseFeature):
    tag = Feature.CIRCLE_OF_THE_SEA_SPELLS
    _desc = """Circle of the Sea Spells"""
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        assert character.druid is not None
        spells = Reason(
            "Circle of the Sea Spells", Spell.FOG_CLOUD, Spell.GUST_OF_WIND, Spell.RAY_OF_FROST, Spell.SHATTER, Spell.THUNDERWAVE
        )
        if character.druid.level >= 5:
            spells |= Reason("Circle of the Sea Spells", Spell.LIGHTNING_BOLT, Spell.WATER_BREATHING)
        if character.druid.level >= 7:
            spells |= Reason("Circle of the Sea Spells", Spell.CONTROL_WATER, Spell.ICE_STORM)
        if character.druid.level >= 9:
            spells |= Reason("Circle of the Sea Spells", Spell.CONJURE_ELEMENTAL, Spell.HOLD_MONSTER)
        return spells


#############################################################################
class WrathOfTheSea(BaseFeature):
    tag = Feature.WRATH_OF_THE_SEA

    @property
    def desc(self) -> str:
        dice = max(1, self.owner.wisdom.modifier)
        return f""" As a Bonus Action, you can expend a use of your Wild Shape to manifest a 5-foot Emanation that
        takes the form of ocean spray that surrounds you for 10 minutes. It ends early if you dismiss it (no action
        required), manifest it again, or have the Incapacitated condition.

        When you manifest the Emanation and as a Bonus Action on your subsequent turns, you can choose another
        creature you can see in the Emanation. The target must succeed on a Constitution saving throw against your
        spell save DC or take Cold damage and, if the creature is Large or smaller, be pushed up to 15 feet away from
        you. To determine this damage, roll {dice}d6s"""


#############################################################################
class AquaticAffinity(BaseFeature):
    tag = Feature.AQUATIC_AFFINITY
    _desc = """The size of the Emanation created by your Wrath of the Sea increases to 10 feet.

    In addition, you gain a Swim Speed equal to your Speed."""

    def mod_swim_movement(self, character: "Character") -> Reason[int]:
        return Reason[int]("Aquatic Affinity", character.speed.value)


#############################################################################
class Stormborn(BaseFeature):
    tag = Feature.STORMBORN
    _desc = """Your Wrath of the Sea confers two more benefits while active, as detailed below.
        
        Flight. You gain a Fly Speed equal to your Speed.

        Resistance. You have Resistance to Cold, Lightning, and Thunder damage."""


#############################################################################
class OceanicGift(BaseFeature):
    tag = Feature.OCEANIC_GIFT
    _desc = """Instead of manifesting the Emanation of Wrath of the Sea around yourself, you can manifest it around 
    one willing creature within 60 feet of yourself. That creature gains all the benefits of the Emanation and uses 
    your spell save DC and Wisdom modifier for it. In addition, you can manifest the Emanation around both the other 
    creature and yourself if you expend two uses of your Wild Shape instead of one when manifesting it."""

from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.bard import Bard
from charsheets.constants import Feature, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "BEGUILING_MAGIC", "Beguiling Magic")
extend_enum(Feature, "MANTLE_OF_INSPIRATION", "Mantle of Inspiration")
extend_enum(Feature, "MANTLE_OF_MAJESTY", "Mantle of Majesty")


#################################################################################
class BardGlamourCollege(Bard):
    _class_name = "Glamour College Bard"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        assert self.character is not None
        self.add_feature(BeguilingMagic())
        self.add_feature(MantleOfInspiration())

    #############################################################################
    def level6(self, **kwargs: Any):
        assert self.character is not None
        self.add_feature(MantleOfMajesty())


#################################################################################
class BeguilingMagic(BaseFeature):
    tag = Feature.BEGUILING_MAGIC
    recovery = Recovery.LONG_REST
    _goes = 1
    _desc = """Immediately after you cast an Enchantment or Illusion spell using a spell slot, you can cause a 
    creature you can see within 60 feet of yourself to make a Wisdom saving throw against your spell save DC. On a 
    failed save, the target has the Charmed or Frightened condition (your choice) for 1 minute. The target repeats 
    the save at the end of each of its turns, ending the effect on itself on a success.
    
    You can also restore your use of it by expending one use of your Bardic Inspiration (no action 
    required)."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Beguiling Magic", Spell.CHARM_PERSON, Spell.MIRROR_IMAGE)


#################################################################################
class MantleOfInspiration(BaseFeature):
    tag = Feature.MANTLE_OF_INSPIRATION
    recovery = Recovery.LONG_REST
    _desc = """As a Bonus Action, you can expend a use of Bardic Inspiration, rolling a Bardic Inspiration die. When 
    you do so, choose a number of other creatures within 60 feet of yourself, up to a number equal to your Charisma 
    modifier (minimum of one creature). Each of those creatures gains a number of Temporary Hit Points equal to two 
    times the number rolled on the Bardic Inspiration die, and then each can use its Reaction to move up to its Speed 
    without provoking Opportunity Attacks."""


#################################################################################
class MantleOfMajesty(BaseFeature):
    tag = Feature.MANTLE_OF_MAJESTY
    recovery = Recovery.LONG_REST
    _goes = 1
    _desc = """As a Bonus Action, you cast 'Command' without expending a spell slot, and you take on an unearthly 
    appearance for 1 minute or until your Concentration ends. During this time, you can cast 'Command' as a Bonus 
    Action without expending a spell slot.

    Any creature Charmed by you automatically fails its saving throw against the 'Command' you cast with this feature.

    You can also restore your use of it by expending a level 3+ spell slot (no action required)."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Mantle of Majesty", Spell.COMMAND)


# EOF

from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.druid import Druid
from charsheets.constants import Feature, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


extend_enum(Feature, "COSMIC_OMEN", "Cosmic Omen")
extend_enum(Feature, "STARRY_FORM", "Starry Form")
extend_enum(Feature, "STAR_MAP", "Star Map")
extend_enum(Feature, "TWINKLING_CONSTELLATIONS", "Twinkling Constellations")


#################################################################################
class DruidCircleOfTheStars(Druid):

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(StarMap())
        self.add_feature(StarryForm())

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(CosmicOmen())

    #############################################################################
    def level10(self, **kwargs: Any):
        self.add_feature(TwinklingConstellations())


#############################################################################
class StarMap(BaseFeature):
    tag = Feature.STAR_MAP
    recover = Recovery.LONG_REST

    @property
    def goes(self) -> int:
        return max(1, self.owner.wisdom.modifier)

    _desc = """While holding the star chart, you have the Guidance and Guiding Blot spells prepared, and you can cast
    Guiding Bolt without expending a spell slot."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Star Map", Spell.GUIDANCE, Spell.GUIDING_BOLT)


#############################################################################
class StarryForm(BaseFeature):
    tag = Feature.STARRY_FORM
    _desc = """As a Bonus Action you can expend a use of your Wild Shape feature to take on a starry form rather than
    shape-shifting.

    While in your starry form, you retain your game statistics, but your body becomes luminous, your joints glimmer
    like stars, and glowing lines connect them as on a star chart. This form sheds Bright Light in a 10-foot radius
    and Dim Light for additional 10 feet. The form lasts for 10 minutes. It ends early if you dismiss it
    (no action required), have the Incapacitated condition, or use this feature again.

    Whenever you assume your starry form, choose which of the following constellations glimmers on your body;
    your choice gives you certain benefits while in the form.

    Archer. A constellation of an archer appears on you. When you activate this form and as a Bonus Action on your
    subsequent turns while it lasts, you can make a ranged spell attack, hurling a luminous arrow that targets one
    creature within 60 feet of yourself. On a hit, the attack deals Radiant damage equal to 1d8 plus your Wisdom
    modifier.

    Chalice. A constellation of a life-giving goblet appears on you. Whenever you cast a spell using a spell slot that
    restores Hit Points to a creature, you or another creature within 30 feet of you can regain Hit Points equal to
    1d8 plus your Wisdom modifier.

    Dragon. A constellation of a wise dragon appears on you. When you make an Intelligence or a Wisdom check or a
    Constitution saving throw to maintain Concentration, you can treat a roll of 9 or lower on the d20 as a 10.
    """


#############################################################################
class CosmicOmen(BaseFeature):
    tag = Feature.COSMIC_OMEN
    recovery = Recovery.LONG_REST

    @property
    def goes(self) -> int:
        return max(1, self.owner.wisdom.modifier)

    _desc = """Whenever you finish a Long Rest, you can consult your Star Map for omens and roll a die. Until you
    finish your next Long Rest, you gain access to a special Reaction based on whether you rolled an even or an odd
    number on the die:

    Weal (Even). Whenever a creature you can see within 30 feet of you is about to make a D20 Test, you can take a
    Reaction to roll 1d6 and add the number rolled to the total.

    Woe (Odd). Whenever a creature you can see within 30 feet of you is about to make a D20 Test, you can take a
    Reaction to roll 1d6 and subtract the number rolled to the total."""


#############################################################################
class TwinklingConstellations(BaseFeature):
    tag = Feature.TWINKLING_CONSTELLATIONS
    _desc = """The constellations of your Starry Form improve.

            The 1d8 of the Archer and the Chalice becomes 2d8, and while the Dragon is active, you have a Fly Speed 
            of 20 feet and can hover.

            Moreover, at the start of each of your turns while in your Starry Form, you can change which 
            constellation glimmers on your body."""


# EOF

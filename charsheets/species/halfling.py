from aenum import extend_enum
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.species.base_species import BaseSpecies

extend_enum(Feature, "BRAVE", "Brave")
extend_enum(Feature, "HALFLING_NIMBLENESS", "Halfling Nimbleness")
extend_enum(Feature, "LUCK", "Luck")
extend_enum(Feature, "NATURALLY_STEALTHY", "Naturally Stealthy")


#############################################################################
class Halfling(BaseSpecies):
    #########################################################################
    def species_feature(self) -> set[BaseFeature]:
        return {Brave(), HalflingNimbleness(), Luck(), NaturallyStealthy()}


#############################################################################
class Brave(BaseFeature):
    tag = Feature.BRAVE
    _desc = """You have Advantage on saving throws you make to avoid or end the Frightened condition."""


#############################################################################
class HalflingNimbleness(BaseFeature):
    tag = Feature.HALFLING_NIMBLENESS
    _desc = """You can move through the space of any creature that is a size larger than you, but you can't stop in
    the same space."""


#############################################################################
class Luck(BaseFeature):
    tag = Feature.LUCK
    desc = """When you roll a 1 on the d20 of a D20 Test, you can reroll the die, and you must use the new roll."""


#############################################################################
class NaturallyStealthy(BaseFeature):
    tag = Feature.NATURALLY_STEALTHY
    _desc = """You can take the Hide action even when you are obscured only by a creature that is at least one size larger
    than you."""


# EOF
